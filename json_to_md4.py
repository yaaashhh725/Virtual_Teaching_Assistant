# /// script
# dependencies = [
#   "bs4",
#   "markdownify",
#   "requests",
#   "google-genai",
#   "dotenv",
#   "tdqm"
# ]
# ///

from bs4 import BeautifulSoup
import os
import json
from pathlib import Path
import glob
from markdownify import markdownify as md
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
from tqdm import tqdm

import requests

def get_image_description(image_path):
    # cookie = os.getenv("DISCOURSE_COOKIE")
    # prompt = 'Describe this image in detail, focusing on the key elements, text, and context that would be helpful for someone who cannot see the image.'
    # if not cookie:
    #     raise ValueError("DISCOURSE_COOKIE not found in environment variables.")

    # headers = {'cookie': cookie}
    # image_path = "https://discourse.onlinedegree.iitm.ac.in/uploads/short-url/ztYoarmvww2WIkqZVCfsxgyDyhj.png"
    
    image_bytes = requests.get(image_path).content
    image = types.Part.from_bytes(
    data=image_bytes, mime_type="image/jpeg"
    )

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        config=types.GenerateContentConfig(
            system_instruction="You are a visual guide how describes an image given to you focusing on key elements, text and context. Give the description in brief and the text present as it is (if any). Present the output like this image description : ... image text: ... . If unsure about the description don't make it up. Output should be reproducible",
        ),
        contents=image,
    )

    time.sleep(6) # request per minute 10 for this model 
    return response.text
    # response = requests.get(image_path).content
    # if response.status_code != 200:
    #     print(image_path)

    # return "Some image description"

def convert_html_to_markdown(html_content):
  """
  Converts a string of HTML content to Markdown.

  Args:
    html_content: The HTML content as a string.

  Returns:
    The converted Markdown content as a string.
  """
  # The strip_tags argument can be used to remove any tags not handled
  # The heading_style='ATX' ensures that headers are formatted with '#'
  markdown_text = md(html_content, heading_style='ATX').strip()
  return markdown_text


def parse_images(html_content):
  """
  Parses HTML content, replaces a specific image structure with a description,
  and returns the remaining content as a string.

  Args:
    html_content: The HTML content as a string.

  Returns:
    The parsed content as a string with image structures replaced.
  """
  soup = BeautifulSoup(html_content, 'html.parser')

  for lightbox in soup.find_all('div', class_='lightbox-wrapper'):
    image_link = None
    # Prioritize the link from the <a> tag
    a_tag = lightbox.find('a', class_='lightbox')
    if a_tag and a_tag.has_attr('href'):
      image_link = a_tag['href']

    # Fallback to the <img> tag's src if the <a> tag is not found or has no href
    if not image_link:
      img_tag = lightbox.find('img')
      if img_tag and img_tag.has_attr('src'):
        image_link = img_tag['src']

    if image_link:
      # Get the image description and replace the whole lightbox structure
      image_description = get_image_description(image_link)
      lightbox.replace_with(image_description)

  return str(soup)

def extract_post_data(json_file_path):
    """
    Extract post data from a single JSON file.
    
    Args:
        json_file_path (str): Path to the JSON file
    
    Returns:
        list: List of dictionaries containing extracted post data
    """
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        posts_data = []
        topic_slug = None
        if 'post_stream' in data and 'posts' in data['post_stream']:
            posts = data['post_stream']['posts']
            
            for post in tqdm(posts):
                raw_cooked = post.get('cooked', '')
                cleaned_content = parse_images(raw_cooked)
                cleaned_content = convert_html_to_markdown(cleaned_content)
                
                post_info = {
                    'file_source': os.path.basename(json_file_path),
                    'post_id': post.get('id', ''),
                    'username': post.get('username', ''),
                    'name': post.get('name', ''),
                    'created_at': post.get('created_at', ''),
                    'post_number': post.get('post_number', 1),
                    'topic_id': post.get('topic_id', ''),
                    'topic_slug': post.get('topic_slug', ''),
                    'reply_count': post.get('reply_count', 0),
                    'reads': post.get('reads', 0),
                    'score': post.get('score', 0.0),
                    'raw_cooked': raw_cooked,
                    'cleaned_content': cleaned_content
                }
                if topic_slug==None:
                   topic_slug = post_info['topic_slug']
                posts_data.append(post_info)
        
        return posts_data,topic_slug
    
    except Exception as e:
        print(f"Error processing file {json_file_path}: {str(e)}")
        return []

def save_as_markdown(posts_data, output_file,topic_slug):
    """
    Save extracted posts data as a markdown file.
    
    Args:
        posts_data (list): List of post dictionaries
        output_file (str): Output file path
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # Document header
            f.write(f"# {topic_slug}\n\n")
            
            for i, post in enumerate(posts_data, 1):
                
                
                if post['cleaned_content'].strip():
                    # Split into paragraphs and write each one
                    paragraphs = post['cleaned_content'].split('\n\n')
                    for paragraph in paragraphs:
                        if paragraph.strip():
                            f.write(f"{paragraph.strip()}\n\n")
                
                f.write("---\n\n")
        
        print(f"✓ Saved {len(posts_data)} posts to: {output_file}")
        
    except Exception as e:
        print(f"Error saving markdown file {output_file}: {str(e)}")


def process_json_files(input_directory, output_directory=None, output_format='md'):
    """
    Process all JSON files in a directory and extract post content.
    
    Args:
        input_directory (str): Directory containing JSON files
        output_directory (str): Output directory (default: same as input)
        output_format (str): Output format ('md' or 'json')
    """
    # Set default output directory
    if output_directory is None:
        output_directory = os.path.join(input_directory, 'extracted_content')
    
    # Create output directory
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files
    json_pattern = os.path.join(input_directory, "*.json")
    json_files = glob.glob(json_pattern)
    
    if not json_files:
        print(f"❌ No JSON files found in directory: {input_directory}")
        return
    
    print(f"📁 Found {len(json_files)} JSON files to process")
    print(f"📁 Output directory: {output_directory}")
    print(f"📄 Output format: {output_format.upper()}")
    print("-" * 50)
    
    all_posts = []
    processed_files = 0
    
    for json_file in json_files:
        filename = os.path.basename(json_file)
        print(f"Processing: {filename}")
        
        posts_data,topic_slug = extract_post_data(json_file)
        
        if posts_data:
            # Save individual file
            base_name = os.path.splitext(filename)[0]
            individual_output = os.path.join(output_directory, f"{base_name}_posts.{output_format}")
            
            # if output_format == 'md':
            save_as_markdown(posts_data, individual_output,topic_slug)
            # elif output_format == 'json':
            #     save_as_json(posts_data, individual_output)
            
            all_posts.extend(posts_data)
            processed_files += 1
            print(f"  → Extracted {len(posts_data)} posts")
        else:
            print(f"  → No posts found")
        
        print()

def main():
    """
    Main function to run the JSON post extractor.
    """
    print("🚀 JSON Posts Content Extractor")
    print("=" * 50)
    
    output_format = 'md'
    input_dir = './discourse_json'
    output_dir = './discourse_md'
    
    
    # Process files
    process_json_files(input_dir, output_dir, output_format)

if __name__ == "__main__":
    main()