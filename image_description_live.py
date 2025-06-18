# /// script
# dependencies = [
#   "dotenv",
#   "google-genai",
# ]
# ///

from dotenv import load_dotenv
load_dotenv()
from google import genai 
from google.genai import types
import os

def get_image_description(image) -> str:
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

import base64
with open("test.png", "rb") as image_file:
    b64_img = base64.b64encode(image_file.read()).decode()

print(get_image_description(b64_img))