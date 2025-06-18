# doubts-in-q7-q8

**post_id:** 590924  
**author:** Sakshi6479  
**timestamp:** 2025-02-05T16:57:48.827Z

# doubts-in-q7-q8

sir I am not able to solve these question I have tried all thing also the video which you shared but still after using postman also i am unable to answer it (showing methods not allowed everytime)and also in Q8 I am having this problem  
Here's a description of the image:
The image displays a browser window with a URL in the address bar and some JSON data in the body. The URL includes a query string related to ticket status. The JSON data suggests an error, possibly indicating a missing field or an invalid query.
image text:
```
"retty print
]
i
127.0.0.1:8000/execute?query=what%20is%20the%20status%20of%20ticket
"detail": [
{
"type": "missing",
"loc": [
],
"query",
"q"
"msg": "Field required",
"input": null
}
```

```
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import util
from fastapi.middleware.cors import CORSMiddleware
from typing import List

# Create FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allow OPTIONS and POST
    allow_headers=["*"],  # Allow all headers
)

# Pydantic model to parse incoming data
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# OpenAI API key and URL
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/embeddings"
API_KEY = "enter your key"  # Replace with your actual API key

def get_embeddings(docs: List[str]) -> List[List[float]]:
    """Retrieve embeddings for a list of documents from OpenAI's API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    
    data = {
        "model": "text-embedding-3-small",  # Use the correct model
        "input": docs
    }

response = requests.post(API_URL, json=data, headers=headers)

if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="API request failed")

response_data = response.json()
    if 'data' not in response_data:
        raise KeyError("Missing 'data' field in API response")

return [embedding['embedding'] for embedding in response_data['data']]

@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    # Get embeddings for docs and query
    docs = request.docs
    query = request.query

# Get embeddings for the documents and query
    all_docs = docs + [query]  # Combine documents and query into one list
    embeddings = get_embeddings(all_docs)  # Get embeddings from OpenAI API

doc_embeddings = embeddings[:-1]  # All embeddings except for the query
    query_embedding = embeddings[-1]  # The last embedding is for the query

# Calculate cosine similarities
    similarities = util.cos_sim(query_embedding, doc_embeddings)[0].cpu().numpy()

# Sort documents by similarity (highest first)
    sorted_docs = sorted(zip(docs, similarities), key=lambda x: x[1], reverse=True)

# Return the top 3 most similar documents
    top_matches = [doc for doc, _ in sorted_docs[:3]]
    
    return {"matches": top_matches}

```

for Q8

```
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)
    
    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
    
    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]
    
    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)
    
    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

```

---

