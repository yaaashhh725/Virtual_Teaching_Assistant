# regarding-project1-for-file-not-detecting-after-sending-post-request

**post_id:** 594941  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T12:38:47.883Z

# regarding-project1-for-file-not-detecting-after-sending-post-request

sir i am getting an error in this function calling which you have demonstrate yesterday , i am attaching my code also the error with it. Please take a look and provide the solution as the deadline is close please help me as soon as possible.  
is there anything to do with dockerfile or anything else please explain it how to do it step by step.

```
import os
from dotenv import load_dotenv
import json
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
load_dotenv()
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "enter your token here")

def sort_contacts(contacts_file_path: str, output_file_path: str):
    try:
        contacts = pd.read_json(contacts_file_path)
        contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
        return {"message": f"Contacts sorted and saved to {output_file_path}"}
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}

a4_tool = {
    "type": "function",
    "function": {
        "name": "sort_contacts",
        "description": "This function takes data from a json file and sorts the data first by last name and then by first name, then it stores it inside the speicfied location.",
        "parameters": {
            "type": "object",
            "properties": {
                "contacts_file_path": {
                    "type": "string",
                    "description": "The relative path to the input JSON file containing the contacts."
                },
                "output_file_path": {
                    "type": "string",
                    "description": "The relative path to the output JSON file to store the sorted contacts."
                }
            },
            "required": ["contacts_file_path", "output_file_path"],
            "additionalProperties": False
        },
        "strict": True
    },
}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]

def query_gpt(user_input: str, tools: list[dict] = tools) -> dict:
    response = requests.post(
        url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "tools": tools,
            "tool_choice": "auto"
        }
    )
    return response.json()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="File does not exist")

@app.post("/run")
async def run(task: str):
    query = query_gpt(task)
    print(query)  # Print the full response to inspect it.
    
    if 'choices' not in query:
        raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
    
    try:
        tool_calls = query['choices'][0]['message'].get('tool_calls', [])
        if tool_calls:
            func_name = tool_calls[0]['function']['name']
            args = json.loads(tool_calls[0]['function']['arguments'])
            
            # Map function names to their respective functions
            function_map = {
                "cakebake": cakebake,
                "install_uv_and_run_datagen": install_uv_and_run_datagen,
                "format_markdown_file": format_markdown_file,
                "count_wednesdays": count_wednesdays,
                "sort_contacts": sort_contacts,
                "extract_recent_logs": extract_recent_logs,
                "create_markdown_index": create_markdown_index,
                "extract_sender_email": extract_sender_email,
                "extract_credit_card_number": extract_credit_card_number,
                "find_similar_comments": find_similar_comments,
                "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
            }
            
            if func_name in function_map:
                output = function_map[func_name](**args)
            else:
                raise HTTPException(status_code=500, detail="Unknown function called")
        else:
            raise HTTPException(status_code=500, detail="No function call found in response")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
    
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

image description: The image shows a software interface, presumably a tool for making HTTP requests. The interface is displaying the results of a POST request. The request was sent to an endpoint on localhost, specifically to "http://127.0.0.1:8000/run?task=Sort the array of contacts in ...". The response status is "200 OK". The body of the response is JSON format, indicating an error: "Failed to sort contacts: File /data/contacts.json does not exist".
image text: New Import
GET http:/ POST http POST http POST http
+
No environment
HTTP http://127.0.0.1:8000/run?task=Sort the array of contacts in /...
Save Share
POST http://127.0.0.1:8000/run?task=Sort the array of contacts in
Send
Params Auth Headers (7) Body Scripts Tests Settings
Cookies
task
Key Sort the array of contacts i...
Value
Description
Body
200 OK • 2.96 s • 201 B
000
{} JSON
Preview Visualize
1
{
2
"error": "Failed to sort contacts: File /data/contacts.json does
not exist"
3
}

[@Saransh\_Saini](/u/saransh_saini) , [@Jivraj](/u/jivraj) , [@carlton](/u/carlton)

---

**post_id:** 594951  
**author:** carlton  
**timestamp:** 2025-02-14T13:01:08.797Z

Hi Sakshi,

The error is quite clear, it cannot find the file /data/contacts.json

Question: What creates the /data/contacts.json file?

---

**post_id:** 594962  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T13:30:26.445Z

so how to do it sir that the thing i am not able to understand.

---

**post_id:** 594971  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T13:59:34.581Z

sir kindly help me with this the time is running and i am still at the starting stage of project.  
[@carlton](/u/carlton)

---

**post_id:** 594980  
**author:** Saransh_Saini  
**timestamp:** 2025-02-14T14:16:24.088Z

Sakshi as the error says it’s unable to find your file. Try adding a . (dot) before the location.

---

**post_id:** 595001  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T14:32:12.846Z

sir i have used the dot(.) while sending the request to postman in the query which i provided to the task. Is the dot(.) should be added somewhere else?

---

**post_id:** 595018  
**author:** Saransh_Saini  
**timestamp:** 2025-02-14T15:07:26.713Z

If you have added that dot as a prefix to your locations then, you would have to structure your query\_gpt in such a way that it takes these dots into consideration.

---

**post_id:** 595104  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T17:48:35.347Z

sir i have tried that by putting by doing this

```
import os
from dotenv import load_dotenv
import json
import requests
from dateutil import parser as date_parser
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from fastapi.responses import StreamingResponse, JSONResponse
from typing import Dict, Any, List
import subprocess
import datetime
from pathlib import Path
import sqlite3
import base64
import mimetypes
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

#AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
def cakebake(no_people: int, flavor: str):
    return {"message": f"Making a {flavor} cake for {no_people} people"}

bakecake = {
    "type": "function",
    "function": {
        "name": "cakebake",
        "description": "Make a cake for all iitm students contain its emailids",
        "parameters": {
            "type": "object",
            "properties": {
                "no_people": {
                    "type": "integer",
                    "description": "Number of people"
                },
                "flavor": {
                    "type": "string",
                    "description": "Flavor of the cake"
                }
            },
            "required": ["no_people", "flavor"],
            "additionalProperties": False
        },
        "strict": True
    }
}

def sort_contacts(contacts_file_path: str, output_file_path: str):
    try:
        contacts = pd.read_json(contacts_file_path)
        contacts.sort_values(["last_name", "first_name"]).to_json(output_file_path, orient="records")
        return {"message": f"Contacts sorted and saved to {output_file_path}"}
    except Exception as e:
        return {"error": f"Failed to sort contacts: {str(e)}"}

tools = [bakecake, a1_tool, a2_tool, a3_tool, a4_tool, a5_tool, a6_tool, a7_tool, a8_tool, a9_tool, a10_tool]

def query_gpt(user_input: str, tools: list[dict] = tools) -> dict[str, Any]:
    response = requests.post(
        url="https://aiproxy.sanand.workers.dev/openai/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AIPROXY_TOKEN}"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "system",
                    "content": """
                        Whenever you receive a system directory location, always make it into a realtive path, for example adding a . before it would make it relative path, rest is on you to manage, I just want the relative path"""
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "tools": tools,
            "tool_choice": "auto"
        }
    )
    return response.json()

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/read")
def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        raise HTTPException(status_code=404, detail="File does not exist")

