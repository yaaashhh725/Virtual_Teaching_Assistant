# /// script
# dependencies = [
#   "dotenv",
#   "google-genai",
#   "fastapi",
#   "numpy",
#   "aiohttp",
#   "uvicorn"
# ]
# ///



import os
import json
import numpy as np
import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import aiohttp
import asyncio
import logging
from fastapi.responses import JSONResponse
import uvicorn
import traceback
from dotenv import load_dotenv

from google import genai
from google.genai import types

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
NPZ_PATH = "final_embeddings.npz"
SIMILARITY_THRESHOLD = 0.50  # Lowered threshold for better recall
MAX_RESULTS = 10
MAX_CONTEXT_CHUNKS = 4
load_dotenv()
API_KEY = os.getenv("API_KEY")

class QueryRequest(BaseModel):
    question: str
    image: Optional[str] = None  # Base64 encoded image

class LinkInfo(BaseModel):
    url: str
    text: str

class QueryResponse(BaseModel):
    answer: str
    links: List[LinkInfo]

app = FastAPI(title="RAG Query API", description="API for querying the RAG knowledge base")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not API_KEY:
    logger.error("API_KEY environment variable is not set. The application will not function correctly.")

def load_npz_data(npz_path=NPZ_PATH):
    arr = np.load(npz_path, allow_pickle=True)
    chunks = arr["chunks"]
    embeddings = arr["embeddings"]
    metadata = [json.loads(m) for m in arr["metadata"]]
    return chunks, embeddings, metadata

def cosine_similarity(vec1, vec2):
    try:
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        if np.all(vec1 == 0) or np.all(vec2 == 0):
            return 0.0
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0
        return dot_product / (norm_vec1 * norm_vec2)
    except Exception as e:
        logger.error(f"Error in cosine_similarity: {e}")
        logger.error(traceback.format_exc())
        return 0.0

async def get_embedding(text, max_retries=3):
    if not API_KEY:
        error_msg = "API_KEY environment variable not set"
        logger.error(error_msg)
        raise Exception(error_msg)
    retries = 0
    while retries < max_retries:
        try:
            logger.info(f"Getting embedding for text (length: {len(text)})")
            url = "https://aipipe.org/openai/v1/embeddings"
            headers = {
                "Authorization": API_KEY,
                "Content-Type": "application/json"
            }
            payload = {
                "model": "text-embedding-3-small",
                "input": text
            }
            logger.info("Sending request to embedding API")
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status == 200:
                        result = await response.json()
                        logger.info("Successfully received embedding")
                        return result["data"][0]["embedding"]
                    elif response.status == 429:
                        error_text = await response.text()
                        logger.warning(f"Rate limit reached, retrying after delay (retry {retries+1}): {error_text}")
                        await asyncio.sleep(5 * (retries + 1))
                        retries += 1
                    else:
                        error_text = await response.text()
                        error_msg = f"Error getting embedding (status {response.status}): {error_text}"
                        logger.error(error_msg)
                        raise Exception(error_msg)
        except Exception as e:
            error_msg = f"Exception getting embedding (attempt {retries+1}/{max_retries}): {e}"
            logger.error(error_msg)
            logger.error(traceback.format_exc())
            retries += 1
            if retries >= max_retries:
                raise Exception(error_msg)
            await asyncio.sleep(3 * retries)

def get_image_description(image: Optional[str]) -> str:
    """
    Dummy function to simulate extracting a description from an image.
    This can be an image URL or a base64-encoded image string.
    For now, returns a static description.
    """
    if not image:
        return ""
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="You are a visual guide how describes an image given to you focusing on key elements, text and context. Give the description in brief and the text present as it is (if any). Present the output like this image description : ... image text: ... . If unsure about the description don't make it up. Output should be reproducible",
        ),
        contents=image,
    )

    # time.sleep(6) # request per minute 10 for this model 
    return response.text
    # return "This is a dummy description of the provided image."

async def process_multimodal_query(question, image_base64):
    try:
        logger.info(f"Processing query: '{question[:50]}...', image provided: {image_base64 is not None}")
        if not image_base64:
            logger.info("No image provided, processing as text-only query")
            return await get_embedding(question)
        logger.info("Processing multimodal query with image")
        # Dummy image description logic
        image_description = get_image_description(image_base64)
        combined_query = f"{question}\nImage context: {image_description}"
        return await get_embedding(combined_query)
    except Exception as e:
        logger.error(f"Exception processing multimodal query: {e}")
        logger.error(traceback.format_exc())
        return await get_embedding(question)

