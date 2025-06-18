# project-1-solution-repository-link

**post_id:** 616382  
**author:** Nomit  
**timestamp:** 2025-04-07T03:41:26.209Z

# project-1-solution-repository-link

Can anyone share the link to project 1 solution github repo.

---

**post_id:** 616421  
**author:** carlton  
**timestamp:** 2025-04-07T05:50:26.193Z

The repo has not been made public. But until that happens, we are allowed to share the solution.  
Just name the script app.py, build the docker image according to test environment. This also happened to be the highest scoring script getting 19 tasks correct.

```
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "fastapi",
#   "httpx",
#   "uvicorn",
# ]
# ///

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import httpx
import re
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

token = os.environ["LLMFOUNDRY_TOKEN"]

async def llm(system_prompt: str, user_prompt: str) -> str:
    """Call GPT-4o-Mini via AI Proxy."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(
            "https://llmfoundry.straive.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            },
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

system_prompt = """The user will provide a task description.
Write one or more `bash` or `python` scripts to execute the task.

CODING RULES:

- uv, the Python runner, is ALREADY installed. Run with `uv run [URL] [ARGUMENTS]`
- Parse dates with `python-dateutil`
- Sender email is in the `From: "Name <email@...>` header
- When removing a prefix (e.g. `/data/docs/`) from a path, retain the path after the prefix
- Call an LLM via a POST request to `https://llmfoundry.straive.com/openai/v1/chat/completions` with `Authorization: Bearer {os.getenv("LLMFOUNDRY_TOKEN")}` and this JSON body:
    {
      model: "gpt-4o-mini",
      messages: [
        { role: "system", content: "[INSERT SYSTEM PROMPT]" },
        { role: "user", content: [
        { type: "text", text: "[INSERT USER MESSAGE]" }, // for text
        { type: "image_url", image_url: { url: `data:[IMAGE MIME TYPE];base64,[IMAGE BASE64]`, detail: "low" } }, // for image. Get MIME type DYNAMICALLY from image
        ]}
      ],
      // response_format: "json_object",  // forces JSON response
    }
  Response is in `response.choices?.[0]?.message?.content`. Error is in `response.error?.message`.
- Calculate embeddings with a POST request to `https://llmfoundry.straive.com/openai/v1/embeddings` with `Authorization: Bearer {os.getenv("LLMFOUNDRY_TOKEN")}` and this JSON body:
    {
      model: "text-embedding-3-small",
      input: [array of strings],
    }
  Embeddings are in response.data[*].embedding - an array of floats.
  Calculate the dot product of the embeddings (skipping the diagonal) to find the most similar pair of strings.

client.post(
            f"{openai_api_base}/embeddings",
            headers={"Authorization": f"Bearer {openai_api_key}"},
            json={"model": "text-embedding-3-small", "input": data},
        )
- When extracting card information, use the system prompt "Extract the EXACT dummy credit card number from this test image"

EXECUTION RULES: An automated agent will blindly run the scripts you provide. So ONLY
write the FINAL script(s) to run in ```bash or ```python code fences.
"""

@app.post("/run")
async def run_task(task: str):
    """Execute a plain-English automation task."""
    response = await llm(system_prompt, task)
    print(f"\n🟡 Running task:\n{task.strip()}\n")
    print(f"\n🟡 {response}\n")

results = []
    for language, code in re.findall(r"```(python|bash)\n(.*?)\n```", response, re.DOTALL):
        print(f"\n🟡 Running {language} code:\n{code}\n")
        if language == "python":
            result = await execute_python(code)
        else:  # bash
            result = await execute_bash(code)
        results.append({"lang": language, **result})

print(f"\n🟡 Results:\n{results}\n")
    return {"response": response, "results": results}

@app.get("/read")
async def read_file(path: str):
    """Read contents of a file."""
    # Validate path is within /data
    path = os.path.normpath(path)
    if not path.startswith("/data/"):
        raise HTTPException(status_code=400, detail="Invalid path")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path)

@app.post("/execute/python")
async def execute_python(code: str):
    """Execute Python code directly."""
    proc = await asyncio.create_subprocess_exec(
        "python3",
        "-",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate(code.encode())

if proc.returncode != 0:
        print(f"\n🔴 Python execution failed:\n{stderr.decode()}")
        raise HTTPException(status_code=500, detail=f"Execution failed: {stderr.decode()}")

return {"stdout": stdout.decode(), "stderr": stderr.decode()}

@app.post("/execute/bash")
async def execute_bash(code: str):
    """Execute bash code directly."""
    proc = await asyncio.create_subprocess_exec(
        "bash",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate(code.encode())

if proc.returncode != 0:
        print(f"\n🔴 Bash execution failed:\n{stderr.decode()}")
        raise HTTPException(status_code=500, detail=f"Execution failed: {stderr.decode()}")

return {"stdout": stdout.decode(), "stderr": stderr.decode()}

@app.get("/")
async def read_root():
    """Serve the index.html file."""
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn

uvicorn.run(app, host="0.0.0.0", port=8000)

```

---

