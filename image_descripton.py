# /// script
# dependencies = [
#   "requests",
#   "google-genai",
#   "dotenv"
# ]
# ///
import os
import time
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()


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

    # print(response.text)
    time.sleep(1)
    return response.text

# def get_image_description(image_path):
#     cookie = os.getenv("DISCOURSE_COOKIE")
#     prompt = 'Describe this image in detail, focusing on the key elements, text, and context that would be helpful for someone who cannot see the image.'
#     if not cookie:
#         raise ValueError("DISCOURSE_COOKIE not found in environment variables.")

#     headers = {'cookie': cookie}
#     # image_path = "https://discourse.onlinedegree.iitm.ac.in/uploads/short-url/ztYoarmvww2WIkqZVCfsxgyDyhj.png"
#     image_bytes = requests.get(image_path,headers = headers).content
#     image = types.Part.from_bytes(
#     data=image_bytes, mime_type="image/jpeg"
#     )

#     client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
#     response = client.models.generate_content(
#         model="gemini-2.0-flash-exp",
#         config=types.GenerateContentConfig(
#             system_instruction="You are a visual guide how describes an image given to you focusing on key elements, text and context. Give the description in brief and the text present as it is (if any). Present the output like this image description : ... image text: ... . If unsure about the description don't make it up. Output should be reproducible",
#         ),
#         contents=image,
#     )

#     # print(response.text)
#     time.sleep(1)
#     return response.text

# def get_image_description(image_path):
    # image_path = "https://goo.gle/instrument-img"
    # image_bytes = requests.get(image_path).content
    # image = types.Part.from_bytes(
    # data=image_bytes, mime_type="image/jpeg"
    # )

    # client = genai.Client(api_key="GOOGLE_API_KEY")
    # response = client.models.generate_content(
    #     model="gemini-2.0-flash-exp",
    #     contents=["What is this image?", image],
    # )

    # return response.text
    
if __name__ == '__main__':
    image_path = "https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/1/b14fdd8db7fa7f4f811065f54b5b478db50f61ac.png"
    print(get_image_description(image_path))