@app.post("/run")
async def run(task: str):
    query = query_gpt(task)
    print(query)  # Print the full response to inspect it.
    
    if 'choices' not in query:
        raise HTTPException(status_code=500, detail="Invalid response format from GPT API")
    
    try:
        tool_calls = query['choices'][0]['message'].get('tool_calls', [])
        if tool_calls:
            func_name = tool_calls[0]['function']['name']
            args = json.loads(tool_calls[0]['function']['arguments'])
            
            # Map function names to their respective functions
            function_map = {
                "cakebake": cakebake,
                "install_uv_and_run_datagen": install_uv_and_run_datagen,
                "format_markdown_file": format_markdown_file,
                "count_wednesdays": count_wednesdays,
                "sort_contacts": sort_contacts,
                "extract_recent_logs": extract_recent_logs,
                "create_markdown_index": create_markdown_index,
                "extract_sender_email": extract_sender_email,
                "extract_credit_card_number": extract_credit_card_number,
                "find_similar_comments": find_similar_comments,
                "calculate_gold_ticket_sales": calculate_gold_ticket_sales,
            }
            
            if func_name in function_map:
                output = function_map[func_name](**args)
            else:
                raise HTTPException(status_code=500, detail="Unknown function called")
        else:
            raise HTTPException(status_code=500, detail="No function call found in response")
    except KeyError as e:
        raise HTTPException(status_code=500, detail=f"KeyError: Missing key in response - {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the request: {str(e)}")
    
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```

and also i am sending postman request as <http://localhost:8000/run?task=The> file ./data/dates.txt contains a list of dates, one per line. Count the number of Wednesdays in the list, and write just the number to ./data/dates-wednesdays.txt  
do I need to use dockerfile for this? i am still getting the same error as  
Here's the image description:
The image shows a screenshot of a tool with a POST request. The request URL is "http://localhost:8000/run?task=The file ./data/dates.txt co". The response status is "200 OK". The body of the response contains a JSON object with an "error" key, indicating a failure related to a file named "./data/dates.txt".
image text:
POST
http://localhost:8000/run?task=The file ./data/dates.txt co
Send
Params Auth Headers (7) Body Scripts Tests Settings
The file ./data/dates.txt c...
Value
Description
task
Key
Body
{} JSON
Preview
Visualize
1
2
3
Cookies
200 OK
2.72 s 220 B
000
"error": "Failed to count Wednesdays: [Errno 2] No such file or
directory: './data/dates.txt'"
T
  
[@carlton](/u/carlton) , [@Saransh\_Saini](/u/saransh_saini) , [@Jivraj](/u/jivraj)

---

**post_id:** 595110  
**author:** 23f2004752  
**timestamp:** 2025-02-14T17:55:28.433Z

have you first post a request for task A1 as it creates the data folder along with all the other files .

---

**post_id:** 595117  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T18:19:59.123Z

no actually do we have to create another file for that or we have to request post in this one ? can you guide me for that step wise . it would be very helpful.

---

**post_id:** 595118  
**author:** 23f2004752  
**timestamp:** 2025-02-14T18:22:49.379Z

by running task A1 , it automatically creates a data folder along with all the files in it. Without running task A1 you can’t do rest of A tasks

---

**post_id:** 595122  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T18:38:09.127Z

how can i run A1 task can elaborate a little bit. do i have to create data folder manually or using this code by giving query taskA1 it will generate that folder ?

---

**post_id:** 595123  
**author:** 23f2004752  
**timestamp:** 2025-02-14T18:39:57.491Z

simply give task=“task”  
task: copy the task a\_1 from project document

---

**post_id:** 595125  
**author:** Sakshi6479  
**timestamp:** 2025-02-14T18:44:30.274Z

it is showing

```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
{'id': 'chatcmpl-B0uvU556EOCy6HOPHV9ni7YJY403i', 'object': 'chat.completion', 'created': 1739558524, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': None, 'tool_calls': [{'id': 'call_JXkfp14QEEo6M2zdgBXKduqi', 'type': 'function', 'function': {'name': 'install_uv_and_run_datagen', 'arguments': '{"email":"24f2006749@ds.study.iitm.ac.in"}'}}], 'refusal': None}, 'logprobs': None, 'finish_reason': 'tool_calls'}], 'usage': {'prompt_tokens': 732, 'completion_tokens': 30, 'total_tokens': 762, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'service_tier': 'default', 'system_fingerprint': 'fp_00428b782a', 'monthlyCost': 0.09109908, 'cost': 0.002376, 'monthlyRequests': 137}
Collecting uv
  Downloading uv-0.6.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (11 kB)
Downloading uv-0.6.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.3/16.3 MB 3.2 MB/s eta 0:00:00
Installing collected packages: uv
Successfully installed uv-0.6.0
python: can't open file '/home/sakshi-tds/tds_project1/https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py': [Errno 2] No such file or directory
INFO:     127.0.0.1:34758 - "POST /run?task=Install%20uv%20(if%20required)%20and%20run%20https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py%20with%2024f2006749@ds.study.iitm.ac.in%20as%20the%20only%20argument. HTTP/1.1" 200 OK

```

Here's a description of the image:
The image is a screenshot of a software application interface, likely a tool for making HTTP requests. It is showing a POST request to "http://localhost:8000/run?task=Install uv (if required) and ru...". The response status is "200 OK". The body of the response displays a JSON object with an "error" message: "Failed to run datagen.py...".
image text: HTTP http://localhost:8000/run?task=Install uv (if required) and ru...
POST
Params Auth Headers (7) Body Scripts Tests Settings
task
Install uv (if required) and ...
Body
{} JSON
1
{
2
"error": "Failed to run datagen.py: Command '['python', 'https://
raw.githubusercontent.com/sanand0/tools-in-data-science-public/
tds-2025-01/project-1/datagen.py', '24f2006749@ds.study.iitm.
ac.in']' returned non-zero exit status 2."
3
}

---