def find_similar_content(query_embedding, chunks, embeddings, metadata):
    results = []
    for idx, emb in enumerate(embeddings):
        similarity = cosine_similarity(query_embedding, emb)
        if similarity >= SIMILARITY_THRESHOLD:
            meta = metadata[idx]
            url = meta.get("original_url") or meta.get("source_file") or ""
            if not url or not str(url).startswith("http"):
                url = f"https://docs.onlinedegree.iitm.ac.in/{meta.get('topic', '')}"
            results.append({
                "source": meta.get("source_type", "unknown"),
                "id": idx,
                "title": meta.get("topic", "unknown"),
                "url": url,
                "content": chunks[idx],
                "chunk_index": meta.get("chunk_index", 0),
                "similarity": float(similarity)
            })
    results.sort(key=lambda x: x["similarity"], reverse=True)
    # Group by source document and keep most relevant chunks
    grouped_results = {}
    for result in results:
        key = f"{result['source']}_{result['title']}"
        if key not in grouped_results:
            grouped_results[key] = []
        grouped_results[key].append(result)
    final_results = []
    for key, group in grouped_results.items():
        group.sort(key=lambda x: x["similarity"], reverse=True)
        final_results.extend(group[:MAX_CONTEXT_CHUNKS])
    final_results.sort(key=lambda x: x["similarity"], reverse=True)
    return final_results[:MAX_RESULTS]

def enrich_with_adjacent_chunks(results, chunks, metadata):
    enriched_results = []
    for result in results:
        idx = result["id"]
        current_chunk_index = result["chunk_index"]
        topic = result["title"]
        source = result["source"]

        additional_content = ""
        # Previous chunk
        prev_idx = None
        next_idx = None
        for i, meta in enumerate(metadata):
            if meta.get("topic", "") == topic and meta.get("chunk_index") == current_chunk_index - 1 and meta.get("source_type") == source:
                prev_idx = i
            if meta.get("topic", "") == topic and meta.get("chunk_index") == current_chunk_index + 1 and meta.get("source_type") == source:
                next_idx = i
        if prev_idx is not None:
            additional_content += chunks[prev_idx] + " "
        if next_idx is not None:
            additional_content += " " + chunks[next_idx]
        if additional_content:
            result["content"] = f"{result['content']} {additional_content}"
        enriched_results.append(result)
    return enriched_results

async def generate_answer(question, relevant_results, max_retries=2):
    if not API_KEY:
        error_msg = "API_KEY environment variable not set"
        logger.error(error_msg)
        raise Exception(error_msg)
    retries = 0
    while retries < max_retries:
        try:
            logger.info(f"Generating answer for question: '{question[:50]}...'")
            context = ""
            for result in relevant_results:
                source_type = "Discourse post" if result["source"] == "discussion_forum" else "Documentation"
                context += f"\n\n{source_type} (URL: {result['url']}):\n{result['content'][:1500]}"
            prompt = f"""Answer the following question based ONLY on the provided context. 
If you cannot answer the question based on the context, say "I don't have enough information to answer this question."

Context:
{context}

Question: {question}

Return your response in this exact format:
1. A comprehensive yet concise answer
2. A "Sources:" section that lists the URLs and relevant text snippets you used to answer

Sources must be in this exact format:
Sources:
1. URL: [exact_url_1], Text: [brief quote or description]
2. URL: [exact_url_2], Text: [brief quote or description]

Make sure the URLs are copied exactly from the context without any changes.
"""
            logger.info("Sending request to LLM API")
            url = "https://aipipe.org/openai/v1/chat/completions"
            headers = {
                "Authorization": API_KEY,
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant that provides accurate answers based only on the provided context. Always include sources in your response with exact URLs."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            }
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload) as response:
                    if response.status == 200:
                        result = await response.json()
                        logger.info("Successfully received answer from LLM")
                        return result["choices"][0]["message"]["content"]
                    elif response.status == 429:
                        error_text = await response.text()
                        logger.warning(f"Rate limit reached, retrying after delay (retry {retries+1}): {error_text}")
                        await asyncio.sleep(3 * (retries + 1))
                        retries += 1
                    else:
                        error_text = await response.text()
                        error_msg = f"Error generating answer (status {response.status}): {error_text}"
                        logger.error(error_msg)
                        raise Exception(error_msg)
        except Exception as e:
            error_msg = f"Exception generating answer: {e}"
            logger.error(error_msg)
            logger.error(traceback.format_exc())
            retries += 1
            if retries >= max_retries:
                raise Exception(error_msg)
            await asyncio.sleep(2)

