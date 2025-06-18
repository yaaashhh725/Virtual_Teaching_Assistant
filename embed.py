# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "semantic-text-splitter",
#     "numpy",
#     "tqdm",
#     "google-genai",
#     "aiohttp",
#     "pyyaml",
#   "dotenv"
# ]
# ///

import hashlib
import httpx
import json
import numpy as np
import os
import time
from pathlib import Path
from semantic_text_splitter import MarkdownSplitter
from tqdm import tqdm
from typing import List, Dict, Tuple
import re
from dotenv import load_dotenv
import yaml
load_dotenv()


class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0
    
    def wait_if_needed(self):
        current_time = time.time()
        
        # Per-second rate limiting
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1.0 / self.requests_per_second):
            sleep_time = (1.0 / self.requests_per_second) - time_since_last
            time.sleep(sleep_time)
        
        # Per-minute rate limiting
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]
        
        if len(self.request_times) >= self.requests_per_minute:
            sleep_time = 60 - (current_time - self.request_times[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
                # Clean up old requests after sleeping
                current_time = time.time()
                self.request_times = [t for t in self.request_times if current_time - t < 60]
        
        self.request_times.append(current_time)
        self.last_request_time = current_time


rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)


import asyncio
import aiohttp
import json


async def get_embedding_async(session: aiohttp.ClientSession, text: str, api_key: str, max_retries: int = 3) -> List[float]:
    """Get embedding for text chunk using OpenAI API through aipipe proxy"""
    
    # Model limit is 8191 tokens for text-embedding-3-small
    max_chars = 8000  # Conservative limit to stay under token limit
    
    # If text is too long, truncate it (you might want to handle this differently)
    if len(text) > max_chars:
        text = text[:max_chars]
        print(f"Warning: Text truncated to {max_chars} characters")
    
    retries = 0
    while retries < max_retries:
        try:
            # Apply rate limiting
            rate_limiter.wait_if_needed()
            
            # Call the embedding API through aipipe proxy
            url = "https://aipipe.org/openai/v1/embeddings"
            headers = {
                "Authorization": api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "model": "text-embedding-3-small",
                "input": text
            }
            
            async with session.post(url, headers=headers, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    embedding = result["data"][0]["embedding"]
                    return embedding
                elif response.status == 429:  # Rate limit error
                    error_text = await response.text()
                    print(f"Rate limit reached, retrying after delay (retry {retries+1}): {error_text}")
                    await asyncio.sleep(5 * (retries + 1))  # Exponential backoff
                    retries += 1
                else:
                    error_text = await response.text()
                    print(f"Error embedding text (status {response.status}): {error_text}")
                    raise Exception(f"API Error: {response.status}")
                    
        except Exception as e:
            print(f"Exception embedding text: {e}")
            retries += 1
            if retries < max_retries:
                await asyncio.sleep(3 * retries)  # Wait before retry
    
    raise Exception(f"Failed to embed text after {max_retries} retries")


def get_embedding(text: str, max_retries: int = 3) -> List[float]:
    """Synchronous wrapper for the async embedding function"""
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")
    
    async def _get_embedding():
        async with aiohttp.ClientSession() as session:
            return await get_embedding_async(session, text, api_key, max_retries)
    
    # Run the async function in the current event loop or create a new one
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If we're already in an async context, we need to handle this differently
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(asyncio.run, _get_embedding())
                return future.result()
        else:
            return loop.run_until_complete(_get_embedding())
    except RuntimeError:
        return asyncio.run(_get_embedding())


def parse_frontmatter(content: str) -> Tuple[Dict, str]:
    """Parse YAML frontmatter from markdown content"""
    # Check if content starts with frontmatter
    if not content.strip().startswith('---'):
        return {}, content
    
    try:
        # Split content at the frontmatter boundaries
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content
        
        # Parse YAML frontmatter
        frontmatter_yaml = parts[1].strip()
        main_content = parts[2].strip()
        
        # Parse the YAML
        frontmatter = yaml.safe_load(frontmatter_yaml) or {}
        
        return frontmatter, main_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML frontmatter: {e}")
        return {}, content
    except Exception as e:
        print(f"Error processing frontmatter: {e}")
        return {}, content


def extract_title_from_discussion(content: str) -> str:
    """Extract title from the first line of discussion forum markdown"""
    lines = content.strip().split('\n')
    if lines:
        # Remove markdown formatting from title
        title = lines[0].strip()
        # Remove common markdown headers
        title = re.sub(r'^#+\s*', '', title)
        title = re.sub(r'^\*+\s*', '', title)
        title = re.sub(r'^_+\s*', '', title)
        return title
    return "Unknown Discussion"


def get_chunks_with_overlap(file_path: Path, chunk_size: int = 2000, overlap: int = 200) -> List[Dict]:
    """Get overlapping chunks from markdown file with metadata"""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Determine source type based on parent directory
    parent_dir = file_path.parent.name.lower()
    if 'discussion' in parent_dir or 'forum' in parent_dir:
        source_type = "discussion_forum"
        topic = extract_title_from_discussion(content)
        # For discussion forums, use the content as-is
        processing_content = content
        frontmatter = {}
    else:
        source_type = "course_content"
        # Parse frontmatter for course content
        frontmatter, processing_content = parse_frontmatter(content)
        
        # Extract topic from frontmatter title, fallback to filename
        if frontmatter.get('title'):
            topic = frontmatter['title']
        else:
            topic = file_path.stem
    
    # Create splitter for base chunks
    splitter = MarkdownSplitter(chunk_size)
    base_chunks = splitter.chunks(processing_content)
    
    chunks_with_metadata = []
    
    # If we only have one chunk, no overlap needed
    if len(base_chunks) <= 1:
        for i, chunk in enumerate(base_chunks):
            metadata = {
                'source_file': str(file_path),
                'source_type': source_type,
                'topic': topic,
                'chunk_index': i,
                'total_chunks': len(base_chunks),
                'overlap_type': 'none'
            }
            
            # Add frontmatter data for course content
            if source_type == "course_content" and frontmatter:
                metadata.update({
                    'original_url': frontmatter.get('original_url', ''),
                    'downloaded_at': frontmatter.get('downloaded_at', ''),
                    'frontmatter': frontmatter
                })
            
            chunks_with_metadata.append({
                'text': chunk,
                'metadata': metadata
            })
    else:
        # Create overlapping chunks
        full_text = processing_content
        
        # Calculate positions for overlapping windows
        positions = []
        current_pos = 0
        
        while current_pos < len(full_text):
            end_pos = min(current_pos + chunk_size, len(full_text))
            positions.append((current_pos, end_pos))
            
            # Break if we've reached the end
            if end_pos == len(full_text):
                break
                
            # Move forward by (chunk_size - overlap)
            current_pos += (chunk_size - overlap)
        
        # Create chunks from positions
        for i, (start, end) in enumerate(positions):
            chunk_text = full_text[start:end]
            
            # Skip very small chunks at the end
            if len(chunk_text.strip()) < 100:
                continue
            
            metadata = {
                'source_file': str(file_path),
                'source_type': source_type,
                'topic': topic,
                'chunk_index': i,
                'total_chunks': len(positions),
                'overlap_type': 'overlapping',
                'char_start': start,
                'char_end': end
            }
            
            # Add frontmatter data for course content
            if source_type == "course_content" and frontmatter:
                metadata.update({
                    'original_url': frontmatter.get('original_url', ''),
                    'downloaded_at': frontmatter.get('downloaded_at', ''),
                    'frontmatter': frontmatter
                })
            
            chunks_with_metadata.append({
                'text': chunk_text,
                'metadata': metadata
            })
    
    return chunks_with_metadata


async def process_directories_async(course_content_dir: str = "course_content", 
                                  discussion_forum_dir: str = "discussion_forum",
                                  chunk_size: int = 2000,
                                  overlap: int = 200,
                                  api_key: str = None,
                                  batch_size: int = 10) -> Tuple[List[str], List[List[float]], List[Dict]]:
    """Async version of process_directories for better performance with API calls"""
    
    if not api_key:
        api_key = os.environ.get("API_KEY")
        if not api_key:
            raise ValueError("API_KEY environment variable not set")
    
    all_chunks = []
    all_embeddings = []
    all_metadata = []
    
    # Get all markdown files from both directories
    course_files = []
    discussion_files = []
    
    if os.path.exists(course_content_dir):
        course_files = [*Path(course_content_dir).glob("*.md"), *Path(course_content_dir).rglob("*.md")]
        print(f"Found {len(course_files)} course content files")
    
    if os.path.exists(discussion_forum_dir):
        discussion_files = [*Path(discussion_forum_dir).glob("*.md"), *Path(discussion_forum_dir).rglob("*.md")]
        print(f"Found {len(discussion_files)} discussion forum files")
    
    all_files = course_files + discussion_files
    
    if not all_files:
        print("No markdown files found! Please check your directory structure.")
        return [], [], []
    
    # Process all files to get chunks
    total_chunks = 0
    file_chunks = {}
    
    print("Analyzing files and creating chunks...")
    for file_path in all_files:
        try:
            chunks_with_metadata = get_chunks_with_overlap(file_path, chunk_size, overlap)
            if chunks_with_metadata:
                file_chunks[file_path] = chunks_with_metadata
                total_chunks += len(chunks_with_metadata)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue
    
    print(f"Total chunks to process: {total_chunks}")
    
    # Collect all chunks for batch processing
    all_chunk_data = []
    for file_path, chunks_with_metadata in file_chunks.items():
        for chunk_data in chunks_with_metadata:
            all_chunk_data.append(chunk_data)
    
    # Process embeddings in batches
    async with aiohttp.ClientSession() as session:
        with tqdm(total=len(all_chunk_data), desc="Processing embeddings") as pbar:
            for i in range(0, len(all_chunk_data), batch_size):
                batch = all_chunk_data[i:i+batch_size]
                
                # Create tasks for the batch
                tasks = []
                for chunk_data in batch:
                    task = get_embedding_async(session, chunk_data['text'], api_key)
                    tasks.append((task, chunk_data))
                
                # Process the batch
                results = await asyncio.gather(*[task for task, _ in tasks], return_exceptions=True)
                
                # Handle results
                for j, (result, (_, chunk_data)) in enumerate(zip(results, tasks)):
                    if isinstance(result, Exception):
                        print(f"Skipping chunk due to error: {result}")
                        pbar.update(1)
                        continue
                    
                    all_chunks.append(chunk_data['text'])
                    all_embeddings.append(result)
                    all_metadata.append(chunk_data['metadata'])
                    
                    pbar.set_postfix({
                        "batch": f"{i//batch_size + 1}/{(len(all_chunk_data) + batch_size - 1)//batch_size}",
                        "total": len(all_chunks)
                    })
                    pbar.update(1)
                
                # Sleep between batches to avoid rate limits
                if i + batch_size < len(all_chunk_data):
                    await asyncio.sleep(2)
    
    return all_chunks, all_embeddings, all_metadata


def save_embeddings(chunks: List[str], embeddings: List[List[float]], metadata: List[Dict], 
                   output_file: str = "teaching_assistant_embeddings.npz"):
    """Save embeddings, chunks, and metadata to numpy archive"""
    
    # Convert metadata to a format that can be saved in numpy
    metadata_json = [json.dumps(meta) for meta in metadata]
    
    np.savez_compressed(
        output_file,
        chunks=np.array(chunks, dtype=object),
        embeddings=np.array(embeddings),
        metadata=np.array(metadata_json, dtype=object)
    )
    
    print(f"Saved {len(chunks)} chunks and embeddings to {output_file}")
    
    # Print some statistics
    course_content_count = sum(1 for meta in metadata if meta['source_type'] == 'course_content')
    discussion_count = sum(1 for meta in metadata if meta['source_type'] == 'discussion_forum')
    
    print(f"Statistics:")
    print(f"  Course content chunks: {course_content_count}")
    print(f"  Discussion forum chunks: {discussion_count}")
    print(f"  Total chunks: {len(chunks)}")
    
    # Show some example metadata
    if metadata:
        print(f"\nExample metadata structure:")
        example_course = next((meta for meta in metadata if meta['source_type'] == 'course_content'), None)
        example_discussion = next((meta for meta in metadata if meta['source_type'] == 'discussion_forum'), None)
        
        if example_course:
            print(f"Course content example:")
            print(f"  Topic: {example_course['topic']}")
            print(f"  Original URL: {example_course.get('original_url', 'N/A')}")
            print(f"  Downloaded: {example_course.get('downloaded_at', 'N/A')}")
        
        if example_discussion:
            print(f"Discussion forum example:")
            print(f"  Topic: {example_discussion['topic']}")
            print(f"  Source: {Path(example_discussion['source_file']).name}")
    
    # Show unique topics
    topics = set(meta['topic'] for meta in metadata)
    print(f"  Unique topics: {len(topics)}")
    for topic in sorted(topics)[:10]:  # Show first 10 topics
        print(f"    - {topic}")
    if len(topics) > 10:
        print(f"    ... and {len(topics) - 10} more")


async def main():
    # Configuration
    COURSE_CONTENT_DIR = "markdown_dummy"
    DISCUSSION_FORUM_DIR = "md"
    CHUNK_SIZE = 2000
    OVERLAP = 200
    OUTPUT_FILE = "discourse.npz"
    BATCH_SIZE = 10  # Process embeddings in batches
    
    print("Starting Teaching Assistant Embedding Generation...")
    print(f"Course content directory: {COURSE_CONTENT_DIR}")
    print(f"Discussion forum directory: {DISCUSSION_FORUM_DIR}")
    print(f"Chunk size: {CHUNK_SIZE}, Overlap: {OVERLAP}")
    print(f"Batch size: {BATCH_SIZE}")
    
    # Check for API key
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: API_KEY environment variable not set!")
        print("Please set your API key: export API_KEY='your_api_key_here'")
        return
    
    try:
        # Process directories and generate embeddings
        chunks, embeddings, metadata = await process_directories_async(
            COURSE_CONTENT_DIR, 
            DISCUSSION_FORUM_DIR, 
            CHUNK_SIZE, 
            OVERLAP,
            api_key,
            BATCH_SIZE
        )
        
        if chunks:
            # Save results
            save_embeddings(chunks, embeddings, metadata, OUTPUT_FILE)
            print("Embedding generation completed successfully!")
        else:
            print("No chunks were processed. Please check your file structure and try again.")
            
    except Exception as e:
        print(f"Error during processing: {e}")


if __name__ == "__main__":
    asyncio.run(main())