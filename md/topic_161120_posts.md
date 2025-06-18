# ga2-deployment-tools-discussion-thread-tds-jan-2025

**post_id:** 575521  
**author:** s.anand  
**timestamp:** 2025-01-03T07:12:14.469Z

# ga2-deployment-tools-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 2 - Deployment Tools](https://exam.sanand.workers.dev/tds-2025-01-ga2).

---

**post_id:** 576110  
**author:** carlton  
**timestamp:** 2025-01-08T03:10:51.093Z

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](/c/docs-discourse/45)! ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

**post_id:** 579138  
**author:** 22f3001315  
**timestamp:** 2025-01-12T17:08:02.850Z

Deadline: Sunday, February 2, 2025 6:29 PM

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

**post_id:** 578933  
**author:** 22f3001315  
**timestamp:** 2025-01-12T17:12:33.282Z

---

**post_id:** 578996  
**author:** Jivraj  
**timestamp:** 2025-01-12T21:38:16.588Z

image description: The image is a screenshot showing a form with an error message. The top of the image poses a question regarding the GitHub Pages URL with an example format. Below that is a text field with a red outline and an exclamation mark icon. Below that, there's an error message in red, detailing the response and specific HTML content.
image text: What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/
Error: 22f3001315@ds.study.iitm.ac.in is not in the response: <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Dolphin Facts</title> <style> body { font-family: Arial, sans-serif; background-color: #e0f7fa; color: #333; text-align:
  
i have included the email address still its giving error

---

**post_id:** 578997  
**author:** Jivraj  
**timestamp:** 2025-01-12T21:39:45.792Z

image description: The image presents a dark theme with pink text and a highlighted text box. The top of the image asks about the Vercel URL and provides an example of the URL structure. Inside the text box, a URL is displayed. Below, a "TypeError" message indicates a fetch failure.
image text: What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://markdarshan.vercel.app/api
TypeError: Failed to fetch
  
that website is working fine . just write the parameters after /api

---

**post_id:** 579058  
**author:** 22f3001315  
**timestamp:** 2025-01-13T04:10:58.317Z

Hi Guddu,

Can you share your GitHub repo. For GitHub pages question.

---

**post_id:** 579445  
**author:** 23F300327  
**timestamp:** 2025-01-13T20:23:32.007Z

Check your browser console most probably CORS is causing problem.

Try adding CORS to your code it might work.

Kind regards  
Jivraj

---

**post_id:** 579556  
**author:** 22f2001640  
**timestamp:** 2025-01-14T08:16:40.821Z

[github.com](https://github.com/gkmfrombs/dolfacts)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/b/1b67fc201449a012745d92b7efdcf9e92fc7a35b_2_690x344.png)

### [GitHub - gkmfrombs/dolfacts](https://github.com/gkmfrombs/dolfacts)

Contribute to gkmfrombs/dolfacts development by creating an account on GitHub.

I have added email in body two times in different ways.

---

**post_id:** 579564  
**author:** carlton  
**timestamp:** 2025-01-14T08:51:38.605Z

image description: The image is a screenshot of a computer terminal running Python code, alongside a Uvicorn server. The terminal displays the output from the code execution, including server startup messages, API requests, and responses. The Python code, displayed in a code editor, defines an API endpoint that fetches student data from a CSV file. The code uses libraries such as FastAPI, CORSMiddleware, and CSV. The terminal also shows the execution details of the Uvicorn server.
image text:
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv
app = FastAPI()
#Enable CORS
app.add\_middleware(
CORSMiddleware,
allow\_origins=["\*"], # Allow all origins
allow\_credentials=True,
allow\_methods=["\*"], # Allow all methods
allow\_headers=["\*"], # Allow all headers
#Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
reader = csv.DictReader(file)
for row in reader:
students.append({
"studentId": int(row["studentId"]),
"class": row["class"]
})
@app.get("/api")
async def get\_students(class\_: Optional[List[str]] = Query(None)):
print(f"Requested classes: {class\_}") # Debugging line
if class\_:
filtered\_students = [student for student in students if student["class"]
print(f"Filtered students: {filtered\_students}") # Debugging line
return {"students": filtered\_students}
return {"students": students}
if \_\_name\_\_ == "\_\_main\_\_":
import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)
  
[@carlton](/u/carlton) can you please tell me what is wrong in this because I am getting “Error: Response undefined does not match expected” to my answer

---

**post_id:** 579571  
**author:** 22f3001315  
**timestamp:** 2025-01-14T09:20:15.143Z

Facing Issue in GA 2 Question 10 LLM ngrok  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows an error message related to an ngrok service. A progress bar at the top indicates the service is encountering issues. The error message reads "ERR\_NGROK\_8012," stating that the ngrok agent tunneled traffic but failed to connect to the upstream web service at `http://localhost:8080`. The error encountered was "dial tcp 127.0.0.1:8080: connect: connection refused". Further down, the page provides instructions for developers, suggesting to ensure the web service is running and to test with cURL or a browser. It also includes instructions for visitors to refresh or contact the developer.
\*\*image text:\*\*
ERR\_NGROK\_8012
Traffic was successfully tunneled to the ngrok agent, but the agent failed to establish a connection to the upstream web
service at http://localhost:8080. The error encountered was:
dial tcp 127.0.0.1:8080: connect: connection refused
Get help with this error
If you're the developer of this page
On the machine where the ngrok agent is running, make sure a web service is running on http://localhost:8080. Try to cURL or open
the address in a browser to see that you get the correct response.
Check out the docs to get help with this error.
If you're a visitor of this page
Wait a few minutes and refresh the page. If that still doesn't work, please contact the developer of this page for more information.
  
I tired multiple times but issue is still there.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) Kindly help me out.

---

**post_id:** 579593  
**author:** 23F300327  
**timestamp:** 2025-01-14T10:12:42.463Z

Hi Mishkat,

Please use triple backticks to encapsulate code, so that we can debug your code more easily.

eg

```
if __name__ == "__main__":
   print ("Hello")

```

Please use this discourse etiquette to share code.

Thanks and kind regards

---

**post_id:** 579600  
**author:** Jivraj  
**timestamp:** 2025-01-14T10:30:40.928Z

sir did you check yet what is the problem in this one?

---

**post_id:** 579603  
**author:** 23F300327  
**timestamp:** 2025-01-14T10:38:20.276Z

```
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class_: Optional[List[str]] = Query(None)):
    print(f"Requested classes: {class_}")  # Debugging line
    if class_:
        filtered_students = [student for student in students if student["class"] in class_]
        print(f"Filtered students: {filtered_students}")  # Debugging line
        return {"students": filtered_students}
    return {"students": students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

```

---

**post_id:** 579617  
**author:** Jivraj  
**timestamp:** 2025-01-14T11:17:13.952Z

Hi Mishkat,

This error is because you are filtering on `class_` instead of `class`

So if you send a request on `http://127.0.0.1/api?class_=1S` you will see response for that `1S` class only.

kind regards

---

**post_id:** 579621  
**author:** Nelson  
**timestamp:** 2025-01-14T11:23:37.066Z

thank you so much after modifying the code it got accepted

---

**post_id:** 579625  
**author:** Jivraj  
**timestamp:** 2025-01-14T11:26:08.672Z

Hi Guddu,

Inside `index.html` file of your repo, don’t put html code just put your email in the file nothing else.

This issue is because when you deploy on github pages it encrypts any email that’s on page.

kind regards.

---

**post_id:** 579634  
**author:** s.anand  
**timestamp:** 2025-01-14T11:43:33.780Z

I am facing an issue with Docker Desktop.

image description: The image is a screenshot showing an error message from Docker Desktop related to WSL (Windows Subsystem for Linux). The error message is displayed on a dark blue background, with text in white and blue.
image text: Docker Desktop - Unexpected WSL error
An unexpected error occurred while executing a WSL command.
Either shut down WSL down with wsl --shutdown , and/or reboot your machine.
You can also try reinstalling WSL and/or Docker Desktop. If the issue persists,
collect diagnostics and submit an issue .
deploying WSL2 distributions
ensuring main distro is deployed: deploying "docker-
desktop": importing WSL distro "WSL2 is not supported with
Read our policy for uploaded diagnostic data
Gather diagnostics
Quit

I have uninstalled and installed Docker (run as administrator).

wsl --version

```
WSL version: 2.3.26.0
Kernel version: 5.15.167.4-1
WSLg version: 1.0.65
MSRDC version: 1.2.5620
Direct3D version: 1.611.1-81528511
DXCore version: 10.0.26100.1-240331-1435.ge-release
Windows version: 10.0.19045.5011

```

Tried many solutions after googling for the issue.  
So far no solution. Anyone else faced this issue and found a solution?

---

**post_id:** 579653  
**author:** 22f2001640  
**timestamp:** 2025-01-14T12:26:01.055Z

Hi Telvin,

Try opening `localhost:8080` in browser if that works, if it opens in browser then issue might be with some network configurations.

I solved this question in github codespace, which didn’t require me to make any changes in network.

kind regards

kind regards

---

**post_id:** 579662  
**author:** s.anand  
**timestamp:** 2025-01-14T12:52:41.809Z

[@Nelson](/u/nelson) I would recommend [Podman](https://podman.io/) or [Docker CE](https://docs.docker.com/engine/install/ubuntu/) rather than [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Docker Desktop is [not free for organizations over 250 people](https://docs.docker.com/subscription/desktop-license/) and many organizations have therefore moved away from it.

---

**post_id:** 579678  
**author:** Nelson  
**timestamp:** 2025-01-14T13:29:23.620Z

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) I tired , in browser localhost:8080 is working fine but ngrok is not working. Is there any other tools for tunneling that can be used.

---

**post_id:** 579794  
**author:** 23F300327  
**timestamp:** 2025-01-14T18:45:33.556Z

[@22f2001640](/u/22f2001640) in that case

* a firewall or local security settings might block access to port 8080, or
* a network restriction is blocking access to port 8080

Please try one of these:

* Try the same on a personal laptop on a public / home network
* GitHub codespaces, as [@Jivraj](/u/jivraj) suggested

You *could* try an ngrok alternative like [localtunnel](https://localtunnel.github.io/www/) but I don’t think that’ll work.

---

**post_id:** 579845  
**author:** carlton  
**timestamp:** 2025-01-15T04:11:18.135Z

Thank you, Sir!

> What is the Docker image URL? It should look like: `https://hub.docker.com/repository/docker/$USER/$REPO/general`

If I use Podman, will the answer be correct assuming I have done all steps correctly?

---

**post_id:** 579846  
**author:** 23F300327  
**timestamp:** 2025-01-14T17:13:30.532Z

Here's a brief description of the image:
The image is a screenshot of a coding environment, possibly a web development or API testing interface. It includes:
\* \*\*Web Browser:\*\* Showing a URL `127.0.0.1:8000/api?class\_=1S` and a response with JSON data.
\* \*\*Terminal:\*\* Showing python code and HTTP request logs.
\* \*\*Text area with instructions:\*\* detailing the requirements for a class parameter in an API and what the response should include.
\* \*\*Error Output:\*\* showing a response error from an API call.
image text:
```
127.0.0.1:8000/api?class\_=1S
Pretty print
{"students": [{"studentId":280,"class":"1S"}, {"studentId":298, "class":"1S"},
{"studentId":498,"class":"1S"}, {"studentId":1501,"class":"1S"}]}
If the URL has a query parameter class, it should return only students in those classes. For
example, /api?class=1A should return only students in class 1A. /api?class=1A&class=1B
should return only students in class 1A and 1B. There may be any number of classes
specified. Return students in the same order as they appear in the CSV file (not the order of
the classes).
Ensure that you have CORS enabled. Otherwise, we can't send requests to your server.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
Error: Response [{"studentId":1,"class":"101"},{"studentId":2,"class":"12M"},
{"studentId":3,"class":"5V"},{"studentId":4,"class":"2"},{"studentId":5,"class":"9E"},
{"studentId":6,"class":"7U"},{"studentId":7,"class":"12P"},{"studentId":8,"class":"4Y"},
{"studentId":9,"class":"9Q"},{"studentId":10,"class":"4G"},{"studentId":11,"class":"81"},
{"studentId":12,"class":"7G"},{"studentId":13,"class":"12D"},{"studentId":14,"class":"111"},
{"studentId":15,"class":"10"},{"studentId":16,"class":"3O"},{"studentId":17,"class":"7C"},
{"studentId":18,"class":"5P"},{"studentId":19,"class":"9G"},{"studentId":20,"class":"5R"},
{"studentId":21,"class":"8N"},{"studentId":22,"class":"2F"},{"studentId":23,"class":"100"},
{"studentId":24,"class":"1P"},{"studentId":25,"class":"6R"},{"studentId":26,"class":"8W"},
{"studentId":27,"class":"9P"},{"studentId":28,"class":"5X"},{"studentId":29,"class":"2Z"},
{"studentId":30,"class":"8U"},{"studentId":31,"class":"7D"},{"studentId":32,"class":"11Q"},
{"studentId":33,"class":"1L"},{"studentId":34,"class":"2W"},{"studentId":35,"class":"81"},
{"studentId":36,"class":"2U"},{"studentId":37,"class":"8L"},{"studentId":38,"class":"3V"},
```  
[@carlton](/u/carlton) my answer got excepted before but now it is only working on the terminal after I modified the code but when I paste the url in the answer box it is again showing error

---

**post_id:** 579910  
**author:** 23F300327  
**timestamp:** 2025-01-15T07:10:33.142Z

Hi Mishkat,

The GA url encoded parameter is `class`  
In your screenshot, you are using `class_`  
Your code that we examined earlier also accepts `class_` as the parameter instead of `class` as required by the GA  
The GA will test your deployment by sending it a request with the url encoded parameter `class`

---

**post_id:** 580435  
**author:** carlton  
**timestamp:** 2025-01-16T08:27:32.543Z

image description: A web page displaying an error message related to the ngrok service. The error indicates a failure to connect to a web service at "http://localhost:5000." The page offers troubleshooting steps for both developers and visitors.
image text:
ERR\_NGROK\_8012
Traffic was successfully tunneled to the ngrok agent, but the agent failed to establish a connection to the upstream web
service at http://localhost:5000. The error encountered was:
dial tcp [::1]:5000: connect: connection refused
Get help with this error
If you're the developer of this page
On the machine where the ngrok agent is running, make sure a web service is running on http://localhost:5000. Try to cURL or open
the address in a browser to see that you get the correct response.
Check out the docs to get help with this error.
If you're a visitor of this page
Wait a few minutes and refresh the page. If that still doesn't work, please contact the developer of this page for more information.
Powered by ngrok
  
[@s.anand](/u/s.anand) [@carlton](/u/carlton) I am facing this issue i have run the entire thing thrice but still i am facing this issue, what should I do?

---

**post_id:** 580590  
**author:** kushabarodekar  
**timestamp:** 2025-01-16T13:35:41.934Z

```
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the specified CSV file
students = []
with open('/Users/mish/Downloads/q-fastapi.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({
            "studentId": int(row["studentId"]),
            "class": row["class"]
        })

@app.get("/api")
async def get_students(class: Optional[List[str]] = Query(None)): 
    """
    Retrieves a list of students, optionally filtered by class.

Args:
        class: A list of class names to filter by. If None, returns all students.

Returns:
        A dictionary containing a list of students.
    """
    print(f"Requested classes: {class}")  # Debugging line
    if class:
        filtered_students = [student for student in students if student["class"] in class]
    else:
        filtered_students = students
    print(f"Filtered students: {filtered_students}")  # Debugging line
    return {"students": filtered_students}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

```

[@Jivraj](/u/jivraj) this is the code I’m executing which is not getting accepted in the answer box the last time I modified the code it got accepted and I also saved the answer but when I reopened the page till now it is not getting accepted

---

**post_id:** 580668  
**author:** 23f2000983  
**timestamp:** 2025-01-16T16:46:03.955Z

Hi Mishkat,

In your code, the word `class` is a reserved keyword in python. So simply changing `class_` to `class` is not going to work. The *only* thing you need to change is the keyword accepted by the api *not* the variable name used inside your function. Hope that helps you narrow down the problem.

Kind regards

---

**post_id:** 581310  
**author:** kushabarodekar  
**timestamp:** 2025-01-17T16:13:14.478Z

Hi Team ,

For GA - 2 , Question 6:  
I am done with the code, deployed same on vercel.  
And It is working fine gives correct json response as expected in browser.

But When I try to that on portal It gives me “CORS Missing Allow Origin” Error.  
image description: The image shows a web browser's developer tools, with a section detailing a network request related to a Vercel API. The top portion of the image includes code instructions, specifically related to creating and deploying a Python app to Vercel. There is an error message indicating a network problem when attempting to fetch a resource. The bottom part shows the network activity, including the request and response headers.
image text: Download this q-vercel-python.json which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON
response with the marks of the names X and Y like this:
{ "marks": [10,20]}
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://vercel-
shagra-barodekars-projects.vercel.app/api
TypeError: NetworkError when attempting to fetch resource.
7 Create a GitHub Action (1.5 marks)
Inspector Console Debugger Network {} Style Editor Performance Memory Storage Accessibility Application
Filter URLs
Status Met... Domain File Type Initiator Transferred Si... Headers Cookies Request Response Timings Stack Trace Security All HTML CSS JS XHR Fonts Images Media WS Other
Disable Cache No Throttling
Block Resend

I have added “Access-Control-Allow-Origin” as “\*” for allowing request from any origin.

I get the correct response in browser but it fails in quiz portal.  
Can anyone please suggest what exactly I am missing here.

Thanks  
Kushagra

---

**post_id:** 581401  
**author:** Jivraj  
**timestamp:** 2025-01-17T21:59:24.820Z

Here's a description of the image:
The image shows a screenshot of a web page with a question and an error message. A text input field is present.
image text: What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://your-app2.vercel.app/api
TypeError: Failed to fetch
  
Hello, this is working when I put in parameters, but not when I submit on quiz portal. What to do?

---

**post_id:** 581402  
**author:** Jivraj  
**timestamp:** 2025-01-17T22:16:46.059Z

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj) ,  
Can you please help on this one.

---

**post_id:** 581416  
**author:** 23f2003751  
**timestamp:** 2025-01-17T05:35:36.902Z

Hi Kushagra,

can you share vercel url so that I can test.

Kind regards

---

**post_id:** 581405  
**author:** Jivraj  
**timestamp:** 2025-01-17T22:31:12.505Z

Hi Aindree,

I tried to send a request to your application `https://your-app2.vercel.app/api` with url encoded parameter `class=7Q`. It should fetch marks of that particular class. But in response it sends `{"marks": []}`.

Check if your csv file is correct. Also check if code is correct.

Kind regards  
Jivraj

---

**post_id:** 581561  
**author:** 23f2000983  
**timestamp:** 2025-01-18T08:45:27.617Z

For the questions such as cors, llm i have to locally run the code and submit it.After a while if i have to submit it again the prev url that i have submitted is throwing an error. Maybe becaue it is checking the url again at the time of submission. Fix this issue, the similar issue lies with the image compression problem. when i upload the code and checks and submits it at that time i got the marks but after sometime if i make the change in some other question the file that i uploaded prev is nowhere to found.so please fix this issue  
[@s.anand](/u/s.anand)

---

**post_id:** 581587  
**author:** kushabarodekar  
**timestamp:** 2025-01-18T10:00:50.108Z

Hi Tushar,

For questions which require submitting a url, when you click on save button all those server’s should be running.

For that image uploading question one solution would be to keep image in a particular directory, and then upload from there every time you make a submission.

Kind regards  
Jivraj

---

**post_id:** 581805  
**author:** 22f3001307  
**timestamp:** 2025-01-19T04:40:58.902Z

<https://your-app2.vercel.app/api?name=gy5&name=nk&name=ySOPVNRtt>  
is the one I tried. Somehow it worked correctly at my end. I’ll recheck though. Thanks

---

**post_id:** 582002  
**author:** 23f2005138  
**timestamp:** 2025-01-19T12:52:31.848Z

Hi Jivraj,

I tried with another public url, It is working for me now.

Thanks  
Kushagra

---

**post_id:** 582003  
**author:** Akash1  
**timestamp:** 2025-01-19T12:55:34.118Z

Hi,  
I have downloaded the Llamafile as instructed. But I can’t run it on my mac. It says command not found.  
Pls let me know what I should do.

---

**post_id:** 582206  
**author:** 23f2003751  
**timestamp:** 2025-01-19T10:56:23.313Z

For the Q.2 on image compression, for PNG, SVG or WEBP files, I’m getting the error “Could not process image. Is it browser supported image? Image pixels do not match the original” (I believe the last part is not applicable as the image was not processed ). Visually, I could not find any difference between the two files and the size of new file is less than 1,500 bytes.

Tried through Chrome v132.0.6834.83 without any add-ons/extensions.

Here's a description of the image:
The image displays an error message related to an image upload. It contains a file upload section and an error message.
image text: Upload your losslessly compressed image (less than 1,500 bytes)
Choose File shapes\_compressed.png
Error: Could not process image. Is it a browser-supported image? Image pixels do not match the original

---

**post_id:** 582025  
**author:** Jivraj  
**timestamp:** 2025-01-19T13:20:12.288Z

this mainly happens when ngrok able to tunnel to given port but nothing is running on that port,so check that first

---

**post_id:** 582046  
**author:** 23f2003751  
**timestamp:** 2025-01-19T13:50:57.854Z

i am getting this error  
Here's a brief description of the image:
The image is a dark-themed webpage displaying instructions related to deploying a Python app to Vercel. The text explains how to create an API endpoint. A URL is provided, along with a "TypeError: Failed to fetch" message.
image text:
Download this q-vercel-python.json which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the
marks of the names X and Y like this:
{ "marks": [10, 20] }
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://student-marks-gb9zwxnfx-tushars-projects-f2a54030.vercel.app/api
TypeError: Failed to fetch
  
i have tried to submit it will a query as well but than also it is giving me the same error.But for me it is giving me the correct output.  
Here's a description of the image:
The image shows a web browser window displaying a JSON response. The URL in the address bar indicates it is related to a student marks project. The content of the JSON response includes "marks" with the values [65, 74].
image text:
```json
{
"marks": [65, 74]
}
```
  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

**post_id:** 582213  
**author:** carlton  
**timestamp:** 2025-01-20T05:36:20.460Z

Hi Tushar,

Make sure cors are enabled, if so can you share screenshot of console tab in browser?

kind regards  
Jivraj

---

**post_id:** 582214  
**author:** 23F300327  
**timestamp:** 2025-01-18T19:38:22.246Z

```
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api",
      "dest": "app.py"
    }
  ],
  "headers": [
    {
      "source": "/api/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Credentials", "value": "true" },
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET,OPTIONS,PATCH,DELETE,POST,PUT"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version"
        }
      ]
    }
  ]
}

```

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
i have added the header key in order to use the cors as said in the vercel doc but still i am getting that error.  
what to do?  
i have added the cors in the app.py file as well

```
from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the data
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.route("/api", methods=["GET"])
def get_marks():
    names = request.args.getlist("name")
    marks = [student["marks"] for student in data if student["name"] in names]
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()

```

<https://student-marks-4vsd75x3f-tushars-projects-f2a54030.vercel.app/api>

---

**post_id:** 582220  
**author:** carlton  
**timestamp:** 2025-01-20T05:48:46.646Z

[@23f2003751](/u/23f2003751)  
While I understand why you might choose to use `flask` due to your familiarity with it,  
the `http.server` library is just very simple to use.

The **only extra line of code** you would need inside your `get` request if you used the `http.server` library would be:

`self.send_header("Access-Control-Allow-Origin", "*")`

Try to rewrite your code using `http.server` library so that your debugging for simple tasks like this is easy.

The boilerplate code for a `get` request using the `http.server` library was already given in Q6. So you have to do very minimal modifications to it and it works like a charm.

Kind regards

---

**post_id:** 582479  
**author:** Divya1  
**timestamp:** 2025-01-20T16:46:54.354Z

In GA-2 Q6, Q9 and Q10 answers are not getting accepted on my device(Mac book air) but when I am executing the same thing from my friends device(windows 11 pro) it is getting accepted and then when I try to save it from her device and then do the final submission from my my device then again the answers are not getting submitted for the same three questions.

[@s.anand](/u/s.anand) Sir please help me through this

---

**post_id:** 582633  
**author:** 23F300327  
**timestamp:** 2025-01-21T08:09:40.078Z

[@23F300327](/u/23f300327) You would have to be a bit more specific on what exactly is the nature of your error on your machine.

GA2 - Q6 has no dependency on the OS or your computer. It uses Github (an online platform), it uses Vercel (an online platform) and thats it. I have a macbook air and it works fine for GA2 - Q6. Since the code you are running has no such dependency on your local machine it should not have problems.

Now typical problems for example Q6 (and other questions) might involve the use of CORS. So for example the url might work in your browser when you access the vercel deployment url directly, but when using it via the GA, the request triggers a CORS error, because a third party application is requesting rather than you directly.

Also the live sessions on [youtube](https://youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C&si=NE4LEQe48XfzAYbc) will address some of these deployment related issues that students are facing.

There will be session 2025-01-20T14:30:00Z→2025-01-20T16:30:00Z which will be recorded that will address any concerns on how to use these technologies and libraries.

The session is in your course calendar and the meet link is [meet.google.com/baz-ayij-ziy](http://meet.google.com/baz-ayij-ziy)

Kind regards

---

**post_id:** 582645  
**author:** 23F300327  
**timestamp:** 2025-01-21T08:35:03.754Z

1.how to sign into github

2.what is user name there…it is not working

---

**post_id:** 582661  
**author:** carlton  
**timestamp:** 2025-01-21T09:02:30.157Z

image description: The image shows a browser window with a black background. In the address bar, there is a URL: https://vercel-fastapi-aa0kdktjz-mishkat02s-projects.vercel.app/api?name=IE&name=G6k. Below the address bar, the text "Pretty print" and a json object containing the key "marks" with the value [50, 53].
image text: Pretty print
{"marks": [50,53]}
  
when I paste the url it is showing TypeError: Failed to fetch  
my code:

```
import json
import pandas as pd
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# Load the CSV file into a DataFrame
try:
    data = pd.read_csv('marks.csv')
except FileNotFoundError:
    data = None

class MarksHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if data is None:
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "marks.csv not found"}).encode())
            return

parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        names = query_params.get('name', [])  # Get list of names from query parameters

marks = [
            int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
            for name in names
        ]

response = json.dumps({"marks": marks})
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # Enable CORS
        self.end_headers()
        self.wfile.write(response.encode())

if __name__ == "__main__":
    server_address = ('', 8000)  # Run on port 8000
    httpd = HTTPServer(server_address, MarksHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

```

---

**post_id:** 582864  
**author:** 23f2003717  
**timestamp:** 2025-01-21T15:53:27.561Z

```
from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the CSV file into a DataFrame
data = pd.read_csv('marks.csv')

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the list of names from query parameters
    names = request.args.getlist('name')
    
    # Ensure the order of the names in the response matches the query
    marks = [
        int(data[data['name'] == name]['marks'].values[0]) if not data[data['name'] == name].empty else None 
        for name in names
    ]
    
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)

```

this is the 2nd code I am trying but same error TypeError: Failed to fetch

---

**post_id:** 582892  
**author:** Divya1  
**timestamp:** 2025-01-21T16:44:47.511Z

[@23F300327](/u/23f300327)

Typically for a vercel application, and in particular for GA2-Q6, the applications are basically function calls. You are not expected to setup and run a local http server as you are doing in your code.

When a call is made to the endpoint which in this scenario is /api  
with parameters, only one function is required, i.e the function that handles the get request.

The rest is also automagically handled by vercel. There might be a conflict between vercel’s webserver deployment and the one you explicitly have encoded in your program.

That’s why if you see in the course content about vercel, the simplest API service that you can launch with vercel looks something like this

```
# api/index.py
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return

```

Notice there is no `if __name__ == "__main__":` code block.  
This would instruct the interpreter that this is the starting point of your module. Clearly we do not want that, we want vercel to handle all the backend server stuff because vercel might be running some preflight code before it runs your application.

`if __name__ == "__main__":` is used to execute some code **only** if the file was run directly, and not imported. In vercel, it might not be the starting point of the application.

Try rewriting it with just the required endpoint function inside the default `handler` class. Avoid custom named classes until you can get a working prototype working using the boilerplate that has been shared.

Another possible problem:  
By default, the JSON module encodes Unicode objects (such as str and Unicode) into the \u escape sequence when generating JSON data. The GA however is expecting a serialised UTF-8 JSON response instead. These might look the same on the screen but are not equivalent at the bytecode level. These encoding problems were covered in one of the videos that talked about encoding issues [TDS > Development Tools > unicode](https://tds.s-anand.net/#/unicode)

So converting your output to UTF-8 might fix it.

Let us know what worked. We are all learning from each other.

Kind regards

---

**post_id:** 582893  
**author:** Divya1  
**timestamp:** 2025-01-21T16:46:33.440Z

image description: A screenshot of a terminal-like interface with text regarding repository URLs and an error message. Key elements include a prompt asking for the repository URL, an example URL, and a provided URL with an error message.
image text: What is your repository URL? It will look like: https://github.com/USER/REPO
https://github.com/NAMAN-BERI/actions.git
Error: No runs found

even though its their

i don’t know why i am facing this issue anyone please check my git

* [GitHub - NAMAN-BERI/actions](https://github.com/NAMAN-BERI/actions.git)

---

**post_id:** 582897  
**author:** GaURaVinDeX  
**timestamp:** 2025-01-21T16:52:01.539Z

how to create a iitm account in github…i am not getting the username  
please guide  
its proceeding like this …for my user name  
image description: The image shows a form with the fields for Password and Username. The password field contains asterisks, indicating a hidden password. The username field has "navya" entered and a warning message says that "Username navya is not available". Also, suggestions are provided for similar usernames.
image text: Password
...
Password should be at least 15 characters OR at least 8 characters including a
number and a lowercase letter.
Username
navya
Username navya is not available.
navya-stack, navya-cmyk, or navya856 are available.

---

**post_id:** 583190  
**author:** Jivraj  
**timestamp:** 2025-01-22T09:21:40.762Z

Doubt :  
Should the 3rd question (github) done in the iitm github mail or any of the personal mail ?

---

**post_id:** 583198  
**author:** Jivraj  
**timestamp:** 2025-01-22T09:33:31.252Z

Im not able to get the ngrok question correct. I have attached a screenshot  
image description : The image shows a webpage with a title indicating a "Worker threw exception". The webpage contains error details, a ray ID, and a description of the error, along with information for the website owner.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://58e1-150-107-42-211.ngrok-free.app
Error: Response is not valid JSON: <!DOCTYPE html> <!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]--> <!--[if IE 7]> <html class="no-js ie7 oldie" lang="en-US"> <![endif]--> <!--[if IE 8]> <html class="no-js ie8 oldie" lang="en-US"> <![endif]--> <!--[if gt IE 8]><!--> <html class="no-js" lang="en-US"> <!--<![endif]--> <head> <title>Worker threw exception | exam.sanand.workers.dev | Cloudflare</title> <meta charset="UTF-8" /> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <meta http-equiv="X-UA-Compatible" content="IE=Edge" /> <meta name="robots" content="noindex, nofollow" /> <meta name="viewport" content="width=device-width, initial-scale=1" /> <link rel="stylesheet" id="cf\_styles-css" href="/cdn-cgi/styles/cf.errors.css" /> <!--[if lt IE 9]> <link rel="stylesheet" id='cf\_styles-ie-css' href="/cdn-cgi/styles/cf.errors.ie.css" /> <![endif]--> <style>body{margin:0;padding:0}</style> <!--[if gte IE 10]><!--> <script> if (!navigator.cookieEnabled) {window.addEventListener('DOMContentLoaded', function () { var cookieEl = document.getElementById('cookie-alert'); cookieEl.style.display = 'block'; }) } </script> <!--<![endif]--> </head> <body> <div id="cf-wrapper"> <div class="cf-alert cf-alert-error cf-cookie-error" id="cookie-alert" data-translate="enable\_cookies" > Please enable cookies.</div> <div id="cf-error-details" class="cf-error-details-wrapper"> <div class="cf-wrapper cf-header cf-error-overview"> <h1> <span class="cf-error-type" data-translate="error">Error</span> <span class="cf-error-code">1101</span> <small class="heading-ray-id">Ray ID: 9058ac347bd6dc94 &bull; 2025-01-21 16:27:37 UTC</small> </h1> <h2 class="cf-subheadline" data-translate="error\_desc">Worker threw exception</h2> </div> <!-- /.header --> <section> </section> <!-- spacer --> <div class="cf-section cf-wrapper"> <div class="cf-columns two"> <div class="cf-column"> <h2 data-translate="what\_happened">What happened?</h2> <p>You've requested a page on a website (exam.sanand.workers.dev) that is on the <a href="https://www.cloudflare.com/5xx-error-landing/" target="\_blank">Cloudflare</a> network. An unknown error occurred while rendering the page.</p> </div> <div class="cf-column"> <h2 data-translate="what\_can\_i\_do">What can I do?</h2> <p> <strong>If you are the owner of this website:</strong><br />you should <a href="https://www.cloudflare.com/login?utm\_source=error\_100x" target="\_blank">login to Cloudflare</a> and check the error logs for exam.sanand.workers.dev.</p> </div> </div> </div> <!-- /.section --> <div class="cf-error-footer cf-wrapper w-240 lg:w-full py-10 sm:py-4 sm:px-8 mx-auto text-center sm:text-left border-solid border-0 border-t border-gray-300"> <p class="text-13"> <span class="cf-footer-item sm:block sm:mb-1">Cloudflare Ray ID: <strong class="font-semibold">9058ac347bd6dc94</strong></span> <span class="cf-footer-separator sm:hidden"> &bull;</span> <span id="cf-footer-item-ip" class="cf-footer-item hidden sm:block sm:mb-1"> Your IP: <button type="button" id="cf-footer-ip-reveal" class="cf-footer-ip-reveal-btn">Click to reveal</button> <span class="hidden" id="cf-footer-ip">150.107.42.211</span> <span class="cf-footer-separator sm:hidden"> &bull;</span> </span> <span class="cf-footer-item sm:block sm:mb-1"> <span>Performance &amp; security by</span> <a rel="noopener noreferrer" href="https://www.cloudflare.com/5xx-error-landing" id="brand\_link" target="\_blank">Cloudflare</a></span> </p> <script>(function(){function d(){var b=a.getElementById("cf-footer-item-ip"),c=a.getElementById("cf-footer-ip-reveal");b&&"classList"in b&&(b.classList.remove("hidden"),c.addEventListener("click",function(){c.classList.add("hidden");a.getElementById("cf-footer-ip").classList.remove("hidden")}))}var a=document;document.addEventListener&&a.addEventListener("DOMContentLoaded",d)})(); </script> </div> <!-- /.error-footer --> </div> <!-- /#cf-error-details --> </div> <!-- /#cf-wrapper --> <script> window.\_cf\_translation = {}; </script> </body> </html>
  
The link is working fine in browser and running the LLM there.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

**post_id:** 583199  
**author:** Jivraj  
**timestamp:** 2025-01-22T09:35:12.607Z

Hi Mishkat,

I think url that you are submitting is wrong one. In below image there are two url’s under Domains those would be correct url’s to be submitted.  
For example `https://tds21jan.vercel.app/`.

Here's the image description:
The image shows a section from a website with a dark theme, possibly a deployment platform. The upper part of the frame highlights a "404 NOT\_FOUND" error. It also displays details like the code and ID. On the right side there are details about a deployment, domains, status (ready) and source code access. At the bottom is a prompt to connect the project with a Git repository.
image text: 404: NOT\_FOUND
Code: 'NOT\_FOUND
ID: sf01::x147q-1737473362971-adc9c00e6fa8'
Read our documentation to learn more about this error.
Deployment
tds21jan-ghtj3xr7w-jivraj-18s-projects.vercel.app
Domains
tds21jan.vercel.app tds21jan-jivraj-18s-projects.vercel.app +1
Status
Created:
Ready 18h ago by jivraj-18
Source
<> View code
> vercel deploy
Connect your Project with a Git repository to create a Production Deployment.
Connect Git re

kind regards  
Jivraj

---

**post_id:** 583208  
**author:** 23F300327  
**timestamp:** 2025-01-22T09:48:18.254Z

Hi Gaurav,

This is problem with Cloudflare content delivery service where application is served. Try it out after some time it will work.

Kind regards

---

**post_id:** 583209  
**author:** Jivraj  
**timestamp:** 2025-01-22T09:48:35.490Z

Hi Divya,

You can use any github account, it need not be associated with IITM account.

---

**post_id:** 583216  
**author:** carlton  
**timestamp:** 2025-01-22T10:00:15.756Z

Here's a description of the image:
The image shows the overview page of a project named "vercel-ga2" within the Vercel platform. The page provides information about the project's deployments, domains, and other related details. The production deployment is highlighted, showing its status as "Ready" and the time it was created. There's also a preview deployment area. The page also has navigation options such as "Project", "Deployments", "Analytics", etc.
image text:
Graded Assignment 2 ::
vercel.com/mishkat02s-projects/vercel-ga2
mishkat02's projects Hobby
vercel-ga2
Project Deployments Analytics Speed Insights Logs Observability Firewall Storage Settings
vercel-ga2
Production Deployment
Deployment
vercel-ga2-f7la455gq-mishkat02s-projects.vercel.app
Domains
vercel-ga2.vercel.app +2
Status Created
• Ready 22h ago by mishkat02
Source
<> View code
> vercel deploy
Connect your Project with a Git repository to create a Production Deployment.
Preview Deployments
  
I tried both the url in domain still it is showing failed to fetch

---

**post_id:** 583228  
**author:** Jivraj  
**timestamp:** 2025-01-22T10:23:15.623Z

Hi NamanBeri,

Just remove `.git` it will work.

---

**post_id:** 583232  
**author:** 23F300327  
**timestamp:** 2025-01-22T10:29:27.059Z

[UPDATE 22/02/2025]: GA 2 NEW DEADLINE: 2025-02-02T18:29:00Z

---

**post_id:** 583576  
**author:** roy2003  
**timestamp:** 2025-01-22T16:06:08.129Z

I’m not sure of the exact reason for the issue, but there are different ways to deploy to Vercel. One approach is using a `vercel.json` configuration file, and another is adding headers directly in the API code.

You can follow [Gui Bibeau’s guide](https://www.frontend-devops.com/blog/python-on-vercel) to add CORS headers to your deployment setup. Also check the recording from yesterday’s session for more clarity in that session Carlton deployed application directly from github repository. If you’re still facing issues, you can join today’s session at 9 PM.

For deploying a Flask or FastAPI app to Vercel, refer to [this guide on DEV Community](https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k). I’ve tried both methods, and they work well.

---

**post_id:** 583600  
**author:** Jivraj  
**timestamp:** 2025-01-22T16:20:28.196Z

Okay, I’ll try to it again using these methods and let you know  
Thank you

---

**post_id:** 583636  
**author:** roy2003  
**timestamp:** 2025-01-22T16:46:41.766Z

Sir im facing problem in week2 ga question 10. At first when i have pasted the URL its showing correct and i saved that i got 8. When i refresh the page and reload the same 8scored but its showing 5.5 and the URL for lamma file showing wrong . why is like that? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

my student email: 23f1001348@ds.study.iitm.ac.in  
image description: The image is a screenshot of a webpage with instructions, recent saves, and other related information. At the top, there are the time, score, and buttons for "Check" and "Save". The main body of the page contains instructions numbered from 1 to 7, covering aspects like learning, checking answers, saving, reloading, browser behavior, using resources, and the hackability of the content. Below the instructions, there's a section for "Have questions?" with a link to "Join the discussion on Discourse". Further down, it displays user login information and a "Logout" button. The "Recent saves" section shows the history of saved progress with timestamps and scores. At the bottom, there are instructions for downloading and running a Llamafile, creating a tunnel, and displaying an ngrok URL. Finally, an error message related to "ngrok-free.app" and HTML code is present.
image text: 11:59 pm IST Score: 5.5 / 10 Check Save
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the qu
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can c
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will be e
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change exce
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different bro
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use an
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. Th
Have questions? Join the discussion on Discourse
You are logged in as 23f1001348@ds.study.iitm.ac.in.
Logout
Recent saves
Loaded from 1/22/2025, 1:31:03 PM. Score: 8
Loaded from 1/22/2025, 1:30:56 PM. Score: 8
Reload from 1/22/2025, 1:07:45 PM. Score: 7
Download Llamafile. Run the Llama-3.2-18-Instruct.06 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://0ed0-103-76-82-164.ngrok-free.app
Error: Response is not valid JSON: <!DOCTYPE html> <html class="h-full" lang="en-US" dir="ltr"> <head> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-
Regular-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Regularltalic-WebS.woff" as="font"
type="font/woff" crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Medium-WebS.woff" as="font" type="font/woff"
crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Semibold-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link
rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Mediumltalic-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-Text.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-TextItalic.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBold.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBoldItalic.woff" as="font" type="font/woff" crossorigin="anonymous" /> <meta charset="utf-8"> <meta name="author"
content="ngrok"> <meta name="description" content="ngrok is the fastest way to put anything on the internet with a single command."> <meta name="robots" content="noindex, nofollow"> <meta
name="viewport" content="width=device-width, initial-scale=1"> <link id="style" rel="stylesheet" href="https://cdn.ngrok.com/static/css/error.css"> <noscript> Tunnel Oed0-103-76-82-164.ngrok-
free.app not found (ERR\_NGROK\_3200)</noscript> <script id="script" src="https://cdn.ngrok.com/static/js/error.js" type="text/javascript"></script> </head> <body class="h-full" id="ngrok"> <div
id="root" data-
payload="eyJjZG5CYXNIIjoiaHR0cHM6Ly9jZG4ubmdyb2suY29tLylslmNvZGUiOilzMjAwliwibWVzc2FnZSI6IIR1bm5lbCAwZWQwLTEwMy03Ni04Mi0xNjQubmdyb2stZnJIZS5hcHAgbm90IGZvdW5kliwidGI0bGU
iOiJob3QgRm91bmQifQ=="></div> </body> </html>

---

**post_id:** 584109  
**author:** 23f2003717  
**timestamp:** 2025-01-23T13:25:40.286Z

From image that you have shared, it explains ngrok tunnel that you are submitting in answer is not running.

For any assignment if it involves running some server then you would need to keep all the server’s running when you submit

Kind regards  
Jivraj

---

**post_id:** 584143  
**author:** 21f3000031  
**timestamp:** 2025-01-23T14:54:10.445Z

that means at every time i need to run the system at backend when i submit. hows that possible it requires very lengthy process. When i had submitted thats showing correct again i have reloaded the previous one showing wrong.

---

**post_id:** 584149  
**author:** 23ds1000022  
**timestamp:** 2025-01-23T10:43:58.135Z

Here's a brief description of the image:
The image is a dark-themed display containing text related to the setup of a "Llamafile" model. It instructs the user on how to create a tunnel to the Llamafile server using "ngrok" and provides an example URL. There's also an error message stating that the response is not valid JSON.
image text:
Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://4d63-2409-40d0-100e-46d9-419e-d652-5b0e-f8fe.ngrok-free.app/
Error: Response is not valid JSON: error code: 524

any one please guide what is this error - everything is working when i open this link and even i can view it is making request to the server

18:43:30.941 IST GET /json-schema-to-grammar.mjs 200 OK

which means server is working properly then i dont know whats the issue

---

**post_id:** 584193  
**author:** 23f2004169  
**timestamp:** 2025-01-23T17:36:33.864Z

sir ühere i üill get the live session link or notification

---

**post_id:** 584249  
**author:** Jivraj  
**timestamp:** 2025-01-23T21:15:43.857Z

i am getting this error in the last question. pls help to solve  
Here's a description of the image:
The image is a screenshot of a web browser window. The webpage appears to be related to a coding exercise or tutorial. The top bar shows the browser's address with a URL, and some menu options. The central part of the image displays a webpage content, that includes instructions to download a "Llamafile" and create a tunnel. A red box highlights an error response message.
image text: Chrome File Edit View History Bookmarks Profiles Tab Window Help
exam.sanand.workers.dev/tds-2025-01-ga2
Due Sun, 26 Jan, 2025, 11:59 pm IST Score: 5.5 / 10 Check Save
Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://b1ae-117-198-90-156.ngrok-free.app
Error: Response is not valid JSON: <!DOCTYPE HTML> <html lang="en"> <head> <meta charset="utf-8"> <title>Error response</title>
</head> <body> <h1>Error response</h1> <p>Error code: 501</p> <p>Message: Unsupported method ('POST').</p> <p>Error code
explanation: 501 - Server does not support this operation.</p> </body> </html>

i am unable to open the dashboard of ngrok in laptop but i did the authtoken genration in mobile and used it

---

**post_id:** 584250  
**author:** Jivraj  
**timestamp:** 2025-01-23T21:18:44.212Z

image description: The image shows an error message from ngrok, indicating that the ngrok agent failed to connect to the upstream web service. The page displays a progress bar indicating the steps involved, with a red X at "Your Service". The error message provides details about the failure, suggesting a connection refused error on a specific port. Instructions are provided for developers and visitors, including troubleshooting steps.
image text: ERR\_NGROK\_8012
Traffic was successfully tunneled to the ngrok agent, but the agent failed to establish a connection to the upstream web service at undefined://localhost:52525. The error encountered was:
dial tcp [::1]:52525: connect: connection refused
Get help with this error
If you're the developer of this page
On the machine where the ngrok agent is running, make sure a web service is running on undefined://localhost:52525. Try to cURL or open the address in a browser to see that you get the correct response.
Check out the docs to get help with this error.
If you're a visitor of this page
Wait a few minutes and refresh the page. If that still doesn't work, please contact the developer of this page for more information.
  
I tried using github codespace for ngrok and cmd for llamafile, but im still encountering the same error no matter which port i use [@Jivraj](/u/jivraj)

---

**post_id:** 584251  
**author:** Jivraj  
**timestamp:** 2025-01-23T21:26:50.926Z

Hi Naman,

error code 524 is generally because of timeout in response, one thing you can check is if there is load on Llama server as information that I got by a google search [Error 524: A Timeout Occurred (What It Is & How to Fix It)](https://www.lifewire.com/error-524-a-timeout-occurred-4782741). I tried submitting now while replying at 2:45 am it was working fine.

[@s.anand](/u/s.anand) Is there any problem from our end, such as tds hosting server receiving lots of traffic on website.

---

**post_id:** 584252  
**author:** Jivraj  
**timestamp:** 2025-01-23T21:33:27.479Z

Hi daniyal,

[Tools in Data Science](https://tds.s-anand.net/#/?id=jan-2025-links) you can get calendra invite link from here and add to google calendra.

---

**post_id:** 584262  
**author:** 23f2005138  
**timestamp:** 2025-01-24T02:30:10.234Z

Hi Srividhya,

This error is because you are trying to access a feature of ngrok which requires to pay [ERR\_NGROK\_501 | ngrok documentation](https://ngrok.com/docs/errors/err_ngrok_501/#:~:text=Only%20Personal%2C%20Pro%2C%20Enterprise%2C%20or%20Pay-as-you-go%20accounts%20can,resolving%20this%20error%2C%20please%20reach%20out%20to%20support%40ngrok.com).

I think you didn’t use authtoken to authenticate through your laptop. Follow second step on this page [Quickstart | ngrok documentation](https://ngrok.com/docs/getting-started/) to authenticate.

kind regards  
Jivraj

---

**post_id:** 584297  
**author:** roy2003  
**timestamp:** 2025-01-24T04:53:27.747Z

Hi Irina,

This issue is because localhost is not there is no server available to listen on localhost.You are running ngrok in codespace but Llama server in local machine. run both of them in same machine either codespace or local machine.

Here is reference of error [ERR\_NGROK\_8012 | ngrok documentation](https://ngrok.com/docs/errors/err_ngrok_8012/)

kind regards  
Jivraj

---

**post_id:** 584327  
**author:** 23f2003853  
**timestamp:** 2025-01-24T05:55:53.028Z

[@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) Dear Sir, could you please let me know how to proceed with this as I’m still getting the same error.

---

**post_id:** 584384  
**author:** 23f2003717  
**timestamp:** 2025-01-24T07:53:36.408Z

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
sir please reply

---

**post_id:** 584399  
**author:** 23f2003853  
**timestamp:** 2025-01-24T08:08:25.705Z

Regarding question no. 9 Web Framework: FastAPI. I got the following error for the answer to the question  
image description: The image shows a computer screen with text related to API endpoints and error messages, likely related to a coding task. The top portion of the screen outlines instructions for retrieving student data using a query parameter "class" in an API call. There are examples of how to use the query parameter. There is also a CORS note and the API endpoint. In the middle of the screen, there is an error message, suggesting a mismatch between the expected and actual responses. The bottom of the image contains the desktop taskbar and the time.
image text: If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A /api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
Error: Response undefined does not match expected [["studentid":67,"class":"6X"],["studentid":86,"class":"5T"],["studentid":91,"class":"5T"],["studentid":187,"class":"7B"],["studentid":217,"class":"6X"],["studentid":221,"class":"5T"],["studentid":408,"class":"6X"],["studentid":471,"class":"22"],["studentid":708,"class":"6X"],["studentid":734,"class":"5T"],["studentid":735,"class":"22"],["studentid":928,"class":"7B"],["studentid":1007,"class":"5T"],["studentid":1029,"class":"5T"],["studentid":1090,"class":"7B"],["studentid":1106,"class":"22"],["studentid":1154,"class":"6X"],["studentid":1313,"class":"6X"],["studentid":1354,"class":"6X"],["studentid":1414,"class":"6X"],["studentid":1422,"class":"6X"],["studentid":1429,"class":"22"],["studentid":1494,"class":"7B"],["studentid":1994,"class":"7B"]]
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
06:54 24-01-2025 ENG
  
But when I run the url in my browser I got the following response  
Here's a description of the image:
The image displays a webpage showing JSON data. The URL in the browser's address bar is "127.0.0.1:8000/api?class=6X&class=5T&class=78&class=22". Below the address bar, the text "Pretty-print" is displayed. The main body of the page contains a list of JSON objects, each representing a student with "studentId" and "class" attributes. The footer shows the current time and date.
image text:
← 127.0.0.1:8000/api?class=6X&class=5T&class=78&class=22
Pretty-print
[{"studentId":67,"class":"6X"}, {"studentId":86, "class":"5T"}, {"studentId":91, "class":"5T"}, {"studentId":187, "class":"78"}, {"studentId":217, "class":"6X"},
{"studentId":221,"class":"5T"}, {"studentId":408, "class":"6X"}, {"studentId":471, "class":"22"}, {"studentId":708, "class":"6X"}, {"studentId":734, "class":"5T"},
{"studentId":735, "class":"22"}, {"studentId":928, "class":"78"}, {"studentId":1007, "class":"5T"}, {"studentId":1029, "class":"5T"}, {"studentId":1090, "class":"78"},
{"studentId":1106, "class":"22"}, {"studentId":1154, "class":"6X"}, {"studentId":1313, "class":"6X"}, {"studentId":1354, "class":"6X"}, {"studentId":1414, "class":"6X"},
{"studentId":1422, "class":"6X"}, {"studentId":1429, "class":"22"}, {"studentId":1494, "class":"78"}, {"studentId":1994, "class":"78"}]
☆
90 ENG
06:55
24-01-2025
  
I have checked both the expected result from the assignment and result from direct running of url both are same. I don’t find any difference.  
[@carlton](/u/carlton) can you clarify where went wrong

---

**post_id:** 584532  
**author:** Divya1  
**timestamp:** 2025-01-24T13:44:41.940Z

Thank You Now it’s working and I have Done Everything. But just a Question while doing it last time i had my own webpage for llama open is their any chance it could made issue even if i was not using it, it was just open. because this time , before submitting i closed it first, i don’t know why but just did and it went well.

---

**post_id:** 584720  
**author:** Jivraj  
**timestamp:** 2025-01-25T06:10:32.807Z

Can any one help me to fix the following error in respect to answer to question 10  
image description: The image is a screenshot of a web page with instructions. It is primarily white, with some text and two buttons at the bottom. The primary text is a set of instructions to use the ngrok and includes a URL that triggers an error.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6\_K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://6eb1-27-7-78-14.ngrok-free.
Error: Response is not valid JSON: error code: 1016
Check Save

---

**post_id:** 584742  
**author:** roy2003  
**timestamp:** 2025-01-22T16:01:06.475Z

image description: The image is a dark-themed screenshot of a webpage, possibly related to GitHub Actions. It includes text instructions and code examples. Key elements include instructions on creating a GitHub action, example code, and an error message.
image text: How to handle secrets in GitHub Actions
How to run Github Actions on a Schedule
Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address 23f3001255@ds.study.iitm.ac.in.
For example:
jobs:
test:
steps:
name: 23f3001255@ds.study.iitm.ac.in
run: echo "Hello, world!"
Trigger the action and make sure it is the most recent action.
What is your repository URL? It will look like: https://github.com/USER/REPO
https://github.com/divya23f3001255/divya.github.io
Error: No step matches 23f3001255@ds.study.iitm.ac.in
①
  
can anyone please explain what’s the error and how to correct it ?

---

**post_id:** 584060  
**author:** Jivraj  
**timestamp:** 2025-01-23T11:57:45.289Z

Hi Sarang,

This is because image is expected to be in same number of pixels, Can you mention how you are trying to solve.

I used the web software that’s mentioned in the question to solve. [Squoosh](https://squoosh.app/)

---

**post_id:** 584749  
**author:** 23f2005138  
**timestamp:** 2025-01-25T07:08:13.117Z

Here's a brief description of the image:
The image is a webpage with instructions for a quiz or assignment. It displays instructions on how to complete the quiz, including checking answers, saving progress, and using resources. Below the instructions, it shows recent saves with their scores and timestamps. Additional instructions on downloading and creating a tunnel using ngrok are also present. It also provides an error message indicating a tunnel not found.
image text:
11:59 pm IST Score: 5.5 / 10 Check Save
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the qu
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can c
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will be e
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change exce
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different bro
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use an
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. Th
Have questions? Join the discussion on Discourse
You are logged in as 23f1001348@ds.study.iitm.ac.in.
Logout
Recent saves
Loaded from 1/22/2025, 1:31:03 PM. Score: 8
Loaded from 1/22/2025, 1:30:56 PM. Score: 8
Reload from 1/22/2025, 1:07:45 PM. Score: 7
Download Llamafile. Run the Llama-3.2-18-Instruct.06 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://0ed0-103-76-82-164.ngrok-free.app
①
Error: Response is not valid JSON: <!DOCTYPE html> <html class="h-full" lang="en-US" dir="ltr"> <head> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-
Regular-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Regularltalic-WebS.woff" as="font"
type="font/woff" crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Medium-WebS.woff" as="font" type="font/woff"
crossorigin="anonymous" /> <link rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Semibold-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link
rel="preload" href="https://cdn.ngrok.com/static/fonts/euclid-square/EuclidSquare-Mediumltalic-WebS.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-Text.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-TextItalic.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBold.woff" as="font" type="font/woff" crossorigin="anonymous" /> <link rel="preload"
href="https://cdn.ngrok.com/static/fonts/ibm-plex-mono/IBMPlexMono-SemiBoldItalic.woff" as="font" type="font/woff" crossorigin="anonymous" /> <meta charset="utf-8"> <meta name="author"
content="ngrok"> <meta name="description" content="ngrok is the fastest way to put anything on the internet with a single command."> <meta name="robots" content="noindex, nofollow"> <meta
name="viewport" content="width=device-width, initial-scale=1"> <link id="style" rel="stylesheet" href="https://cdn.ngrok.com/static/css/error.css"> <noscript> Tunnel Oed0-103-76-82-164.ngrok-
free.app not found (ERR\_NGROK\_3200)</noscript> <script id="script" src="https://cdn.ngrok.com/static/js/error.js" type="text/javascript"></script> </head> <body class="h-full" id="ngrok"> <div
id="root" data-
payload="eyJjZG5CYXNIIjoiaHR0cHM6Ly9jZG4ubmdyb2suY29tLylslmNvZGUiOilzMjAwliwibWVzc2FnZSI6IIR1bm5lbCAwZWQwLTEwMy03Ni04Mi0xNjQubmdyb2stZnJIZS5hcHAgbm90IGZvdW5kliwidGI0bGU
iOiJob3QgRm91bmQifQ=="></div> </body> </html>

---

**post_id:** 584967  
**author:** 23f2005138  
**timestamp:** 2025-01-25T13:23:13.730Z

Hi Shouvik,

This `ERR_NGROK_3200` error suggests that ngrok tunnel is not active at the moment.

kind regards  
Jivraj

---

**post_id:** 585135  
**author:** roy2003  
**timestamp:** 2025-01-25T17:22:48.305Z

[@Jivraj](/u/jivraj) Hello Sir, I’m also using Squoosh. The pixel size of the resulting image is 800 x 600 and the file size is 1,473 bytes. The steps I used to create the solution image:

1. Open Squoosh and load the image
2. In the dropdown in “Compress” section, select “OxiPNG”. Left the other options unchanged (Interlace checkbox is unchecked, Effort is at 2).
3. The resulting image is downloaded which has same pixel size as original image but file size is 1,473 bytes

Here's a description of the image:
The image is a screenshot of a UI for editing images. It has a dark gray background with blue highlights. It shows settings for image editing features like resize, reduce palette, and compress. The "Compress" section is highlighted. Within compress, there is a dropdown menu to select "OxiPNG," a checkbox labeled "Interlace", and a slider for "Effort". Below, the current compression progress is displayed as 63% with the file size as 1.41 kB. Finally, there is a download button.
image text: Edit Resize Reduce palette Compress OxiPNG Interlace Effort: ↓63% 1.41 kB 2

I also tried WebP with “Lossless” option selected and “Effort” increased to 9. This gives even smaller filesize at just 630 bytes. However, even that image is not accepted. The selected options for WebP are in the screenshot below.

image description: The image is a user interface for image editing. It shows options for resizing, reducing the palette, and compressing the image. The compression options include WebP format, lossless compression, effort level, slight loss, discrete tone image, and preserve transparent data. A button to download the image is also present.
image text: Edit, Resize, Reduce palette, Compress, WebP, Lossless, Effort:, Slight loss:, Discrete tone image, Preserve transparent data, 83%, 630 B, 9, 0

---

**post_id:** 585717  
**author:** 23f1002382  
**timestamp:** 2025-01-26T13:05:19.951Z

[@Jivraj](/u/jivraj) Hello Sir, I was able to submit the correct response now. Please consider this as solved (unless anyone else is facing similar issue)

---

**post_id:** 585985  
**author:** 23f1002382  
**timestamp:** 2025-01-26T15:21:40.326Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Contineously showing this sir. Even the server is running on background  
image description: The image shows a dark-themed interface with text and interactive elements. The text provides instructions related to downloading, running a file, and creating a tunnel using ngrok. There is also an error message about an invalid JSON response. Two buttons, "Check" (green) and "Save" (blue), are present at the bottom.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6\_K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://328e-43-251-171-164.ngrok-free.app/
Error: Response is not valid JSON: error code: 524
Check Save

---

**post_id:** 586535  
**author:** carlton  
**timestamp:** 2025-01-27T03:45:34.373Z

for the fast api question, would there be an issue if i am using code spaces my url would look like  
<https://symmetrical-space-cod-wrrjw5rw6xv7hvj9p-8000.app.github.dev/api>  
[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj)

Error is  
TypeError: Failed to fetch

image description: The image is a dark theme instruction/example about an API. It describes the expected behavior when the URL has a query parameter. The image shows a failed fetch error and provides an example API URL endpoint.
image text: f the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A./api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
h
TypeError: Failed to fetch
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.

I’m leaving the url running, you can see you get a dummy response(clicking the link), how should i go about it. I’d prefer to use codespaces. Please help me

No problems, I got it , SOLUTION just made the port public

---

**post_id:** 586539  
**author:** 23f1002382  
**timestamp:** 2025-01-27T04:20:07.358Z

for the tunneling, i am currently unable to do it has the ports are mismatched, I’m still working on the issue, but using codespaces and public ports i’ve achieved similar results and the question is marked right. Is this wrong/unethical. I will try to tunnel using ngrok though  
image description: The image shows a dark-themed interface with text instructions and a text box, likely for user input. The instructions involve downloading Llamafile, running a model, creating a tunnel using ngrok, and asking for the ngrok URL. A sample URL format is provided, and a 'Correct' label is at the bottom. The text box's content is obscured with a black rectangle.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
Correct

---

**post_id:** 586774  
**author:** 24f2006531  
**timestamp:** 2025-01-27T13:16:28.130Z

[@23f1002382](/u/23f1002382)

Nothing unethical about using codespaces and public ports. You solved it. Thats what TDS is about. Solutions. How you achieved is not very relevant. There is more than one way to skin a cat.

That being said, it good to find multiple ways to solve a problem, because a single method may not work everytime. Like for example in an ROE. You have no time and you got to be able to on the fly try different approaches, if one way does not work. Also purely from the point of view of being a “scientist”, its fun to be able to solve the question of how do you get a locally running server available on the web to a client. So in that sense, I understand the “spirit of your question”.

Most of the issues that most people face has to do with limited understanding of how applications and networks communicate. These are first and foremost apps that leverage various aspects of network communication. There are entire courses that deal with that subject, we want you to at least understand the basics. In that regard we have not actually provided you sufficient materials to get to grips with that. It is something we ought to address, but then students complain about having to learn too many things. Yet these are basic essentials!

So we are trying to get the balance right. For the most part many just muddle their way through it (like most of us I suspect), but some structured understanding of how these communications happen are probably worth their weight in gold for any aspiring data scientist because you then do not have to get IT nannies to deploy something quickly and you will wow your bosses as the guy/gal who just gets it done.

In the meanwhile:

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/7/975b777f1e9fe2da0778bfac72e555f8c315875f.jpeg "Network Ports Explained")](https://www.youtube.com/watch?v=g2fT-g9PX9o)

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/e/be3a9cfa13491650ab7a84c59b74fe3a050a30ee.jpeg "What is a Firewall?")](https://www.youtube.com/watch?v=kDEX1HXybrU)

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/0/401ecaa00e6cd0305d3ad12930dca10de1f1d13f.jpeg "Virtual Machines vs Containers")](https://www.youtube.com/watch?v=eyNBf1sqdBQ)

There are other great videos on the above channel, but these are probably the most relevant for us. Modern applications also leverage the same concept by using ports to talk to each other and provide services. These then have to be made visible to the outside world using some routing tables, but there are software that does this automagically. But sometimes when things break, understanding why its not working will go a long way towards helping you find the solution. And a fix might be as simple as an entry on a firewall or on a routing table (a one line CLI fix). And everyone thinks you are a genius, when in actual fact you just know a little bit more about the underlying architecture that glues everything.

Kind regards

---

**post_id:** 586779  
**author:** carlton  
**timestamp:** 2025-01-27T13:25:22.133Z

thank you. you have no idea how much this helps sir

---

**post_id:** 586907  
**author:** Jivraj  
**timestamp:** 2025-01-27T21:19:10.943Z

Once i close my local llm and close the nrgrok URL (after entering the answer and the answer being correct), the next time I refresh or check the answer in the Ga2 site, q10 gets marked wrong. I have to redo the entire process for it to be correct again.

Can you clarify why this is happening?

---

**post_id:** 587021  
**author:** 24f2006531  
**timestamp:** 2025-01-27T19:14:05.883Z

because it dynamically checks the answer each time a submit is done and if the ngrok tunnel and the service is not running at the time, then it marks it wrong.

Since every student’s answer is going to be unique (unlike a mathematics question), by necessity we have to dynamically check the answer each submit.

The workaround to prevent having to do it all over again, is to simply check all your answers that do not need active running servers first, then before doing a final save, run the servers for the required questions and the ngrok tunnel and submit to get the full marks.

Just dont forget that your last save is what gets graded. Just ignore for now once you got it working. Solve all the other ones first and then for the final submission “get all your ducks in a row.”

Kind regards

---

**post_id:** 586905  
**author:** Jivraj  
**timestamp:** 2025-01-27T21:09:02.560Z

hi [@23f2003853](/u/23f2003853)

I think you are running your application server inside a virtual machine because of which it doesn’t have visibility to outside world(request coming from other domains). So you would need to identify ipaddress of your virtual machine and would need to use that in place of `127.0.0.1`. Take help from GPT to identify ipaddress of virtual machine.

---

**post_id:** 586921  
**author:** 24f2006531  
**timestamp:** 2025-01-28T02:06:56.083Z

Hello Sir,

I’ve been working on question 6 and I’m facing this error where the marks are not ordered properly. I believe my code appends the marks based on the names that are inputted in the backend but I’m unable to identify the source of this issue. Please shed some light on the same.  
image description: The image is a screenshot of a text-based interface, likely related to a web application or development environment. The background is dark gray. It contains instructions and error messages related to setting up CORS and using a Vercel URL.
image text: Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://new1-ivory.vercel.app/api
Error: Expected [73,73,53,63,61] but got [73,53,61,63,73]

Thanks and Regards  
Shalini

---

**post_id:** 587429  
**author:** 23f2003853  
**timestamp:** 2025-01-29T08:09:55.322Z

Hi Shalini,

I deployed my code with your dataset and checked and checked answers for your dataset, so there is no errors in backend.

Since you are getting some output, it won’t help to look up to logs from vercel, just check your code if it’s logically correct.

Kind regards  
Jivraj

---

**post_id:** 587610  
**author:** 23f3002537  
**timestamp:** 2025-01-29T16:43:46.542Z

Here's a description of the image:
\*\*Image Description:\*\*
The image displays Python code within a dark-themed code editor. It defines a custom HTTP request handler class using the `BaseHTTPRequestHandler` from the `http.server` module, along with related modules. The code features two methods: `do\_GET` which manages GET requests, and `do\_OPTIONS` for handling preflight requests related to Cross-Origin Resource Sharing (CORS). Within `do\_GET`, there are several steps, including setting CORS headers, loading JSON data from a file, parsing query parameters, filtering data based on the provided parameters, and returning a JSON response. The code utilizes `json`, `os`, and `urllib.parse` for file operations and query parsing.
\*\*image text:\*\*
```
import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse\_qs, urlparse
class handler (BaseHTTPRequestHandler):
def do\_GET(self):
# Set CORS headers to allow requests from any origin
self.send\_response(200)
self.send\_header('Access-Control-Allow-Origin', '\*')
self.send\_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
self.send\_header('Access-Control-Allow-Headers', 'Content-Type')
self.send\_header('Content-type', 'application/json')
# Load the JSON data
dir\_path = os.path.dirname(os.path.abspath(\_file\_))
json\_file\_path = os.path.join(dir\_path, "../q-vercel-python.json")
with open(json\_file\_path, "r") as file:
data = json.load(file)
# Parse query parameters
query\_components = parse\_qs(urlparse(self.path).query)
names = query\_components.get('name', [])
if not names:
self.end\_headers()
self.wfile.write(json.dumps({"error": "Please provide a 'name' query parameter"}).encode('utf-8'))
return
# Collect the marks for provided names
marks = []
for entry in data:
if entry['name'] in names:
marks.append(entry['marks'])
self.end\_headers()
if marks:
response = {"marks": (marks)}
else:
response = {"error": "Name not found"}
self.wfile.write(json.dumps(response).encode('utf-8'))
def do\_OPTIONS(self):
# Handle preflight requests for CORS
self.send\_response(200)
self.send\_header('Access-Control-Allow-Origin', '\*')
self.send\_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
self.send\_header('Access-Control-Allow-Headers', 'Content-Type')
self.end\_headers()
```  
Here is my code. Could you please help me identify any issues or clarify where I might be going wrong?

---

**post_id:** 587615  
**author:** Adithya  
**timestamp:** 2025-01-29T16:50:48.340Z

Till yesterday I was able to login ngrok. But today it shows some error  
image description: The image is a screenshot of a web page on the ngrok platform. The page is focused on device activation for MFA (Multi-Factor Authentication). There's an error message that pops up, "The information supplied for MFA verification was invalid.".
image text: ngrok
Device Activation
Enter the code displayed on your device.
4VZTALOCF43MBSGDR63ZL7THHK4B0613
Continue
Back to QR Code
ngrok staff will never ask you to enter a code on this page.
Error
The information supplied for MFA
verification was invalid.
  
can anyone guide me to fix it

---

**post_id:** 587723  
**author:** 22f2000113  
**timestamp:** 2025-01-30T03:09:31.697Z

[@s.anand](/u/s.anand)  
Sir I am facing some err in Q10 of GA2,  
Kindly look at the error :

```
Error: Response is not valid JSON: <!DOCTYPE html> <!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]--> <!--[if IE 7]> <html class="no-js ie7 oldie" lang="en-US"> <![endif]--> <!--[if IE 8]> <html class="no-js ie8 oldie" lang="en-US"> <![endif]--> <!--[if gt IE 8]><!--> <html class="no-js" lang="en-US"> <!--<![endif]--> <head> <title>Worker threw exception | exam.sanand.workers.dev | Cloudflare</title> <meta charset="UTF-8" /> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> <meta http-equiv="X-UA-Compatible" content="IE=Edge" /> <meta name="robots" content="noindex, nofollow" /> <meta name="viewport" content="width=device-width,initial-scale=1" /> <link rel="stylesheet" id="cf_styles-css" href="/cdn-cgi/styles/cf.errors.css" /> <!--[if lt IE 9]><link rel="stylesheet" id='cf_styles-ie-css' href="/cdn-cgi/styles/cf.errors.ie.css" /><![endif]--> <style>body{margin:0;padding:0}</style> <!--[if gte IE 10]><!--> <script> if (!navigator.cookieEnabled) { window.addEventListener('DOMContentLoaded', function () { var cookieEl = document.getElementById('cookie-alert'); cookieEl.style.display = 'block'; }) } </script> <!--<![endif]--> </head> <body> <div id="cf-wrapper"> <div class="cf-alert cf-alert-error cf-cookie-error" id="cookie-alert" data-translate="enable_cookies">Please enable cookies.</div> <div id="cf-error-details" class="cf-error-details-wrapper"> <div class="cf-wrapper cf-header cf-error-overview"> <h1> <span class="cf-error-type" data-translate="error">Error</span> <span class="cf-error-code">1101</span> <small class="heading-ray-id">Ray ID: 909a71f6cd160dfb &bull; 2025-01-29 16:02:11 UTC</small> </h1> <h2 class="cf-subheadline" data-translate="error_desc">Worker threw exception</h2> </div><!-- /.header --> <section></section><!-- spacer --> <div class="cf-section cf-wrapper"> <div class="cf-columns two"> <div class="cf-column"> <h2 data-translate="what_happened">What happened?</h2> <p>You've requested a page on a website (exam.sanand.workers.dev) that is on the <a href="https://www.cloudflare.com/5xx-error-landing/" target="_blank">Cloudflare</a> network. An unknown error occurred while rendering the page.</p> </div> <div class="cf-column"> <h2 data-translate="what_can_i_do">What can I do?</h2> <p><strong>If you are the owner of this website:</strong><br />you should <a href="https://www.cloudflare.com/login?utm_source=error_100x" target="_blank">login to Cloudflare</a> and check the error logs for exam.sanand.workers.dev.</p> </div> </div> </div><!-- /.section --> <div class="cf-error-footer cf-wrapper w-240 lg:w-full py-10 sm:py-4 sm:px-8 mx-auto text-center sm:text-left border-solid border-0 border-t border-gray-300"> <p class="text-13"> <span class="cf-footer-item sm:block sm:mb-1">Cloudflare Ray ID: <strong class="font-semibold">909a71f6cd160dfb</strong></span> <span class="cf-footer-separator sm:hidden">&bull;</span> <span id="cf-footer-item-ip" class="cf-footer-item hidden sm:block sm:mb-1"> Your IP: <button type="button" id="cf-footer-ip-reveal" class="cf-footer-ip-reveal-btn">Click to reveal</button> <span class="hidden" id="cf-footer-ip">2409:40d2:2f:a936:5428:2d9:376:5dcb</span> <span class="cf-footer-separator sm:hidden">&bull;</span> </span> <span class="cf-footer-item sm:block sm:mb-1"><span>Performance &amp; security by</span> <a rel="noopener noreferrer" href="https://www.cloudflare.com/5xx-error-landing" id="brand_link" target="_blank">Cloudflare</a></span> </p> <script>(function(){function d(){var b=a.getElementById("cf-footer-item-ip"),c=a.getElementById("cf-footer-ip-reveal");b&&"classList"in b&&(b.classList.remove("hidden"),c.addEventListener("click",function(){c.classList.add("hidden");a.getElementById("cf-footer-ip").classList.remove("hidden")}))}var a=document;document.addEventListener&&a.addEventListener("DOMContentLoaded",d)})();</script> </div><!-- /.error-footer --> </div><!-- /#cf-error-details --> </div><!-- /#cf-wrapper --> <script> window._cf_translation = {}; </script> </body> </html>

```

image description: The image is a text-based instruction or guide, set against a dark gray background. It outlines a process involving "Llamafile," "ngrok," and a model file.
The text instructs users to download Llamafile, run the specified model with it, and create a tunnel to the Llamafile server using ngrok. It provides an example of what the ngrok URL might look like and shows a sample URL. The sample URL appears within a highlighted red-outlined box, which also contains an information icon.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://fd8c-2405-201-6808-a99e-871-6b1a-adb9-36c5.ngrok-free.app/
①

---

**post_id:** 587733  
**author:** Sakshi6479  
**timestamp:** 2025-01-29T21:24:13.303Z

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir I am getting this “TypeError: Load failed” for Q9 inspite of getting proper responses in “<http://127.0.0.1:8000/api>”, cors is also enabled. Please help me with this, I am finding it difficult to circumvent this.  
image description: The image shows a dark interface with instructions related to API configuration. A text input field shows an example URL address with an error message below.
image text: Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
TypeError: Load failed
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
  
image description: The image displays a dark-themed user interface with a web browser. The browser window shows a JSON structure with student data. The top bar of the browser has the Google logo and navigation controls, along with tabs or links for "Tools in Data Sc..." and "TDS 2025 Jan G...".
image text: {"students":[{"studentId":34,"class":"1A"},{"studentId":453,"class":"1A"},{"studentId":551,"class":"1A"},{"studentId":829,"class":"1A"},{"stude {"studentId":1309,"class":"1A"},{"studentId":1795,"class":"1A"}]}

---

**post_id:** 587737  
**author:** carlton  
**timestamp:** 2025-01-30T04:06:53.137Z

After checking few times now i started getting below error please help  
image description: The image is a text guide or instructions on how to set up something, potentially related to "Llamafile" and "ngrok". It displays a series of steps with a specific URL, and an error message.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://02f4-2402-e280-3e32-27f-4b0-6f91-4275-52f3.ngrok-free.app
Error: Response is not valid JSON: error code: 524

---

**post_id:** 587762  
**author:** 23F3002987_J_SRI_BAL  
**timestamp:** 2025-01-30T05:49:44.346Z

image description: The image is a dark-themed coding interface. It contains a prompt to download a file and create an API using Vercel. It also displays sample JSON response and an example of how to enable CORS. There is an input field with an error message.
image text: ue Sun, 2 Feb, 2025, 11:59 pm IST Score: 8 / 10 Check Save
Download this q-vercel-python.json which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?
name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://vercel-project-three-liard.vercel.app/api
Error: Expected [35,71,83,96,95] but got [null,null,null,null,null]

Please anyone who have done these kindly guide me. As in Q6 i am unable to fetch values it is giving null all time.  
and in Q9 how can I use class as variable name ?

---

**post_id:** 587776  
**author:** daksh76  
**timestamp:** 2025-01-30T08:03:04.204Z

[@22f2000113](/u/22f2000113) Please watch last night’s session where we cleared similar doubts. (Will be available at 2025-01-30T05:30:00Z)

[TDS You Tube Playlist](https://www.youtube.com/playlist?list=PL_h5u1jMeBCl1BquBhgunA4t08XAxsA-C)

Error 524 Indicates a server timeout (i.e its taking too long to get a response from your server).

We have shown various ways to debug ngrok.

Kind regards

---

**post_id:** 587778  
**author:** daksh76  
**timestamp:** 2025-01-30T08:03:42.482Z

iN QUESTION NO 2 is it enough to upload the output image… Everytime we reload the page it disappears. How to answer it?

---

**post_id:** 587780  
**author:** daksh76  
**timestamp:** 2025-01-30T08:07:12.480Z

I have solved the question and when i enter the answer its showing me incorrect, sir could you please help me out. I am attaching the images of my code and the tds

Here's a brief description of the image:
The image is a coding exercise related to image processing with Python in Google Colab. It gives the code to find the number of pixels in the image with a certain lightness. The user has inputted the result and the result is incorrect.
image text:
5 Use an Image Library in Google Colab (0.5 marks)
Download this image. Create a new Google Colab notebook and run this code (after fixin brightness:
import numpy as np
from PIL import Image
from google.colab import files
import colorsys
# There is a mistake in the line below. Fix it
image = Image.open(list(files.upload().keys)[0])
rgb = np.array(image) / 255.0
lightness = np.apply\_along\_axis (lambda x: colorsys.rgb\_to\_hls(\*x) [1], 2, rgb)
light\_pixels = np.sum(lightness > 0.219)
print(f'Number of pixels with lightness > 0.219: {light\_pixels}')
What is the result? (It should be a number)
248985
Incorrect. Try again.

---

**post_id:** 587782  
**author:** daksh76  
**timestamp:** 2025-01-30T08:11:24.919Z

image description: The image shows a Python code snippet for image processing, likely analyzing a ".webp" image named "lenna.webp". The code imports NumPy, PIL, and Google Colab's file upload functionality and colorsys. It uploads the image, converts it to an array, calculates lightness using a lambda function and color conversion, then counts and prints the number of pixels with lightness above 0.219. Below the code, there are UI elements for file selection, displaying the file name, size, and modification date. The result of the code execution shows that 248985 pixels have lightness greater than 0.219.
image text:
import numpy as np
from PIL import Image
from google.colab import files
import colorsys
uploaded=files.upload()
image = Image.open(list(uploaded.keys())[0])
rgb = np.array(image) / 255.0
lightness = np.apply\_along\_axis(lambda x: colorsys.rgb\_to\_hls(\*x)[1], 2, rgb)
light\_pixels = np.sum(lightness >= 0.219)
print(f'Number of pixels with lightness > 0.219: {light\_pixels}')
Choose Files lenna.webp
lenna.webp(image/webp) - 14820 bytes, last modified: 1/30/2025 - 100% done
Saving lenna.webp to lenna (1).webp
Number of pixels with lightness > 0.219: 248985

---

**post_id:** 587945  
**author:** 23f3002537  
**timestamp:** 2025-01-30T14:27:18.177Z

this is my code  
Here's a description of the image:
The image appears to be a screenshot of a code editor or notebook environment. The code is written in Python and involves image processing.
The code imports libraries like numpy, PIL (Pillow), and colorsys. It uploads an image using the google.colab files module and then performs calculations on its pixels. The code calculates the lightness of the image, and counts the number of pixels with lightness greater than 0.219. At the bottom is an output that shows how many pixels have a lightness over the specific value (248985). Below the code is a section that indicates a file named "lenna.webp" was uploaded.
image text:
import numpy as np
from PIL import Image
from google.colab import files
import colorsys
uploaded=files.upload()
image = Image.open(list(uploaded.keys())[0])
rgb = np.array(image) / 255.0
lightness = np.apply\_along\_axis(lambda x: colorsys.rgb\_to\_hls(\*x)[1], 2, rgb)
light\_pixels = np.sum(lightness >= 0.219)
print(f'Number of pixels with lightness > 0.219: {light\_pixels}')
Choose Files lenna.webp
• lenna.webp(image/webp) - 14820 bytes, last modified: 1/30/2025 - 100% done
Saving lenna.webp to lenna (1).webp
Number of pixels with lightness > 0.219: 248985

---

**post_id:** 587948  
**author:** 23f3002537  
**timestamp:** 2025-01-30T14:36:38.042Z

could you also give me a hint

---

**post_id:** 587956  
**author:** daksh76  
**timestamp:** 2025-01-30T15:04:54.917Z

I think in Q.6 its some error in your code’s logic its unable to fetch the data from your code(Even I tried your URL and its just a black page). Make sure your link is working correctly(giving json response) by pasting it to the browser.

In Q9. I have created dictionary of given data. You can check the for format in the given codes just above the question.(see Test with curl api)

---

**post_id:** 587976  
**author:** 23F3002987_J_SRI_BAL  
**timestamp:** 2025-01-30T16:03:02.683Z

I think your code logic seem to be correct but it may be because u have downloaded twice the same image and in your output lenna.webp is saving to lenna(1).webp.  
Try to do it again after deleting those images which are already downloaded!

---

**post_id:** 587978  
**author:** 24ds1000082_Vivek  
**timestamp:** 2025-01-30T16:20:44.459Z

image description: The image displays a Python code snippet within a Google Colab environment. The code imports libraries like NumPy, PIL, Google Colab files, and colorsys. It appears to process an image, calculating lightness and counting pixels above a certain threshold. The bottom part of the image reveals file upload and processing details for "lenna.webp," including file size, modification date, and the result of the calculation: 248985 pixels with lightness greater than 0.219.
image text:
```
import numpy as np
from PIL import Image
from google.colab import files
import colorsys
uploaded = files.upload()
image = Image.open(list(uploaded.keys())[0])
rgb = np.array(image) / 255.0
lightness = np.apply\_along\_axis(lambda x: colorsys.rgb\_to\_hls(\*x)[1], 2, rgb)
light\_pixels = np.sum(lightness > 0.219)
print(f'Number of pixels with lightness > 0.219: {light\_pixels}')
```
```
Choose Files lenna.webp
• lenna.webp(image/webp) - 14820 bytes, last modified: 1/30/2025 - 100% done
Saving lenna.webp to lenna.webp
Number of pixels with lightness > 0.219: 248985
```  
I have laready tried doing that as well but it still doesnt seem to work

---

**post_id:** 587990  
**author:** 23f1002382  
**timestamp:** 2025-01-30T17:43:34.610Z

For Graded Assignment 2 Q6, I’m getting the right answer but in portal it throws an error.  
image description: A screenshot of a web browser window displaying JSON data related to "marks" with a value of 65. The browser's address bar shows a URL.
image text: IIT Madras X
Pretty-print
{"marks":[65]}
✔ Graded Assic X Ex TDS 2025 Jar X-GA2-Deplo) X-GA2-Deploy × Pyth
vercelapp-mvqtg2t29-sri-balajis-projects-ec088a33.vercel.app/api?name="dzPtdczl9"
  
Here's a description of the image:
The image is a webpage section discussing the deployment of a Python app to Vercel. It includes instructions and code snippets related to API requests and JSON responses.
image text: Download this q-vercel-python.json which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON response with the marks of the names X and Y like this:
{ "marks": [ 10, 20 ] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://vercelapp-mvqtg2t29-sri-balajis-projects-ec088a33.vercel.app/api
TypeError: Failed to fetch

This is my vercel deployment  
<https://vercelapp-mvqtg2t29-sri-balajis-projects-ec088a33.vercel.app/api>

---

**post_id:** 588059  
**author:** Jivraj  
**timestamp:** 2025-01-30T21:14:31.406Z

image description: The image is a screenshot of a webpage or a user interface element related to API testing or documentation. The content discusses an API URL endpoint for FastAPI, presents an example URL, and highlights an error message related to the response not matching expected data.
image text: What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
Error: Response undefined does not match expected [{"studentId":57,"class":"5N"},{"studentId":67,"class":"1T"},{"studentId":117,"class":"11P"},{"studentId":311,"class":"9W"},
{"studentId":429,"class":"5N"},{"studentId":524,"class":"5N"},{"studentId":790,"class":"9W"},{"studentId":890,"class":"9W"},{"studentId":954,"class":"9W"},
{"studentId":1136,"class":"1T"},{"studentId":1150,"class":"5N"},{"studentId":1211,"class":"5N"},{"studentId":1261,"class":"5N"},{"studentId":1522,"class":"11P"},
{"studentId":1598,"class":"9W"},{"studentId":1689,"class":"9W"},{"studentId":1714,"class":"5N"},{"studentId":1719,"class":"5N"}]
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
  
image description: The image is a screenshot of a web browser displaying a JSON response related to student data. The URL at the top indicates an API endpoint with parameters for class. The "Pretty-print" formatting is enabled.
image text:
← CA
127.0.0.1:8000/api?class=5N&class=1T&class=11P&class=9W
Pretty-print
[{"studentId":57,"class":"5N"}, {"studentId":67,"class":"1T"},{"studentId":117,"class":"11P"},{"studentId":311,"class":"9W"},{"studentId":429,"class":"5N"},
{"studentId":524,"class":"5N"},{"studentId":790,"class":"9W"},{"studentId":890,"class":"9W"},{"studentId":954,"class":"9W"},{"studentId":1136,"class":"1T"},
{"studentId":1150,"class":"5N"},{"studentId":1211,"class":"5N"},{"studentId":1261,"class":"5N"},{"studentId":1522,"class":"11P"},{"studentId":1598,'
{"studentId":1689,"class":"9W"},{"studentId":1714,"class":"5N"}, {"studentId":1719, "class":"5N"}]
☆

TDS GA2 Q9, I have passed the same class as of the error thrown test case for ease of reference. Both are same to same. Yet I’m getting error when i submit the answer. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) , Kindly please clarify what I’m doing wrong.  
#samesamebutdiffalant

---

**post_id:** 588060  
**author:** Jivraj  
**timestamp:** 2025-01-30T21:19:36.074Z

check expected output, look closely each character within 20-30 characters you might get it

---

**post_id:** 588061  
**author:** Jivraj  
**timestamp:** 2025-01-30T21:22:58.917Z

Hi [@24ds1000082\_Vivek](/u/24ds1000082_vivek) ,

I don’t see any difference between them. Can you share screen shot of browser console tab and Network tab. Also join tomorrow’s session towards ending of each session we use to take doubts.

---

**post_id:** 588064  
**author:** Jivraj  
**timestamp:** 2025-01-30T22:10:20.492Z

[@23F3002987\_J\_SRI\_BAL](/u/23f3002987_j_sri_bal) ,

This must be a production deployment url, that’s why I am not able to access it.

Here's a brief description of the image:
The image shows a webpage with a black background and white text indicating "Team Access Required." It states that the user is signed in as "jivraj-18" but cannot access a unique deployment URL because they are not a team member. It offers a way to view the latest version by requesting access. There's a colorful circle at the top and a link to log in with a different Vercel account.
image text:
https://vercel.com/sso/access/request?next=%2Fsso-api%3Furl%3Dhttps%253A%252F%252Fvercelapp-mvqtg2t29-sri-balajis-proj...
Team Access Required
You are signed in as jivraj-18.
You cannot access this unique deployment URL as you are not a member of the team. You can
view the latest version of this branch by requesting access to the up-to-date deployment URL.
Log in with a different Vercel Account

Solution :

Go to vercel dashboard and select your project, and below domains you would find a url use that.

Here's a description of the image:
The image is a screenshot of a webpage, likely a deployment dashboard. It is displaying a "Not Found" error for a specific URL within the context of a "Production Deployment". Key elements include:
\* \*\*URL Bar:\*\* Displays the URL `https://vercel.com/jivraj-18s-projects/api`.
\* \*\*Main Content:\*\* Shows a "Not Found" error with an explanation, along with deployment details on the right.
\* \*\*Deployment Details:\*\* Includes information like deployment ID, domain, status (Ready), and source code options.
image text:
https://vercel.com/jivraj-18s-projects/api
Project Deployments Analytics Speed Insights Logs Observability Firewall Storage Settings
Production Deployment
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
Deployment
api-6xs8fp81c-jivraj-18s-projects.vercel.app
Domains
api-ruby-seven-48.vercel.app
Status
Created
Ready 28 Jan by jivraj-18
Source
<> View code
> vercel deploy
+2
Build Logs
Runtime Logs
Insta

If this doesn’t solve problem, pls join tomorrow’s session between 8-10 towards ending of session we use to take doubts.

Kind regards  
Jivraj

---

**post_id:** 588071  
**author:** 24ds1000082_Vivek  
**timestamp:** 2025-01-31T01:12:03.951Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/daksh76/48/67052_2.png) daksh76:

> I have laready tried doing that as well but it still doesnt seem to work

Hi [@daksh76](/u/daksh76), Can you mention exact error or problem that you are facing.

---

**post_id:** 588130  
**author:** 23f2003853  
**timestamp:** 2025-01-31T05:49:03.070Z

The issue might be with the IP address you’re using. Try using `127.0.0.1` and check if it’s the correct localhost IP for your machine. Also, test with `http://localhost:8000/api` to see if it works.

If that doesn’t solve the problem and you’re running port 8000 inside a virtual machine, use the `ipconfig` command to check the correct IP address.

We usually address doubts at the end of every session. Our next session is on the 31st—you can join then and ask your question if none of above solutions works.

---

**post_id:** 588133  
**author:** 23f2004644  
**timestamp:** 2025-01-31T06:06:30.490Z

Here's a description of the image:
The image is a screenshot of a web browser's developer tools. It displays a network request and its response in JSON format. The network tab is active, showing the request and response details for a specific API call. The response body contains an array of objects, each having "studentId" and "class" properties.
image text:
```
127.0.0.1:8000/api?class=5N&class=1T&class=11P&class=9W
[{"studentId":57,"class":"5N"},{"studentId":67,"class":"1T"},
{"studentId":117,"class":"11P"},{"studentId":311,"class":"9W"},
{"studentId":429,"class":"5N"},{"studentId":524,"class":"5N"},
{"studentId":790,"class":"9W"},{"studentId":890,"class":"9W"},
{"studentId":954,"class":"9W"},{"studentId":1136, "class":"1T"},
"studentId":1150,"class":"5N"},{"studentId":1211,"class":"5N"},
{"studentId":1261,"class":"5N"},{"studentId":1522, "class":"11P"},
{"studentId":1598,"class":"9W"},{"studentId":1689,"class":"9W"},
{"studentId":1714,"class":"5N"},{"studentId":1719,"class":"5N"}]
api?class=5N&class=1T&class=11P&cl... 200 document Other 694 B 12 m
1 requests 694 B transferred 568 B resources Finish: 12 ms DOMContentLoaded: 27 ms Load: 28 ms
A form field element should have an id or name attribute
```
  
image description: The image shows a browser's developer console displaying a JSON object. The URL in the browser is "127.0.0.1:8000/api?class=5N&class=1T&class=11P&class=9W". The console's "Console" tab is active, and the JSON object consists of an array of objects, each containing "studentId" and "class" keys and values. An issue is flagged: "A form field element should have an id or name attribute".
image text: {"studentId":57,"class":"5N"}, {"studentId":67,"class":"1T"},
"studentId":117,"class":"11P"},{"studentId":311,"class":"9W"},
"studentId":429,"class":"5N"},{"studentId":524,"class":"5N"},
"studentId":790,"class":"9W"},{"studentId":890,"class":"9W"},
"studentId":954,"class":"9W"},{"studentId":1136, "class":"1T"},
"studentId":1150,"class":"5"},{"studentId":1211,"class":"5N"},
"studentId":1261,"class":"5N"},{"studentId":1522,"class":"11P"},
"studentId":1598, "class":"9W"},{"studentId":1689,"class":"9W"},
"studentId":1714,"class":"5N"}, {"studentId":1719,"class":"5N"}]
A form field element should have an id or name attribute
  
[@Jivraj](/u/jivraj) , Thankyou for the quick response. I have attached both console and network screenshots. Hope these are the ones you were referring to. Sure, I will join tonight’s session and try to rectify the issue. Meanwhile will update here if i was able to resolve it.

---

**post_id:** 588157  
**author:** 24ds1000082_Vivek  
**timestamp:** 2025-01-31T06:59:40.374Z

If I entered the URL I get the error Failed to fetch  
image description: A white webpage with text, a code snippet, and a highlighted URL. The page describes how to create and deploy a Python app to Vercel. An error message is present.
image text: Download this q-vercel-python.json which has the marks of 100 imaginary students. Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api/name-X&name-Y is made, it returns a JSON response with the marks of the names X and Y like this: "marks" 10 20 Make sure you enable CORS to allow GET requests from any origin. What is the Vercel URL? It should look like: https://your-app.vercel.app/api https://tdsproject1-ltjsdpii1-23f2003853-projects.vercel.app/api TypeError: Failed to fetch

If I run the same in my browser, I get the output (just I tried for two name available in json file)  
Here's a brief description of the image:
The image is a screenshot of a web browser displaying a web page with the URL "tdsproject1-tjsdpi1-2312003853-projects.vercel.app/api?name=sLrAoQ&name=d2KY". The page's content includes "Pretty-print" text with a checkbox and then the output of something: `{"marks": [1,41]}`.
image text:
My Dashbox
Graded Ass X
TOS 2025Jx
Vercel
tdsproject X
Introducing X
Deploy Py x
tdsproject X
+
X
C
tdsproject1-tjsdpi1-2312003853-projects.vercel.app/api?name=sLrAoQ&name=d2KY
☆
Pretty-print
("marks":[1,41])

Kindly help me to fix the issue

---

**post_id:** 588163  
**author:** daksh76  
**timestamp:** 2025-01-31T07:12:15.016Z

image description: The image displays a dark interface with instructions for running a Llamafile model and creating a tunnel using ngrok. It provides an example ngrok URL and then shows a specific URL with an error message indicating the response is too old, along with detailed JSON data.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6 K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://6714-13-71-3-97.ngrok-free.app/
Error: Response is too old: {"choices":[{"finish\_reason":"stop","index":0,"message":{"content":"```\n{\n \"user\":\"23f2004644\",\n \"domain\":
\"ds.study.iitm.ac.in\"\n}\n```<leot\_id|>","role":"assistant"}}],"created":1738303197,"id":"chatcmpl-Ju9368HuUNKVAiF32ECG1nj3nROtbpoh","model":"unknown","object":"chat.completion","usage":
{"completion\_tokens":29,"prompt\_tokens":31,"total\_tokens":60}}
  
This url shows correct but after few hour it shows this error  
[@carlton](/u/carlton) pls help me to fix this

---

**post_id:** 588164  
**author:** daksh76  
**timestamp:** 2025-01-31T07:14:12.076Z

you need to keep the services running. Else it will fail. Do whats required, regenerate that link and paste it once you complete and save it. this way you can avoid rework.

---

**post_id:** 588227  
**author:** 23f2003853  
**timestamp:** 2025-01-31T10:33:42.441Z

sir the output im getting after correcting the code is showing incorrect on the portal

---

**post_id:** 588276  
**author:** 23ds1000022  
**timestamp:** 2025-01-31T14:18:49.279Z

if you could suggest me why is that happening, where am i making an error because i have cross checked this a lot of times and still am unable to understand where i might be making a mistake

---

**post_id:** 588402  
**author:** Sakshi6479  
**timestamp:** 2025-01-31T20:59:41.314Z

I had faced the same issue. Please ensure the url is not protected against the access of third party (IITM will access your url. To check it, try to open the url in different browser)

---

**post_id:** 588408  
**author:** carlton  
**timestamp:** 2025-02-01T02:50:49.374Z

Hi sakshi in vercel problem i also had similar error. remove this code if **name** == ‘**main**’:

24 # app.run(debug=True) frm your flask app then run it. it worked for me i found this with the help of chatgpt. vercel has some built in features to run so this is not required it seems.

---

**post_id:** 588529  
**author:** 23f2004644  
**timestamp:** 2025-02-01T07:10:12.783Z

I was facing problem that how to make a class as variable name for Q9 in GA2 . but now i get a solution which was helpful for making class as variable. The below command is the solution for the problem of how to make a class variable name in python.  
image description: The image shows a screen recording of a code editor with Python code. The code is related to a FastAPI application, likely for handling API requests. A person named Saransh is presenting.
image text: 10:31 PM Fri, Jan 31 G
nfb-npjg-uij
FastAPI
fast.py 3 X data.csv
fast.py >
11
allow\_credentials=True,
12
allow\_methods=["\*"], # Allows all HTTP methods.
13
allow\_headers=["\*"], # Allows all headers.
14
)
15
16
data = pd.read\_csv("data.csv")
17
18
@app.get("/api")
19
async def root (class\_name: List[str] = Query(default=[], alias="class")):
20
population = int(data.query("city == @city") ["population"].values[0])
21
return {"city": city, "population": population}
Saransh is presenting
  
the async def root() this command line in image is solution for our problem.

---

**post_id:** 588700  
**author:** bhashwar_sengupta  
**timestamp:** 2025-02-01T12:29:59.226Z

Hi Srividya,

Thats right the idea behind vercel is you do not need to create a server. Its serverless! Instead you create functions that respond to endpoints.  
When the endpoint is triggered, the appropriate function runs.

This renders `name == main` part of the code unnecessary at best, since python interpreters only run this line if that file was the starting point of the application (but its not, because a vercel wrapper application(s) or processes have started before it).

In other words you do not create a flask server, or a http server or indeed any server at all. Just functions tied to specific endpoints. So you have to rethink how your application is designed. You *do not* create serverless applications in the same traditional way you have been taught in MAD-1 or MAD-2.

This is a common mistake many students have been making with their approach to vercel. Watching the videos and using the provided code template will greatly help in deploying successful serverless applications.

Thanks for your input.

Kind regards

---

**post_id:** 588711  
**author:** 23f3004114  
**timestamp:** 2025-02-01T12:46:31.098Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) sir pls help me to fix this issue

---

**post_id:** 588713  
**author:** 23f3004114  
**timestamp:** 2025-02-01T12:51:09.174Z

Questions 9 and 10 require running a development server from my side. Right now, the questions are marked correct and I’ve saved the assignment. Since the servers won’t always be running, I hope this won’t cause a problem during evaluation.

---

**post_id:** 588860  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:12:49.184Z

What am i missing here? i am also facing same issue, question 9 . attached screenshots.

Here's a description of the image:
\*\*Image Description:\*\*
The image shows a webpage open in a browser displaying a JSON diff comparison between two datasets. The left and right panes each present JSON data with fields like "class" and "studentId". The structure appears to be an array of objects, where each object contains these two key-value pairs. The website's address is "jsondiff.com". There are several tabs open in the browser, including ones labelled "TDS 2025 Jan GA2-...", "docker hub - Google", "localhost:8000/api", "127.0.0.1:8000/api?", "JSON Diff - The sem...", "Graded Assignment...", "GA2 - Deployment To...", and "Indian Institute of Tec...". The browser also contains the "All Bookmarks" icon.
\*\*image text:\*\*
```json
[
{
"class": "1N",
"studentId": 60
},
{
"class": "1N",
"studentId": 64
},
{
"class": "1N",
"studentId": 106
},
{
"class": "1N",
"studentId": 270
},
{
"class": "8N",
"studentId": 411
},
{
"class": "8N",
"studentId": 522
},
{
"class": "8X",
"studentId": 525
},
{
"class": "4Z",
"studentId": 673
},
{
"class": "4Z",
"studentId": 710
},
{
"class": "8X",
"studentId": 802
},
{
"class": "8N",
"studentId": 934
},
{
"class": "8N",
"studentId": 1034
},
{
"class": "8N",
"studentId": 1331
},
{
"class": "8N",
"studentId": 1354
},
{
"class": "8N",
"studentId": 1485
},
{
"class": "8N",
"studentId": 1511
},
{
"class": "8N",
"studentId": 1573
},
{
"class": "8X",
"studentId": 1591
},
{
"class": "8N",
"studentId": 1611
},
{
"class": "1N",
"studentId": 1678
},
{
"class": "8X",
"studentId": 1826
},
{
"class": "4Z",
"studentId": 1831
},
]
```
```json
[
{
"class": "1N",
"studentId": 60
},
{
"class": "1N",
"studentId": 64
},
{
"class": "1N",
"studentId": 106
},
{
"class": "1N",
"studentId": 270
},
{
"class": "8N",
"studentId": 411
},
{
"class": "8N",
"studentId": 522
},
{
"class": "8X",
"studentId": 525
},
{
"class": "4Z",
"studentId": 673
},
{
"class": "4Z",
"studentId": 710
},
{
"class": "8X",
"studentId": 802
},
{
"class": "8N",
"studentId": 934
},
{
"class": "8N",
"studentId": 1034
},
{
"class": "8N",
"studentId": 1331
},
{
"class": "8N",
"studentId": 1354
},
{
"class": "8N",
"studentId": 1485
},
{
"class": "8N",
"studentId": 1511
},
{
"class": "8N",
"studentId": 1573
},
{
"class": "8X",
"studentId": 1591
},
{
"class": "8N",
"studentId": 1611
},
{
"class": "1N",
"studentId": 1678
},
{
"class": "8X",
"studentId": 1826
},
{
"class": "4Z",
"studentId": 1831
},
]
```  
image description: The image is a screenshot of a web browser's developer tools, focusing on a network request and its response. The page displays a task description related to an API, including instructions to filter students based on class parameters in the URL. The browser's network tab is open, showing details of a GET request and its response.
image text:
Due Sun, 2 Feb, 2025, 11:59 pm IST Score: 7.5 / 10 Check all Save
If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
Error: Response undefined does not match expected [{"studentId":60,"class":"1N"},{"studentId":64,"class":"1N"}, {"studentId":106,"class":"1N"}, {"studentId":270,"class":"1N"}, {"studentId":411,"class":"8N"},{"studentId":522,"class":"8N"}, {"studentId":525,"class":"8X"},{"studentId":673,"class":"4Z"},{"studentId":710,"class":"4Z"},{"studentId":802,"class":"8X"}, {"studentId":934,"class":"8N"},{"studentId":1034,"class":"8N"},{"studentId":1331,"class":"8N"},{"studentId":1354,"class":"8N"}, {"studentId":1485,"class":"8N"}, {"studentId":1511,"class":"8N"}, {"studentId":1573,"class":"8N"},{"studentId":1591,"class":"8X"},{"studentId":1611,"class":"8N"}, {"studentId":1678,"class":"1"},{"studentId":1826,"class":"8X"},{"studentId":1831,"class":"4Z"}, {"studentId":1881,"class":"1N"}, {"studentId":1950,"class":"8N"}, {"studentId":1972,"class":"4Z"},{"studentId":1982,"class":"4Z"}]
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
Check
Name Headers Payload Preview Response Initiator Timing
api?class=1N&class=8N&class=8X&class=4Z
api?class=1N&class=8N&class=8X&class=4Z

---

**post_id:** 588861  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:14:38.883Z

if you have time, could once check my code for question 9. can send github link in chat…

or run this `docker pull 23f3004114/tds_2025_jan_ga2:Q9`

@ [24ds1000082\_Vivek](https://discourse.onlinedegree.iitm.ac.in/u/24ds1000082_Vivek)

---

**post_id:** 588862  
**author:** 22f2000559  
**timestamp:** 2025-02-01T18:19:24.743Z

Hi [@23f2004644](/u/23f2004644) and [@bhashwar\_sengupta](/u/bhashwar_sengupta) ,

You would need to keep all the servers active whenever you click on save button.

---

**post_id:** 588864  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:24:12.470Z

Hi [@23f2003853](/u/23f2003853) ,

did you enable cors ? If yes then pls send screenshot of console and network tab.

Kind regards

---

**post_id:** 588866  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:25:15.938Z

So if I kept the server running and saved the answer, but after reloading it’s showing incorrect  
We can’t just keep it running.

---

**post_id:** 588879  
**author:** 22f2000559  
**timestamp:** 2025-02-01T18:45:33.253Z

Hi [@daksh76](/u/daksh76) ,

I didn’t actually used python to solve this particular question. I tried for some time but it was not working. So I just used [Squoosh](https://squoosh.app/), for now pls use this.

---

**post_id:** 588880  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:46:31.780Z

whenever you want to submit your answers by pressing save button at that time only all servers should must be running.

---

**post_id:** 588883  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:47:31.571Z

I did that, while running all the severs i saved my answers and it showed “correct”.  
But after sometime when I re-loaded my answers it showed incorrect.

---

**post_id:** 588888  
**author:** Jivraj  
**timestamp:** 2025-02-01T18:49:53.544Z

Hi [@24ds1000082\_Vivek](/u/24ds1000082_vivek), [@23f3004114](/u/23f3004114) ,

You guys are not using correct format for response.

```
{
  "students": [
    {
      "studentId": 1,
      "class": "1A"
    },
    {
      "studentId": 2,
      "class": "1B"
    }, ...
  ]
}

```

This is correct for which have a object with key `students` which is not present in your response.

kind regards

---

**post_id:** 588959  
**author:** 24DS1000121_ULAGAOOZ  
**timestamp:** 2025-02-01T22:28:35.680Z

That’s okay, when you click on save answers button just make sure all servers are running.

---

**post_id:** 588974  
**author:** 23f2000573  
**timestamp:** 2025-02-02T02:06:43.292Z

Yes Hari, most probably that’s what the problem is. [@23F3002987\_J\_SRI\_BAL](/u/23f3002987_j_sri_bal) Check if cors are enabled.

Kind regards

---

**post_id:** 589121  
**author:** bhashwar_sengupta  
**timestamp:** 2025-02-02T06:32:26.016Z

@ carlton @ Jivraj  
Gentlemen! In GA2 answers, I have a problem.  
Question 10, the ngrok tunnel url was once correct and I saved it . When I revisited the GA2 again, the question 10 was marked incorrect.  
Do I need to do anything else ?  
Secondly the image comression file needs to be reloaded everytime I reconnect to the GA2. When I reload the last saved version, it does not take into the answer already saved.  
Third, the url link as given on publishing the page via github is obviously correct. But on checking, even after ?v = 1 …it does not work. Could you kindly look into them and advise if anything else needs to be done at my end? thanks & regards.

---

**post_id:** 589270  
**author:** GaURaVinDeX  
**timestamp:** 2025-02-02T09:00:12.407Z

Week-2 Question-8, I am getting error

Here's a description of the image:
The image shows a dark interface with text fields and a button. The top of the interface asks "What is the Docker image URL?". Below, there is a field with the suggested URL format, a field with the URL provided and an error message. There is a "Check" button at the bottom.
image text: What is the Docker image URL? It should look like: https://hub.docker.com/repository/docker/$USER/$REPO/general
https://hub.docker.com/repository/docker/23f2000573/first-rep/general
Error: 23f2000573 is not one of the tags in https://hub.docker.com/v2/namespaces/23f2000573/repositories/first-rep/tags
Check

I have pushed my image in the repository, pulled it and ran once, it worked

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/3/13ab7f2c8e18b815cbd92a4d462580bc9ed35d33.png)

This is how my docker hub repository looks,

image description: A screenshot of a Docker Hub repository's "General" page, displaying details about the repository named "23f2000573/first-rep". The page shows the last push time, repository size, and options to add a description and category. A section labeled "Docker commands" provides the command "docker push 23f2000573/first-rep:tagname". Below, there is information about "Automated builds" and available subscription options.
image text: dockerhub Explore Repositories Organizations Usage Search Docker Hub ctrl+K 2 23f2000573 / Repositories / first-rep / General 23f2000573/first-rep Last pushed 19 minutes ago Repository size: 364.1 MB Add a description Add a category General Tags Builds Collaborators Webhooks Settings Tags This repository contains 1 tag(s). Tag v1 OS Type Pulled Pushed Image 22 minutes ago 22 minutes ago See all Docker commands Public view To push a new tag to this repository: docker push 23f2000573/first-rep:tagname Automated builds Manually pushing images to Docker Hub? Connect your account to GitHub or Bitbucket to automatically build and tag new images whenever your code is updated, so you can focus your time on creating. Available with Pro, Team and Business subscriptions. Read more about automated builds. Upgrade

`https://hub.docker.com/repository/docker/23f2000573/first-rep/general`

---

**post_id:** 589303  
**author:** 21f3000745  
**timestamp:** 2025-02-02T10:35:35.189Z

Yes sir. I did keep them active when saving the assignment and the answers were saved successfully(The score was 10/10). I was talking about evaluation after deadline.

---

**post_id:** 589334  
**author:** Saransh_Saini  
**timestamp:** 2025-02-02T11:13:54.825Z

In the ngrok question I was getting that same json error as everybody else since last 7 days or so. The ngrok link was working fine in browser every time but. Today i ran the LLama file with `--n-gpu-layers 35` parameter at the end which makes it run using my laptops graphics card i guess. After i ran LLama file using this and ngrok later, my link was accepted in the GA 2 and i did not get any error after that.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) did this happen because i ran LLama file using my laptop GPU? This was suggested to me by another student who had the same problem.

---

**post_id:** 589362  
**author:** 21f3000745  
**timestamp:** 2025-02-02T11:51:31.819Z

image description: The image is a screenshot of a web browser displaying JSON data. The browser's address bar shows a URL. The main content area displays the JSON data.
image text:
```
C
new-deploy12345.vercel.app/api?name=Mn&name=m
iitm-tds-project1/sc...
PROJECT2/autolysis....
2 Indian Institute of T...
Pretty-print
{"marks": [5,78]}
```
  
here it is giving output but when i run on question page it gives error.  
image description: The image shows a webpage with a question about a Vercel URL, an input field for the URL, an error message, and a "Check" button.
image text: What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://new-deploy12345.vercel.app/api
Error: Expected [98,92,56,72,17] but got [48,"Not Found","Not Found","Not Found","Not Found"]
Check
  
please look into this [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
<https://new-deploy12345.vercel.app/api?name=Mn&name=m>

---

**post_id:** 589370  
**author:** Saransh_Saini  
**timestamp:** 2025-02-02T11:59:29.929Z

Try these [@21f3000745](/u/21f3000745)

1. Download the data file once again and replace it with your current file, then deploy.  
   **If this doesn’t work, then:**
2. Try clicking on Check button once again. There are few cases where due to duplicity or other problems in the data, this bug occurs. The next check will most probably work.
3. Reload the page, open the Networks Tab in the Inspect menu, click on Fetch/XHR filter button. Next click on check, if this error prompts up, you will get the request the system sent to check your answer. Copy that request and check on localhost.

---

**post_id:** 589375  
**author:** 21f3000745  
**timestamp:** 2025-02-02T12:04:26.993Z

yeah it worked. thankyou [@Saransh\_Saini](/u/saransh_saini)  
actually on every reload of page , it generates new data which makes question so tedious.

---

**post_id:** 589467  
**author:** Jivraj  
**timestamp:** 2025-02-02T13:50:10.748Z

So the problem was with the JSON data or you just clicked again on check and it worked?

---

**post_id:** 589491  
**author:** 22ds3000103  
**timestamp:** 2025-02-02T14:10:49.716Z

i loaded the data again as you said and clicked on check again. then it gave correct

---

**post_id:** 589510  
**author:** 24f1002359  
**timestamp:** 2025-02-02T14:18:56.612Z

Hi [@24DS1000121\_ULAGAOOZ](/u/24ds1000121_ulagaooz) ,

For the **ngrok tunnel** question and any other question requiring a server URL, make sure to **keep all servers running** when clicking the **Save** button.

Also, I couldn’t find the **GitHub Pages URL** in your **GA2 response**, and many answers are unmarked. It seems you **didn’t click the Save button**.

Your current score is **4.5/10**.

---

**post_id:** 589548  
**author:** Jivraj  
**timestamp:** 2025-02-02T14:43:42.988Z

Here's a description of the image:
The image shows a webpage related to an assignment. It is a screenshot of a browser window with a course page from IIT Madras. The page focuses on "Graded Assignment 2".
image text: IIT Madras Jan 2025-TDS
Graded Assignment 2
Due date for this assignment: 2025-02-02, 23:59 IST.
You may submit any number of times before the due date. The final submission will be considered for grading.
You have last submitted on: 2025-01-22, 13:11 IST
If you have any difficulty accessing the Graded Assignment, please check the following causes:
Ad blockers need to be disabled/removed.
The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
Javascript is required for the site to work correctly.
Chrome Browser is the recommended software to access the contents.
Disable any browser extensions that may be interfere with the site from working correctly.
Overly aggressive anti-virus software may also cause similar access problems.
You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Graded Assignment, otherwise your score will not be considered for evaluation.
Graded Assignment 2 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga2. Please attempt it.
  
Not able to submit GA2 assignment Since I’m seeing this page there is no submit button available.Will it take last saved for submission.

---

**post_id:** 589549  
**author:** Jivraj  
**timestamp:** 2025-02-02T14:47:48.219Z

I am facing several problems with the submission portal …

1. In question no 5 I entered the answer 78918 It was correct , I submitted it after few hours when I reloaded the portal its showing incorrect … I tried to enter twice thrice also solved it again but no use…
2. In question 10 I entered the required link it was correct after saving it and reloading the portal it shows incorrect …
3. In question 9 I did all the necessary thing but the portal is showing couldn’t fetch … My system is able to fetch the data but the portal says “failed to fetch”

Here's a description of the image:
The image is a terminal window, likely in an IDE, displaying output from a Python application using FastAPI. The output shows server logs, including the startup process, and HTTP requests with their corresponding status codes. Some requests resulted in "404 Not Found", and others resulted in "200 OK".
image text:
```
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
python3.12 - Fastapi +
INFO: Will watch for changes in these directories: ['F:\\BS DATA SCIENCE\\Diploma Level\\TERM 2\\TDS\\Week 2\\Fastapi']
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [18904] using StatReload
INFO: Started server process [17712]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: 127.0.0.1:53983 - "GET / HTTP/1.1" 404 Not Found
INFO: 127.0.0.1:53983 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO: 127.0.0.1:53984 - "GET /api HTTP/1.1" 200 OK
INFO: 127.0.0.1:54003 - "GET /api?class=1A HTTP/1.1" 200 OK
INFO: 127.0.0.1:54004 - "GET /api?class=1A HTTP/1.1" 200 OK
INFO: 127.0.0.1:54145 - "GET /api?class=1A HTTP/1.1" 200 OK
```  
image description : The image shows a web browser displaying JSON data. The data appears to be a list of students with their student IDs and classes, all belonging to "1A" class. The URL in the address bar is "127.0.0.1:8000/api?class=1A". "Pretty-print" is checked.
image text:
```
← 127.0.0.1:8000/api?class=1A X +
Pretty-print✔
{
"students": [
{
"studentId": 224,
"class": "1A"
},
{
"studentId": 226,
"class": "1A"
},
{
"studentId": 750,
"class": "1A"
},
{
"studentId": 1241,
"class": "1A"
},
{
"studentId": 1408,
"class": "1A"
},
{
"studentId": 1704,
"class": "1A"
}
]
}
```  
Here's a description of the image:
The image appears to be a section of a webpage or a user interface, likely related to API interaction or a testing platform. It focuses on providing instructions and testing an API endpoint. Key elements include:
\* \*\*Instructions:\*\* The top section provides guidelines.
\* \*\*API endpoint:\*\* An API endpoint, http://127.0.0.1:8000/api is displayed.
\* \*\*Error Message:\*\* Below the API URL, a `TypeError: Failed to fetch` message indicates that a request to the API failed.
\* \*\*Button:\*\* A "Check" button is present at the bottom.
image text:
If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?class=1A&class=
should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
TypeError: Failed to fetch
We'll check by sending a request to this URL with?class=... added and check if the response matches the data.
Check

---

**post_id:** 589571  
**author:** Jivraj  
**timestamp:** 2025-02-02T15:08:09.930Z

Hi [@23f2000573](/u/23f2000573) ,

As error mentions to add tag to image.

Adding different tags is like versioning your docker image, image with a particular tag can be pulled.

For adding tag use  
image description: The image displays a text in a dark background, the text is about commands used to build, run and deploy a container.
image text: To build, run, and deploy the container, run these commands:
# Create an account on https://hub.docker.com/ and then login
podman login docker.io
# Build and run the container
podman build -t py-hello .
podman run -it py-hello
# Push the container to Docker Hub. Replace $DOCKER\_HUB\_USERNAME with your Docker Hub username.
podman push py-hello:latest docker.io/$DOCKER\_HUB\_USERNAME/py-hello
# Push adding a specific tag, e.g. dev
TAG=dev podman push py-hello docker.io/$DOCKER\_HUB\_USERNAME/py-hello:$TAG

---

**post_id:** 589667  
**author:** 23f2000573  
**timestamp:** 2025-02-02T15:59:16.831Z

For GA2 there is not question that asks if you visited GA2 page or not.  
Just answer on GA2 page [TDS 2025 Jan GA2 - Deployment Tools](https://exam.sanand.workers.dev/tds-2025-01-ga2#hq-docker-hub-image).

---

**post_id:** 589795  
**author:** 24DS1000121_ULAGAOOZ  
**timestamp:** 2025-02-02T16:54:03.510Z

Hi [@24f1002359](/u/24f1002359)

For **Question 10**, ensure that **all servers are running** every time you submit (click the **Save** button). Since **ngrok generates a new URL each time it runs**, double-check that the **ngrok URL is correct** before submitting.

For **Question 9**, did you **enable CORS**? To verify, check your **browser console**—if CORS is not enabled, you should see an error message indicating the issue.

image description: The image is a screenshot of a browser's developer console, specifically the "Console" tab. It displays a series of messages related to a web request. The top of the console shows navigation options, like "Elements", "Console", "Sources", etc. The main content includes: "starting ajax request to the resource." "ajax request done." and an error message: "Access to XMLHttpRequest at 'http://google.com/' from origin 'null' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource."
image text: Elements Console Sources Network Performance Memory Application >> 1 × top Filter Default levels starting ajax request to the resource. index.html:14 ajax request done. index.html:29 Access to XMLHttpRequest at 'http://google.com/' from origin 'null' has been blocked by index.html:1 CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

For question 5, I have tried executed script with your set of parameters, your answer is correct. Will discuss it internally.

Kind regards.

---

**post_id:** 589831  
**author:** Jivraj  
**timestamp:** 2025-02-02T17:14:46.295Z

for question 9 u can use ,

`from fastapi import FastAPI, Query`

and

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/e/eeb2657ff48229df8814e1756112074a16590de2_2_690x51.png)

---

**post_id:** 589838  
**author:** 22f3000657  
**timestamp:** 2025-02-02T17:17:42.209Z

Dear Sir,

Thank you very much sir for your kind reply.  
I have published the page on GITHUB and this is the screen shot. As you see the url link is:  
<https://ulagaoozhian.github.io/TDS-page/>  
But I dont know the GA portal does not accept the answer. That also I have given a screenshot.  
Please look into it sir. I am loosing 1 precise mark !!!  
thanks and regards,  
ULAGAOOZHIAN  
image description: The image is a screenshot of a web page on GitHub, specifically the "Settings" page for a project named "TDS-page" under the user "ULAGAOOZHIAN". The page focuses on "GitHub Pages" settings. The main sections are: "GitHub Pages" with information about the live site address, "Build and deployment" with source selection and branch settings, and "Custom domain". The page also displays options to enforce HTTPS, and links to documentation.
image text: GitHub Pages is designed to host your personal, organization, or project pages from a GitHub repository.
Your site is live at https://ulagaoozhian.github.io/TDS-page/
Last deployed by ULAGAOOZHIAN 19 hours ago
Build and deployment
Source
Deploy from a branch
Branch
Your GitHub Pages site is currently being built from the main branch. Learn more about configuring the publishing source for your site.
main / (root)
Learn how to add a Jekyll theme to your site.
Your site was last deployed to the github-pages environment by the pages build and deployment workflow.
Learn more about deploying to GitHub Pages using custom workflows
Custom domain
Custom domains allow you to serve your site from a domain other than ulagaoozhian.github.io. Learn more about configuring custom domains.
✔ Enforce HTTPS

Here's the image description:
The image is a screenshot of a web page on a computer screen. It appears to be a coding or development related task. The page includes text instructions and code snippets. The primary focus of the page seems to be instructing the user on publishing a page using GitHub Pages and including their email address in the HTML.
\*\*image text:\*\*
```
My Dashboard
WOL3: Complex
BDM Capstone
About the Cours
Graded Assignm
Latest Courses/T
Ex TDS 2025 Jan GA
Pages
exam.sanand.workers.dev/tds-2025-01-ga2
☆
Navigation privée
01:37:36 left Score: 0/10
Check all
Save
3423-86-1511437:17. INSTALLATION ID
2015-04-20718/ONG: false
243-84-STA-3[endgroup]
2013-04-25736:28.Parsed event values:
2017-04-21716-2718-31817547
54
35
2823-04-2016:27:18.3136647
Reñor maintainers
Username of commenter: Mriduls
Repa Owner: community
56
200-BESTIAOCleaning up orphan processes
#4306
#4397
54
4306
31
#4305
#4394
#4303
#4302
Add collaboratort
Set up job
Perform invitation action
Complete job
>#4391
SETTINGS
Codespaces main ०० ४० CodeStream Live Share Quokka Wallaby
Spaces: 4 Plain Text Layout: US Spell CodeQuote No Matches RC
Publish a page using GitHub Pages that showcases your work. Ensure that your email address 24ds1000121@ds.study.iitm.ac.in is in the page's HTML.
GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a:
<!--email\_off-->24ds1000121@ds.study.iitm.ac.in<!--/email\_off-->
What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/
https://ulagaoozhian.github.io/TDS-page/?v=1, ?v=2
Error: 24ds1000121@ds.study.iitm.ac.in is not in the response: <!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-
scale=1.0"> <title>My Model Page</title> </head> <body> <h1>My Model Page</h1> <p>Contact me at: <a href="/cdn-cgi/l/email-
protection#2416104057151414141516156440570a575051405d0a4d4d50490a45470a4d4a"> <span class="\_cf\_email\_" data-
cfemail="9aa8aefee9abaaaaaaaba8abdafee9b4e9eeeffee3b4f3f3eef7b4fbf9b4f3f4">[email&#160;protected] </span></a></p> <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-
static/email-decode.min.js"> </script> </body> </html> ...
If a recent change that's not reflected, add ?v=1, ?v=2 to the URL to bust the cache.
Check
Q Rechercher
X
17:52
(DELL
人
FRA
02/02/2025
```
  
Sir, the page I have published via GITHUB is as below:  
Here's a description of the image:
The image is a screenshot of a webpage displayed in a web browser. The webpage has a title "My Model Page". The browser's address bar shows "ulagaoozhian.github.io/TDS-page/". Below the title is text saying, "Contact me at: 24ds1000121@ds.study.iitm.ac.in". The bottom of the screen shows the Windows taskbar.
image text:
My Dashboard - IIT M X
WOL3: Complex Data X
BDM Capstone
X
About the Course :: || X
Graded Assignment
X
Ex TDS 2025 Jan GA2 - X
My Model Page
X
ulagaoozhian.github.io/TDS-page/
My Model Page
Contact me at: 24ds1000121@ds.study.iitm.ac.in
Rechercher
DELL
0
X
FRA
Navigation privée
17:58
02/02/2025

---

**post_id:** 589971  
**author:** 24DS1000121_ULAGAOOZ  
**timestamp:** 2025-02-02T18:11:48.000Z

Hi [@24DS1000121\_ULAGAOOZ](/u/24ds1000121_ulagaooz) ,

That’s because GitHub protects your email when an external website requests a GitHub Page. To disable this protection, create a `.nojekyll` file in your root folder of your repository.

Here's a brief description of the image:
The image shows a web development environment with a debugging tool open. On the left, there's a display related to a GitHub Pages URL, and a web page showing "My Model Page." The right side features a Chrome developer tools panel with the "Preview" tab open, displaying the content of a webpage.
image text: [Admin] 01:19:33 left Score: 0/10 Check all Save
What is the GitHub Pages URL? It might look like:
https://[USER].github.io/[REPO]/
https://ulagaoozhian.github.io/TDS-page/
Error: 24ds1000121@ds.study.iitm.ac.in is not in the response:
<!DOCTYPE html> <html lang="en"> <head> <meta charset="UTF-
8"> <meta name="viewport" content="width=device-width, initial-
scale=1.0"> <title>My Model Page</title> </head> <body>
<h1>My Model Page</h1> <p>Contact me at: cgi/l/email-
protection#380a0c5c4b09080808090a09785c4b164b4c4d5c4116515
14c5516595b165156"><span class="\_cf\_email\_" data-
cfemail="c7f5f3a3b4f6f7f7f7f6f5f687a3b4e9b4b3b2a3bee9aeaeb3aa
e9a6a4e9aea9">[email&#160;protected] </span></a></p> <script
data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-
static/email-decode.min.js"> </script> </body> </html> ...
If a recent change that's not reflected, add ?v=1, ?v=2 to the
URL to bust the cache.
Filter
Invert More filters
All Fetch/XHR Doc CSS JS Font Img Media Manifest WS Wasm Other
10 ms 20 ms 30 ms 40 ms 50 ms 60 ms 70 ms 80 ms 90 ms 100 ms 110
Name X Headers Preview Response Initiator Timing
TDS-page/
My Model Page
Contact me at: [email protected]
1 requests 0 B transferred 61
Console Developer resources Network conditions Issues Performance monitor +
| top Filter Default levels 12

Kind regards

---

**post_id:** 589976  
**author:** 24DS1000121_ULAGAOOZ  
**timestamp:** 2025-02-02T18:15:27.000Z

I am facing this issue. It is stating the error as mentioned  
image description: The image is a screenshot of a text-based programming interface. The text on the image discusses how a URL with a query parameter, class, should function in an API. It gives example URL, notes the need to enable CORS, and displays an API endpoint with an error message which contains a list of student IDs and classes.
image text: If the URL has a query parameter class, it should return only students in those classes. For example, /api?class=1A should return only students in class 1A. /api?
class=1A&class=1B should return only students in class 1A and 1B. There may be any number of classes specified. Return students in the same order as they appear in
the CSV file (not the order of the classes).
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for FastAPI? It might look like: http://127.0.0.1:8000/api
http://127.0.0.1:8000/api
Error: Response [{"studentId":113,"class":"5W"},{"studentId":206,"class":"8H"},{"studentId":231,"class":"4Z"},{"studentId":246,"class":"4Z"},{"studentId":355,"class":"11E"},
{"studentId":507,"class":"8H"},{"studentId":548,"class":"8H"},{"studentId":558,"class":"4Z"},{"studentId":586,"class":"11E"},{"studentId":879,"class":"4Z"},{"studentId":946,"class":"8H"},
{"studentId":1105,"class":"4Z"},{"studentId":1236,"class":"5W"},{"studentId":1489,"class":"8H"}, {"studentId":1555,"class":"4Z"},{"studentId":1689,"class":"5W"},{"studentId":1812,"class":"4Z"},
{"studentId":1817,"class":"5W"},{"studentId":1859,"class":"5W"},{"studentId":1883,' s":"5W"},{"studentId":1883,"class":"5W"},{"studentId":1978,"class":"11E"}] does not match expected [{"studentId":202,"class":"4Z"},
{"studentId":304,"class":"5W"},{"studentId":367,"class":"4Z"},{"studentId":497,"class":"5W"},{"studentId":551,"class":"11E"},{"studentId":592,"class":"4Z"},{"studentId":613,"class":"5W"},
{"studentId":746,"class":"4Z"},{"studentId":955,"class":"11E"},{"studentId":995,"class":"8H"}, {"studentId":1023,"class":"8H"},{"studentId":1284,"class":"8"},{"studentId":1363,"class":"4Z"},
{"studentId":1399,"class":"4Z"},{"studentId":1474,"class":"11E"},{"studentId":1544,"class":"5W"},{"studentId":1608,"class":"11E"},{"studentId":1750,"class":"8"},{"studentId":1761,"class":"8H"},
{"studentId":1782,"class":"5W"},{"studentId":1792,"class":"8H"}, {"studentId":1882,"class":"8H"}]
We'll check by sending a request to this URL with ?class=... added and check if the response matches the data.
①

The /api is working perfectly fine manually either I specify the class or without it  
Here's a brief description of the image:
The image is a screenshot of a webpage displaying a JSON object. The JSON object contains an array of "students", each with a "studentId" and a "class". The webpage uses "Pretty-print" formatting to make the JSON readable.
image text: {"students":[{"studentId":1,"class":"100"},{"studentId":2,"class":"7K"},{"studentId":3,"class":"2G"},{"studentId":4,"class":"100"},{"studentId":5,"class":"4W"},{"studentId":6,"class":"10H"},
{"studentId":7,"class":"8F"},{"studentId":8,"class":"126"},{"studentId":9,"class":"8B"},{"studentId":10,"class":"1R"},{"studentId":11,"class":"7E"},{"studentId":12,"class":"120"},
{"studentId":13,"class":"12H"},{"studentId":14,"class":"5X"},{"studentId":15,"class":"8B"},{"studentId":16,"class":"7L"},{"studentId":17,"class":"60"},{"studentId":18,"class":"9p"},
{"studentId":19,"class":"111"},{"studentId":20,"class":"12R"},{"studentId":21,"class":"6T"},{"studentId":22,"class":"5H"},{"studentId":23,"class":"9E"},{"studentId":24,"class":"120"},
{"studentId":25,"class":"4J"},{"studentId":26,"class":"3M"},{"studentId":27,"class":"8B"},{"studentId":28,"class":"1J"},{"studentId":29,"class":"1J"},{"studentId":30,"class":"90"},
{"studentId":31,"class":"11B"},{"studentId":32,"class":"5Z"},{"studentId":33,"class":"4B"},{"studentId":34,"class":"4L"},{"studentId":35,"class":"125"},{"studentId":36,"class":"100"},
{"studentId":37,"class":"5K"},{"studentId":38,"class":"8E"},{"studentId":39,"class":"1N"},{"studentId":40,"class":"116"},{"studentId":41,"class":"6A"},{"studentId":42,"class":"4U"},
{"studentId":43,"class":"10T"},{"studentId":44,"class":"91"},{"studentId":45,"class":"5F"},{"studentId":46,"class":"8X"},{"studentId":47,"class":"12G"},{"studentId":48,"class":"5Z"},
{"studentId":49,"class":"116"},{"studentId":50,"class":"90"},{"studentId":51,"class":"108"},{"studentId":52,"class":"12A"},{"studentId":53,"class":"11"},{"studentId":54,"class":"6D"},
{"studentId":55,"class":"81"},{"studentId":56,"class":"11P"},{"studentId":57,"class":"10H"},{"studentId":58,"class":"9A"},{"studentId":59,"class":"7Y"},{"studentId":60,"class":"2N"},
{"studentId":61,"class":"8F"},{"studentId":62,"class":"6K"},{"studentId":63,"class":"9A"},{"studentId":64,"class":"80"},{"studentId":65,"class":"9Z"},{"studentId":66,"class":"4M"},
{"studentId":67,"class":"6N"},{"studentId":68,"class":"3Q"},{"studentId":69,"class":"10P"},{"studentId":70,"class":"6Z"},{"studentId":71,"class":"8T"},{"studentId":72,"class":"12F"},
{"studentId":73,"class":"6F"},{"studentId":74,"class":"12B"},{"studentId":75,"class":"70"},{"studentId":76,"class":"4U"},{"studentId":77,"class":"12Y"},{"studentId":78,"class":"4Y"},
{"studentId":79,"class":"1K"},{"studentId":80,"class":"8A"},{"studentId":81,"class":"1V"},{"studentId":82,"class":"9W"},{"studentId":83,"class":"2C"},{"studentId":84,"class":"30"},
{"studentId":85,"class":"2Z"},{"studentId":86,"class":"12B"},{"studentId":87,"class":"3R"},{"studentId":88,"class":"10"},{"studentId":89,"class":"41"},{"studentId":90,"class":"2D"},
{"studentId":91,"class":"4V"},{"studentId":92,"class":"110"},{"studentId":93,"class":"2C"},{"studentId":94,"class":"2U"},{"studentId":95,"class":"12R"},{"studentId":96,"class":"1T"},
{"studentId":97,"class":"11M"},{"studentId":98,"class":"2Q"},{"studentId":99,"class":"4V"},{"studentId":100,"class":"11Z"},{"studentId":101,"class":"6A"},{"studentId":102,"class":"10Z"},
{"studentId":103,"class":"12T"},{"studentId":104,"class":"11X"},{"studentId":105,"class":"3K"},{"studentId":106,"class":"7Z"},{"studentId":107,"class":"6B"},{"studentId":108,"class":"3Z"},
{"studentId":109,"class":"116"},{"studentId":110,"class":"9E"},{"studentId":111,"class":"6R"},{"studentId":112,"class":"9R"},{"studentId":113,"class":"5W"},{"studentId":114,"class":"12N"},
{"studentId":115,"class":"10F"},{"studentId":116,"class":"5F"},{"studentId":117,"class":"11M"},{"studentId":118,"class":"2J"},{"studentId":119,"class":"5K"},{"studentId":120,"class":"11P"},
{"studentId":121,"class":"8P"},{"studentId":122,"class":"9Y"},{"studentId":123,"class":"6V"},{"studentId":124,"class":"11Z"},{"studentId":125,"class":"11U"},{"studentId":126,"class":"2K"},
{"studentId":127,"class":"51"},{"studentId":128,"class":"9L"},{"studentId":129,"class":"11X"},{"studentId":130,"class":"6L"},{"studentId":131,"class":"12B"},{"studentId":132,"class":"9G"},
{"studentId":133,"class":"7U"},{"studentId":134,"class":"2G"},{"studentId":135,"class":"5T"},{"studentId":136,"class":"8V"},{"studentId":137,"class":"8U"},{"studentId":138,"class":"9E"},
{"studentId":139,"class":"10F"},{"studentId":140,"class":"11Y"},{"studentId":141,"class":"6J"},{"studentId":142,"class":"8W"},{"studentId":143,"class":"5V"},{"studentId":144,"class":"9T"},
{"studentId":145,"class":"2S"},{"studentId":146,"class":"2Z"},{"studentId":147,"class":"2D"},{"studentId":148,"class":"3R"},{"studentId":149,"class":"9X"},{"studentId":150,"class":"2F"},
{"studentId":151,"class":"9Y"},{"studentId":152,"class":"10L"},{"studentId":153,"class":"6Q"},{"studentId":154,"class":"9W"},{"studentId":155,"class":"10D"},{"studentId":156,"class":"10Q"},
{"studentId":157,"class":"9F"},{"studentId":158,"class":"5D"},{"studentId":159,"class":"2P"},{"studentId":160,"class":"6E"},{"studentId":161,"class":"1B"},{"studentId":162,"class":"2F"},
{"studentId":163,"class":"2D"},{"studentId":164,"class":"10T"},{"studentId":165,"class":"1C"},{"studentId":166,"class":"5I"},{"studentId":167,"class":"7Z"},{"studentId":168,"class":"3F"},
{"studentId":169,"class":"9V"},{"studentId":170,"class":"6D"},{"studentId":171,"class":"2K"},{"studentId":172,"class":"8K"},{"studentId":173,"class":"9S"},{"studentId":174,"class":"1E"},
{"studentId":175,"class":"8P"},{"studentId":176,"class":"7V"},{"studentId":177,"class":"12F"},{"studentId":178,"class":"6X"},{"studentId":179,"class":"12H"},{"studentId":180,"class":"5C"},
{"studentId":181,"class":"7J"},{"studentId":182,"class":"5S"},{"studentId":183,"class":"2I"},{"studentId":184,"class":"10K"},{"studentId":185,"class":"3H"},{"studentId":186,"class":"11W"},
{"studentId":187,"class":"10S"},{"studentId":188,"class":"9I"},{"studentId":189,"class":"3F"},{"studentId":190,"class":"11L"},{"studentId":191,"class":"35"},{"studentId":192,"class":"4C"},
{"studentId":193,"class":"110"},{"studentId":194,"class":"9I"},{"studentId":195,"class":"4U"},{"studentId":196,"class":"1C"},{"studentId":197,"class":"5V"},{"studentId":198,"class":"20"},
{"studentId":199,"class":"10V"},{"studentId":200,"class":"3P"},{"studentId":201,"class":"6I"},{"studentId":202,"class":"9G"},{"studentId":203,"class":"12X"},{"studentId":204,"class":"9Z"},
{"studentId":205,"class":"11C"},{"studentId":206,"class":"8H"},{"studentId":207,"class":"5Y"},{"studentId":208,"class":"7R"},{"studentId":209,"class":"90"},{"studentId":210,"class":"30"},
{"studentId":211,"class":"10C"},{"studentId":212,"class":"30"},{"studentId":213,"class":"7Q"},{"studentId":214,"class":"3P"},{"studentId":215,"class":"4U"},{"studentId":216,"class":"8L"},
{"studentId":217,"class":"8S"},{"studentId":218,"class":"4S"},{"studentId":219,"class":"7Z"},{"studentId":220,"class":"70"},{"studentId":221,"class":"4S"},{"studentId":222,"class":"12L"},
{"studentId":223,"class":"7A"},{"studentId":224,"class":"100"},{"studentId":225,"class":"7C"},{"studentId":226,"class":"2W"},{"studentId":227,"class":"2W"},{"studentId":228,"class":"6I"},
{"studentId":229,"class":"2W"},{"studentId":230,"class":"2H"},{"studentId":231,"class":"4Z"},{"studentId":232,"class":"70"},{"studentId":233,"class":"12L"},{"studentId":234,"class":"6A"},
{"studentId":235,"class":"2K"},{"studentId":236,"class":"2K"},{"studentId":237,"class":"12J"},{"studentId":238,"class":"12J"},{"studentId":239,"class":"11Y"},{"studentId":240,"class":"7D"},
{"studentId":241,"class":"7I"},{"studentId":242,"class":"1Y"},{"studentId":243,"class":"1E"},{"studentId":244,"class":"3E"},{"studentId":245,"class":"7J"},{"studentId":246,"class":"4Z"},
{"studentId":247,"class":"3E"},{"studentId":248,"class":"10K"},{"studentId":249,"class":"3W"},{"studentId":250,"class":"6I"},{"studentId":251,"class":"12B"},{"studentId":252,"class":"9K"}]

Sample class example that I tried manually is below  
Here's a description of the image:
The image shows a computer screen with a black background. The main focus is on a code snippet displayed within a web browser, with a URL of "127.0.0.1:8000/api?class=3Q" visible in the address bar. The code appears to be JSON data, with an object containing a "students" array. The array elements seem to represent student IDs and their associated class, which is consistently "3Q". Below this is a taskbar with various application icons.
image text:
```json
"students":[{"studentId":68,"class":"3Q"},{"studentId":838,"class":"3Q"},{"studentId":902,"class":"3Q"},{"studentId":1096,"class":"3Q"},{"studentId":1623,"class":"3Q"},
{"studentId":1784,"class":"3Q"},{"studentId":1834,"class":"3Q"},{"studentId":1893,"class":"3Q"},{"studentId":1931,"class":"3Q"}]}
```

The main code is below

```
import sys

sys.path.append("C:\\Users\\Deveshu Pathak\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\Scripts")
# tds_q9.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Load CSV file
df = pd.read_csv("q-fastapi.csv")

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

# Convert to dictionary list
    students = filtered_df.to_dict(orient="records")
    return {"students": students}

```

---

**post_id:** 590015  
**author:** Saransh_Saini  
**timestamp:** 2025-02-02T18:26:26.753Z

Gentleman,  
Will you consider my mark or not ?

---

**post_id:** 590021  
**author:** 21f3003255  
**timestamp:** 2025-02-02T18:40:15.664Z

Gentleman,  
I dont understand. I just now, on triggering the Github action, I copied the url of my github repository. It worked !

---

**post_id:** 590023  
**author:** 21f3003255  
**timestamp:** 2025-02-02T18:42:20.205Z

The problem is that, if class param is passed, only then it is filtering as usual, but when no param is passed it returns the entire DataFrame, which is not supposed to happen.

If no parameter is passed it should return an empty list.

I suspect you directly copied this code from ChatGPT without understanding, which is acceptable for us, but not very helpful for you.

---

**post_id:** 590026  
**author:** Abhay222  
**timestamp:** 2025-02-02T18:57:19.255Z

I had submitted the assignment in the evening, but now in the portal it’s showing not submitted.  
image description : A screenshot of a dark-themed user interface displaying a section titled "Recent saves". Below, there are three entries. Each entry has a "Reload" button, followed by the date and time the save was made, and a score.
image text: Recent saves
Reload from 02/02/2025, 18:21:07. Score: 10
Reload from 02/02/2025, 18:20:57. Score: 10
Reload from 02/02/2025, 16:45:08. Score: 8.5  
image description: The image displays a section from a platform. The section is titled "Module 2: Deployment Tools". There's an assignment called "Graded Assignment 2" with the due date of "2 Feb 2025". The assignment status is "Not Submitted". There are three columns: "Your Score", "Peer Average", and "Median Score". Each of them contains a hyphen.
image text: Module 2: Deployment Tools Assignment Graded Assignment 2 Assessment (Due: 2 Feb 2025) Not Submitted Your Score Peer Average Median Score

---

**post_id:** 590097  
**author:** Saransh_Saini  
**timestamp:** 2025-02-03T05:06:38.596Z

Even there is no submission button provided in GA2 and GA3 on the portal unlike Graded Assignment 1.  
image description: The image is of a webpage displaying information about a graded assignment. The title is "Graded Assignment 2." It provides details like the deadline, submission rules, and troubleshooting steps for any access issues. There is a link to access the assignment.
image text: Graded Assignment 2
The due date for submitting this assignment has passed.
Due on 2025-02-02, 23:59 IST.
You may submit any number of times before the due date. The final submission will be considered for grading.
If you have any difficulty accessing the Graded Assignment, please check the following causes:
Ad blockers need to be disabled/removed.
The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
Javascript is required for the site to work correctly.
Chrome Browser is the recommended software to access the contents.
Disable any browser extensions that may be interfere with the site from working correctly.
Overly aggressive anti-virus software may also cause similar access problems.
You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Graded Assignment, otherwise your score will not be considered for evaluation.
Graded Assignment 2 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga2. Please attempt it.

---

**post_id:** 590109  
**author:** 22f2001630  
**timestamp:** 2025-02-03T05:53:20.398Z

same problem, please sir [@carlton](/u/carlton) consider this GA marks otherwise our efforts will be wasted

---

**post_id:** 590114  
**author:** Saransh_Saini  
**timestamp:** 2025-02-03T06:04:25.854Z

We have removed that button, cause it was causing confusion among the students.

If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.

Regards,  
TDS TA

---

**post_id:** 590115  
**author:** 22f2001630  
**timestamp:** 2025-02-03T06:05:51.002Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png) Saransh\_Saini:

> ers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.
>
> Regards,

Does this go for GA1 also ?

---

**post_id:** 590390  
**author:** Pururaj  
**timestamp:** 2025-02-03T18:59:09.558Z

Yes. The scores you achieve in the TDS portal are your scores for the GA. It’s not necessary to do anything on the Seek Portal.

---

**post_id:** 590404  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:49:02.479Z

Actually even on the portal it’s showing like this:  
image description: The image is a screenshot of a webpage related to an online degree program. The webpage has a red banner at the top indicating that the quiz ended on January 26, 2025, at 11:59 PM IST, with a score of 0. It presents a question with a comment about hacking the code. It also provides guidelines for deciding whether to take the TDS term. There are also details about the user's login, recent saves and the discussion forum.
image text: Outline :: IITM Online Degree
Tools in Data Science
Ex TDS 2025 Jan GA1 - Developme X
GA2 - Deployment Tools - Discu X
Ended at Sun, 26 Jan, 2025, 11:59 pm IST Score: 0 Check all Save
7. It s nackable. It's possible to get the answer to some questions by nacking the code for this quiz. That's allowed.
Should you take TDS this term?
• If this assignment takes you under 2 hours to complete, you will likely do OK in TDS.
• If you score above 8 / 10, you might get an S or A grade, with effort and luck.
Have questions? Join the discussion on Discourse
You are logged in as 22f2001630@ds.study.iitm.ac.in.
Logout
Recent saves
Reload from 1/25/2025, 10:56:53 PM. Score: 6.5
Reload from 1/25/2025, 10:56:53 PM. Score: 6.5
Reload from 1/25/2025, 10:56:53 PM. Score: 6.5
Questions
Type here to search
Activate Windows
Go to Settings to activate Windows.
11:35
03-02-2025
  
So it’s confusing.

Just Checked my Score Card.  
Here's a description of the image:
The image is a screenshot of a webpage from the IIT Madras online degree platform. It displays the user's dashboard, specifically the "My Current Courses" section. Two courses are listed: "Tools in Data Science" (New Course) and "Business Data Management - Project" (Retry Project). The page also shows the user's Cumulative Grade Point Average (CGPA) and Project CGPA for the current term. The date displayed on the page is 03 February, 2025.
image text:
My Dashboard - IIT Madras Onl x BDM Capstone x Tools in Data Science x Ex TDS 2025 Jan GA1 - Developme x GA2 - Deployment Tools - Discu x +
app.onlinedegree.iitm.ac.in/student\_dashboard/current\_courses
☆
IIT Madras
Degree in Data Science and Applications
TANMAY GARG Latest Updates SIGN OUT
03 February, 2025
JANUARY 2025 TERM
My Current Courses
Cumulative Grade Point Average (CGPA) till this term - 8.3
Project Cumulative Grade Point Average (Project CGPA) till this term - 0.0
Tools in Data Science
NEW COURSE
Week 1 Assignment - 65.00
Go to Course page >
Business Data
Management - Project
RETRY PROJECT
Registered
Go to Project page >
Reporting harassment: IITM BS Degree Team is committed to ensuring that everyone is equally valued and treats one another with respect. All complaints of bullying or harassment will be taken seriouly and will be dealt with quickly and with respect for all people
involved. Learners may write to this email id students-grievance@study.iitm.ac.in which will be considered as a formal complaint. We will make reasonable and appropriate efforts to preserve an individual's privacy and protect the confidentiality of information.
Type here to search
ENG
11:37
03-02-2025
  
Thank you for your attention to our problems you are the real heroes.  
[@Saransh\_Saini](/u/saransh_saini)

---

**post_id:** 591241  
**author:** Pratiyush  
**timestamp:** 2025-02-06T13:20:27.517Z

Same problem with my submission

---

**post_id:** 591242  
**author:** Pratiyush  
**timestamp:** 2025-02-06T13:21:38.546Z

Hi Tanmay,

No need to worry. From Recent Saves top one will be selected for grading.

---