def parse_llm_response(response):
    try:
        logger.info("Parsing LLM response")
        parts = response.split("Sources:", 1)
        if len(parts) == 1:
            for heading in ["Source:", "References:", "Reference:"]:
                if heading in response:
                    parts = response.split(heading, 1)
                    break
        answer = parts[0].strip()
        links = []
        if len(parts) > 1:
            sources_text = parts[1].strip()
            source_lines = sources_text.split("\n")
            for line in source_lines:
                line = line.strip()
                if not line:
                    continue
                line = re.sub(r'^\d+\.\s*', '', line)
                line = re.sub(r'^-\s*', '', line)
                url_match = re.search(r'URL:\s*\[(.*?)\]|url:\s*\[(.*?)\]|\[(http[^\]]+)\]|URL:\s*(http\S+)|url:\s*(http\S+)|(http\S+)', line, re.IGNORECASE)
                text_match = re.search(r'Text:\s*\[(.*?)\]|text:\s*\[(.*?)\]|[""](.*?)[""]|Text:\s*"(.*?)"|text:\s*"(.*?)"', line, re.IGNORECASE)
                if url_match:
                    url = next((g for g in url_match.groups() if g), "")
                    url = url.strip()
                    text = "Source reference"
                    if text_match:
                        text_value = next((g for g in text_match.groups() if g), "")
                        if text_value:
                            text = text_value.strip()
                    if url and url.startswith("http"):
                        links.append({"url": url, "text": text})
        logger.info(f"Parsed answer (length: {len(answer)}) and {len(links)} sources")
        return {"answer": answer, "links": links}
    except Exception as e:
        error_msg = f"Error parsing LLM response: {e}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        return {
            "answer": "Error parsing the response from the language model.",
            "links": []
        }

@app.post("/query")
async def query_knowledge_base(request: QueryRequest):
    try:
        logger.info(f"Received query request: question='{request.question[:50]}...', image_provided={request.image is not None}")
        if not API_KEY:
            error_msg = "API_KEY environment variable not set"
            logger.error(error_msg)
            return JSONResponse(
                status_code=500,
                content={"error": error_msg}
            )
        chunks, embeddings, metadata = load_npz_data()
        logger.info("Processing query and generating embedding")
        query_embedding = await process_multimodal_query(
            request.question,
            request.image
        )
        logger.info("Finding similar content")
        relevant_results = find_similar_content(query_embedding, chunks, embeddings, metadata)
        if not relevant_results:
            logger.info("No relevant results found")
            return {
                "answer": "I couldn't find any relevant information in my knowledge base.",
                "links": []
            }
        logger.info("Enriching results with adjacent chunks")
        enriched_results = enrich_with_adjacent_chunks(relevant_results, chunks, metadata)
        logger.info("Generating answer")
        llm_response = await generate_answer(request.question, enriched_results)
        logger.info("Parsing LLM response")
        result = parse_llm_response(llm_response)
        if not result["links"]:
            logger.info("No links extracted, creating from relevant results")
            links = []
            unique_urls = set()
            for res in relevant_results[:5]:
                url = res["url"]
                if url not in unique_urls:
                    unique_urls.add(url)
                    snippet = res["content"][:100] + "..." if len(res["content"]) > 100 else res["content"]
                    links.append({"url": url, "text": snippet})
            result["links"] = links
        logger.info(f"Returning result: answer_length={len(result['answer'])}, num_links={len(result['links'])}")
        return result
    except Exception as e:
        error_msg = f"Unhandled exception in query_knowledge_base: {e}"
        logger.error(error_msg)
        logger.error(traceback.format_exc())
        return JSONResponse(
            status_code=500,
            content={"error": error_msg}
        )

@app.get("/health")
async def health_check():
    try:
        chunks, embeddings, metadata = load_npz_data()
        return {
            "status": "healthy",
            "npz_loaded": True,
            "api_key_set": bool(API_KEY),
            "num_chunks": len(chunks),
            "num_embeddings": len(embeddings)
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(
            status_code=500,
            content={"status": "unhealthy", "error": str(e), "api_key_set": bool(API_KEY)}
        )

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)