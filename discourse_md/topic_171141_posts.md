# tds-official-project1-discrepencies

Please post any discrepancies related to project1.

[@carlton](/u/carlton)

## Who were evaluated? How did we decide what to evaluate?

All the image ids we evaluated were what *you* submitted to us. This is the list of docker repos that was given to us by [@s.anand](/u/s.anand) as the official list that met all the pre-requisites of Project 1. Therefore we will only evaluate those on this list who are eligible for evaluation with the repos *you* gave us.

For clarity. Your docker repo gets a unique id every time it is changed. We will ONLY evaluate the image id which was present at the time of the docker repo being pulled. This acts as a time stamped frozen version of your repo. No other image id will be evaluated.

## How to fix bugs in our scripts

Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

### **Docker Image Architecture Issue Report**

If your Docker image was run on the wrong architecture, please fill out this form:  
[Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

## Bug fixes

If you find bugs in our evaluation scripts, you might benefit from more marks because of the bug fix. So it is in your interest to look through our scripts and logs and identify bugs or anomalies. You might just go from 0 to heros.

Kind regards,  
TDS Team

---

---

What is the highest mark anyone has scored? Is it 22/20  
[@Carlton](/u/carlton)?

---

How come me and my group used same code but some got 10 some 11 some 12?

---

[@carlton](/u/carlton) Please make clear what the average marks are, what highest marks are, and how the project will be evaulated.

We are very close to the end semester exam, and we are still not clear on assignment and project marks. It is a bit frustrating to plan in such circumstances.

---

You have to see the logs for that. We have shared the logs. Everyone was graded by the exact same code, so there is no partiality. Your code did not produce consistent results.

---

I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.

This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

---

My evaluation log file is missing, although I followed all the steps to generate the docker image correctly, it’s showing the server didn’t start for 5 minutes but when I uploaded it, it was working fine. Please help me out sir, I worked hard on the project. I’ll get a zero, but I made the submissions correctly. Some other student also got the “server didn’t start in 5 minutes” but he has an evaluation log file. Please kindly help me out. My roll no. is 22f2001389

---

We will check and rerun on arm if we ran it on the wrong emulation.

---

Any suggestions for my case sir ? I’m really tensed.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002933/48/118648_2.png) 22f3002933:

> I have noticed that my image was run on a `x86_64` architecture ( I can see my email in the logs shared ) whereas I built this docker image on my mac which is `ARM`. This is why I can see that my docker image never ran properly and threw the `exec format error`.
>
> This was never mentioned on which architecture machine, our images will be evaluated. I request that my evaluation be done again on the right machine.

[@carlton](/u/carlton) same issue, My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error` and **Evaluation log file** is MISSING.

Actually my image was run on x86\_64 architecture as it was present in that log file and because of the wrong architecture it never started.

I also request that my evaluation be done again on the right machine.

Here's a description of the image:
The image displays information about a Docker image. Key elements include:
\* \*\*Tag\*\*: "latest"
\* \*\*Details\*\*: The image was last pushed about 1 month ago by "pradeepmondal".
\* \*\*Digest\*\*: "a4d9cad3b5f5"
\* \*\*OS/ARCH\*\*: "linux/arm64/v8"
\* \*\*Last pull\*\*: "1 day"
\* \*\*Compressed size\*\*: "179.2 MB"
\* \*\*Docker pull command\*\*: "docker pull pradeepmondal/final-tds-project-pradeep-mondal:latest" with a "Copy" button.
image text:
TAG
latest
Last pushed about 1 month by pradeepmondal
Digest
a4d9cad3b5f5
docker pull pradeepmondal/final-tds-project-pradeep-mondal:latest
Copy
OS/ARCH
Last pull
Compressed size
linux/arm64/v8
1 day
179.2 MB

Even just now I tried running the exact image:  
image description: A terminal output with podman commands and server status information.
image text:
```
→ ~ podman run --rm -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 047fa151bf43
INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

It is running fine on my macbook air m1 (ARM)

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001389/48/12849_2.png) 22f2001389:

> uploaded

Facing the same issue sir, kindly look into it. I had made sure all the files including the docker file were working perfectly fine. Please help me out.  
Roll no. 23f1002056

---

My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly. I request for re evaluation of my project. my roll no is 22f1000703

---

Respected,

I haven’t received any mail yet regarding the TDS Project 1 marks.  
Please look into it.

Regards,  
Soham

---

My evaluation log file is missing.  
The 2 other log files i’m given doesnt have my email inside it listed.  
the Image id which is given in the MAIL is not present in my docker desktop, my project’s docker image is listed in docker desktop, which doesnot matches the image id given in the MAIL,  
What was evaluated? How it was evaluated?

This is the id of the docker image that was evaluated: 0ade87d1bf07

My terminal shows 2 images as last, with respective image ids. I am not sure which one is the real, so please check with both the ids.  
tds-project-1 latest c854274f078d 5 weeks ago 1.38GB  
ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB

I am requesting to look into this case. I think there has been some mistake somewhere.

21f3001194

---

I have also built the image on Mac and facing the same issue

`exec format error`

It is running fine on my Macbook Pro M1

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

Sir I have noticed a technical glitch for the docker issue, wherein I mistakenly uploaded the wrong docker image link so kindly please kindly re evaluate it.

---

Sir I haven’t received any mail regarding this Project1 marks. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

[@carlton](/u/carlton) Sir , my Docker image is built on Macbook M1 which as you know uses ARM64 architecture . But evaluated with x86\_64 which caused the exec format error due to cross platform compatibility issues . I am kindly requesting you to re-evaluate the project once again .

---

This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

Please, look over it.

Regards,  
Harsh Jaiswal  
23f1001995

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I wanted to kindly request if you could review the bonus additional tasks, as they were not reflected in the evaluation, despite being mentioned in the instructions. Apart from that I understand and accept my score overall, especially since I had hardcoded the folder paths in my prompt for some questions, which I believe led to those failures.

* **Bonus: Additional tasks**. We *may* pass additional tasks beyond the list above. If your code handles them correctly, you get 1 bonus mark per task.  
  Regards,

---

Would you mind reviewing the evaluation.log screenshot I have attached? I believe I may deserve marks for Task B6. [@carlton](/u/carlton), could you kindly take a look?  
image description: The image shows the results of a web request, likely a test or a script execution, with a green indicator at the top and a red "FAILED" indicator at the bottom. There are HTTP response codes and the data expected, the result of the operation.
image text: HTTP 200 "Scraped data saved to ./data/b6.json"
HTTP Request: GET http://localhost:8052/read?path=/data/b6.json "HTTP/1.1 200 OK"
/data/b6.json
▲ EXPECTED:
['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A.
Edison', 'Eleanor Roosevelt', 'Steve Martin']
!
RESULT:
[
{
".author": [
"Albert Einstein",
"J.K. Rowling",
"Albert Einstein",
"Jane Austen",
"Marilyn Monroe",
"Albert Einstein",
"Andr\u00e9 Gide",
"Thomas A. Edison",
"Eleanor Roosevelt",
"Steve Martin"
]
}
]
X B6 FAILED

---

I am also facing the same Please help my roll no is 21f3001750

---

can you please take a look at this screenshot?  
Here's a description of the image:
The image contains text describing a series of operations related to extracting a credit card number from an image and writing it to a file. The process involves sending HTTP requests to a local server, checking results and comparing the result.
image text:
A7 PASSED
Running task: `/data/card.jpg` has a credit card. Pass the image to an LLM, extract the card
number, and write it without spaces to `/data/cc-number.txt`
HTTP Request: POST http://localhost:8001/run?
task=%60%2Fdata%2Fcard.jpg%60+has+a+credit+card.+Pass+the+image+to+an+LLM%2C+extract+the+card+num
ber%2C+and+write+it+without+spaces+to+%60%2Fdata%2Fcc-number.txt%60 "HTTP/1.1 200 OK"
HTTP 200 {
"result": "The task of extracting the card number from the image and writing it to `/data/cc-
number.txt` has been completed successfully."
}
HTTP Request: GET http://localhost:8001/read?path=/data/cc-number.txt "HTTP/1.1 200 OK"
/data/cc-number.txt
! EXPECTED:
6011598665215965
! RESULT:
6011598656215965
  
The task was done but the LLM made a mistake. I think this type of mistake was outside our control. [@carlton](/u/carlton)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Please correct me if I’m wrong, but I noticed that for tasks **B7**, **B8**, and **B10**, the evaluation log does not include any **`POST` or `GET` request traces**, unlike the other tasks which have clearly recorded request flows, generated code, and outputs. In these three cases, the log shows only the failure message without any indication that the script was executed or that the output file was read.  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a log or output from a program or script that appears to be testing web scraping and file operations. It contains several HTTP requests, status codes, and debugging information.
\*\*Key elements:\*\*
\* \*\*HTTP Requests:\*\* There are POST and GET HTTP requests, indicating interactions with a server.
\* \*\*Status Codes:\*\* HTTP 200 OK responses indicate success.
\* \*\*Task Description:\*\* The program is tasked with web scraping quotes and authors from a website.
\* \*\*Code Snippets:\*\* Python code snippets are present, illustrating the scraping process using libraries like requests, BeautifulSoup, and json.
\* \*\*Task Execution:\*\* The program checks the status of several tasks.
\* \*\*Status Indicators:\*\* Green circles with a check mark indicating "PASSED" for task B6. and red circles with a "X" indicating "FAILED" for tasks B7 and B8.
\*\*Image text:\*\*
```text
HTTP Request: POST http://localhost:8278/run?
task=https%3A%2F%2Fquotes.toscrape.com%2F+has+quotes+from+famous+people.%0AThe+.author+class+has+the+quote+author%27s+name.%0AExtract+and+save+all+authors+
from+the+first+page%2C+in+order%2C+to+%2Fdata%2Fb6.json+as+an+array+of+strings.%0AE.g.+%60%5B%22Douglas+Adams%22%2C+%22J.K.+Rowling%22%2C+...%5D%60%0A
"HTTP/1.1 200 OK"
HTTP 200 {
"status": "success",
"task": "https://quotes.toscrape.com/ has quotes from famous people.\nThe author class has the quote author's name. \nExtract and save all authors from
the first page, in order, to /data/b6.json as an array of strings.\nE.g. `[\"Douglas Adams\", \"J.K. Rowling\", ...] `\n",
"generated\_code": "import requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://quotes.toscrape.com/'\nauthors = []\n\ntry:\n
response = requests.get(url)\n
response.raise for status()\n soup = BeautifulSoup (response.text, 'html.parser')\n
soup.find all (class ='author')\n authors = [author.get text() for author in author elements]\n\n
json.dump(authors, f) \nexcept Exception as e:\n print (f'An error occurred: {e}')",
"output":
}
""
HTTP Request: GET http://localhost:8278/read?path=/data/b6.json "HTTP/1.1 200 OK"
B6 PASSED
author elements =
with open('/data/b6.json', 'w') as f:\n
Running task: Download the image at https://dummyimage.com/100x100/ad0434/ad0434.png, resize it to 50x50 px and save it to `/data/b7.png`
B7 failed:
X B7 FAILED
B8 failed: not all arguments converted during string formatting
X B8 FAILED
```

---

Same issue with my. I have built my docker image in mac air m1 but i found that my image was run on a x86\_64 architecture (I can see this in the logs shared for x86\_server\_start.log)

---

[@carlton](/u/carlton) sir i have same issue.  
I have built my docker image in mac air m1 but i found that my image was run on a x86\_64 architecture.

---

Sir even my evaluation log file is missing and I really don’t know what to do because during submission 8/10 of my A tasks were working. Please look into it sir. This is really going to affect my grade and I remember how hard I tried just to get my A tasks running. Please sir  
Role nom 23f2000599  
image description : The image appears to be a screenshot of a mobile device displaying a text-based explanation or evaluation report related to a Docker image. The text discusses potential issues with the image and provides details on specific log files, including their contents and how they are used in the evaluation process. There are also details on the evaluation of the docker image.
image text: evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us. MISSING files will result in a score of 0. Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet. 1. Evaluation log file. MISSING This contains your performance report on your individual tasks. 2. Docker log file. https://drive.google.com/file/d/1Zn-ajY5yB1M1xxhraquPcPFNvqe7-ebC/view? usp=drivesdk This provides the technical performance of your container. 3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests. 4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism. 5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks. 6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications. 7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core concepts of LLMs to achieve the desired result. This is the id of the docker image that was evaluated: e1f186d9ce91

---

Hi [@jivraj](/u/jivraj),

The contents of Expected and Result matches, but still test case’s failed.  
Is there formatting check for answer , Isn’t prettier to be done ?  
I see that your expected answer isn’t formatted using prettier , am i wrong ?

eg:

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=14 ":warning:") EXPECTED:  
[{‘first\_name’: ‘Kevin’, ‘last\_name’: ‘Allen’, ‘email’: ‘tonya41@example.com’}, {‘first\_name’: ‘Kimberly’, ‘last\_name’: ‘Allison’, ‘email’: ‘vmendoza@example.com’}, {‘first\_name’: ‘Kathleen’, ‘last\_name’: ‘Baldwin’, ‘email’: ‘amclean@example.com’}, {‘first\_name’: ‘Jason’, ‘last\_name’: ‘Banks’, ‘email’: ‘sharptara@example.org’}, {‘first\_name’: ‘Tami’, ‘last\_name’: ‘Bass’, ‘email’: ‘kristy61@example.com’}, {‘first\_name’: ‘Brenda’, …

![:warning:](https://emoji.discourse-cdn.com/google/warning.png?v=14 ":warning:") RESULT:  
[  
{  
“first\_name”: “Kevin”,  
“last\_name”: “Allen”,  
“email”: “[tonya41@example.com](mailto:tonya41@example.com)”  
},  
{  
“first\_name”: “Kimberly”,  
“last\_name”: “Allison”,  
“email”: “[vmendoza@example.com](mailto:vmendoza@example.com)”  
},  
{  
“first\_name”: “Kathleen”,  
“last\_name”: “Baldwin”,  
“email”: “[amclean@example.com](mailto:amclean@example.com)”  
},  
{  
“first\_name”: “Jason”,  
“last\_name”: “Banks”,  
“email”: “[sharptara@example.org](mailto:sharptara@example.org)”  
},  
{  
“first\_name”: “Tami”,  
“last\_name”: “Bass”,  
“email”: “[kristy61@example.com](mailto:kristy61@example.com)”  
},  
{  
“first\_name”: “Brenda”,  
“last\_name”: “Bradford”,  
“email”: “[amandakeith@example.com](mailto:amandakeith@example.com)”  
},…

---

---

Hi @all

We will identify why arm images created a problem and were run using x86 platform.

We will also rerun evaluations for all the x86 and arm images one more time, before pushing to the dashboard.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f3003302/48/67422_2.png) 23f3003302:

> Hi [@jivraj](/u/jivraj),

[@23f3003302](/u/23f3003302) output from your server’s response is correct, we will update our evaluation script.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2004912/48/108710_2.png) 23f2004912:

> image description: The image shows a text output. The output displays the results of a HTTP GET request with the expected and actual results. The output reveals that the test case "B6 FAILED." The expected and actual results are lists of names.
> image text: HTTP 200 "Scraped data saved to ./data/b6.json"
> HTTP Request: GET http://localhost:8052/read?path=/data/b6.json "HTTP/1.1 200 OK"
> /data/b6.json
> ▲ EXPECTED:
> ['Albert Einstein', 'J.K. Rowling', 'Albert Einstein', 'Jane Austen', 'Marilyn Monroe', 'Albert Einstein', 'André Gide', 'Thomas A. Edison', 'Eleanor Roosevelt', 'Steve Martin']
> ! RESULT:
> [
> {
> ".author": [
> "Albert Einstein",
> "J.K. Rowling",
> "Albert Einstein",
> "Jane Austen",
> "Marilyn Monroe",
> "Albert Einstein",
> "Andr\u00e9 Gide",
> "Thomas A. Edison",
> "Eleanor Roosevelt",
> "Steve Martin"
> ]
> }
> ]
> X B6 FAILED

[@23f2004912](/u/23f2004912) We will discuss internally if we can do something about it, but I can’t assure if you will get marks for it, since output from your server is a bit different.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001611/48/67277_2.png) 23f1001611:

> image description: The image presents a series of API requests, responses, and task statuses. The first part shows a POST request and a successful response, followed by a code snippet. The next part displays a GET request, the status of task B6 which is "PASSED", and a "Running task" message. Finally, there are error messages for tasks B7 and B8.
> image text: HTTP Request: POST http://localhost:8278/run?
> task=https%3A%2F%2Fquotes.toscrape.com%2F+has+quotes+from+famous+people.%0AThe+.author+class+has+the+quote+author%27s+name.%0AExtract+and+save+all+authors+
> from+the+first+page%2C+in+order%2C+to+%2Fdata%2Fb6.json+as+an+array+of+strings.%0AE.g.+%60%5B%22Douglas+Adams%22%2C+%22J.K.+Rowling%22%2C+...%5D%60%0A
> "HTTP/1.1 200 OK"
> HTTP 200 {
> "status": "success",
> "task": "https://quotes.toscrape.com/ has quotes from famous people.\nThe author class has the quote author's name. \nExtract and save all authors from
> the first page, in order, to /data/b6.json as an array of strings.\nE.g. `[\"Douglas Adams\", \"J.K. Rowling\", ...] `\n",
> "generated\_code": "import requests\nfrom bs4 import BeautifulSoup\nimport json\n\nurl = 'https://quotes.toscrape.com/'\nauthors = []\n\ntry:\n
> response = requests.get(url)\n
> response.raise for status()\n soup = BeautifulSoup (response.text, 'html.parser')\n
> soup.find all (class ='author')\n authors = [author.get text() for author in author elements]\n\n
> json.dump(authors, f) \nexcept Exception as e:\n print (f'An error occurred: {e}')",
> "output":
> }
> ""
> HTTP Request: GET http://localhost:8278/read?path=/data/b6.json "HTTP/1.1 200 OK"
> B6 PASSED
> author elements =
> with open('/data/b6.json', 'w') as f:\n
> Running task: Download the image at https://dummyimage.com/100x100/ad0434/ad0434.png, resize it to 50x50 px and save it to `/data/b7.png`
> B7 failed:
> X B7 FAILED
> B8 failed: not all arguments converted during string formatting
> X B8 FAILED
>
> image2003×745 95 KB

[@23f1001611](/u/23f1001611) we will look into it

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/harshjaiswal/48/69560_2.png) HarshJaiswal:

> This is the id of the docker image that was evaluated: d0f14a872042 , but i had never provided this docker image then how it get evaluated, also none of the docker image created by me has this id.

[@HarshJaiswal](/u/harshjaiswal) I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information `harshjaiswal1/tds_project_final latest d0f14a872042 5 weeks ago 214MB`

[@AYUSH\_SINGH](/u/ayush_singh)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png) AYUSH\_SINGH:

> ayush6871/fastapi-agent latest 27e8375b0ab1 6 weeks ago 1.66GB

This was submitted to us through google form, for project1.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/ayush_singh/48/14039_2.png) AYUSH\_SINGH:

> The 2 other log files i’m given doesnt have my email inside it listed.

We are aware about it results for 12 students are not generated, we will look into it, and see what caused those 12 images not to run.

[@22f1000703](/u/22f1000703)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f1000703/48/125463_2.png) 22f1000703:

> My evaluation log file is missing in report provided. It says tasksA was not found. but I have submitted tasksA in my project file. Also it says server didnt start for 5 mins but for me image was working fine. please kindly help me out. I have made submissions correctly.

It would have run at your end but it was supposed to run at anywhere, after dockerising it didn’t run, reason is taskA module was not found.

---

Same issue for me sir. When I evaluated my file using evaluate.py my 9 cases out of the 10 in Task A was passed but the email I received shows that my evaluation log file is missing. I don’t understand why does it show like that. Please do check and help me out sir.

Reg no. 24f1002633

---

I suspect there is something wrong with how the evaluation has been done. Although A1 task succeeded, all of my A tasks failed.

---

I have checked my log file in all of the cases where a file is required it says file not found or directory not found error in the code, how can I check /data folder was provided to the program?

[@carlton](/u/carlton)

---

[@Jivraj](/u/jivraj) , [@carlton](/u/carlton)  
It was a good project, and I have obtained the log files. Upon reviewing the log files, I realized that they are unable to read the files. I checked my project on GitHub and discovered that I forgot to uncomment the line that defines the path using the `os` library. As a result, all file evaluations returned errors such as “can’t read the file.”

I understand that this oversight was my mistake. However, is there any way to reevaluate the code by simply uncommenting that line? I believe the rest of the code is properly written, but due to this single comment, all the files remained unchecked or resulted in errors.

image description: The image is a screenshot of a terminal or log file showing various HTTP requests and task results. The top of the screen displays a Google Drive file path. The main content area shows log entries with timestamps, request details, and error messages. Some entries show "FAILED" with red marks. The tasks involve file operations and interactions with a LLM. There are HTTP 500 and 404 errors.
image text:
```
Proje
Ex TDS 2 Ex TDS 2 Ex TDS 2 Ex TDS 2 Ex TDS 2
Proje
IIT M
Untitl
Settin
New CO Welco
My D
Proje
Tds-o M TDS J
A2 X
+
drive.google.com/file/d/1Te0WdJaRAYUQc7shZrO2bBFVnOZO92ca/view
HTTP Request: POST http://localhost:8138/run?
24f1002555@ds.study.iitm.ac.in\_evaluation.log0+contains+an+email-
P
Open with Google Docs
an+LLM+with+instructio tra+the+send Share
P
7s+email+address%2C+and+write+just+the+email+address+to+bU%2Fdata%2Fmall-sender.txt%60 "HTTP/1.1 500 Internal Server Error
"detail": "500: [Errno 2) No such file or directory: '/app./data/mail.txt'"
HTTP 500 {
}
HTTP Request: GET http://localhost:8138/read?path=/data/mail-sender.txt "HTTP/1.1 404 Not Found"
A7 failed: Cannot read /data/mail-sender.txt
X A7 FAILED
Running task: `/data/card.jpg` has a credit card. Pass the image to an LLM, extract the card number, and write it without
spaces to `/data/cc-number.txt`
HTTP Request: POST http://localhost:8138/run?
task=%60%2Fdata%2Fcard.jpg%60+has+a+credit+card.+Pass+the+image+to+an+LLM%2C+extract+the+card+number%2C+and+write+it+without+
spaces+to+%60%2Fdata%2Fcc-number.txt%60 "HTTP/1.1 500 Internal Server Error"
}
HTTP 500 {
"detail": "500: [Errno 2) No such file or directory: './data/card.jpg'"
HTTP Request: GET http://localhost:8138/read?path=/data/cc-number.txt "HTTP/1.1 404 Not Found"
A8 failed: Cannot read /data/cc-number.txt
X A8 FAILED
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
Running task: `/data/comments.txt contains a list of comments, one per line. Using embeddings, find the most similar pair
of comments and write them to `/data/comments-similar.txt`, one per line
HTTP Request: POST http://localhost:8138/run?
Q +
task=%60%2Fdata%2Fcomments.txt%60+contains+a+list+of+comments%2C+one+per+line.+Using+embeddings%2C+find+the+most+similar+pair
+of+comment.s+and+write+them+to+%60%2Fdata%2Fcomments-similar.txt.%60%2C+one+per+line "HTTP/1.1 200 OK"
5 23°C
Sunny
X
ENG
US
08:39 AM
29-03-2025
```  
Here's a description of the image:
\*\*Overall:\*\* The image is a screenshot of a code editor displaying the `app.py` file from a GitHub repository related to "LLM-based-Automation-Agent". The interface shows code, a file explorer, and a "Symbols" panel.
\*\*Key Elements:\*\*
\* \*\*Code Editor:\*\* The central part of the image features the `app.py` file. Code is highlighted with syntax coloring. The code focuses on defining API endpoints and functions like `start`, `read\_file`, and `run\_task`.
\* \*\*File Explorer:\*\* On the left side, a file explorer lists files like `Dockerfile`, `LICENSE`, `README.md`, `app.py`, `package.json`, `pyproject.toml`, and `uv.lock`.
\* \*\*Symbols Panel:\*\* On the right side, a "Symbols" panel lists functions, constants, and other elements defined within the `app.py` file.
\*\*Text:\*\*
\* `LLM-based-Automation-Agent / app.py`
\* The code itself, including comments and function definitions.
\* Text in the "Symbols" panel, like `ai\_proxy\_url`, `start`, `read\_file`, etc.
\* File names in the file explorer.
\* Other text related to the interface (menu options, labels, etc.).
\*\*Context:\*\* The image provides a glimpse into the codebase of a project that uses automation agents and likely involves language models. The code defines API endpoints and functions related to tasks such as reading files and executing other operations. The user seems to be viewing the code and exploring the file structure, and symbol definitions.

---

Same here. I also dis not recieve any mail sir.

---

I noticed that my Docker image was run on an x86\_64 architecture (as indicated by my email in the shared logs), whereas I originally built it on my Mac (ARM architecture). Due to this mismatch, the image failed to run properly and resulted in an exec format error.

Since there was no prior mention of the architecture on which our images would be evaluated, I request that my evaluation be conducted again on the appropriate machine. Please help as after doing it correctly getting 0 marks because of such an error feels wrong

---

[@23f2001975](/u/23f2001975) we had to rely on docker telling us whether an image was arm or x86. So thats why we just did what docker software told us. If it classified an image as arm then we ran it on arm. If it did not then we ran it on x86. Thats why we need students to look through the logs and identify issues so that we can make sure you get the correct evaluation.

If students notify us their image is actually arm based, then we will run it on arm. So dont worry, just inform us of any discrepancy as well as bugs. Our evaluation might not be perfect, there may be bugs. If students can precisely create bug reports then we can take that into consideration when evaluating students as well. The benefit being you might get extra marks because of the bug fix.

We have a script that looks at this discourse post each day and tells us who requires a fresh evaluation. So we will check your image on arm.

Kind regards

---

image description: The image shows a traceback log, typical in programming errors. It highlights an issue with a key, "AIRPROXY\_TOKEN," missing in the environment. The traceback indicates the file and line numbers where the error occurred, suggesting a problem with environment variable access in the code.
image text: Traceback (most recent call last):
File "/app/app.py", line 30, in <module>
AIPROXY\_TOKEN = os.environ['AIRPROXY\_TOKEN']
~~~~~~~~~~~~~~~
File "<frozen os>", line 716, in \_getitem\_
KeyError: 'AIRPROXY\_TOKEN'

This is a screenshot of my docker log file. This works if you pass the actual value of the airproxy token at the command line while pulling the docker image. Please do look into this as I’ve put a lot of effort into this.

Thank you

Regards,  
23f3002677

---

@cartlon Same issue.

My image was also run on a `x86_64` architecture. I too built on my mac which is `ARM` (M1 Processor). I too can see that my docker image never ran properly and threw the `exec format error` and **Evaluation log file** is MISSING.

Can you please rerun the image on ARM based

---

You have a misspelling in your environment variable, thats why it failed. We do pass the token to your docker exactly as specified in Project 1 page.  
image description: A code snippet highlighting a traceback error related to an environment variable named 'AIRPROXY\_TOKEN'. The error message indicates a KeyError, which means the variable was not found.
image text: Traceback (most recent call last):
File "/app/app.py", line 30, in <module>
AIPROXY\_TOKEN = os.environ['AIRPROXY\_TOKEN']
~~~~~~~~~~~~~~
File "<frozen os>", line 716, in \_getitem\_
KeyError: 'AIRPROXY\_TOKEN'

Kind regards

---

You have to identify the exact bug for your claim to be considered. Thats why we have provided you with the scripts and the logs. You might get lots of marks. Its in your interest to identify the bug.

Kind regards

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) what do I do sir am seriously clueless and heartbroken rn pls help atleast for A tasks we should get it

---

We demoed in the live session the complete process of how to dockerise your project so that it can be run anywhere. Running on your local machine is not a sufficient criteria for passing the evaluation. It is absolutely vital for students to understand deployment. This is a critical skill for anyone who is serious about working in this field.

Also just check if yours is an arm based image or x86. Sometimes that makes a difference. For us there is no way to know other than docker software telling us. As it turns out several students had an arm based image but docker did not tell us that. So we will re run those.

If yours has been run on the wrong emulation then we will re run.

Kind regards

---

[@carlton](/u/carlton)

I encountered an HTTP 500 error with the following detail:

```
{
"detail": "'choices'"
}

```

This issue appears across all tasks, even though they were running fine before submission. I suspect there might be a problem with APIPROXY\_TOKEN. Could you please look into this?

Additionally, my solution is very similar to the one shared by the System Commands team in their email.

image description: The image shows a console output log with a series of commands, HTTP requests, and error messages. It begins with a running task to install and run a script from a GitHub gist. The image then shows several HTTP requests, some of which result in "HTTP/1.1 500 Internal Server Error" and "HTTP/1.1 404 Not Found" errors. There are also a couple of "A1 FAILED" and "A2 FAILED" messages.
image text:
Running task: Install `uv` (if required) and run the script
`https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466052b66ae/datagen.py`
with `22f3001777@ds.study.iitm.ac.in` as the only argument
HTTP Request: POST http://localhost:8180/run?
task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fgist.githubusercontent.com%2Fsanand0%2Ff19b6797f82b36da39ac4
4f3a7d4392a%2Fraw%2F13246698088795e1942179856aafd466052b66ae%2Fdatagen.py%60%0Awith+%6022f3001777%40ds.study.iitm.ac.in%60+as+the+only+argu
ment%0A "HTTP/1.1 500 Internal Server Error"
HTTP 500 {
"detail": ""choices'"
}
HTTP Request: GET http://localhost:8180/read?path=/data/format.md "HTTP/1.1 404 Not Found"
A1 failed: Cannot read /data/format.md
X A1 FAILED
Running task: Format `/data/format.md` with `prettier@3.4.2` in-place
HTTP Request: POST http://localhost:8180/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 500
Internal Server Error"
HTTP 500 {
"detail": ""choices'"
}
HTTP Request: GET http://localhost:8180/read?path=/data/format.md "HTTP/1.1 404 Not Found"
A2 failed: Cannot read /data/format.md
X A2 FAILED

---

We have given you the evaluation scripts. Identify where exactly you believe the bug is.

Just guesses is not going to get you extra marks. You have to give us something specific.

Kind regards

---

[@Jivraj](/u/jivraj) sir please kindly look into it. Please re-evaluate my image, everything was working fine it is an issue with the docker image. Please re-evaluate it sir and please guide me as what to do

---

I encountered the same issue with `evaluate.py`. However, since you previously advised against coding strictly with `evaluate.py`, I didn’t pursue it further. Now, I’m concerned—how is this a mistake?

Here's a brief description of the image:
The image is a text-based document. It begins with the file path and name, followed by the text marked as "EXPECTED". This section presents several sentences, and then the text marked as "RESULT" appears. The final line notes "X A5 FAILED."
image text:
/data/logs-latest.txt
▲ EXPECTED:
Clearly drug health quickly field everyone majority as. Investment direction themselves suddenly.
West son we reflect. Size quite they new assume manager.
Official one draw various between time box goal. Wonder appear happen themselves. Include want key draw late list.
Hair hit rule employee.
Option guess fish difficult our add. Bill practice main discover. Focus couple ball through network should leave.
Within PM race former. Pressure property piece treat thus interesting. Eight so affect.
Different indicate pretty most pay leg today. Administration partner performance off get check.
Clear your upon sign. Type per task win.
Consumer beyond economy easy friend piece increase. With city write.
Matter statement last trial television. Not black owner most million answer. Toward contain girl member.
▲ RESULT:
Clearly drug health quickly field everyone majority as. Investment direction themselves suddenly. West son we reflect. Size quite they new assume manager.Official one draw
various between time box goal. Wonder appear happen themselves. Include want key draw late list. Hair hit rule employee. Option guess fish difficult our add. Bill practice main
discover. Focus couple ball through network should leave. Within PM race former. Pressure property piece treat thus interesting. Eight so affect.Different indicate pretty most
pay leg today. Administration partner performance off get check.Clear your upon sign. Type per task win.Consumer beyond economy easy friend piece increase. With city
write.Matter statement last trial television. Not black owner most million answer. Toward contain girl member.
X A5 FAILED

---

Please provide more time for this. Right now, we are also busy with the second project. There are other courses as well.

---

yaa same issue i am also facing ,  
and this LLM thing is very new for us , and we tried our best to complete. , but because of local machine issue , or anything , people end up getting 0 marks , or 4-5 marks , ..  
As a lot of students are getting 0 , so please give some bonus , or some marking for there efforts ,  
TDS dont have quiz , ,and getting 0 in project will decrease our CGPA too .  
please think for it sir [@carlton](/u/carlton)

---

This is the id of the docker image that was evaluated: 468630ef32b8  
I believe this is not my docker ID that was submitted, my docker ID is “bd2d0e570ec6”:

proof:  
REPOSITORY TAG DIGEST IMAGE ID CREATED SIZE  
rohit23f1001156/project1\_tds v3 sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542 bd2d0e570ec6 5 weeks ago 816MB

Please, look over it.

Also, in my docker log file, it is showing the error as:  
image description : The image is a console log showing the execution of a program or application. The log includes information about server processes, application startup, and function calls. Errors are highlighted.
image text: INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:root:10
INFO:root: Inside run task with task: Say Hello Carlton
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::
INFO:root:Inside execute\_function\_call with function\_call: {'name': 'extract\_specific\_text\_using\_llm', 'arguments': '{"input\_file": "system\_input.txt", "output\_file": "output.txt", "task": "Say Hello Carlton"}'}
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::
INFO:root:PRINTING RESPONSE:::PRINTING RESPONSE:::PRINTING RESPONSE:::
{'id': 'chatcmpl-BFxBDCiJKlmlJzchh8kqUoQsXAubf', 'object': 'chat.completion', 'created': 1743142107, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assistant', 'content': None, 'tool calls': [{'id': 'call LXuHWHK5LZZLE3XW0MkVmpjy', 'type': 'function', 'function': {'name': 'extract\_specific\_text\_using\_llm', 'arguments': '{"input\_file": "system\_input.txt", "output\_file": "output.txt", "task": "Say Hello Carlton"}'}}, {'id': 'call\_oAYG8U5d7BPv4Gc6Z6MfEa9t', 'type': 'function', 'function': {'name': 'extract\_specific\_text\_using\_llm', 'arguments': '{"input\_file": "system\_input.txt", "output\_file": "output.txt", "task": "Say Hello Carlton"}'}}], 'refusal': None, 'annotations': []}, 'logprobs': None, 'finish\_reason': 'tool\_calls'}], 'usage': {'prompt\_tokens': 1294, 'completion\_tokens': 83, 'total\_tokens': 1377, 'prompt\_tokens\_details': {'cached\_tokens': 0, 'audio\_tokens': 0}, 'completion\_tokens\_details': {'reasoning\_tokens': 0, 'audio\_tokens': 0, 'accepted\_prediction\_tokens': 0, 'rejected\_prediction\_tokens': 0}}, 'service\_tier': 'default', 'system\_fingerprint': 'fp\_86d0290411', 'monthlyCost': 0.012489, 'cost': 0.00438, 'monthlyRequests': 2, 'costError': 'crypto.createHash is not a function'}
Calling function: extract\_specific\_text\_using\_llm
Arguments: {'input\_file': 'system\_input.txt', 'output\_file': 'output.txt', 'task': 'Say Hello Carlton'}
IN HERE True
INFO: 172.17.0.1:33072 - "POST /run?task=Say+Hello+Carlton HTTP/1.1" 500 Internal Server Error
ERROR: Exception in ASGI application
Traceback (most recent call last):
File "/app/main.py", line 121, in execute\_function\_call
function\_to\_call(\*\*function\_args)
File "/app/function\_tasks.py", line 290, in extract\_specific\_text\_using\_llm
with open (input\_file\_path, "r") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'system\_input.txt'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/app/main.py", line 146, in run\_task
execute\_function\_call (tool ["function"])
File "/app/main.py", line 126, in execute\_function\_call
raise HTTPException(status\_code=500,
fastapi.exceptions.HTTPException: 500: Error executing function in execute\_function\_call: [Errno 2] No such file or directory:
'system\_input.txt'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):

what is the reason for this?  
It was running properly before, please help.

Regards,  
Rohit  
23f1001156

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

[@ROHIT\_B\_LAKSHMANAN](/u/rohit_b_lakshmanan)

This is **exactly** what **you** submitted. We will ONLY consider this as valid.

2/16/2025 9:30:05 23f1001156@ds.study.iitm.ac.in [GitHub - Rohit23f1001156/project1\_tds](https://github.com/Rohit23f1001156/project1_tds) rohit23f1001156/project1\_tds

---

Yes, I agree.  
So, did my docker ID change when I submitted?  
I am sorry sir, but I did not make any changes after submitting the project, so I guess my Docker ID should remain the same as before, if I am not mistaken. I kindly request you to check just once more please, as I really don’t know where I have went wrong.

Jivraj Sir had checked liked this for another student, so I just wanted to confirm the same for me.  
*" I looked for your response for project1 docker image, and found out that we used correct image id. Here is repo information `harshjaiswal1/tds_project_final latest d0f14a872042 5 weeks ago 214MB` "*

Also sir, could you please tell me why the error as shown in my previous message is being shown? and if there is no chance of it getting correct.

thanks

---

Hi [@carlton](/u/carlton) !

I am reaching out with deep frustration and concern regarding the evaluation of my project. I have worked tirelessly on this for almost two weeks, dedicating day and night to ensure that the tasks were executed correctly. During my own testing, I was able to get at least 7 out of 10 A tasks working as expected. However, after the evaluation, I was informed that none of the tasks were executed properly, which was quite shocking!

Given the effort and time I have put in, I kindly request you to review my project once more. I am more than willing to demonstrate the functionality in real time to clarify any issues or misunderstandings. Please let me know if there is a possibility to discuss this further, as I genuinely believe my work deserves another review.

---

[@carlton](/u/carlton),

Jivraj said, *“We will discuss internally if we can do something about it.”* I understand this well. The output from my server is slightly different, but it still achieves over 95% accuracy. Please do consider it.

---

Hi [@Pritul\_raut](/u/pritul_raut)  
No, we won’t reevaluating it.

---

Hi [@22f2001389](/u/22f2001389)

```
  File "/app/app.py", line 4, in <module>
    from tasksA import *
ModuleNotFoundError: No module named 'tasksA'

```

The error occurs because Python cannot find the `tasksA` module. This is due to the file not existing, not being in the correct directory.

Kind regards

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png) ROHIT\_B\_LAKSHMANAN:

> This is the id of the docker image that was evaluated: 468630ef32b8

We evaluated you on correct file

image description: The image is a terminal output showing a Docker pull and image search operation.
image text: usr\_22f3002542\_ds\_study\_iitm\_ac\_@tds-course-temp-bq:~$ docker pull --platform arm64 rohit23f1001156/project1\_tds:v3
v3: Pulling from rohit23f1001156/project1\_tds
Digest: sha256:bd2d0e570ec6b9a4a2b1565602a7c6abd118c4df06ca39e9dd78b0c06cab7542
Status: Downloaded newer image for rohit23f1001156/project1\_tds:v3
docker.io/rohit23f1001156/project1\_tds:v3
usr\_22f3002542\_ds\_study\_iitm\_ac\_@tds-course-temp-bq:~$ docker images | grep "rohit23f1001156/project1\_tds"
rohit23f1001156/project1\_tds v3 468630ef32b8 5 weeks ago 581MB
usr\_22f3002542\_ds\_study\_iitm\_ac\_@tds-course-temp-bq:~$~

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/rohit_b_lakshmanan/48/67205_2.png) ROHIT\_B\_LAKSHMANAN:

> what is the reason for this?  
> It was running properly before, please help.

Try running docker container after pulling, check if evaluate.py is able to do it’s job.

If you feel there is some issues from our side, we have provided with scirpts we used. You can create a pull request to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1)

---

I’m facing “exec /usr/local/bin/uvicorn: exec format error” , My roll number is 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) .

---

I cannot understand why the project marks are marked zero for me ? i have used the same code as usual but the results are not same ?

---

No no sir, I can send you an SS of my code, it’s very much there sir, the tasksA file, i really don’t know why this happened.  
Here's a description of the image:
The image is a screenshot of a code editor, likely Visual Studio Code, displaying a file directory and coding-related information. The left side displays a file explorer with various files, including Python files (.py), and other configuration files. The file "app.py" is highlighted in blue. On the right side, there's a "PROBLEMS" section, possibly listing errors or issues in the code, and it appears to show terminal output. The bottom of the screen mentions "Python extension loading...".
image text:
```
≡ pip.exe
≡ pip3.13.exe
≡ pip3.exe
≡ python.exe
≡ pythonw.exe
◆.gitignore
\* pyvenv.cfg
➡.dockerignore
.env
app.py
datagen.py
docker-compose.deb...
docker-compose.yml
Dockerfile
evaluate.py
requirements.txt
tasksA.py
> OUTLINE
> TIMELINE
0 0 Python extension loading...
Type here to search
17
18
19
20
)
21
22
PROBLEMS
C:\Users\Ri
(tds\_roe) C
\* History
OPS C:\Users
```

---

Same issue with me also

---

Yeah, it’s there on your local machine, but you didn’t copy it to docker container.  
Below is content of your docker file which doesn’t copy tasksA.py file it only copies app.py. You could have figured this out by just running docker container on your local machine earlier, it would have shown you that error.

```
FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app

# Copy application files
COPY app.py /app

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

```

---

[@carlton](/u/carlton) good afternoon sir,  
I completed my project 1 and submitted it as instructed. But the result show that evaluate file missing. I did everything right but don’t know how this as the result come. I also had evaluation file in my project too. Please go through things again as this is very unfair for those who took 2 weeks to do this project. My roll no. is 22f3001664. I hope I will get marks, of not full then should be 10/20.  
Thank you sir

---

What to do now sir ? Is there no way to fix this now ? I can change the docker file and overwrite the docker image if you allow me to do so.

---

image description: The image is a meme. It depicts a stadium under construction, and the text implies a parallel between refactoring code and the physical construction.
image text: WHEN YOU CANNOT REFACTOR THE CODE BECAUSE OF A TIGHT DEADLINE imgflip.com

---

Figure out the problem in our script and do a pull request to it, we will fix it if it’s a valid bug.

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> Create Pull requests to [Jivraj-18/tds-jan25-project1](https://github.com/Jivraj-18/tds-jan25-project1) .

---

We looked at your script and there are errors in it. It doesn’t follow what we mentioned in live sessions.

Line number 81 of your app.py

`subprocess.run(["uv", "run", script_name, "--root", "./data"] + args, check=True)`

which creates a data directory inside app directory but evaluate.py expects data directory to be in root directory.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

I’m writing here to express my concerns regarding the evaluation of my TDS Project-1. Also, kindly pardon me for the long message.

I have received a MISSING statement in my evaluation log file in the project 1 score mail that was released yesterday.

These are the detailed point wise concerns :

1. I at the earlier stages, found the Tools in Data Science course relatively challenging as it’s just my second term in Diploma and I have only completed BDM and MLF Course till now. Hence, I decided to drop the course in February, however when I could still view the course on the portal, and raised concerns, the assistance provided to me was very grim and low, and after numerous follow-ups, I was finally informed 2½ weeks after dropping my course, that my drop application was received in draft and they would not proceed with it, and I had to continue my course.
2. By this time, I had already missed 2 graded assignment deadlines and the project 1 submission was due in the coming 2 days. Not losing my spirit and with whatever I could learn and implement I completed the TDS project 1. However, I accidentally attached the wrong docker image link, and I also raised the issue, but didn’t receive a reply.
3. I understand that it was a fault on my part, but evaluating a student as 0, even though all their functions are right, and they give the required answers, is also wrong since we are expected to provide correct answers, and learn to build the docker image, however, there can be occurrences where a student might make a small mistake like uploading the wrong link, and they must be given a small chance to reprimand them.
4. I also didn’t receive the mail from the TDS Team which they issued for students whose docker image or GitHub link was erroneous, and hence I realised after the deadline that I had uploaded the wrong docker image link.

I have rechecked all my function, and they are all correct, giving a 0 to a student, who worked hard within the limited available time(given the student had dropped the course but the course team didn’t process it) is very unfair.

Kindly provide me a way to either re-upload my project-1 Docker image link, or ask them to provide me marks on the basis of the functions and codes written, whichever is feasible, atleast to encourage the efforts and time put into the project with little knowledge.

I hope you would look into my plight, and take necessary measures.

Thanks and Regards

---

I haven’t received any mails regarding the tds project 1 please look into my concern  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

Sir please consider a re-evaluation for me, please :’)

---

Please consider my situation a peer whos results were exactly same as mine has received 9, then how could I get 1 . 23f1002630 this is my role number please reconsider  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Few Students including me have not received any mails regarding TDS Project 1. We don’t even know what went wrong or why we didn’t received. Initially I thought that it can be due to some sending error and i will receive little late but even after 14hrs we have not received anything from the team. How are we supposed to check log and see our mistakes when we didn’t even received marks and logs. I request to check into it and provide us our marks and logs.  
Thank You.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

I had built the project well on my Mac OS machine. I am very disappointed with the scores. How do i make amends for revaluation as I feel the code ran well for all tasks on my machine. Please give written steps for revaluation.

---

Its saying that my evaluation log file is missing, i submitted everything properly. It also says no module named TasksA is found while i got 9/10 marks in the tasksA evaluation script. Kindly look into this, i worked really harrd for this project, [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

[@22f3000935](/u/22f3000935) [Page Not Found | Docker Hub](https://hub.docker.com/r/pscoeds24/dataworks-agent)

you submitted this docker url through form response for project1, this repo doesn’t exists on docker.

---

[@Jivraj](/u/jivraj) sir please tell me whats the issue am very confused and worried

---

We are aware about such mistakes and we are looking into it. We will reevaluate those images.

---

If evaluation file is missing for anyone, we will reevaluate it once more and send same through email.

Can you fill form for architecture detection.

---

Also please , kindly share evaluation log file after execution

---

I did upload all the necessary files but it stil says tasksA is missing, and i am getting zero marks. Kindly help out [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
image description: The image is a screen capture from a code repository. It shows a list of files and directories within the "App" directory of a project named "TDS\_Project\_1". The top of the screen indicates the current location "TDS\_Project\_1/App/" and includes an option to "Add file". A user named "RaunakNarwal735" recently updated the Dockerfile.
image text: TDS\_Project\_1 / App / Add file RaunakNarwal735 Update Dockerfile c07b746 · last month History Name Last commit message Last commit date .env Add files via upload last month Dockerfile Update Dockerfile last month app.py Add files via upload last month readme.md Create readme.md last month tasksA.py Add files via upload last month tasksB.py Add files via upload last month

---

image description: The image is a screenshot of data related to a "latest" tag. It includes information about when it was last pushed, by whom, the digest, and the OS/ARCH.
image text: TAG
latest
Last pushed about 1 month by 23f2000599
Digest
5217284cc507
OS/ARCH
linux/amd64

linux/amd64  
which form should i fill sir?

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/aditya_naidu/48/12438_2.png) Aditya\_Naidu:

> 21f3003062@ds.study.iitm.ac.in , My roll is in x86 list/log , not in ARM list/log. I have written and tested my code on ARM computer. I request to please check my code manually. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) .

please fill the form for collecting architecture, so that we can rerun evals earlier we relied on docker api to tell us which architecture is being used, but it didn’t classify them correctly.

---

Hi [@23f2000599](/u/23f2000599) check this out

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> ### **Docker Image Architecture Issue Report**
>
> If your Docker image was run on the wrong architecture, please fill out this form:  
> [Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

---

mine is linux/amd64 sir it doesnt come under arm or x86 i think

---

Hi [@23f2002400](/u/23f2002400)

Check your Dockerfile if it copies tasksA.py file to docker container.  
If it does where does it copy, these are possible mistakes. You were expected to test docker images.

---

Hi [@23f2000599](/u/23f2000599)

amd64 is x86

---

Ok sir, will fill the form, thank you

---

One issue file is my app is listening on port 8000. But evaluations being done on 8219 port. so how it will succeed. Please guide what to do.

---

That’s external port mapping, we mapped your docker’s port 8000 to external 8219 port, so it won’t create issues.

Just look at docker\_orchestration.py file for logic behind it, basically it was for evaluating multiple images parallely.

---

There is a mistake in the url I guess check this out I have a fully functional image which was pushed 1 month ago  
Here's a description of the image:
The image is a screenshot of a web interface for Docker image management. The interface shows details about a specific image named "pscodes24/dataworks-agent". The image has been pushed about a month ago, with a repository size of 490.1 MB. There are tabs for "General", "Tags", "Image Management (BETA)", "Collaborators", "Webhooks", and "Settings". There's a search function. A section titled "Docker commands" is present which gives instructions for pushing a new tag. Below are the image details showing digests, tags, media types, OS/ARCH, size, last pushed and last pulled information. There are two images listed.
image text: pscodes24/dataworks-agent
Last pushed about 1 month ago • Repository size: 490.1 MB
Add a description
Add a category
General Tags Image Management BETA Collaborators Webhooks Settings
Search by tag (tag:abc...) or digest (sha256:abc...)
Where to start? Report an issue
Digest Tags Media type OS/ARCH Size Last pushed Last pulled
sha256:6e6057d5a26 latest Image linux/amd64 273.5 MB about 1 month 19 days
sha256:c9b258fe4894 Image linux/amd64 262.3 MB about 1 month about 1 month
1-2 of 2
Docker commands
To push a new tag to this repository.
Public view
docker push pscodes24/dataworks-agen
t:tagname
Preview and delete (0)
Filter by
< >

Please check this out

url::<https://hub.docker.com/repository/docker/pscodes24/dataworks-agent/general>

---

Here's a description of the image:
The image is a screenshot of a code testing or validation process, likely related to formatting. The file being tested is `/data/format.md`. The "EXPECTED" section shows a table representing a header row, while the main section includes the phrase "Paragraph has extra spaces and trailing whitespace" and a code snippet using the `print` function. The "RESULT" section shows the output of the test, followed by a "A2 FAILED" status.
image text:
```
/data/format.md
▲ EXPECTED:
# Header
| Start | Mid | End |
| :--- | :--- | :---: |
| 1 | 2 | 3 |
Paragraph has extra spaces and trailing whitespace.
```py
print("23f3001745@ds.study.iitm.ac.in")
```
▲ RESULT:
"# Header\n\n| Start | Mid | End | \n| :--- | :--- | :---: |\n| 1 | 2 | 3 |\n\nParagraph has extra spaces and trailing whitespace.\n\n```py\nprint(\"23f3001745@ds.study.iitm.ac.in\")\n\n```\n"
X A2 FAILED
```  
This is the correct answer, eval script is not considering newlines properly. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

same with me ![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14 ":smiling_face_with_tear:") i dont understand how i got 0.

---

This is the id of the docker image that was evaluated: 2a8ffa96b140 , but i had never provided this docker image instead my image id is 735a5a477fb2 then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) .

Regards,  
Atharva Antapurkar  
23f1002558

---

Sir, my evaluation log file is missing, even though I followed all the steps to generate the Docker image correctly. The system indicates that the server didn’t start within 5 minutes, but when I uploaded it, everything was working fine. I put in a lot of effort into this project, and I’m worried I might receive a zero despite making the submission correctly. Kindly help me resolve this issue. My roll number is 22F3004068.

Additionally, my Docker image ID was **d2f27c03b878**, but the ID mentioned in the email was **dfac8596cd4c**. Please provide clarity on this discrepancy.

I have also attached my Docker [log file](https://drive.google.com/file/d/1exrdQOCjbrCFux2hC4OQH_BfgiijCzD1/view?usp=drivesdk) for reference  
Docker [image](https://hub.docker.com/repository/docker/docaravind21/tds-project-1/tags)

---

I realized that I made a mistake in my project by forgetting to uncomment a single line of code: os.path.join(os.getcwd(), “path\_given”). I feel really bad about this oversight, especially after working so hard on the project and formatting everything carefully. It was an honest mistake, and I take full responsibility for it.

I sincerely request you to consider re-evaluating my work, as I believe it reflects the effort and dedication I put into it. I truly regret this error and will be more careful in the Project 2

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

image description: The image shows a traceback from a Python program. It lists the sequence of function calls that led to an error. The error is a KeyError: 'USER\_EMAIL', indicating that the program tried to access an environment variable named 'USER\_EMAIL' that wasn't set. The traceback points to several files within the Python installation and the application's code.
image text: Traceback (most recent call last):
File "/usr/local/bin/uvicorn", line 8, in <module>
sys.exit(main())
File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1161, in \_\_call\_\_
return self.main(\*args, \*\*kwargs)
File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1082, in main
rv = self.invoke(ctx)
File "/usr/local/lib/python3.10/site-packages/click/core.py", line 1443, in invoke
return ctx.invoke(self.callback, \*\*ctx.params)
File "/usr/local/lib/python3.10/site-packages/click/core.py", line 788, in invoke
return callback(\*args, \*\*kwargs)
File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 412, in main
run(
File "/usr/local/lib/python3.10/site-packages/uvicorn/main.py", line 579, in run
server.run()
File "/usr/local/lib/python3.10/site-packages/uvicorn/server.py", line 66, in run
return asyncio.run(self.serve(sockets=sockets))
File "/usr/local/lib/python3.10/asyncio/runners.py", line 44, in run
return loop.run\_until\_complete(main)
File "/usr/local/lib/python3.10/asyncio/base\_events.py", line 649, in run\_until\_complete
return future.result()
File "/usr/local/lib/python3.10/site-packages/uvicorn/server.py", line 70, in serve
await self.\_serve(sockets)
File "/usr/local/lib/python3.10/site-packages/uvicorn/server.py", line 77, in \_serve
config.load()
File "/usr/local/lib/python3.10/site-packages/uvicorn/config.py", line 435, in load
self.loaded\_app = import\_from\_string(self.app)
File "/usr/local/lib/python3.10/site-packages/uvicorn/importer.py", line 19, in import\_from\_string
module = importlib.import\_module(module\_str)
File "/usr/local/lib/python3.10/importlib/\_\_init\_\_.py", line 126, in import\_module
return \_bootstrap.\_gcd\_import(name[level:], package, level)
File "<frozen importlib.\_bootstrap>", line 1050, in \_gcd\_import
File "<frozen importlib.\_bootstrap>", line 1027, in \_find\_and\_load
File "<frozen importlib.\_bootstrap>", line 1006, in \_find\_and\_load\_unlocked
File "<frozen importlib.\_bootstrap>", line 688, in \_load\_unlocked
File "<frozen importlib.\_bootstrap\_external>", line 883, in exec\_module
File "<frozen importlib.\_bootstrap>", line 241, in \_call\_with\_frames\_removed
File "/app/main.py", line 22, in <module>
USER\_EMAIL = os.environ["USER\_EMAIL"]
File "/usr/local/lib/python3.10/os.py", line 680, in \_\_getitem\_\_
raise KeyError(key) from None
KeyError: 'USER\_EMAIL'

Sir so the user\_email isn’t passed while pulling the docker image?

Thank you.

---

Hi Team,

I have resolved the issues and pushed a new Docker image.  
**New Docker Image ID:** `913320f92eb3`  
**Tag:** `latest`  
**OS/ARCH:** `linux/amd64`  
Please evaluate my updated submission.

Thanks!

---

Hello,

My log file shows a “file not found” or “directory not found” error. Could you confirm whether `datagen.py` was executed inside the Docker container or on the host OS? If it ran on the host, I don’t see any mounting process for the `/data` folder into the container. Could you please clarify this?

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

is it like this: FileNotFoundError: [Errno 2] No such file or directory: ‘system\_input.txt’ ?  
I am getting this error.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir, I have fixed my docker image issue that was causing the error. Please re-pull my docker image so that I can get score. Please consider me for re-evaluation. All the codes were correct, only issue was a glitch in the docker image.

---

Hello Sir, I am facing the same issue. Please look into it. Before submission, I ran my Docker file with the evaluation script to ensure it was working, and it worked fine. Kindly help me out. My roll number is 23F3004321.

---

Yes, something like that, My log file shows when script tries to access file it says file not found or directory not found.

---

Sir, I checked my evaluation log, and the error occurred because the **AI proxy token limit was exceeded**. I ran the evaluation script to verify, and I scored **12/20**.  
image description: A console output shows the execution of a Flask application, including debugging information, server addresses, and various HTTP requests with their respective responses. It also includes tracebacks for errors that occurred during the processing of these requests.
image text:
\* Debug mode: on
[31m [1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. [0m
\* Running on all addresses (0.0.0.0)
\* Running on http://127.0.0.1:8000
\* Running on http://172.17.0.8:8000
[33mPress CTRL+C to quit [0m
\* Restarting with stat
\* Debugger is active!
\* Debugger PIN: 710-864-711
72.17.0.1 - - [28/Mar/2025 05:59:25] " [35m [1mPOST /run?task=Say+Hello+Carlton HTTP/1.1 [0m" 500 -
raceback (most recent call last):
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1536, in \_call\_
return self.wsgi\_app(environ, start\_response)
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1514, in wsgi\_app
response = self.handle\_exception(e)
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1511, in wsgi\_app
response = self.full\_dispatch\_request()
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 919, in full\_dispatch\_request
rv = self.handle\_user\_exception (e)
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 917, in full\_dispatch\_request
rv = self.dispatch\_request()
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 902, in dispatch\_request
return self.ensure\_sync(self.view\_functions (rule.endpoint]) (\*\*view\_args) # type: ignore [no-any-return]
File "/usr/src/app/app.py", line 22, in run\_task
action = classification.get("action", "").lower()
AttributeError: 'NoneType' object has no attribute 'lower'
72.17.0.1 - - [28/Mar/2025 05:59:30] " [35m [1mPOST /run?task=%0AInstall+`uv`+
if+required)
+and+run+the+script+`https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466
52b66ae/datagen.py`%0Awith+`23f2004644@ds.study.iitm.ac.in'+as+the+only+argument%0A HTTP/1.1 [0m" 500 -
72.17.0.1 - - [28/Mar/2025 05:59:30] " [33mGET /read?path=/data/format.md HTTP/1.1 [0m" 404 -
72.17.0.1 - - [28/Mar/2025 05:59:36] " [35m [1mPOST /run?task=Format+`/data/format.md+with+`prettier@3.4.2`+in-place HTTP/1.1 [0m" 500 -
72.17.0.1 - - [28/Mar/2025 05:59:36] " [33mGET /read?path=/data/format.md HTTP/1.1 [0m" 404 -
72.17.0.1 - - [28/Mar/2025 05:59:39] " [35m [1mPOST /run?
ask=/data/datefile.txt+has+list+of+dates,+one+per+line.%0ACount+the+number+of+Thursdays+in+the+list+and+write+just+the+number+to+`/data/dates-
Thursdays.txt` HTTP/1.1 [0m" 500 -
raceback (most recent call last):
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1536, in \_call\_
return self.wsgi\_app (environ, start\_response)
File "/usr/local/lib/python3.9/site-packages/flask/app.py", line 1514, in wsgi\_app
response = self.handle\_exception(e)

image description : The image shows error messages, HTTP requests, and status codes. The overall context appears to be related to a system that is unable to open a database file.
image text: "error": "unable to open database file"
}
HTTP Request: GET http://localhost:8000/read?path=/data/b10.csv "HTTP/1.1 404 NOT FOUND"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 12 / 20
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"

---

Sir, my project scored 1/20, with only B1 passed. However, when I ran the evaluation script, I got 6/10 in A tasks. Is there any way this can be checked, as the project works on deployed.  
Kind Regards and thanks

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir,  
This is the id of the docker image that was evaluated: 82aeb74ca739 ,  
but i had never provided this docker image instead my image id is de8235663462  
then how it get evaluated, also none of the docker image created by me has this id. My docker image was created on linux/amd64.

Please, look over it [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) .

Regards,  
S Sharmile  
23f3001688

---

Sir the evaluated docker file ID was mentioned as 5b28fd5b25a7 in the mail sent by you but my docker file ID is 4d8c0cc34e35. I think my docker file is not evaluated properly. Kindly do check this and help me out. My reg no 24f1002633.

---

[@carlton](/u/carlton)  
My docker logs shows that `OSError: Cannot find resource` error occurred when the data generation script tried to access font files in generation for a8.  
image description: The image displays a terminal output showing a series of Python traceback errors related to file or resource access. The errors indicate an inability to open resources, specifically font files, during an image processing task.
image text: Installed 3 packages in 42ms
Traceback (most recent call last):
File "/tmp/datagenmrt9km.py", line 220, in a8\_credit\_card\_image
large\_font = ImageFont.truetype("arial.ttf", size=60)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 879, in truetype
return freetype (font)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 876, in freetype
return FreeTypeFont (font, size, index, encoding, layout\_engine)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 284, in \_init\_
self.font = core.getfont(
~~~~^
font, size, index, encoding, layout\_engine=layout\_engine
(
OSError: cannot open resource
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/tmp/datagenmrt9km.py", line 303, in <module>
a8\_credit\_card\_image ()
File "/tmp/datagenmrt9km.py", line 224, in a8\_credit\_card\_image
large\_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=60)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 879, in truetype
return freetype (font)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 876, in freetype
return FreeTypeFont (font, size, index, encoding, layout\_engine)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 284, in \_init\_
self.font = core.getfont(
~~~~^
font, size, index, encoding, layout\_engine=layout\_engine
(
OSError: cannot open resource
INFO: 172.17.0.1:35176 - "POST /run?
task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fgist.githubusercontent.com%2Fsanand0%2Ff19b6797f82b36da39ac4

The datagen.py script looked for Arial font in the try block and when it encountered error it went to the except block to use DejaVuSans, the Pillow default, except it encountered the same error there, which was not handled. Thus, datagen.py stopped abruptly without creating files for A9 and A10 as well. So effectively, my A9 and A10 did not get evaluated properly as it did not have the required files due to error during data generation for A8. Can you please re-evaluate by enclosing each of the data generation function calls in their own try-except blocks?  
Here's a description of the image:
\*\*Image description:\*\*
The image displays a list of Python function names. The list is written in a dark grey font on a black background.
\*\*image text:\*\*
a2\_format\_markdown()
a3\_dates()
a4\_contacts()
a5\_logs()
a6\_docs()
a7\_email()
a8\_credit\_card\_image()
a9\_comments()
a10\_ticket\_sales()
  
I think it would be better to enclose each of these function calls in their own try-except blocks. This screenshot is taken from the datagen.py file sent in yesterday’s results mail.

So, will it be possible to re-evaluate my task A1, A8, A9 and A10? At least A9 and A10 did not even get the files to work on as they weren’t even created due to insufficient error handling in datagen.py .

Also, can you help me to identify the cause of even the Pillow default font not being available? I don’t understand how a font not being available could be caused by my code.

Thank you

---

image description: The image is a text-based display, likely a console or terminal output. It reports on the execution of a task and subsequent errors.
image text: Running task: Install `uv` (if required) and run the script
`https://gist.githubusercontent.com/sanand0/f19b6797f82b36da39ac44f3a7d4392a/raw/13246698088795e1942179856aafd466052b66ae/datagen.py`
with `23f3003196@ds.study.iitm.ac.in` as the only argument
HTTP Request: POST http://localhost:8503/run?
task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fgist.githubusercontent.com%2Fsanand0%2Ff19b6797f82b36da39ac4
4f3a7d4392a%2Fraw%2F13246698088795e1942179856aafd466052b66ae%2Fdatagen.py%60%0Awith+%6023f3003196%40ds.study.iitm.ac.in%60+as+the+only+argu
ment%0A "HTTP/1.1 500 INTERNAL SERVER ERROR"
}
HTTP 500 {
"error": "Agent error: 429 Client Error: Too Many Requests for url: https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
}

this is a 429 from sanand which is an error from your side. The evaluation already so delayed now has such issues because of which I am getting 1/20. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

does that mean our script is not evaluated?

---

Hi [@Vihaanv07](/u/vihaanv07)

This was a good spot, we will rerun all the images where string `Agent Errro: 429 Client Error....` is present.

Thanks and kind regards

---

Hi [@Jayeshbansal](/u/jayeshbansal)

There were 12 emails for which we didn’t rerun, we will be fair with grading you and will take care of it.

---

image description: The image is a terminal window showing the output of the `docker images` command. It lists various Docker images with details such as repository, tag, image ID, creation date, and size.
image text: Last login: Sat Mar 29 19:14:55 on ttys003
mish@Mishs-MacBook-Air ~ % docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
tds-project1 latest dc8c1e7528b8 5 weeks ago 1.75GB
mishkat02/automation-agent latest 07b16dc68225 6 weeks ago 367MB
franky1/tesseract latest b3042ad1e731 2 months ago 2.33GB
mish/myrepo 23f3003027 07940877fae1 2 months ago 12.2MB
mishkat02/myrepo 23f3003027 07940877fae1 2 months ago 12.2MB
docker/welcome-to-docker latest eedaff45e3c7 16 months ago 29.5MB
vimagick/tesseract latest a2716ea6a3e9 19 months ago 289MB
otiai10/tesseract latest 288660ceb79d 7 years ago 2.2GB
ngrok/ngrok latest f0dd0d51e8d7 55 years ago 244MB
mish@Mishs-MacBook-Air ~ %
  
My docker image id is different than the one I submitted  
“This is the id of the docker image that was evaluated: 10f11a0e0cd6”

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) plz check this

---

Hi [@23F300327](/u/23f300327)

This is what you submitted to us in the gform.

23f3003027@ds.study.iitm.ac.in mishkat02/automation-agent:latest

We will only evaluate this image.

Kind regards

---

[@carlton](/u/carlton) then why is the image id different?

in the docker hub as well as my local terminal the image id is 07b16dc68225

---

When we build it after pulling it, it will get a unique identifier that makes sure we will only ever evaluate exactly that version. We pull it from your submission in the form.

In other words, if any changes occur to the docker repo, our id will no longer match a newer version of the file. This way we can make sure we are evaluating the right version every time. Your id does not have to match ours.

But we can detect changes made to the docker repo through our image id. I hope that is clear.

We will do some extra sanity checks before the 1/4/2025 just incase there are any issues. But thanks for asking the question.

Kind regards

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

My logs show, ‘exec format error’ and it is due to architecture issue, image was built on mac.

I have updated the google form regarding the architecture. Please rerun my image. Thanks

---

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> ### **Docker Image Architecture Issue Report**
>
> If your Docker image was run on the wrong architecture, please fill out this form:  
> [Submit Report](https://docs.google.com/forms/d/e/1FAIpQLSerCpqod-5ArJWTW_QW5PenyfZJHH_cmcUw3s8dAoG3zDZm8g/viewform?usp=sharing)

Just fill the google form, we are rerunning such images.

---

Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between `pandas` and `numpy` caused the container to fail. To my surprise, the same versions (`pandas==2.0.3` and `numpy==1.24.3`) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (`santoshsharma003/tds-project-one-1:latest`). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!

---

Hi [@carlton](/u/carlton), I checked my Docker log file now and realised I missed to push a couple of files to the image. Is there anything I could do now? I have all the required files in my Git repo though. Please help.

---

Sir in my logs it is showing that there’s cv2 module missing i mightve missed adding that in the requirements. Is there anything you could do to help me please?

---

I am also facing the same issue. I tried evaluating the scripts with the evaluation file also. Please rerun and let me know. My Roll No is 21F1002866.

---

Hi,

For Tasks A8, A9 & A10, I am not seeing any errors in my Docker execution logs. I am assuming the evaluation script failed to fetch the output file to verify the output for some reason. Can you please try rerunning these three tasks again? These tasks are working fine for me.

For Task B1. “Data outside /data is never accessed or exfiltrated, even if the task description asks for it.” - So when the evaluation asked to write something to /tmp/hello.txt it has correctly thrown an error saying access denied. I think this should be marked as correct. As the task description itself says so, the return is passed as 200 OK

```
ERROR:main:Error executing write_file: Access denied: /tmp/hello.txt
INFO:     172.17.0.1:60918 - "POST /run?task=Write+%27Hello+World%27+to+%60%2Ftmp%2Fhello.txt%60 HTTP/1.1" 200 OK

```

Similarly for task B2.

```
INFO:main:Checking file path: /data/format.md
ERROR:main:Error executing file_folder_deletion: Deletion not allowed: /data/format.md
INFO:     172.17.0.1:59446 - "POST /run?task=Delete+%2Fdata%2Fformat.md HTTP/1.1" 200 OK

```

For Task B4, if branch is not given we are assuming it as ‘main’ branch. Is it not correct? We would have at least expected the branch passed in the request.

For Task B8, I could not see the task description sent in the request in evaluation log file. Can you please check if the task request was passed properly?  
Because I see only “=4 B8 failed: not all arguments converted during string formatting” for Task B8

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Thanks for your encouragement.. tried debugging the issue of image not starting up in the orchestrator script.. I found that the issue was happening because of the http and https proxies being set in docker build

```
ARG http_proxy=http://www-proxy-adcq7.us.<xxx>.com:80
 ARG https_proxy=http://www-proxy-adcq7.us.<xxx>.com:80

ENV http_proxy=${http_proxy}
 ENV https_proxy=${https_proxy}

```

This was required as my office environment was behind the proxy and it was required for uv to download the dependencies on startup..

So this had caused the image to run in my office environment and not in orchestrator environment.. now removed the same and tested in a different vm altogether and noticed that the container started up without issues..

Checkin url: [Update Dockerfile removed hard coded proxies · rsjay1976/TDS-Project1-Jan25@a71e3a8 · GitHub](https://github.com/rsjay1976/TDS-Project1-Jan25/commit/a71e3a84b284d7621f2a769308340454ebd58583)

Have pushed the latet image (rsjay1976/tds-project1-jan25:latests) to docker hub as well.. didnt make any source changes or any other changes in the image.. Would be great if this is considered and image be considered for reevaluation… Appreciate your help

---

I am also with the same situation sir. Please help with this issue. I have submitted everything correctly and it was working fine. Thanks

---

Hello Sir,

Greetings,

I have not recieved amy mail regarding my Project 1 Marks, can you please look into it.

Thank you/

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) please sir could you help me with this issue previously when i ran on my system it was working perfectly fine

---

Hello sir

I noticed that the log mentioned:  
“python: can’t open file ‘/app/app/main.py’: [Errno 2] No such file or directory.”

However, my main file was named run.py, which might have caused the issue. Since the code was present, I was given a 0. Would it be possible to run it again or consider partial marks for the submission?

Thank you for your time and consideration. I appreciate your help!

---

Even my file saying the same. I got the ‘No module named tasksA’ error whereas at the time of submission it was working perfectly fine. Please kindly look into this issues sir.  
Thank you.

---

no taskA.py even though i ran the evalution getting 12 score still no evalution.log  
help the students please give them second chance

---

on a side note, to validate and test our docker/podman images on a platform outside of our dev environment we can use <https://labs.play-with-docker.com/>.. this is a free platform to download run and test docker images …

---

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

I might have found a bug in my code, I have hardcoded my file directory into my code but I didn’t change it later. I have created a safe\_open function that will throw a HTTP\_403\_FORBIDDEN error when tried to access files outside that directory. Because of this all the tasks failed. There also might be environment and configuration issues in my Dockerfile. When I tested locally, it worked fine but because of this small mistake I am now only getting 1/20. Is it possible to change/modify my code?

Thanks for considering, any help would be appreciated. Worked very hard for this

---

The docker id of the image that was evaluated (as specified the mail 1ae3f64427f0) is not correct, the correct id is 51168f246618.

Name of Docker image -  
garriimaa/llm\_automation:latest  
Please evaluate with the above image name.

GitHub repository for reference - [GitHub - Garima1603/llm\_automation](https://github.com/Garima1603/llm_automation)

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir I fixed my issue with docker during the given window for discrepancy and requested a re-pulling of the image but still got a mail of score 0. Please sir, I request you to do a re-evaluation, the docker issue is fixed long back by me. It’s an earnest request sir.

---

Dear sir, [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I got result as fail for the project 1 and the reasons listed are as in the screenshot. But as you can see in the second screenshot, i still have that repository which is public, have license file and docker file in it, created 2 months back. I actually don’t know how this issues come in, please resolve this.  
image description : The image is a screenshot containing text that outlines the prerequisites for a project, followed by the evaluation results. The project requires several GitHub repository conditions to be met. The evaluation results are listed as "Is Docker image present in dockerhub AND is public: PASS", "Is Github repo present AND public: FAIL", "Is Dockerfile present in root of github repo: FAIL", and "Is MIT license present at root of github repo: FAIL". The overall prerequisite status is FAIL and the project score is 0.
image text: Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0
  
image description: This image shows a GitHub repository named "tds\\_proj1". It displays a list of files and directories with their respective update statuses and timestamps.
image text: tds\\_proj1 Public
main 1 Branch 0 Tags Pin Unwatch Go to file t Add file Code 21f2000304 update 5e4785c. 2 months ago 10 Commits \\_pycache\\_ update 2 months ago data update 2 months ago env update 2 months ago Dockerfile update 2 months ago LICENSE Create LICENSE 2 months ago app.py update 2 months ago datagen.py update 2 months ago evaluate.py update 2 months ago requirements.txt update 2 months ago tasksA.py update 2 months ago

---

[@carlton](/u/carlton)  
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link: [GitHub - karthiksirimilla/tds\_project1\_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20  
Roll no : 23f1002398  
Mailid: 23f1002398@ds.study.iitm.ac.in

My evaluation.log  
image description: The image shows a series of HTTP requests and responses. There are several "FAILED" notifications and a score of 6/20. The text includes details on data processing tasks and connection errors.
image text: HTTP Request: GET http://localhost:8309/read? path=/data/b9.html "HTTP/1.1 404 Not Found"
B9 failed: Cannot read /data/b9.html
B9 FAILED
✔ Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background. From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv? sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv. Then stop the datasette server.
HTTP Request: POST http://localhost:8309/run? task=Run+datasette+via+%60uvx+datasette+%2Fdata%2Fticket-sales.db+-- port+8001%60+in+the+background.%0AFrom+%60tickets%60+ count+the+number+of+rows+where+%60type%60+is+%22Bronze%22+using%0Ahttp%3A%2F%2Flocalhost%3A8001%2Fticket- sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM%2Btickets%2BWHERE%2Btype%2B%3D%2522Bronze%2522%0Aand+save +it+to+%2Fdata%2Fb10.csv.%0AThen+stop+the+datasette+s erver.%0A "HTTP/1.1 400 Bad Request"
HTTP 400 { "detail": "HTTPConnectionPool(host='localhost', port=8001): Max retries exceeded with url: /ticket- sales.csv? sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x76deb5efeb40>: Failed to establish a new connection: [Errno 111] Connection refused'))" }
HTTP Request: GET http://localhost:8309/read? path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
B10 FAILED
Score: 6 / 20
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"

---

image description: The image is a screenshot of an email regarding the scores for Project 1. The email is addressed to the learner and lists the pre-requisite checks that need to be met. The evaluation results show that the Dockerfile is not present in the root of the github repo, the pre-requisites are failed and the project score is 0.
image text: 1:30 TDS Jan 25 Project 1 Scores ... to me Dear Learner, Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page: 1. Your GitHub repository exists and is publicly accessible 2. Your GitHub repository has a LICENSE file with the MIT license 3. Your GitHub repository has a valid Dockerfile 4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME 5. Your Docker image uses the same Dockerfile as in your GitHub repository If you fail to meet this minimum requirement your submission will not get evaluated. These are your Project 1 Prerequisite evaluations: Is Docker image present in dockerhub AND is public: PASS Is Github repo present AND public: PASS Is Dockerfile present in root of github repo: FAIL Is MIT license present at root of github repo: PASS Prerequisites: FAIL Project 1 Score: 0 ...

---

[@carlton](/u/carlton) Sir, the image id written in my notification email is wrong. The correct image is this: <https://hub.docker.com/repository/docker/24f1002064/project1/general>

can you please double check this? You can also verify that I have made no changes to it since the due date.

---

[@carlton](/u/carlton)  
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link: [GitHub - karthiksirimilla/tds\_project1\_final](https://github.com/karthiksirimilla/tds_project1_final)

My evaluation.log , contains the score 6/20  
Roll no : 23f1002398  
Mailid: 23f1002398@ds.study.iitm.ac.in  
image description: The image is a screenshot of an email, likely related to a project submission evaluation. It displays a list of prerequisites and their evaluation results, indicating whether they passed or failed. The email mentions GitHub repositories, Docker images, and licensing requirements. The final score for Project 1 is displayed as 0, and prerequisites are marked as FAIL.
image text:
1:30
TDS Jan 25 Project 1 Scores
22t1 se2002 1:27AM
to me
19
Dear Learner,
Project 1 requires you to pass some pre-requisite
checks as detailed on the TDS Project 1:
Evaluation page:
1. Your GitHub repository exists and is publicly
accessible
2. Your GitHub repository has a LICENSE file with
the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and
runs via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p
8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as
in your GitHub repository
If you fail to meet this minimum requirement your
submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is
public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github
repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
...

---

Your dockerfile is misspelt.

---

Thanks for your quick response sir. I just wanted to clarify that my dockerfile was recognized by Docker, and my image was successfully built, so it seems that Docker itself didn’t have an issue with the filename.

However, I understand that the evaluation script might be case-sensitive and specifically looking for “Dockerfile” with an uppercase “D”. If that’s the issue, should I rename and push the file again to the repo sir.

Please let me know if that’s the right fix or if I need to do anything else sir.

---

The image id varies depending on the system it was built on. When we build it on our Xeon cloud compute it will get a different image id from yours (unless you have a Xeon system). What is common is the dcoker hub image name and tag we used. We used the one you submitted on your form.

But the image id serves the same purpose. If you alter the dockerhub image, our image will no longer match the one from dockerhub. the image id sha will change. So do not worry about whether your sha matches our sha. It just acts as a way for us to make sure that we are consistently looking at the same image.

Kind regards

---

I recently received an email stating that my Docker image is not publicly available, resulting in a failed prerequisite check for the TDS Project 1. However, I have ensured that my Docker image is publicly accessible. Please help.

[@carlton](/u/carlton)

My Docker image ID is "**99d08f2002fa** ", and it is set to public. I kindly request you to review this issue, as I have worked very hard on this project and would appreciate the opportunity for a fair evaluation.

---

can you share the sha?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

There might be some glitches in the system. Could you kindly verify the process again?

image description: The image is a screenshot of an email. The email is addressed to a learner and provides the project prerequisites. The email states the requirements for a project and the evaluation results.
image text: 02:55
22t1 se2002 01:25
to me
Dear Learner,
Project 1 requires you to pass some pre-requisite
checks as detailed on the TDS Project 1:
Evaluation page:
1. Your GitHub repository exists and is publicly
accessible
2. Your GitHub repository has a LICENSE file with
the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and
runs via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p
8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile
as in your GitHub repository
If you fail to meet this minimum requirement your
submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is
public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

I’ve already received my score in the evaluation log. Additionally, the Docker Hub run logs show no errors, and both the GitHub repo and Docker image are publicly accessible. All the content has been verified and meets the prerequisites.

Let me know if any further action is needed from my end.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) please kindly re-pull my docker image and re-evaluate my project sir. I fixed the issue long back. Please reply kindly. My roll no is : 22f2001389. I have been trying to get to you for long now. Please kindly help me out. Please reply.

---

[@carlton](/u/carlton)  
I have submitted my Project 1, and my GitHub repository meets all the listed requirements. However, I received a FAIL for the check:

“Is Dockerfile present in root of GitHub repo?”

Despite this, my dockerfile is present in the root directory of my repository.

Github repo link: [GitHub - Vansh-22f300/project\_tds](https://github.com/Vansh-22f300/project_tds.git)

My evaluation.log , contains the score .  
Roll no : 22f3001851  
Mail id:22f3001851@ds.study.iitm.ac.in  
image description: The image is a screenshot of a GitHub repository interface. It shows the main branch and the files present in the repository. The top of the screen displays the repository name, license, and other details. Below is a list of files and folders, including ".env", ".gitignore", "LICENSE", "README.md", and Python files like "app.py", "datagen.py", "evaluate.py", "tasksA.py", and "tasksB.py". Each entry includes the last update time.
image text:
9:11
MIT license
0 stars 0 forks
0 Tags
Activity
Public repository
main
Vansh-22f300 2 months ago
\_pycache\_ 2 months ago
.env 2 months ago
.gitignore 2 months ago
LICENSE 2 months ago
README.md 2 months ago
app.py 2 months ago
datagen.py 2 months ago
dockerfile 2 months ago
evaluate.py 2 months ago
requirements.txt 2 months ago
tasksA.py 2 months ago
tasksB.py 2 months ago

---

dockerfile is spelling mistake it should be Dockerfile same thing happened to me .

---

[@carlton](/u/carlton)

Pls look into this evaluation.py contains two result  
Can u confirm that u guys will use 10/20 one ?  
image description: The image is a screenshot of a phone screen displaying terminal output. The text instructs on how to use `curl` to retrieve data, stop a server, and provides additional notes about system configuration and data verification. It also shows HTTP requests and their statuses, with an error indicating a failed attempt to read a CSV file.
image text: starting the server.\n\n### Step 2: Count Rows
with SQL\n\n1. Use `curl` or a web browser to
make a request to the URL that runs the SQL
query. Replace `curl` with your choice of method
if necessary.\n\n If using `curl`, run the
following command:\n\n
bash\n curl
\"http://localhost:8001/ticket-sales.csv?
sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type=%22B
ronze%22\" -o /data/b10.csv\n ```\n\n
This
command requests the CSV output of the SQL query
and saves it to `/data/b10.csv`.\n\n### Step 3:
Stop the Datasette Server\n\n1. If you are in a
terminal session and want to stop the server,
you can bring the server process to the
foreground with the `fg` command if needed, or
you can kill the process directly using:\n\n
```bash\n kill $(jobs -p)\n ```\n\n This
command will stop all background jobs started in
that terminal session. Alternatively, if you
know the PID of the Datasette server, you can
use:\n\n
u\yseq、、、
kill <PID>\n
u\u\、、
Replace `<PID>` with the actual process ID of
the Datasette server.\n\n### Summary of
Commands\n\n```bash\nuvx datasette /data/ticket-
sales.db --port 8001 &\ncurl
\"http://localhost:8001/ticket-sales.csv?
sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type=%22B
ronze%22\" -o /data/b10.csv\nkill $(jobs
p)\n```\n\n### Additional Notes\n\n- Ensure that
uvx` and `datasette` are installed and
configured correctly on your system.\n- Make
sure that the `/data` directory is writable by
your user or the command may fail.\n- You may
wish to check the contents of `/data/b10.csv`
after the operation to ensure that it contains
the expected results."
HTTP Request: GET http://localhost:8064/read?
path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 10 / 20
HTTP Request: POST
https://aiproxy.sanand.workers.dev/openai/v1/emb
eddings "HTTP/1.1 200 OK"
  
image description : A black screen displaying a series of technical outputs related to HTTP requests and data processing. There are several error messages including "HTTP 500 Internal Server Error," "404 Not Found," and "429 Too Many Requests." The screen also shows commands to install and run scripts along with file paths and URLs.
image text: 8:51 AM
23f2005702@ds.stud...
Bronze%22
and save it to /data/b10.csv.
Then stop the datasette server.
HTTP Request: POST http://localhost:8462/run?
task=Run+datasette+via+%60uvx+datasette+%2Fdata%
2Fticket-sales.db+--
port+8001%60+in+the+background.%0AFrom+%60ticket
s%60+count+the+number+of+rows+where+%60type%60+i
s+%22Bronze%22+using%0Ahttp%3A%2F%2Flocalhost%3A
8001%2Fticket-
sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM
%2Btickets%2BWHERE%2Btype%2B%3D%2522Bronze%2522%
0Aand+save+it+to+%2Fdata%2Fb10.csv.%0AThen+stop+
the+datasette+server.%0A "HTTP/1.1 500 Internal
Server Error"
HTTP 500 {
"detail": "'choices'"
}
HTTP Request: GET http://localhost:8462/read?
path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 1 / 20
HTTP Request: POST
https://aiproxy.sanand.workers.dev/openai/v1/emb
eddings "HTTP/1.1 429 Too Many Requests"
Failed to send request to OpenAI API: 429
Running task: Install `uv`(if required) and
run the script
`https://gist.githubusercontent.com/sanand0/f19b
6797f82b36da39ac44f3a7d4392a/raw/13246698088795e
1942179856aafd466052b66ae/datagen.py`
with `23f2005702@ds.study.iitm.ac.in` as the
only argument
HTTP Request: POST http://localhost:8064/run?
task=%0AInstall+%60uv%60+%28if+required%29+and+r
un+the+script+%60https%3A%2F%2Fgist.githubuserco
ntent.com%2Fsanand0%2Ff19b6797f82b36da39ac44f3a7
d4392a%2Fraw%2F13246698088795e1942179856aafd4660
52b66ae%2Fdatagen.py%60%0Awith+%6023f2005702%40d

---

HELLO SIR , DOCKET IMAGE PRESENT IN DOCKER HUB AND IT IS PUBLIC THEN WHY IT IS FAIL  
image description : This image presents an evaluation of project 1 prerequisites. It lists several checks, their statuses, and the final score.
image text: These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
image description: The image shows a webpage displaying repository details, focusing on tags associated with "data\_automation\_agent".
image text: 23f2004644/data\_automation\_agent
Last pushed about 1 month ago • Repository size: 757 MB
Add a description
i
Add a category
i
General
Tags
Image Management BETA
Collaborators
Webhooks
Settings
Tags
This repository contains 1 tag(s).
Tag
latest
OS
Type
Pulled
Pushed
Image
5 days
about 1 month
See all
  
![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/e/f/efd0ca8b5a79aca303f8ae07d632c1a62c07bb1f_2_690x37.png)  
[@carlton](/u/carlton)

---

same issue i am also facing ,  
[@carlton](/u/carlton)

---

Respected Sir,

I have received a **FAIL** status for the prerequisite check:  
*“Is Docker image present in Docker Hub AND is public.”*

However, as shown in my Docker Hub repository, my Docker images are publicly accessible.

I have attached a screenshot for the reference.

Thank you for your time and support.

Here's a description of the image:
The image is a screenshot of a webpage, likely a platform for managing code repositories. The main section displays a list of repositories under the "santoshsharma003" namespace. It provides details like repository name, last pushed date, content, visibility, and scout status. There is a navigation menu on the left that includes "Repositories", "Settings", "Billing" and "Usage". There are also search and filter options at the top.
image text: santoshsharma003 Docker Personal Repositories All repositories within the santoshsharma003 namespace. Search by repository name All content Repositories Settings Default privacy Notifications Billing Usage Name santoshsharma003/tds-project-one-1 Create a repository Last Pushed ↑ Contains Visibility Scout 2 days ago IMAGE Public Inactive

---

Dear team,

The evaluation shows that the Github repo was not found, however the repository has published and public.  
image description : A white background with black text. The text describes Project 1 prerequisite evaluations and results, which includes if the Docker image is present in dockerhub and public, a Github repo present and public, Dockerfile present in the root of github repo, and a MIT license present at the root of github repo. The prerequisites and project score are also presented.
image text: If you fall to
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

Github URL [GitHub - 22f3003029/llm\_agent](https://github.com/22f3003029/llm_agent)

Roll Number: 22f3003029

Request your assistance on the issue.

Thank you

---

Respected Team,  
I received an email stating I failed to fulfil prerequisite and scored 0 because of it.  
image description: The image is a screenshot of a checklist evaluating a project based on several criteria. The criteria include whether a Docker image is public, whether a GitHub repository is public, the presence of a Dockerfile, and the presence of an MIT license. The overall prerequisites are marked as FAIL, and the project score is 0.
image text: If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
I checked my Docker Hub and there it is showing “Public”  
Here's a brief description of the image:
The image is a table showing information related to an image named "coolsisters7/llm". The table has columns for "Name," "Last Pushed," "Contains," "Visibility," and "Scout." The "coolsisters7/llm" image was last pushed about 1 month ago, contains an image, is public, and is currently inactive.
image text:
Name
Last Pushed ↑
Contains
Visibility
Scout
coolsisters7/llm
about 1 month ago
IMAGE
Public
Inactive
  
Can Anyone explain what I did wrong ?

---

Here's a description of the image:
The image is a text document. It begins with a message to a learner about Project 1. The message lists several prerequisites that must be met. There are points about GitHub repository and Dockerfile. After the prerequisites are listed, there is a section for the evaluation of the project's requirements. It concludes with a "FAIL" for the prerequisites and a score of "0".
image text:
Dear Learner,
Project 1 requires you to pass some pre-requisite checks as
detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT
license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via
podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p
8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your
GitHub repository
If you fail to meet this minimum requirement your submission
will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
Here's a description of the image:
The image is a screenshot of a web interface, likely a repository or container management platform. It focuses on the 'Tags' section of a project named "jayeshbansal/tds\\_project1". The interface displays the details of the "latest" tag, including its digest, OS/ARCH, and last pull information. Additional sections on the page show docker commands and the repository size.
image text: jayeshbansal/tds\\_project1 Last pushed about 1 month ago • Repository size: 77 MB Add a description Add a category General Tags Image Management BETA Collaborators Webhooks Settings Sort by Newest Filter tags Delete TAG latest Last pushed about 1 month by jayeshbansal Digest OS/ARCH Last pull 2bdbd090a678 linux/amd64 about 1 month Docker commands To push a new tag to this repository: docker push jayeshbansal/tds\\_project1:tagna me docker pull jayeshbansal/tds\\_project1:latest Copy Compressed size 77.02 MB
  
Sir, I have the image in the docker and it is upload last month and it is public. So why have I received a message saying that the image is not available in the hub. Can you confirm and reevaluate the error.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)

---

Hi [@Jayeshbansal](/u/jayeshbansal) ,

The docker repo name that you submitted through submission form was different than what your screenshot shows. `/jayeshbansal/add9a05689d3` docker repo doesn’t exists or might not be public, that’s why it failed for you.

image description: The image presents a table with information about a project. The table has columns for timestamp, email address, GitHub repository link, and DockerHub image name.
image text: Preview Code Blame 1069 lines (1069 loc) 127 KB Raw Q 24f1001895@ds.study.iitm.ac.in 1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub? 1022 2/16/2025 23:55:44 24f1001895@ds.study.iitm.ac.in https://github.com/jayesh-bansal/TDS-Project1/ jayeshbansal/add9a05689d3

---

The log file provided to me too contains File not found error for task A. However, running the code on the evaluate.py files gave me results. Could you please look into the datagen part?  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

Thanks

---

It is the request to the team,to consider this since it is a problem of just a case letter otherwise the whole hardwork of doing the project will be wasted.  
Thank you

---

Dear instructors, I received the mail today regarding project 1 TDS scores and I have been marked fail because the MIT license is not present. But as can be seen in the screenshot below the MIT license file is present in my GitHub repository. Pls look into this matter.  
Here's a description of the image:
The image is a screenshot of a GitHub repository named "Project1-TDS". The repository has one branch and no tags. The screenshot shows the files and folders within the repository.
image text: Project1-TDS Public main 1 Branch 0 Tags Go to file Unpin Unwatch 1 t + <> Code PalakAnand30 Rename LICENSE to MIT LICENSE ab381b5 2 months ago 5 Commits \_pycache\_ Initial commit 2 months ago app commiting final files 2 months ago .DS\_Store commiting final files 2 months ago Dockerfile Rename dockerfile to Dockerfile 2 months ago MIT LICENSE Rename LICENSE to MIT LICENSE 2 months ago datagen.py Initial commit 2 months ago evaluate.py Initial commit 2 months ago requirements.txt commiting final files 2 months ago

---

It depends where you tested it running, if it’s running inside a docker container and you feel there is problem with our script then you can debug our code and create a pull request on repo.

---

Hi [@24ds2000125](/u/24ds2000125)

You didn’t meet the standard naming convention for mit license naming. Name should be LICENSE(all caps) or LICENSE.md.  
check this out.  
[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

Hi [@22f3001851](/u/22f3001851)

Standard naming convention for Dockerfile name was not followed we won’t be able to evaluate it.

---

image description: The image displays a list of checks with PASS or FAIL statuses. The first check "Is Docker image present in dockerhub AND is public" is marked as FAIL and is highlighted in red. A red underline highlights "FAIL" under "Prerequisites." "Project 1 Score" is marked as 0.
image text: Is Docker image present in dockerhub AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/c/ec83ed7abc829b1bf89cfa30f9c84c1075717a63.png)

My email is 22f3001642@ds.study.iitm.ac.in  
[@Jivraj](/u/jivraj) Could you please check what’s wrong?

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) any updates for the people like me whose image was run on the wrong architecture - mine was ARM ( was evaluated or ×86 ). I filled the form that was later sent for selecting the architecture.

I haven’t received any mail since then. But found many mails are sent to others in while.

---

image description: The image is a screenshot of a GitHub repository named "tds-trail-1." The repository is public and belongs to the user "Mayank8IITM." The main content displayed includes a list of files and directories, along with information like the last commit message and the time since the last commit. Key files such as "Dockerfile," "LICENSE," and "README.md" are highlighted.
image text: Mayank8IITM / tds-trail-1
tds-trail-1 Public
main 1 Branch 0 Tags
Mayank8IITM Rename dockerfile to Dockerfile
\_pycache\_
data Project is done 7/10 2 months ago
.dockerignore updated dockerfile 2 months ago
Dockerfile Rename dockerfile to Dockerfile 2 months ago
LICENSE Create LICENSE 2 months ago
README.md Create README.md 2 months ago
datagen.py A2 and A9 left 2 months ago
evaluate.py A2 and A9 left 2 months ago
main.py Project is done 7/10 2 months ago
requirements.txt added dockerfile 2 months ago
  
image description: The image shows a document with the result of project prerequisites. Key elements in the document are the "Prerequisites: FAIL" and "Project 1 Score: 0" messages and the list of checks that failed.
image text:
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

Sir , I received the mail today regarding project 1 TDS scores and I have been marked fail because my repo is not public , and no docker file , no licence . but they all are present in my repo , and it is public too , , i am attaching the screenshot , you can see that too ,  
My email is 23f1000598@ds.study.iitm.ac.in  
Could you please check what’s wrong?  
[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

The task B6 was  
<https://quotes.toscrape.com/> has quotes from famous people.  
The .author class has the quote author’s name.  
Extract and save all authors from the first page, in order, to /data/b6.json as an array of strings.  
E.g. `["Douglas Adams", "J.K. Rowling", ...]`

The output in your file is not an array of double quoted strings.

Instead it is an array of an json object with the keyword author and values as an array of authors.

These are two different things. Almost there but not quite.

Kind regards

---

Hi Course Team,

I have also received an email today saying that my Project1 failed. But few days back I received an email with evaluation log saying I got 8/20. Which one is true?

image description: The image is a screenshot of an email from "TDS Team". The subject of the email is "TDS Jan 25 Project 1 Scores". The email indicates that the recipient's Project 1 score is 0 because they failed to meet the project prerequisites. The email lists the prerequisites, including the presence of a Docker image in Dockerhub, a public Github repository, a Dockerfile, and an MIT license. The "Dockerfile" check failed.
image text: TDS Jan 25 Project 1 Scores Inbox
2
22t1 se2002 1:24 am
to me
Dear Learner,
Project 1 requires you to pass some pre-requisite checks as
detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT
license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via
podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p
8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your
GitHub repository
If you fail to meet this minimum requirement your submission will
not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
Kind regards,
TDS Team

---

Can someone from TA team reply to this?

---

can somebody tell me how the dockerfile not running in 5 mins is my fault? i had the same requirements.txt as many other people and their file ran in given time while mine did not. what was the need for this, sorry for my harsh words but i’m frustrated, stupid rule?

---

For your case there was problem with our script that, we have correct, and your submission have dockerfile, license and repo exisits as well, it will be evaluated.

---

image description : The image shows a list of prerequisite evaluations for Project 1. The evaluations cover whether a Docker image is present in dockerhub and public, a Github repo present and public, a Dockerfile present in the root of the github repo, and an MIT license present at the root of the github repo. Some evaluations pass while one fails.
image text: These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: PASS

my dockerfile is available in github, Please look into the issue  
Thank you

---

[@Jivraj](/u/jivraj)

I also have same issue, can you check this…

[Repo link](https://github.com/21f3001076/TDS_Project_1)

image description: The image displays a code repository interface. The top section shows the main branch selection, code button and user information. There are several files listed with their modification times: Dockerfile, LICENSE, README.md, app.py, requirements.txt, and task\_handler.py. The bottom section includes a README file and MIT license details. The main content displayed is "TDS Project 1 - LLM-based Automation Agent".
image text: main, Code, lakshay654 2 months ago, Dockerfile 2 months ago, LICENSE 2 months ago, README.md 2 months ago, app.py 2 months ago, requirements.txt 2 months ago, task\_handler.py 2 months ago, README, MIT license, TDS Project 1 - LLM-based Automation Agent, Create an API

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) My P1 submission successfully passed all the basic sanity checks on February 15th and obtained a satisfactory score in the P1 evaluation, which was disclosed on March 29th. However, I received a communication today, April 1, stating that my Docker image is not present or public on DockerHub. I kindly request the TDS course team to investigate this matter at the earliest and provide a resolution for students encountering similar issues.

This situation is particularly disheartening—**seeing days of effort and dedication to Project 1 reduced to nothing, especially given the already demanding pace of the course.**

I will appreciate your prompt attention to this matter.

Kind regards

---

I understand the problem. It may be possible that the image id i gave may be different as i had multiple dockerfile and there is a possibility that i gave the wrong image id due to some confusion. Is it possible for reevaluation. I have worked very hard and I don’t want to lose my marks because of some wrong id misconfusion. I request to check my dockerfile once again and provide the marks accordingly

---

dear [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Dear Sirs,

I have seen that many others have posted similar issues to mine, and you have responded to some of them. To seek your attention, I am replying to this thread.

Please consider my request as well, as I do not want to lose marks on a project I have worked hard on, while also helping others. I am expecting a timely and positive response from your end.

Thank you.

---

Dear Sir,  
I hope you’re doing well. I haven’t received any email regarding the results of Project 1. Could you please check if my result was sent or if there’s any update on this?  
I would really appreciate your confirmation.  
Mail id - 23f2000798@ds.study.iitm.ac.in

---

[@carlton](/u/carlton)  
Respected Sir,  
I have submitted my project following all the guidelines and fulfilling all the prerequisites. My docker file is available publicly and it is present in the root directory of github repo, still the mail says that the file is missing and my score is zero. Can you please look into this issue

image description: The image displays a list of files, along with their versions and the time they were last modified. The file names include "datagen.py", "dockerfile", "evaluate.py", "requirements.txt", "tasksA.py", and "tasksB.py". The versions are labeled as v1 or v1.1, and all files were last modified "2 months ago".
image text:
datagen.py v1 2 months ago
dockerfile docker updatae 2 months ago
evaluate.py v1 2 months ago
requirements.txt v1.1 2 months ago
tasksA.py v1 2 months ago
tasksB.py v1 2 months ago

---

Name of your dockerfile doesn’t match the standard’s.  
It should be `Dockerfile`(with D caps).

---

No we are doing another run of evaluations. Results will be sent soon.

---

dockerfile name should be Dockerfile as this is the standard they are considering .so it was not evaluated you better change that, if they revaluate it will be passed

---

Your submission have Dockerfile, LICENSE and repo exists as well, we found some problems because of redirects not handled in our script.

Your submission will be evaluated.

---

We won’t be considering changes after deadline, our script looks for commits before deadline and fetches latest commits before deadline.

---

That’s not possible, anything after deadline is not appreciated.

---

We have updated just files names will it be considered??

---

same issue with me , my repo has both the dockerfile , license and is public. Please look into this . [@carlton](/u/carlton) sir . [@Jivraj](/u/jivraj) [GitHub - veershah1231/tds\_proj\_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.

image description: The image is a screenshot of an email. The email is from "22t1 se2002" and sent "to me". The email is about "Project 1" and its requirements. The email states that the project requires the learner to pass some pre-requisite checks and provides details on how to do so. It includes a list of checks, such as the GitHub repository being public, having a MIT license, a valid Dockerfile, and a publicly accessible Docker image. Below, a table lists the prerequisites evaluation results, which is mainly FAIL, resulting in a Project 1 Score of 0.
image text: 22t1 se2002 1:27 am
to me
Dear Learner,
Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

---

![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14 ":cross_mark:") Did Not Receive Project 1 Score – Need Clarification

**Post Content:**

> **Hello, sir** [@carlton](/u/carlton) [@Jivraj](/u/jivraj)
>
> I received the evaluation email for my **Project 1 Docker Image** submission, but unlike my friend (who got an email with his score), my email did **not** include my score.
>
> My Docker image ID: **6f446c9b84da**
>
> The email I received only contains logs and attachments, but no information about my actual score. in the mail recieved by my friend the score is clearly mentioned,
>
> I would really appreciate it if you could **clarify my project score** and let me know if it was properly evaluated. If there is any issue, I request a reconsideration of my project evaluation.
>
> Thank you for your help!
>
> **Attachments:**

but in the email which i recieved i got the below thing , there is no information about the project score

image description: The image is a screenshot of an email. The sender is '22t1 se2002', and the subject is a notification about a docker image submission. The email content discusses the evaluation process, providing file names and links, and mentions that missing files will result in a score of 0. It also outlines how the scores will be finalized and encourages feedback.
image text: 22t1 se2002 to me Dear Learner, We have evaluated your project 1 docker image submission. Please find the following files. MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us. MISSING files will result in a score of 0. Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet. 1. Evaluation log file. MISSING This contains your performance report on your individual tasks. 2. Docker log file. https://drive.google.com/file/d/10hrAjeGSjUOvpc6YNUj6WL8v5wKXK51W/view?usp=drivesdk This provides the technical performance of your container. 3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests. 4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism. 5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks. 6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications. 7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core concepts of LLMs to achieve the desired result. This is the id of the docker image that was evaluated: 6f446c9b84da These scores are not final but they indicate what our current evaluation standards will score you. If you have discovered a bug in our scripts or have a discrepancy to report with how the various scripts functions then we are happy to address your concern and where necessary make amendments to your score. You will have until Tuesday to report any problems. After which the score will be considered final. We will listen to feedback and then come up with a final marking schema. We will also look at the highest scores (including the score of the sample script we shared) to decide the mark on which the rest of the scores will be normalised. We look forward to your feedback and apologise for the delay in providing you with the scores.

sir could you please clarify about my project score ???  
waiting for the response

---

I am also facing the same issue sir please provide proper answer for our query. Please consider to recheck the project once again.  
Docker image - 5ff55c499b54  
image description: The image shows an email sent to the recipient "to me" 3 days ago. The email is about the evaluation of a docker image submission with information about missing files and evaluation criteria.
image text: 22t1 se2002 3 days ago
to me
Dear Learner,
We have evaluated your project 1 docker image
submission. Please find the following files.
MISSING indicates that the file is not available because the
evaluation did not run or the docker image was
misconfigured. If you feel this is in error you can still
contact us.
MISSING files will result in a score of 0.
Your docker image is supposed to become responsive in 5
minutes from launch. If it does not, then we will not
consider it. The images were all run on an 8 core Xeon
Google Cloud compute unit. So performance of the server
was not a bottleneck for your docker image. Also each
docker image had 1 Gigabit of dedicated network
bandwidth available which is nearly 5 times faster than the
fastest domestic internet.
1. Evaluation log file. MISSING This contains your
performance report on your individual tasks.
2. Docker log file. https://drive.google.
com/file/d/1yWyBsDHHcV1\_
nbfB5uZksMumimiHtzmG/view?usp=drivesdk This
provides the technical performance of your
container.
3. Server start log file (separate logs for arm vs x86)
(See attachment). If your docker service did not start
or respond to attempts to our requests.
4. Evaluation script file (separate logs for arm vs x86)
(See attachment). This file has the actual tests that
were run against your submission and the scoring
mechanism.
5. Data generation file (See attachment). The
evaluation file depends on this file to create the data
for the tasks.
6. Docker orchestration file (See attachment). This file
handles the retrieval of your docker image from

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Got a email stating that prereq failed stating below..  
Is Docker image present in dockerhub AND is public: FAIL

but i can see that image is public as shown below image.. am i missing something..

Here's a description of the image:
The image is a table showing details of an image repository. The table has columns for "Name", "Last Pushed", "Contains", and "Visibility". The row displayed contains the following information: "rsjay1976/tds-project1-jan25", "2 days ago", "IMAGE", and "Public".
image text:
Name
Last Pushed
Contains
Visibility
rsjay1976/tds-project1-jan25
2 days ago
IMAGE
Public

---

Given that you noticed an error on our side, you could have informed us about the same. However, you made your changes 22 hours ago, which is not acceptable.

```
tags = httpx.get(
                f"https://hub.docker.com/v2/repositories/{username}/{repo}/tags?ordering=last_updated",timeout = 60
            ).json()
            tag, size = next(
                (
                    (tag["name"], tag["full_size"])
                    for tag in tags.get("results", [])
                    if pd.Timestamp(tag["last_updated"]) <= DEADLINE
                ),
                (None, 0),
            )

```

This is part of our script that does the validation check for docker repo.

---

Sir,

The License file is present in the github repository however i received a mail that said that it was absent.

Here's a brief description of the image:
The image is a screenshot of a GitHub repository named "tds\_project-1". It displays the main branch and various files within the repository, including "LICENSE", "app.py", "requirements.txt", and others. The commit history and timestamps are also visible.
image text:
tds\_project-1 Public
main
1 Branch 0 Tags
Pin
◆ Unwatch
Go to file
Add file
Code
22f3000585 Create LICENSE
c61a6ef. now
6 Commits
\_pycache\_
Final Submission
2 months ago
venv
First submission
2 months ago
Dockerfile
First submission
2 months ago
LICENSE
Create LICENSE
now
MIT LICENSE
Rename LICENSE to MIT LICENSE
2 months ago
app.py
Final Submission
2 months ago
requirements.txt
First submission
2 months ago
test.txt
First submission
2 months ago

image description: The image displays evaluation results for a project. Key elements include a list of prerequisites, their pass/fail status, and the final project score.
image text:
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

Sir I thought that the ‘LICENSE’ file had to be renamed to ‘MIT LICENSE’.  
Can you please look into it. Thankyou!

---

[@Jivraj](/u/jivraj)

Can you also clarify my issue?

My submission meets all the prerequisites according to my Git repository and Docker image. Additionally, I can see the results in the evaluation log.  
You can check the details in the images below. Screenshot of mail and repository

Roll no. : 21f3001076

[GitHub Repo link](https://github.com/21f3001076/TDS_Project_1)

Here's a description of the image:
The image shows text on a dark background, likely representing the evaluation of a project's prerequisites. The text is structured in a list format, detailing several checks with PASS or FAIL results. The overall prerequisites are marked as FAIL, and the project score is 0.
image text:
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is
public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0

image description: The image is a screenshot that displays three items each with a title, a link, and a description. The image uses a black background.
image text: Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet. 1. Evaluation log file. https://drive.google. com/file/d/1AO\_ ycjKp7CPzaiiEHqSMGBYGg/view? usp=drivesdk This contains your performance report on your individual tasks. 2. Docker log file. https://drive.google. com/file/d/1W3gD9x8woaemahTQdtx- ovkg3z9yL/view?usp=dm.cok This provides the technical performance of your container. 3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our

image description: The image is a screenshot of a project repository on a platform like GitHub. It displays a list of files, their timestamps, and information about the repository.
image text:
main
Code
lakshay654 2 months ago
...
Dockerfile 2 months ago
LICENSE 2 months ago
README.md 2 months ago
app.py 2 months ago
requirements.txt 2 months ago
task\_handler.py 2 months ago
README
MIT license
TDS Project 1
LLM-based

---

Standard name of dockerfile is Dockerfile that’s why it didn’t pass Dockerfile check

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
I understand sir Dockerfile name was misspelt sir. Since my Docker image was built and recognized, I didn’t realize this would prevent evaluation.  
I worked hard on this project sir, and my Docker image was built successfully. Please consider my submission sir.

---

I have been trying to resolve all the errors but just noticed that my docker image id associated with the project is “c9dc7fbcf405” , meanwhile the mail I received mentions that some other image id was evaluated.  
Can you please look into this matter and evaluate the correct Image ID.  
Roll number: 23F1001012

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

[@Jivraj](/u/jivraj) [@Carlton](/u/carlton) I completely understand that changes to the Docker image after the deadline cannot be accepted.

***However, there are specific cases like mine where the Project 1 submission successfully passed the sanity checks on Feb 15 and received a decent score when the evaluation results were released on Mar 29.***

image description: The image is a list of 7 items, each describing a file related to a software evaluation or project. The text is structured as numbered points, providing file names, links, and short descriptions. The image also includes the ID of the docker image that was evaluated.
image text: available which is nearly 5 times faster than the fastest domestic internet.
1. Evaluation log file. https://drive.google.com/file/d/1GYe44D8gieDOlu9dCrKdsKwVAQ7i\_C-N/view?usp=drivesdk This contains your performance report on your individual tasks.
2. Docker log file. https://drive.google.com/file/d/1VTVeD-lwg3CFPFUYAcUqNzaGD7MlzyeC/view?usp=drivesdk This provides the technical performance of your container.
3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests.
4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism.
5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks.
6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will be required by your container to function and the port mappings for communications.
7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core concepts of LLMs to achieve the desired result.
This is the id of the docker image that was evaluated: 11aa22fc1545

But here’s the catch:\*\* Since the problem statement for Project 1 and Project 2 is nearly the same, I took the opportunity to improve upon my Project 1 and use it as the foundation for my Project 2 submission, which I did by:\*

* Implementing a ReAct-based workflow planning & orchestration agent, inspired by the paper [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629).
* Implementing various tools for web-serping, web-scraping, read-eval-print-loops interpreters for quick calculations, etc.
* Enhancing Shell-use & Python-use by improving upon the existing code interpreter I had implemented for P1. This allowed the agent to dynamically generate and execute code without hardcoding anything.
* Adding useful API endpoints, including an **`/api/`** multipart/form endpoint, alongside the existing **`/read`** and **`/run`** endpoints from Project 1, plus a **`/clear`** endpoint to reset the agent’s conversation memory if the context window gets saturated.
* **Deploying the entire project on a paid GCP VM Instance with a static IP**, utilizing my own OpenAI API key while keeping OpenAI’s API as a fallback in case AIPROXY ever gave up.

All this hard work evolved my project into something far beyond a simple Tool-Calling Agent—it essentially became a ReAct Principles based Computer-Using Agent capable of executing complex, non-linear workflows entirely within a container. And I’m not exaggerating: You could ask it to perform something like **hyperparameter tuning for a Random Forest Classifier, offloading the results locally on a JSON file and displaying its contents**, and it would do that for you—without **ever** declining the request. I like to think of it as a **terminal version of** [OpenAI’s Computer-Using Agent](https://openai.com/index/computer-using-agent/).

---

Given all the effort, time, and money that went into this, it’s incredibly discouraging to see my project **naturally fail a sanity check (Docker image digest mismatch) (because of the aforesaid updates)** and not get evaluated as a result. This is not the kind of experience that encourages students to learn, experiment, and innovate.

## To clarify, **all the updates mentioned above took place after March 29**, **after Project 1 had already been evaluated, and results had been handed out.** Furthermore, we were **never informed** that a reevaluation would take place on April 1. Had I known, I would have ensured that my original submission remained unchanged and considered creating a duplicate of my Docker image and implementing all the aforementioned enhancements on it.

My only request is that if my **updated P1 submission cannot be evaluated** due to the changes made after March 29 (before the P1 reevaluation on April 1), I would really appreciate it if my **original P1 eval score could be reinstated** instead of receiving a **0**—since it was already evaluated and graded.

Would highly appreciate your prompt support in this regard [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Here's a description of the image:
The image is a screenshot of a mobile device displaying an email or message regarding a project evaluation. The background is dark. The text is white.
image text: submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
Kind regards, TDS Team
  
Actually I got the email as my docker file is not in root git hub repository. But everything thing looks fine and my docker file also runs well.. I want to check my repo again ..sir kindly do my my evaluation again and we have put lot of efforts doing this project 1 . Hope the team evaluated and gives the deserved marks  
[@carlton](/u/carlton)  
@ TDS TEAM

---

There is no Dockerfile in the root directory of your GitHub repository. The standard naming convention for a Dockerfile is Dockerfile.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) please let know if any issues in my end on the docker image not present issue.. As explained in earlier thread , the only reason docker image had to be pushed was the removal my office proxies in the docker image which was making the container not to startup from orchestration environment.. any help is appreciated..

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) I updated google form 4 days ago on the architecture, Could you let me know when it will be re-evaluated ? Thanks

---

Hi [@thinkmachine](/u/thinkmachine) [@22f3002723](/u/22f3002723)

Since you updated docker repo few days ago and docker api doens’t support timestamp based pulling we will pull your GitHub repo before 18 th feb and will build through it and run evaluations.

We also have your docker repo evaluation score, will discuss which one to keep.

This is for anyone who updated their docker repo and there are around 10-20 such cases

---

Thanks for the understanding [@Jivraj](/u/jivraj)

---

Hi [@thinkmachine](/u/thinkmachine)  
As we said before that changes in Docker image after deadline won’t be accepted. Even an extension of the deadline won’t help in this case, simply because Docker API doesn’t support timestamp based pulling. However we would be pulling your GitHub repositories before 18th Feb build a Docker container and run evaluations on that.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) request your help in clarification for the same, the Github repo has been always present but it is marking it as fail. Thank you

---

A sigh of relief! Thank you so much for the heads up [@Jivraj](/u/jivraj).

[@Saransh\_Saini](/u/saransh_saini) Yup! The Docker issue is perfectly understandable. Even I checked my Hub repo, and I couldn’t seem to find an image having the pre-18th Feb digest. Had I been aware of this issue, and the fact that a re-eval would be carried out, I would’ve tagged the updated image differently. Hopefully, cases like mine will aid in resolving any issues in the future.

Once again, thank you both!

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

I am still uncertain as to why I received a second email regarding my project 1 score, indicating a failure due to unmet pre-requisites. I have inquired multiple times, yet I have not received a response. Meanwhile, several other posts, both before and after mine, have been addressed. Kindly clarify about that mail.

Thankyou

---

[@carlton](/u/carlton) Sir pls see my issue

---

I have the same issue. I also received a second mail stating I had failed due to some missing prerequisites though in the first mail my project evaluation had been carried out.

---

Hi [@lakshaygarg654](/u/lakshaygarg654)

Dont worry you passed pre-requsites. The script that was used earlier for basic checks used a stricter criteria, the newer one we wrote allowed for a looser check. You have scored very well in your latest run. 12 correct tasks.

We have not responded quickly because we are in the midst of finalising all the scores and doing normalisation etc, i.e operational work for Project 1 and 2.

We hope to have Project 2 scores out by this weekend.

Kind regards

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir can you also see the case of Dockerfile name. Many students have named it dockerfile , lower case ‘d’ character instead of upper case.  
Please sir see through it

---

Thanks [@carlton](/u/carlton) , for your response.

I was never worried about the result, whether it comes late or early. I know you will release it once everything is processed correctly. My concern was only about getting a response. Anyway, thanks for replying.

Also, today’s session has been canceled. I wanted to ask about the issue with editing responses in the Project 2 form. Is there any update on this?

---

Hi just wanted to know, there was no mail prior stating to keep the Dockerfile in the root folder of the repo (correct me if im wrong). Therefore i have put everything inside a folder - wont this be considered? Please clarify if possible.

Here's a description of the image:
The image is a screenshot of a GitHub repository. Key elements include:
\* \*\*Repository Name:\*\* `tds\_project1` with a "Public" tag.
\* \*\*Branch:\*\* "main" with 1 branch and 0 tags.
\* \*\*Commit Details:\*\* Information on the latest commit including ID, message "done" and last updated 2 months ago.
\* \*\*File Structure:\*\* Displays the contents of the repository: "tds-project-1", "LICENSE", and "README.md".
image text: `tds\_project1 Public main 1 Branch 0 Tags Pin Unwatch 1 Go to file t Add file Code A 21f1002409 done 4d2f5e5 · 2 months ago 14 Commits tds-project-1 done 2 months ago LICENSE Initial commit 2 months ago README.md readme changes 2 months ago README MIT license`

Here's a description of the image:
The image shows a file directory structure, likely from a code repository hosting platform. It displays a list of files and folders within a project named "tds\_project1 / tds-project-1/". The top of the image includes details about the project's latest commit, including the commit ID "21f1002409" and the message "done". The file directory shows the following entries: "app" folder, ".gitignore", "Dockerfile", and "README.md". Each entry also displays the last commit message as "done" and the last commit date as "2 months ago".
image text: tds\_project1 / tds-project-1/
21f1002409 done
Add file
4d2f5e5 • 2 months ago
History
Name
Last commit message
Last commit date
..
app
done
2 months ago
.gitignore
done
2 months ago
Dockerfile
done
2 months ago
README.md
done
2 months ago

---

image description : The image is a screenshot of a server error message on a black background. The error message indicates a HTTP 500 error. The error details mention "Task handling error" along with "Failed to get LLM response after 3 attempts." It also mentions "Your authentication token is not from a valid issuer" and some additional details about the error type and code.
image text: • HTTP 500 {
"details": "Task handling error: Failed to get
LLM response after 3 attempts: Error code: 401
{'error': {'message': 'Your authentication token
is not from a valid issuer.', 'type':
'invalid\_request\_error', 'param': None, 'code':
'invalid\_issuer'}}",
"error": "Internal server error"
}
  
Can anyone explain what errors of this sort mean?

---

You have to show which task triggered this error. Is it all of them or only one of them. Only then we can diagnose what the problem is.

---

image description: The image is a screenshot of a command-line interface output. It presents a series of operations and error messages related to a formatting task.
image text: Running task: Format `/data/format.md` with `prettier@3.4.2` in-place
HTTP Request: POST http://localhost:8365/run? task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 500 INTERNAL SERVER ERROR"
HTTP 500 {
"details": "Task handling error: Failed to get LLM response after 3 attempts: Error code: 401 - {'error': {'message': 'Your authentication token is not from a valid issuer.', 'type': 'invalid\_request\_error', 'param': None, 'code': 'invalid\_issuer'}}", "error": "Internal server error"
}
HTTP Request: GET http://localhost:8365/read? path=/data/format.md "HTTP/1.1 400 BAD REQUEST"
A2 failed: Cannot read /data/format.md
X A2 FAILED
  
Here it is with the task, however the error doesn’t seem to be related to the task itself based on the returned message in the JSON. It seems to be something wrong with the OpenAI API key. From the reading I did, it seems that the key was perhaps not set properly during evaluation? Not completely sure but please look into it.

---

Did all tasks produce the same error?

---

Yes except B1 somehow.

---

Hi [@AryanTikam](/u/aryantikam)

I looked at your github repo, You have used python’s `openai` module for doing project1, but AIPROXY\_TOKEN is supposed to be used through anand sir’s proxy.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Can you pls tell me my project 1 marks  
My evaluation.py had 2 score  
First one 1/20 where every task showed error second one had 10/20…

---

Dockerfile has to be insider root directory of github repo.

---

This was mistake from our end we rectified it and reevaluated your submission.  
Your submission has a good score.

---

[swati-iitm/project1\_final](https://github.com/swati-iitm/project1_final)

This is your github repo which doesn’t have a Dockerfile. That’s why It didn’t pass Prechecks

---

We have reevaluated it, we have scores avaliable for your submission.

---

Sir I understand you will be busy evaluating all the files and reevaluating them as well. I just wanted to know if its a confirm 0 for those who got evaluation log file MISSING and didnt get the other mail that many got in the past 2 days… Just to confirm… cause i think am getting 0 from that [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

So can anything be done about it now as it seems to pass more tasks without the proxy requirement? It is fine if not.

---

Please, can you put a screenshot of where it has been communicated, prior to the deadline.

---

We have communicated it in the live sessions. It was also communicated via an email when students failed first prerequisite check pass back in February 16th. At that time we gave students a time window to fix it.

We discussed it internally with [@s.anand](/u/s.anand) and he stated that it is standard industry practise to put Dockerfile in the root folder of a github and he expects students to do it **regardless of whether we explicitly mentioned it or not** on the project 1 page. The reason being, any Docker image being built from a github repo is never going to look for the file sitting inside a directory. All build requirements have to be at root (this is not just for Docker, but also any other type of application build). Since root is where the core files to build an application always reside, again this is standard industry practise.

In our meeting we advocated for a lenient approach to search for Dockerfile inside the github and it was vetoed by [@s.anand](/u/s.anand)

So unless you can give a convincing argument why we should change our evaluation script and re run it for everyone again, (because that is effectively what we would have to do to make it fair to everyone), we will not be able to evaluate your docker image.

Kind regards,  
TDS team

---

[@carlton](/u/carlton) Sir, I would like to respectfully ask if this is some sort of April Fool’s joke, as it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0 Score.

I am not the only one facing this issue; several others have encountered the same problem. I kindly request you to review my submission again.

Additionally, I have faced multiple technical issues in recent times. Initially, I was failed in the L1 viva due to a typing mistake, which was later acknowledged. Similarly, in both OPPE 1 and OPPE 2, many students experienced Google Meet issues. On March 29, during my SC OPPE, I faced camera issues in Google Meet, along with VM lagging. Many students have raised similar concerns with Proctor.

Given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

Here's a brief description of the image:
The image is a screenshot of an email with the subject "TDS Jan 25 Project 1 Scores". The email is from 22t1 se2002 and is addressed to a learner, providing feedback on their Project 1 submission. It lists prerequisites, includes pre-requisite evaluations (Docker image, GitHub repo, Dockerfile, MIT license), and indicates a "FAIL" status for the prerequisites.
image text:
TDS Jan 25 Project 1 Scores Inbox x
22t1 se2002
to me▾
Dear Learner,
Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL

---

image description: The image contains text regarding project prerequisites. There are evaluations of the project's components: docker image, github repo, dockerfile, and MIT license. The overall prerequisites failed, with a project score of 0.
image text: accessible and runs via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -
p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same
Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement
your submission will not get evaluated.
These are your Project 1 Prerequisite
evaluations:
Is Docker image present in dockerhub
AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github
repo: PASS
Is MIT license present at root of github
repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
Same for me sir, i had everything correct still its showing:- Is Docker image present in dockerhub

AND is public: FAIL

I have submitted everything correctly . Please carefully look into this and recheck the project submitted.

---

Sir,it appears that the TDS team is still only verifying the presence of files in the git repository and checking the accessibility of the repository. I fully understand the importance of marks and the effort we put into Project 1. That’s why I carefully ensured that all the necessary files and links were correctly uploaded yet I received a 0  
[@carlton](/u/carlton) Sir please look into this.

image description: The image is a screenshot with dark background and white text, likely showing the evaluation result of a project. It contains information about Docker image, Github repo, Dockerfile, and MIT license. The project prerequisites failed and the project score is 0.
image text: accessible and runs via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -
p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same
Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement
your submission will not get evaluated.
These are your Project 1 Prerequisite
evaluations:
Is Docker image present in dockerhub
AND is public: FAIL
Is Github repo present AND public: PASS
Is Dockerfile present in root of github
repo: PASS
Is MIT license present at root of github
repo: PASS
Prerequisites: FAIL
Project 1 Score: 0
  
[@carlton](/u/carlton) Sir, given this track record of technical problems, I strongly believe this could be another error in evaluation. I sincerely request you to re-evaluate my submission.

---

image description: The image is a screenshot of an email. The subject of the email is "TDS Jan 25 Project 1 Scores". The email is addressed to "Dear Learner". The body of the email includes a list of prerequisites for Project 1, with the prerequisites being "FAIL". It also mentions the project score is "0".
image text: TDS Jan 25 Project 1 Scores Inbox x 22t1 se2002 <se2002@study.iitm.ac.in> to me Dear Learner, Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page: 1. Your GitHub repository exists and is publicly accessible 2. Your GitHub repository has a LICENSE file with the MIT license 3. Your GitHub repository has a valid Dockerfile 4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME 5. Your Docker image uses the same Dockerfile as in your GitHub repository If you fail to meet this minimum requirement your submission will not get evaluated. These are your Project 1 Prerequisite evaluations: Is Docker image present in dockerhub AND is public: FAIL Is Github repo present AND public: FAIL Is Dockerfile present in root of github repo: FAIL Is MIT license present at root of github repo: FAIL Prerequisites: FAIL Project 1 Score: 0 Kind regards, TDS Team

[@carlton](/u/carlton) sir, i would like to ask why marks showing 0 infact i am submitting all my requirements things in that form so plz look into this matter.

---

[@carlton](/u/carlton) sir, similar thing happened to me as well, I had got the mail that git repo, dockerfile and lisence is not present or accessible while all the prerequisites are completed from my end. Can you please reevaluate my submission.  
image description: The image is a text-based document with a light pink background. It appears to be an evaluation report or checklist related to a project on GitHub.
image text: checks as detailed on the TDS Project 1:
Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0
--
Kind regards,
TDS Team
Note: Do NOT reply to this email. It is only meant for official announcements and messages. If you need any further assistance please contact the course team via Discourse.

---

Hi Prashant,

Your prerequisites have passed and your evaluation is 6 tasks have been completed successfully. The email was auto sent because we were doing some checks with an older, stricter script. The newer script passes your evaluation.

Kind regards

---

Thanks for the quick reply, i don’t have a convincing argument to counter. Just a suggestion it would have been better if you have explicitly put in the sanity check requirements. Something so obvious to you might not be so for others.  
if you are referring to this email even here, it was not explicit. Might have missed it in the gmeet. A mail would have been good.

Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of an email. The email is from "donot\_reply@study.iitm.ac.in" and is addressed to "25t1\_se2002-announce". The subject of the email is "[TDS Jan 2025] Important: Please check your submissions for basic sanity". The email body contains information about checking submissions for basic sanity, including checking for a public GitHub repo, an MIT license, a DockerFile, and Docker image accessibility. It also mentions that some submissions have issues and that learners should check their inboxes and spam folders. The email is signed "TDS team".
\*\*image text:\*\*
[TDS Jan 2025] Important: Please check your submissions for basic sanity inbox x
donot\_reply@study.iitm.ac.in
to 25t1\_se2002-announce
Dear Learners,
Before progressing to perform detailed evaluation, we check the repositories for the basic sanity checks given below:
- Is the GitHub repo public?
- Does it have an MIT license?
- Does it have a DockerFile?
- Is the Docker image accessible?
Sun, Feb 16, 8:18 PM
Out of the 530+ submissions, we see that only 284 submissions have cleared this basic sanity check. We have sent out emails to the 250+ learners on the errors that we
observed a little while back. Please do check your Inbox and SPAM folder to see if you have received an email from the course admin id (se2002) with the subject "[IMPORTANT]
Your Project 1 submission is on the risk of scoring 0 Marks". Please note that we have taken the last submission in the form for the validation.
We hope that you will take immediate action to check for sanity of your submission and correct the errors that have been reported.
Regards
TDS team

---

I agree with you. It should have been explicitly mentioned in the project page (even if we have mentioned it in live sessions)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Put some light on this poor soul’s message also ;')

---

my repo has both the dockerfile with correct name (Dockerfile and in the root folder), license and is public. Please look into this . [@carlton](/u/carlton) sir . [@Jivraj](/u/jivraj) [GitHub - veershah1231/tds\_proj\_1: Tds project](https://github.com/veershah1231/tds_proj_1) and i have made them 2 months ago and is not a new commit.  
Here's a description of the image:
image description: The image is a screenshot of an email. The email is from "22t1 se2002" and is addressed "to me". It discusses a project requiring prerequisites to pass. The email lists the requirements for Project 1 which involves GitHub repository and Docker image specifications and includes evaluation results. The recipient has failed prerequisites and got a score of 0.
image text: 22t1 se2002 1:27 am to me Dear Learner, Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page: 1. Your GitHub repository exists and is publicly accessible 2. Your GitHub repository has a LICENSE file with the MIT license 3. Your GitHub repository has a valid Dockerfile 4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME 5. Your Docker image uses the same Dockerfile as in your GitHub repository If you fail to meet this minimum requirement your submission will not get evaluated. These are your Project 1 Prerequisite evaluations: Is Docker image present in dockerhub AND is public: PASS Is Github repo present AND public: FAIL Is Dockerfile present in root of github repo: FAIL Is MIT license present at root of github repo: FAIL Prerequisites: FAIL Project 1 Score: 0

why is it saying i got 0? please look into it.

---

[@carlton](/u/carlton) [@jivraj](/u/jivraj) Sir I received a mail like everyone that my git-hub repository is not public and not MIT licensed. I even filled the g-form correctly while submitting.  
But I had fulfilled the above required criteria. Please look into this matter ASAP.  
Here is my git repo link : [[GitHub - 23f1001415/llm\_aa\_tds\_project](https://github.com/23f1001415/llm_aa_tds_project)]. (<https://github.com/23f1001415/llm_>  
image description: The image is a screenshot of a Gmail interface displaying an email from "22t1 se2002" regarding a project evaluation, with an assessment of certain requirements. The email is about "TDS Project 1".
image text:
M TDS Jan 25 Pro
23f1001415@
23f1001415@
(7) New Tab
Project 1
23f1001415/lln
Repositories
+
https://mail.google.com/mail/u/0/#search/tds/FMfcgzQZTzTShxptLjgTqRkplhdHvmpn
M Gmail
99+
Compose
Mail
Inbox
1,551
Chat
☆ Starred
Snoozed
Meet
Sent
Drafts
1
More
Labels
+
←
tds
Π
22t1 se2002 <se2002@study.iitm.ac.in>
to me
Dear Learner,
+
X
Active
IIT Madras
N
2 of many
<
>
31
Tue, Apr 1, 1:22 AM (2 days ago) ☆
:
Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs via podman run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in your GitHub repository
If you fail to meet this minimum requirement your submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0
Kind regards,
+
>
Search
ENG
IN
14:15
03-04-2025
  
Here's a description of the image:
The image is a screenshot of a GitHub repository page, specifically for a project named "llm\_aa\_tds\_project". The page displays various files and information about the project.
Key elements:
\* \*\*Repository Name:\*\* "llm\_aa\_tds\_project".
\* \*\*File List:\*\* The page shows a list of files, including \\_pycache\\_, data, .dockerignore, .env, Dockerfile, LICENSE, README.md, app.py, datagen.py, evaluate.py, tasksA.py, and tasksB.py.
\* \*\*Commit Information:\*\* Each file has an associated commit message, the time since the commit (e.g., 2 months ago), and a commit hash.
\* \*\*Project Overview:\*\* On the right side, there's an "About" section with no description, the project has a Readme, is MIT licensed, has 0 stars, 1 watching, and 0 forks.
\* \*\*Languages:\*\* Shows the languages used, Python (98.4%) and Dockerfile (1.6%).
\* \*\*Suggested workflows:\*\* There are suggestions based on the tech stack.
image text:
M TDS Jan 25 Pro X
23f1001415@c X
23f1001415@ X
(7) New Tab
X
Project 1
X
23f1001415/lln X
Repositories
X
+
X
https://github.com/23f1001415/llm\_aa\_tds\_project
llm\_aa\_tds\_project Public
main
1 Branch 0 Tags
Pin
Unwatch 1
Fork 0
☆Star 0
Q Go to file
t
Add file
<> Code
About
☆
23f1001415 Initial commit with Dockerfile and application code
50eacaf. 2 months ago 6 Commits
No description, website, or topics provided.
Readme
\_pycache\_
data
Initial commit with Dockerfile and application code
Initial commit with Dockerfile and application code
2 months ago
2 months ago
MIT license
Activity
✩0 stars
.dockerignore
Initial commit with Dockerfile and application code
2 months ago
1 watching
.env
Initial commit with Dockerfile and application code
2 months ago
0 forks
Dockerfile
Initial commit with Dockerfile and application code
2 months ago
Releases
LICENSE
Initial commit
2 months ago
No releases published
Create a new release
README.md
Initial commit
2 months ago
app.py
Create app.py
2 months ago
Packages
No packages published
datagen.py
Initial commit with Dockerfile and application code
2 months ago
Publish your first package
evaluate.py
Initial commit with Dockerfile and application code
2 months ago
Languages
tasksA.py
Create tasksA.py
2 months ago
tasksB.py
Initial commit with Dockerfile and application code
2 months ago
• Python 98.4% • Dockerfile 1.6%
README
বাব MIT license
Q Search
Suggested workflows
Based on your tech stack
\*
ENG
14:15
IN
03-04-2025
  
aa\_tds\_project).  
I have attached screenshots for your reference.

Thank you

---

[@Jivraj](/u/jivraj) I too had the same issue (image was run on wrong architecture) and filled the gform that was circulated. When should we expect to get our scores?

Thanks  
Pradeep Mondal

---

Hi [@21f2000709](/u/21f2000709)

We have used another approach because of architecture problem, by pulling through latest commit from github before 18th feb. Just checked we have results for you.

---

Hi [@23f1001415](/u/23f1001415)

This was a problem from our side and we rechecked and now we score against your submission.

---

Hi [@23f1001524](/u/23f1001524)

This was a problem from our end, we have recitified it your submission was valid.

---

Your latest score through pulling from github and building image thorugh dockerfile have higher score than these 2.

---

Hi [@23f2004563](/u/23f2004563)

I checked we have scores against your submission.

---

There was some problem with our script, later we correct and your submission was valid, I have just checked and confirm you.

---

Can u pls share marks :') dying with curiosity

---

image description: The image is a table displaying data, likely related to a software project, repository or similar. The table has four columns: "Timestamp", "Email Address", "What is the link to your GitHub repository which has the code for Project 1?" and "What is the name of the image published on DockerHub?". The table contains one row of data.
image text:
Preview Code Blame 1069 lines (1069 loc) • 127 KB
Q 23f1000057@ds.study.iitm.ac.in
1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub?
669 2/16/2025 20:39:53 23f1000057@ds.study.iitm.ac.in https://github.com/Vedant22042004/project vedant22042004/project

This was your submission and we could not locate a docker repo against it.

image description: The image shows a "404 Oops!" error page on Docker Hub. A large blue circle dominates the center, displaying the numbers "404" in bold, followed by "Oops!" and a message stating "The page you have requested was not found." Above, the Docker Hub interface is visible, and the URL indicates the page was attempting to reach a project within the "vedant2204" repository.
image text: dockerhub
https://hub.docker.com/r/vedant2204/project/tags
Explore
My Hub
Explore / vedant2204 / project
Search Docker Hub
404
Oops!
The page you have requested was not found

---

Your submission was valid there was some issues with our script for checking. But after building your image after pulling github repo, it didn’t one `taskA` module was missing.

---

If you used openai’s python module then you were needed to pass your own api key, hardcode it in code.

API key that we were sending was only valid through proxy server created by professor anand.

---

mail will be sent by either today or tomorrow.

---

any idea on this sir?..

---

No we pulled through github and build image on gcloud vm. Anyone with valid submission didn’t receive mail, your submission was valid.

---

but my evaluation log file was missing… so that would make it a 0 right..I have accepted my fate that it would be a 0 but just a lil hope ![:melting_face:](https://emoji.discourse-cdn.com/google/melting_face.png?v=14 ":melting_face:")

---

We reevaluated and found your submission was valid but it was running on a different port, 5000 but it was expected to run on 8000 port.

---

oh so… is it going to be considered? like will i get some score other than a 0… am sorry for asking so much

---

No it won’t be considered. It was supposed to be running on 8000 port.

---

Ok got it. Thank you so much ![:cry:](https://emoji.discourse-cdn.com/google/cry.png?v=14 ":cry:")

---

image description: The image is a webpage showcasing details about a Docker image named "zakiy7/my-fastapi-app". It provides information such as its author, update date, and available tags. The "Tags" tab is selected, showing details for the "latest" tag, including its digest, OS/ARCH, last pull date, and compressed size. A button is provided to copy the Docker pull command.
image text: Explore / zakiy7 / my-fastapi-app
zakiy7/my-fastapi-app
By zakiy7 • Updated about 1 month ago
IMAGE
0 26
Overview Tags
Sort by
Newest
Filter tags
TAG
• latest
Last pushed about 1 month by zakiy7
Digest
740fcf3f65bb
OS/ARCH
linux/amd64
Last pull
5 days
Manage Repository
docker pull zakiy7/my-fastapi-app:latest Copy
Compressed size
261.49 MB
  
Hi sir, my Architecture says amd64, in the google docs I have selected x86, i hope it is correct. Also, I have used podman to test the pull and its working well. Please let me know if i need to do anything else.

[@carlton](/u/carlton)

---

We are rebuilding all docker submissions from github commit before 18th of Feb, using your Dockerfile manifest present in the repo.

That way there is no architecture issues.

Its part of our secondary check. And more students have gotten scores in this check. So dont worry.

---

I just checked from my side also, wow a very dumb mistake now costing me a 0…should have read the project document more clearly ![:cry:](https://emoji.discourse-cdn.com/google/cry.png?v=14 ":cry:") So sorry for asking.

Am assuming no lenient correction can be done for that? like during the evaluation …

podman run --rm -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:5000 $IMAGE\_NAME

---

Here's a description of the image:
\*\*Image Description:\*\*
The image shows a GitHub repository for "llm-automation-agent". The repository's file structure is visible, including files like "README.md", "app.py", "requirements.txt", and various python files (e.g., "datagen.py", "evaluate.py"). It lists commits, file changes and their dates.
\*\*Image Text:\*\*
```
github.com/23f1002643/llm-automation-agent
My Dashboard TDS Java MLP SC TDS Rajasthan Books Difficulty Rating for... S 20 Best Account Ma...
main 1 Branch 0 Tags Go to file t Add file Code
23f1002643 Add files via upload c883879. 2 months ago 4 Commits
\_pycache\_ Add files via upload 2 months ago
Dockerfile Add files via upload 2 months ago
LICENSE Initial commit 2 months ago
README.md Initial commit 2 months ago
app.py Add files via upload 2 months ago
datagen.py Add files via upload 2 months ago
evaluate.py Add files via upload 2 months ago
requirements.txt Add files via upload 2 months ago
tasksA.py Add files via upload 2 months ago
tasksB.py Add files via upload 2 months ago
```
  
I checked it multiple times before submitting, I got 9/10 in task A.

---

No. Because someone else might have another minor issue they want to fix. We have to apply the rule uniformly.

---

Ok… I do have a doubt tho, i actually have app.py and main.py in my github, my main.py is running on 8000 and app.py on 5000 …

---

but in Dockerfile in your github repo you didn’t run main.py,

---

In your Dockerfile you didn’t copy taskA.py to the container.

---

Ouch, ok sir… hopefully project 2 doesnt disappoint ![:sob:](https://emoji.discourse-cdn.com/google/sob.png?v=14 ":sob:")

---

It is there in the master branch of the repository. Now, will the previous evaluation mail that we got be considered or this one?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I recently received an email with an evaluation file for Project 1, which included a score. However, in the recent email, I noticed that my score was recorded as zero, despite fulfilling all the prerequisites.  
I kindly request a re-evaluation of my project, as I believe this may be an error.

---

[@Jivraj](/u/jivraj)  
My discrepancy is still not fixed. Please take a look at it

---

[@Jivraj](/u/jivraj)  
Hlo, could you please check and let me know how much am I scoring in Project 1 after the latest evaluation?

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Sir,  
In the mail that i got about project 1 report. In the log file it was written as TasksA.py file not found in docker, which was the case i observed with many students.

image description: The image displays a terminal output with text related to building and installing packages. It also contains an error message at the end.
image text: Building antiorm==1.2.1
Building db==0.1.1
Building db-sqlite3==0.0.1
Downloading scipy (35.6MiB)
Downloading pandas (12.1MiB)
Downloading numpy (15.4MiB)
Downloading pydantic-core (1.9MiB)
Downloading duckdb (19.3MiB)
Downloaded pydantic-core
Built antiorm==1.2.1
Built db==0.1.1
Built db-sqlite3==0.0.1
Downloaded numpy
Downloaded duckdb
Downloaded pandas
Downloaded scipy
Installed 33 packages in 56ms
Traceback (most recent call last):
File "/app/app.py", line 22, in <module>
from tasksA import \*
ModuleNotFoundError: No module named 'tasksA'

This is my Github repo:

image description: The image is a screenshot of a GitHub repository page. The repository is named "tds-project1" and belongs to the user "GaURaVinDeX". The main section of the page displays the files and folders of the repository, including ".gitignore", "Dockerfile", "LICENSE", "app.py", "requirements.txt", "tasksA.py", and "tasksB.py." Each file has an "Initial commit" description and a timestamp of "2 months ago." The right side has information about the repository, including that there's "No description, website, or topics provided.", and has a MIT license. It also shows the languages used: Python (98.0%) and Dockerfile (2.0%). At the bottom, there's a prompt to "Add a README" to help people understand the project.
image text: GaURaVinDeX / tds-project1
tds-project1 Public
main 1 Branch 0 Tags
GaURaVinDeX Initial commit
\_pycache\_
.gitignore
Dockerfile
LICENSE
app.py
requirements.txt
tasksA.py
tasksB.py
README
MIT license
Initial commit
Initial commit
Initial commit
Initial commit
Initial commit
Initial commit
Initial commit
2 Commits
About
No description, website, or topics
provided.
MIT license
✩ 0 stars
1 watching
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
• Python 98.0% • Dockerfile 2.0%
Add a README
Help people interested in this repository understand your project by adding a README.
Add a README

I built the image using docker build command in vs code terminal. And pushed it same way to dockerhub using docker push command. How is it possible that the docker container missed the TasksA.py file while building or pushing it?

After getting this mail, I ran the project locally again mutliple times just to check if there was any issues in the code. It was getting 9/10 test cases passed.

---

This is a common mistake many, many students made. They created a working application but not a working container.

image description: The image is a screenshot of a Dockerfile in a GitHub repository. The file is part of the "tds-project1" repository, and the displayed part of the file is a series of instructions. The Dockerfile has been edited by "GaURaVinDeX" with an "Initial commit". The red arrow is pointing from line 16-20.
image text:
```
FROM python:3.12-slim-bookworm
# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn
# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"
# Set up the application directory
WORKDIR /app
# Copy application files
COPY app.py /app
# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]
```  
You only copied `app.py` into your docker image.

How do you expect your application to run without the other files that your repo clearly shows is needed?

Thats why many people are failing this. Hope the image makes this clear.

Kind regards

---

image description: The image is a screenshot of an email with evaluation results. The email recipient is addressed as Dear Learner, and details the project prerequisites including GitHub repository and Docker image requirements. The email includes a summary of prerequisite evaluations, indicating failures in meeting the MIT license requirement.
image text:
11:06
2
22t1 se2002 3 days ago
to me
LTE↓↑
24%
Dear Learner,
Project 1 requires you to pass some pre-requisite checks
as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly
accessible
2. Your GitHub repository has a LICENSE file with the
MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs
via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000
$IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in
your GitHub repository
If you fail to meet this minimum requirement your
submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is
public: PASS
Is Github repo present AND public: PASS
Is Dockerfile present in root of github repo: PASS
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0
Kind regards,
TDS Team
Note: Do NOT reply to this email. It is only meant for
official announcements and messages. If you need any
further assistance please contact the course team via
  
Here's a description of the image:
The image is a screenshot of a GitHub repository page, with a dark theme. The top of the screen displays the URL "github.com/00-Arya". The repository appears to be public. The main part of the screen lists files and folders within the repository, along with their timestamps, which are all "2 months ago". These include files such as "app.py", "evaluate.py", "requirements.txt", and others, and folders such as "data" and "\\_pycache\\_". Below the file list are the options "README" and "MIT license".
image text: 11:06 Vo)) 5G LTE 23% github.com/00-Arya + 7 0 stars 0 forks 1 watching 1 Branch 0 Tags Activity Public repository main Code 00-Aryan 2 months ago \_pycache\_ 2 months ago data 2 months ago .env 2 months ago Dockerfile 2 months ago LICENCE 2 months ago app.py 2 months ago datagen.py 2 months ago evaluate.py 2 months ago requirements.txt 2 months ago tasksA.py 2 months ago tasksB.py 2 months ago README MIT license
  
I am getting license not present at root of github repo but i have the license added could someone please explain why ?

---

[@thinkmachine](/u/thinkmachine)

Firstly, you have passed evaluation and got a decent score (on a more lenient script that we used for everyone.) The email was sent by a script that used a more stricter evaluation (which understandably caused some stress). So you can breathe a sigh of relief. ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14 ":slight_smile:")

*However* with regards to your long post…

Let me tell you a true story. I personally know a *very* experienced senior engineer at a top defense contractor for the US, here is some pearls of wisdom from him.

What you have done is what is called in industry as **gold plating**. Its a cardinal sin in software engineering. NEVER gold plate. ALWAYS build to spec.

In fact its a good reason to fire an engineer. Why?

1. Because it does not deliver what was required,
2. Wastes valuable time and resources
3. Increases technical debt (this is actually a huge cost over the expected lifetime of the project!)
4. Complicates testing
5. Leads to scope creep

His advice to me was simple: NEVER gold plate.

I hope you take this pearl of wisdom in your career. It will help you advance and make you stand out.

For personal hobbies this does not apply. But for a client (including us) if you fail to deliver the minimum spec then we cannot grant you an evaluation (by the way this post is not targetted specifically for you, it just felt like an appropriate place to explain this).

Kindest regards

---

Hi Sir,  
I just realized that I mistakenly submitted the image tag “abhay227/version1” instead of the correct image ID. The correct image ID is **4db729a03f74** , which is part of version1 that is already present and publicly available.  
I have worked very hard on this project, and I am concerned that due to this error, my whole effort may be wasted. Unfortunately, I did not receive any notification regarding an invalid submission after I submitted the Project1 form, and I only recently became aware of this mistake. I kindly request you please consider this correct image ID.

Thank you for your understanding and assistance. I look forward to your positive response.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Here's a description of the image:
The image shows information related to a docker image version. It displays the tag as "version1", pushed about a month ago by "abhay227". It also includes the digest, OS/ARCH as "linux/amd64", and the last pull time. Additionally, there's a command to pull the docker image and the compressed size.
image text:
TAG
• version1
Last pushed about 1 month by abhay227
Digest
4db729a03f74
OS/ARCH
Last pull
linux/amd64
about 1 month
docker pull abhay227/tds\_project:version1 Copy
Compressed size
261.98 MB

---

Hi Abhay,

This was a basic error. Unfortunately for basic errors we are not able to relax the requirements. All students were given a clear directive on what the minimum requirements were in order to be evaluated. Failure to follow those clear instructions prevents us from making any exceptions, because then we just have to dump all those requirements for all students and that would not be fair to those that took the care to be careful about their submissions.

Kind regards

---

Hi sir, hope you are doing well.  
Could you please check and let me know if I have passed the project 1 and if yes then how much am I scoring in Project 1 after the latest evaluation?  
[@carlton](/u/carlton)

---

Thanks for the clarification regarding the evaluation, [@carlton](/u/carlton). It’s a relief to know that my original submission was successfully evaluated. Had I known that the stricter evaluation script would pull the image matching the digest from the time of submission (which had been overwritten by April 1), I would’ve used a separate tag to avoid the issue altogether.

Regarding your point on gold plating — I completely understand and have come to appreciate the importance of building to spec from personal experience, especially in production or client-facing settings where fixed targets, maintainability, and minimal scope creep are key. That said, with TDS projects, my goal was purely exploratory — to explore the boundaries of what’s possible **within the scope of the problem statement**.

What began as just another (pun intended) *tedious* assignment slowly evolved into a hobbyist research project on LLM agents. ![:grinning_face_with_smiling_eyes:](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14 ":grinning_face_with_smiling_eyes:")

*(…caution: long post ahead ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14 ":sweat_smile:"))*

I noticed that **test cases in Project 1 and 2 were highly specific and often overlapping on Python & Shell use**. While it would’ve been easy to hardcode 50+ Python functions to pass these cases (which, frankly, many of us were doing), it is non-scalable at best. I quickly realized that stochastic parrots + hardcoded functions were a recipe for disaster, especially considering the **inherent randomness in LLM-generated payloads**. No two payloads are exactly alike — even minor differences, like an absolute vs relative file path, or some hidden edge case could cause a hardcoded solution to fail unpredictably. There’s also really no way to predict an edge case caused by an LLM.

Some might suggest using `temperature=0` to get more deterministic LLM behavior — and while true to an extent, it does little to encourage exploration, especially in tasks that require self-correction based on environmental feedback. Prompt engineering too wouldn’t be helpful here as 4o-mini isn’t all that great at 0-shot instruction following, especially when the system prompt is already saturated with 50+ fine-grained instructions. There’s only so much stuff it can pay attention to.

**Hardcoded tool agents also aren’t really “agents” in my view— they’re more like passive AI powered regex matchers**: merely mapping inputs to functions by inferring from context window. That puts all the burden of answering on the hardcoded functions, leaving the agent itself uninvolved in the solutioning process. If they break, the agent will never try to ‘fix’ them and keep calling them like a broken record.

At the core of it, it’s all about **how much flexibility vs rigidity** we give to the agent. Fully rigid solutions (e.g. hardcoding) overfit and break easily; fully flexible ones (e.g. pure LLM based) hallucinate or drift off-target. The sweet spot lies somewhere in between — The right solution would naturally balance the lesser of two evils in an ideal ratio.

Since most LLMs already excel at code generation and structured solutioning, the most effective strategy that I figured out for the agent was to,

* Reason about the task, understand intent,
* Reflect, whether this problem is solvable using available tools without human intervention and design structured workflows, in whatever order appropriate (i.e. *design* a DAG, where each node can be a python step or a shell step or something else)
* Execute those workflows (*walk* the DAG) observing the feedback at each step and reiterating if needed.
* Observe the final result, and repeat if needed.

Interestingly, a similar framework was suggested in [this ICLR 2022 paper](https://arxiv.org/abs/2210.03629). That was all the validation I needed to know I was stepping in the right direction.

To make environment interaction possible, the agent didn’t need dozens of narrow tools — just a small, well-defined set of **general-purpose tools**:

* A REPL executor (for quick calcs)
* A Python script runner
* A Shell executor

With just these, it could handle most tasks flexibly and naturally — avoiding overengineering while still enabling powerful behaviors. Potentially allowing for full fledged Computer-Use via shell and so much more.

As for the fact that it ended up being capable of things beyond the scope of Project 1 (like training & tuning ML models autonomously, reporting results etc.) — that was **emergent behavior**, not deliberate gold plating. It was a pleasant surprise even to me. I’ve yet to discover more of such interesting hidden use cases. While some might naturally call it scope creeping (and yes that is true, given that we had a deadline, and a play-pretend client-business relationship with the course team), I saw it as an opportunity for exploration and research. *Frankly, I AM personally very keen about researching stuff!*

I am actually very thankful to the TDS course team & [@s.anand](/u/s.anand) for devising such a thoughtful project that sparked some interesting ideas that I can tinker with. **Food for thought! Really!**

As for my next project, I now have a fair idea of what I’ll be experimenting with— modalities.

PS: I’m not claiming it’s perfect or production-ready, or it should score a perfect 22/20, but it aligned well with what I believe was the spirit of these projects: **thoughtful use of LLMs in agent design**. At this point, I’m less concerned about the marks, I’m actually enjoying the thought joyride. ![:grinning_face_with_smiling_eyes:](https://emoji.discourse-cdn.com/google/grinning_face_with_smiling_eyes.png?v=14 ":grinning_face_with_smiling_eyes:")

---

**TL;DR**  
My approach doesn’t rely on regex or hardcoded mappings. Instead, it passes user input directly to an LLM, which then plans and executes workflows using general tools inside a containerized environment. It also learns from feedback and iterates — much like a human. The fact that it can do more than just the minimum spec is a byproduct of that framework. I’ve only just wired the pieces together.

Kind regards

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Sir please Consider this request!

---

Hello Sir,

Here's a description of the image:
\*\*Image description:\*\*
The image appears to be a screenshot of an email displayed on a mobile device. The content discusses prerequisites for a project submission.
\*\*Key elements:\*\*
\* Email subject: Likely related to a project assessment or feedback.
\* Evaluation criteria: It lists several criteria for project evaluation (Docker image, GitHub repository, Dockerfile, MIT license).
\* Results: It shows "FAIL" for the GitHub repo, Dockerfile, and MIT license criteria.
\* Score: Indicates a project score of "0".
\* Sender/Organization: TDS Team.
\* Message: It provides important instructions and contact information.
\* Mobile Interface: The screenshot includes mobile UI elements (time, battery, reply buttons).
image text:
6:51 PM
accessible
2. Your GitHub repository has a LICENSE file with the
MIT license
3. Your GitHub repository has a valid Dockerfile
4. Your Docker image is publicly accessible and runs
via podman run -e
AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000
$IMAGE\_NAME
5. Your Docker image uses the same Dockerfile as in
your GitHub repository
If you fail to meet this minimum requirement your
submission will not get evaluated.
These are your Project 1 Prerequisite evaluations:
Is Docker image present in dockerhub AND is
public: PASS
Is Github repo present AND public: FAIL
Is Dockerfile present in root of github repo: FAIL
Is MIT license present at root of github repo: FAIL
Prerequisites: FAIL
Project 1 Score: 0
Kind regards,
TDS Team
Note: Do NOT reply to this email. It is only meant for
official announcements and messages. If you need any
further assistance please contact the course team via
Discourse.
Unsubscribe
Reply
Reply all
Forward
99+
5

I got this mail regarding my project 1 scores. My github repo is present and public as well as MIT License and Dockerfile is also present at the root of the repo

[github.com](https://github.com/SrishtySnehi/Project_1_tds)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/9/f93c7a8f75b0e5f3c99be032499e49464d57c7a2_2_690x344.png)

### [GitHub - SrishtySnehi/Project\_1\_tds](https://github.com/SrishtySnehi/Project_1_tds)

Contribute to SrishtySnehi/Project\_1\_tds development by creating an account on GitHub.

---

Hi [@Srishty\_Snehi](/u/srishty_snehi)

Your submission is valid, we but it failed while running server, with this error.

taskA module missing

For regenerating this error:

1. Pull github repo(latest commit before 18th Feb)
2. Build image using Dockerfile of fetched repo
3. Run that image.

---

We are not considering Dockerfile’s with wrong name(anything other than Dockerfile), and wrong location(anything other than root) in github repo.

---

Will I still get a zero?

---

Can we expect the results for project 1 and 2 by tomorrow? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

when can we expect our project 1 result?  
[@Jivraj](/u/jivraj)

---

I got my result!! 2/20 so happy its not a 0 thank you for the bonus [@carlton](/u/carlton) [@Jivraj](/u/jivraj) ![:sob:](https://emoji.discourse-cdn.com/google/sob.png?v=14 ":sob:")

Also really great how yall have given the error logs for everyone individually ![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14 ":saluting_face:")

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) in earlier evaluation of P1 in that my B1 is passed but in this final scores email it is showing as 0 for B1 pls help  
![finalB1](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/4/04980bbcf7941e08ba08f59e10a384708518a9eb.png)  
image description: The image shows a log of actions. There is a green checkmark and "B1 PASSED". Below, there is an orange circle and "Running task: Delete /data/format.md". The next line is "HTTP Request: POST http://localhost:8325/run?task=Delete+%2Fdata%2Fformat.md "HTTP/1.1 200 OK"". image text: B1 PASSED
Running task: Delete /data/format.md
HTTP Request: POST http://localhost:8325/run?task=Delete+%2Fdata%2Fformat.md "HTTP/1.1 200 OK"

---

Request for Clarification on Zero Marks Given – Repository Was Public with All Required Files

Dear [@Carlton](/u/carlton) sir  
I wanted to kindly request a clarification regarding the evaluation of my project submission. I noticed that I have been awarded zero marks, and I’m a bit confused because I had made sure that everything was in place.

* My GitHub repository was **public** at the time of submission.
* I had included the **Dockerfile** as required.
* I also added the **MIT License** to the project.
* For your reference, I am also attaching a **snapshot** of the repository as it was during the submission time.

Given all these were in place, I would really appreciate it if you could provide a **concrete reason** for giving **zero marks**. I’m eager to understand what went wrong so I can avoid it in the future and improve myself. But u saying in email that my repo was not public , not having dockerfile and not having mit licsence .  
Here's a description of the image:
The image shows a Gmail interface, displaying an email about task scores and grading criteria. The email includes information about the total score, bonus, and how the final score is calculated. It also provides links to submitted repositories and details on pre-requisite checks, followed by a table with scores for different tasks.
image text:
You will get 1 mark for each task completed. A1-A10, B1-B10, C1-C5
C1-C5 are bonus tasks
Your total score is out of 20.
We normalise your task scores to 20 based on the highest score in Project 1 which is 16.
Therefore each task you successfully completed gives you 1.25
Bonus is awarded for number of commits and repo size after removing all cache related and environment files. We do a power transform and scaling with weights of 2.5 for each of these features (so that outliers do not influence the scores)
Your final t score calculation is based on
MIN (20, (task score + bonus))
Github repo submitted: https://github.com/harrypandey829/tds\_llm\_automation-agent
Docker repo submitted: hariompandey6388/ll-automation-agent2
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 0
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 0
Gihub repo check - Dockerfile exists: 0
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
0 0 0 0 0 0 0 0 0 0
B1 B2 B3 B4 B5 B6 B7 B8 B9 B10
0 0 0 0 0 0 0 0 0 0
C1 C2 C3 C4 C5
  
Here's a brief description of the image:
The image is a screenshot of a GitHub repository named "tds\_llm\_automation-agent" owned by "harrypandey829". It displays the repository's files and information.
image text:
```
X
github.com/harrypandey829/tds\_llm\_automation-agent-
harrypandey829 / tds\_llm\_automation-agent-
Code Issues Pull requests Actions Projects Wiki Security Insights Settings
tds\_llm\_automation-agent- Public
main Branches Tags
Q Type to search
☆
+
▼
Pin Fork 0
☆Star 0
H
Add file <> Code
About
This is my final effort towards tds project.
\_pycache\_
.env
LICENSE
app.py
datagen.py
dockerfile
evaluate.py
tasksA.py
tasksB.py
3 Commits
MIT license
Activity
✩0 stars
1 watching
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Languages
Relaunch to update:
README MIT license
Duthon 100.0%
```
  
please just check my repo manually and clarify whether it was public or not . What is going on this degree .

---

And also i ran the evaluate.py and got the 10/10 during submission , atleast you can give 4-5 by which i can pass this course .

---

Hi sir  
I noticed a discrepancy in my Project 1 results. In the initial results shared on March 29th, I had received 8/20 based on the evaluation logs. However, the final result I received today states that none of the tasks in Task A and B were working, and I was awarded only 1 bonus mark.

During my own testing, I was consistently getting 7/10 correct in Task A, so I’m a bit confused about the change.  
Kindly request you to look into this discrepancy sir  
Thank you

---

Dear [@carlton](/u/carlton) Sir,

I was getting 8 marks in your evaluation but today I checked the mail, I was awarded 0 marks. I am not sure what happened. Everything was in place. I would really appreciate if you can provide a reason for zero marks. I rechecked everything and looks good. Awaiting your reply. Thanks.

image description: The image is a screenshot showing the results of a process, likely a software test or a system status report. It highlights a failed test result, a score, and an HTTP request.
image text:
BIO FAILED
Score: 8 / 20
HTTP Request: POST https://aipro...

---

same i also got 8 marks but today in mail i got 0 marks

---

Same issue for me, I was getting 10/20 earlier and now, in mail it shows 1.

---

Same issue for me, i had got 4/20 before but in the mail, my marks is given as 0. Please help

---

Respected sir,  
I have passed all pre-requisites however my file wasn’t evaluated due to port error (127.0.0.1). Please allow me rectify it as it everything else has passed and is in accordance to the guidelines and I had worked really hard for it not to be evaluated only.

---

Dear [@carlton](/u/carlton) Sir,  
I’ve noticed discrepancies in my Project 1 results. During the tests I ran before submitting, I consistently got about 7/10 in Task A. In the results shared earlier, I was informed that my evaluation log file was missing. Later, a Gform regarding the architecture was sent, which I filled and submitted. Now, the final result I received today, shows that the taskA module is missing and I’ve been given a bonus of 1 mark.  
I kindly request you to look into the matter and provide an explanation and solution in this regard.  
Thank you.

---

Respected Sir,

I hope you’re all doing well. I’m writing regarding my Project 1 evaluation, as I’ve encountered a discrepancy that I’d like some help with.

According to the evaluation email I received, my score was 0 for all the tasks with an additional bonus of 1 (totaling a P1 score of 1). However, when I ran the provided evaluation script before my submission, I got 7 in Phase A. Additionally, after reviewing the Docker logs, evaluation logs, and the p1\_evaluation\_error\_logs (from the linked Google Sheets), I couldn’t find any reference to my roll number.

Could someone please help me investigate this issue? I’d really appreciate any guidance from the evaluation team.

Thank you for your time and assistance!

---

[@carlton](/u/carlton) i am sure i had cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found my be but still i have been alloted 0 in all the cases , this is no small issue as project holds a significant amount of weightage in the end term  
I had spent hours finishing my project and this i am sure my marks are not on par with the desired work i did  
Look into this matter as it signifies if i will be able yo pass tds in this term or not.

---

I am facing the exact same issue

---

Hi Hari,

I just *manually* checked your repo.

image description: The image is a 404 error page, showing a web browser window with a github link in the address bar. The background is a desert scene with blue sky. In the center is the number "404" in large white font, and below that a text bubble with the message "This is not the web page you are looking for." To the right is the Github mascot in a robe.
image text:
https://github.com/harrypandey829/tds\_llm\_automation-agent|
404
This is not the
web page you
are looking for.

This is what *you* submitted:

2/15/2025 21:08:32  
21f3002112@ds.study.iitm.ac.in  
<https://github.com/harrypandey829/tds_llm_automation-agent>  
hariompandey6388/ll-automation-agent2  
Kind regards

---

[@carlton](/u/carlton) sir When I submitted project 1, I was passing part A with 8/10 marks but today it is showing 0 marks on my email, but when I run it just now it is showing 4/10 on my vs code.  
Whereas when I download the file from GitHub and run it, it is showing 1/10 now.

Here's a description of the image:
\*\*Overall:\*\* The image is a screenshot of a Visual Studio Code (VS Code) window, displaying code, file explorer, and terminal output related to a Python project. The interface shows a dark theme with a focus on code editing and debugging.
\*\*Key Elements:\*\*
\* \*\*File Explorer:\*\* On the left, the file explorer shows project files, including "app.py", "datagen.py", "evaluate.py", "tasksA.py", and "tasksB.py", alongside other folders like "data" and ".env".
\* \*\*Code Editor:\*\* The right side of the screen features a code editor window, with "app.py" open. The code includes Python syntax, comments, and imports of various libraries like "requests", "fastapi", "uvicorn", "python-dateutil" and "pandas".
\* \*\*Terminal:\*\* Below the code editor is a terminal window. The terminal displays the output of a process, including HTTP requests and responses. It shows "HTTP 200" messages and indicates task completion.
\* \*\*Output & Errors:\*\* There is a section displaying the expected and actual results of a task which is different, indicating that a particular task has failed.
\*\*Image Text:\*\*
\* The text consists of Python code with comments describing dependencies.
\* Terminal output displaying HTTP requests and the "A10 FAILED" status.
\* File names and directory structure from the file explorer are visible.
  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a laptop screen displaying code and terminal output within a coding environment, likely Visual Studio Code. The code appears to be related to data processing or a web application.
\*\*Key Elements:\*\*
\* \*\*Code Editor:\*\* The left side of the screen shows a file explorer with files like "app.py", "evaluate.py", and "tasksA.py". The active file, "app.py", is open in the code editor.
\* \*\*Code Snippet:\*\* The main part of the screen showcases Python code. It includes import statements, comments, and potentially function definitions.
\* \*\*Terminal Output:\*\* The lower part of the screen displays terminal output, showing the results of running the code. It seems to contain HTTP requests and responses, possibly testing a web service.
\* \*\*Error and Status:\*\* The terminal output reveals "A10 FAILED", indicating a failed test case. A score of "4 / 10" is also present.
\* \*\*Laptop Interface:\*\* A keyboard, laptop edge and user interface elements can be seen, like the date and time, and various app icons.
\*\*Image Text:\*\*
```text
EXPLORER
app.py 1 X
evaluate.py
tasksA.py 3
tasksB.py
dockerfile
\*.env
datagen.py
▷
> OPEN EDITORS
app.py >...
TDS\_P...CE
16
#]
17
# ///
>\_pycache\_
18
> data
19
3
\*.env
from fastapi import FastAPI, HTTPException, Query
20
app.py
1
21
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
datagen.py
22
from tasksa import \*
dockerfile
23
from tasksB import \*
1
evaluate.py
PROBLEMS
OUTPUT DEBUG CONSOLE TERMINAL
PORTS COMMENTS
LICENSE
pwsh+
the+items+in+the+%22Gold%22+ticket+type%3F+Write+the+number+in+%60%2Fdata%2Fticket-sales-gold.txt%60 "ΗΤΤΡ/1.1 200 OK"
tasksA.py
3
tasksB.py
HTTP 200 {
A
"message": "A10 Task 'The SQLite database file `/data/ticket-sales.db has a tickets with columns 'type', 'units, and `price`. E
ach row is a customer bid for a concert ticket. What is the total sales of all the items in the \"Gold\" ticket type? Write the numbe
rin`/data/ticket-sales-gold.txt' executed successfully"
}
HTTP Request: GET http://localhost:8000/read?path=/data/ticket-sales-gold.txt "HTTP/1.1 200 ок"
/data/ticket-sales-gold.txt
EXPECTED:
177250.79
ARESULT:
200401.84
> OUTLINE
> TIMELINE
main044
X A10 FAILED
Score: 4/10
OPS C:\Users\avina\Desktop\TDS\_Project3>
I
Avinash Kumar (1 month ago) Ln 23, Col 21 Spaces: 4 UTF-8 CRLF () Python 3.13.1 64-bit Go Live Tabnine: Sign-in is required Prettier
Q Search
L
hp
fo
5
\*
40
41
4+
1
@
2
#
$
%
^
&
3
4
5
6
7
Q
W
E
R
T
Y
U
144
\*
mvhp
ho
Dll
661
)
8
9
4
+
=
brt sc
{
}
P
L
→
17:18
06-04-2025
backspace
A
delete
```

---

To replicate the test environment:

Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can run this code using uv.

```
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import datetime as dt
import zoneinfo
import argparse
import os
import zipfile

parser = argparse.ArgumentParser (description="Fetch the latest commit before a given deadline.")
parser.add_argument (
    "--owner",
    type=str,
    required=True,
    help="GitHub username."
)
parser.add_argument (
    "--repo",
    type=str,
    required=True,
    help="GitHub repository name."
)
parser.add_argument (
    "--save",
    type=str,
    default="../github/",
    help="Path to save the zip file. Default='../github/'"
)
parser.add_argument (
    "--extract",
    type=str,
    default="../github/",
    help="Path to extract the zip file. Default='../github/'"
)

args = parser.parse_args ()
owner = args.owner
repo = args.repo
save_path = args.save
extract_path = args.extract

deadline = dt.datetime (2025, 2, 18, tzinfo=zoneinfo.ZoneInfo("Asia/Kolkata"))
deadline_str = deadline.isoformat ()

github_headers = {
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "fetch_git_before",
}

url = f"https://api.github.com/repos/{owner}/{repo}/commits?until={deadline_str}&per_page=1&page=1"

try:
    response = requests.get (url, headers=github_headers, timeout=60)
    response.raise_for_status ()  # Raise an error for bad responses

# Get the sha
    commits = response.json ()
    if commits:
        latest_sha = commits[0]["sha"]
        print (f"Latest commit before {deadline_str}: {latest_sha}")

# Get the zip of the commit
        zip_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{latest_sha}"
        zip_response = requests.get (zip_url, headers=github_headers, timeout=60)
        zip_response.raise_for_status ()
        zip_filename = f"{latest_sha}.zip"

# Create the directory if it doesn't exist
        os.makedirs (save_path, exist_ok=True)

with open (save_path + zip_filename, "wb") as f:
            f.write (zip_response.content)
        print (f"Downloaded zip file: {zip_filename}")

# Create the directory if it doesn't exist
        os.makedirs (extract_path, exist_ok=True)

# Extract the zip file
        with zipfile.ZipFile (extract_path + zip_filename, "r") as zip_ref:
            zip_ref.extractall (extract_path)
        print (f"Extracted zip file to: {extract_path}")

else:
        print (f"No commits found before {deadline_str}")

except:
    print(f"Error fetching commits: {response.status_code} - {response.text}")

```

Pass the required arguments to the above application and it will find the latest commit before the 18th, fetch it and unzip it to the folder you specified. Please use the appropriate arguments as specified in the application.

`docker build -t <your image name> .`

Run new docker image using  
`docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 <your image name>`

Keep datagen.py and evaluate.py in same folder  
`uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000`

This then re-produces the exact environment how your application was tested.  
You have to provide a token from your environment for testing.

These instructions are same for everyone. So check first before posting here.

---

I am also facing same issue cleared 8/10 test cases in part A of the project despite rigrous checking and no error was found but still i have been alloted 0 in all the cases

---

[@Arunvembu](/u/arunvembu) [@22f2000008](/u/22f2000008) [@23f1000879](/u/23f1000879) [@22f3003201](/u/22f3003201) [@23f2000926](/u/23f2000926) [@22f3001702](/u/22f3001702) [@Santoshsharma](/u/santoshsharma) [@kartikay1](/u/kartikay1) [@Kasif](/u/kasif)

Check first by following the instructions show here:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> git clone <your repo url>
> cd <your repo directory>
> docker build -t <your image name>
> Run new docker image using
> docker run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -P 8000:8000 <your image name>
> Keep datagen.py and evaluate.py in same folder
> uv run evaluate.py --email=<any email> --token\_counter 1 --external\_port 8000
> This then re-produces the exact environment how your application was tested.
> You have to provide a token from your environment for testing.
> The…

Then post with your queries after testing as mentioned above.  
Also check the evaluation logs first to see why it failed. Address that question.  
Posting “it ran before submission” is insufficient evidence.  
The whole point of deployability is that it runs anywhere at anytime.  
That is what is being tested, not that it ran on your machine (unless you replicate the test environment exactly).

Kind regards

---

But in email u said n , your repo was not public, even not had dockerfile nor mit licence that’s what I mentioned.

---

Your repo is not public! Thats why we cannot see any other files either. If its not public we cannot see if other files exist. We cannot evaluate an invisible repo.

---

I got email , your repo was not public even had not a dockerfile nor mit licence, that’ what I mentioned.

---

My repo is public even before it was. How can I set to public..thisis same n while creating new repo u just select the public and not private that’s it n.

---

What else I can do . For public.

---

You misspelt your repo. Did you even check the post i sent with your details?

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/314) [Tools in Data Science](/c/courses/tds-kb/34)

> Hi Hari,
> I just manually checked your repo.
> [[Screenshot 2025-04-06 at 5.32.06 pm]](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/8/28d462abf3d71240022c11eaaef8ef9dd8c62559.jpeg "Screenshot 2025-04-06 at 5.32.06 pm")
> This is what you submitted:
> 2/15/2025 21:08:32
> 21f3002112@ds.study.iitm.ac.in
> <https://github.com/harrypandey829/tds_llm_automation-agent>
> hariompandey6388/ll-automation-agent2
> Kind regards

---

Dear [@Jivraj](/u/jivraj) [@carlton](/u/carlton) Sir,  
I run evalution script that you provide us via mail recently, my code is actively running and able to pass 11 task but I was awarded 1 Marks pls check where is the issue,[My full code was done in linux Environment] (github codespace)  
image description: The image is a screenshot of a terminal window, likely showing the output of a Python program. The text indicates HTTP requests and their responses, along with some error messages. A prompt appears asking to install the 'Python' extension.
image text: HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 404 NOT FOUND"
• C5 failed: Cannot read /data/c5.txt
X C5 FAILED
Score: 11 / 25
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
@singh-yash129 →/workspaces/Large-Language-Model (main) $
Do you want to install the recommended 'Python' extension
from Microsoft for the Python language?
Install Show Recommendations
Ln 61, Col 4 Spaces: 4 UTF-8 LF {} Python Chat limit reached

---

You have to replicate this test environment for testing.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> git clone <your repo url>
> cd <your repo directory>
> docker build -t <your image name>
> Run new docker image using
> docker run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -P 8000:8000 <your image name>
> Keep datagen.py and evaluate.py in same folder
> uv run evaluate.py --email=<any email> --token\_counter 1 --external\_port 8000
> This then re-produces the exact environment how your application was tested.
> You have to provide a token from your environment for testing.
> The…

Please replicate this first. We also run it on a linux server.

Kind regards

---

I am not talking about this , just see the snapshot that I applied above on that email u said your repo is not public

---

We are ONLY going to evaluate what you submitted. Its the same rule for everyone. If the repo you provided is not accessible, you will not be evaluated.

---

Okay tell me one thing if I got fail in this course then in the next term, I will have not to give roe because it’s rule for every other courses.And see provide the content of tds in Indian guy youtuber because we belong to rural areas and not able to understand the accent of foreigners youtuber . It’s kind your sympathy.

---

**Things i have done for my project to work locally:**

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> `git clone <your repo url>`

cloned my repo which looked like this after cloning(ignore those green dots)  
Here's a description of the image:
The image shows a file directory structure. The root folder is named "TDS\_PROJECT\_1", with a subfolder "tds-project-1" and a file labeled "LICENSE" with a key icon. There are a few icons in the top right corner, likely for file operations.
image text:
TDS\_PROJECT\_1
tds-project-1
LICENSE

All the files are in this folder (I wasn’t aware that we cannot have the subfolder in the root directory,I shouldn’t get penalized for this) and added the datagen and evaluate.py file.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> Keep datagen.py and evaluate.py in same folder

when i do this( ![:down_arrow:](https://emoji.discourse-cdn.com/google/down_arrow.png?v=14 ":down_arrow:")) i get this error

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> `docker build -t <your image name>`

```
PS D:\TDS_Project_1\tds-project-1> docker build -t "tushar2k5/tds-project-1"                                                                 
ERROR: "docker buildx build" requires exactly 1 argument.
See 'docker buildx build --help'.

Usage:  docker buildx build [OPTIONS] PATH | URL | -

Start a build

```

Instead,in order to run the docker image successfully we have to do either of the two things(taken help from chatgpt ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14 ":upside_down_face:")):  
1)

```
Use full path (recommended if you're outside the project folder):

docker build -t tushar2k5/tds-project-1 D:\TDS_Project_1\tds-project-1

```

**OR**  
2)

```
Add a dot (.) at the end to specify the current directory as the build context:

docker build -t tushar2k5/tds-project-1 .

```

*Both the things work for me*(![:up_arrow:](https://emoji.discourse-cdn.com/google/up_arrow.png?v=14 ":up_arrow:"))

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> `docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -P 8000:8000 <your image name>`

```
docker run -e AIPROXY_TOKEN=i.am.still.noob.inTDS -p 8000:8000 tushar2k5/tds-project-1

```

Done this(can’t leak my token,already many students stolen it from my project-2🤦‍♂️)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> `uv run evaluate.py --email=<any email> --token_counter 1 --external_port 8000`

```
uv run evaluate.py --email=23f2003751@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

```

Done this to evaluate my project

Any finally the main part (DRUM ROLLS ![:drum:](https://emoji.discourse-cdn.com/google/drum.png?v=14 ":drum:"),not this one ![:oil_drum:](https://emoji.discourse-cdn.com/google/oil_drum.png?v=14 ":oil_drum:") (IUKUK))

image description: The image is a screenshot of a terminal window. It shows a series of commands and their results. The tasks are to determine the connotation of the statement "I hate you." A failure message "C5 failed: Server disconnected without sending a response" is present. The score is 6 / 25.
image text: Running task: Does the statement 'I hate you' have a positive or negative connotation? Reply as a single string containing either 'POSITIVE' or 'NEGATIVE' in uppercase. Save the result to /data/c5.txt
C5 failed: Server disconnected without sending a response.
X C5 FAILED
Score: 6 / 25
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"

**THATS 6/25**

Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly)  
image description : The image shows a list of prerequisites checks with their pass/fail status represented by 1 for pass and 0 for fail. The checks include Docker and Github repo existence and public status, along with the presence of a LICENSE file and a Dockerfile.
image text: Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 0

Hopping to get a response from you guys,  
Thanks a lot(wrote this much for first time for any course)  
(PS:This course has some special place in my heart ![:heart:](https://emoji.discourse-cdn.com/google/heart.png?v=14 ":heart:"))  
[@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

We fetched your latest github commit before 18th Feb and build image through that and evaluated.

Your latest github repo before 18 has:  
username : `singh-yash129`  
Repo : `Large-Language-Model`  
commit\_sha: `88f7439471151283f1218b46d209030dd7f4e5ae`

Use `https://github.com/<username>/<repo>/archive/<commit_sha>.zip` for downloading repo.

If You feel there is any problem with our evaluation script suggest edits to the scirpt.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003751/48/68010_2.png) 23f2003751:

> Currently I’m getting a big 0 beacause the github doen’t contain the dockerfile(which it does clearly

Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

---

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> Dockerfile has to be inside root of any github repo, this is standard and we had discussion with Professor Anand about such cases where it’s not part of root directory, he suggested we will consider only Dockerfile being present in root folder of the repo.

Sorry but its not possible to attend every single session and you guys haven’t informed us via email so how its our fault.For cases like this you guys should allow us to move our files to the root directory so it can work…(we just have to move files in the repo please consider it)[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)  
(i have already made a rookie mistake in my dockerfile otherwise i would have got 9/25 but keeping that aside please let me get 6/25)  
![PuppyDogEyesSadGIF](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/1/41dc27831c97af2f02287cec795a281e9672723d.gif) ![GojoSadGojoGIF](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/e/3e588079c65a2f9979f97bb5f1d81e3c1691ab20.gif)

---

Good evening sir.

My original project evaluation conducted by IITM gave me 7/20, however the new evaluation gave me 0/20.

image description: The image is a screenshot of a log file from a code execution, with various HTTP requests, status codes, and error messages. It appears to be a debugging log related to a data processing or web service operation.
image text: 23f1002223@ds.study.iitm.ac.in\_evaluation.log
Running task: Convert https://raw.githubuserconten to `/data/b9.html`
HTTP Request: POST http://localhost:8301/run?task=Con Knife%2Fd0dd1f61b33d64e29d8bc1372a94ef6a2fee76a9%2FRE
HTTP 200 { "message": "B9 Task 'Convert https://raw.githubuser save it to `/data/b9.html`' executed successfully" }
HTTP Request: GET http://localhost:8301/read?path=/da
B9 failed: Cannot read /data/b9.html
X B9 FAILED
Running task: Run datasette via `uvx datasette /da From `tickets` count the number of rows where `type` http://localhost:8001/ticket-sales.csv?sql=SELECT+COU and save it to /data/b10.csv. Then stop the datasette server.
HTTP Request: POST http://localhost:8301/run?task=Run port+8001%60+in+the+background.%0AFrom+%60tickets%60+ ticket- sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM%2Bti asette+server.%0A "HTTP/1.1 400 Bad Request"
HTTP 400 { "detail": "HTTPConnectionPool (host='localhost', por sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronz Failed to establish a new connection: [Errno 111] Con }
HTTP Request: GET http://localhost:8301/read?path=/da
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
◎ Score: 7 / 20
HTTP Request: POST https://aiproxy.sanand.workers.dev

This was from the official evaluation sir, could you kindly look into it.

---

did everything as mentioned i got 7/25 but in mail i got 2 which is bonus?  
i know i didn’t add flask in docker it was my mistake ![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=14 ":frowning:") but can we just for once neglect that. pleaseeeeeeeee

image description: The image shows a terminal output with HTTP requests, error messages, and a score. The first HTTP request resulted in a 404 Not Found error. A file named "c5.txt" could not be read, and the test "C5" failed. The final score is 7/25, and a subsequent HTTP request was successful.
image text:
```
}
HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 404 Not Found"
C5 failed: Cannot read /data/c5.txt
X C5 FAILED
Score: 7 / 25
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
PS C:\Users\choud\OneDrive\Desktop\tds1\TDS\_Project\_1>
```

---

Please do consider allowing us to change the position of the dockerfile to the root. We are doing nothing but changing its location in the repo. This was not mentioned anywhere in the prerequisites before the submission and it is unfair to not consider all our work for a criteria that was nowhere mentioned in the course page before the submissions. It may be standard practice but a lot of us were unaware. Please do consider this request.

---

Sir, could you please fetch my latest GitHub commit before 18th Feb and build the image through that one?  
I received a mail saying that the Docker image is not accessible, but it is already there. Kindly request you to evaluate my submission.

---

Hi [@Abhay222](/u/abhay222)

Docker image submitted by you doesn’t exists.

image description: The image is a screenshot of a webpage displaying a 404 error message. The webpage is on Docker Hub, as indicated by the logo in the top-left corner and the URL in the address bar. The error message is inside of a big blue circle.
image text: https://hub.docker.com/r/abhay227/version1/tags Explore / abhay227 / version1 404 Oops! The page you have requested was not found dockerhub Search Docker Hub Ctrl+K Update Sign in Sign up

---

Hi [@23f1000879](/u/23f1000879)

This basically tells you didn’t validate docker Dockerfile and docker image by building and running them, otherwise you would have corrected the mistake.

---

Here's a brief description of the image:
The image shows details about a docker image version. It displays the tag, digest, OS/ARCH, last pull information, and compressed size. There's also a command for pulling the image and a "Copy" button.
image text:
TAG
version1
Last pushed about 1 month by abhay227
Digest
4db729a03f74
OS/ARCH
Last pull
linux/amd64
about 1 month
docker pull abhay227/tds\_project:version1 Copy
Compressed size
261.98 MB
  
but it is available under version1.

---

repo that you submitted through google form was different then this one.

Your Gform response

image description: A table with headers and data about a project.
image text: Preview Code Blame 1069 lines (1069 loc) 127 KB
Q 23f1001120@ds.study.iitm.ac.in
1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub?
919 2/16/2025 23:10:43 23f1001120@ds.study.iitm.ac.in https://github.com/23f1001120/Tds\_Project1 abhay227/version1

---

Hi, I work in the IT industry. There is no standard like “docker file has to be only in the root folder.”

If at all you are setting a requirement why was this not mentioned in the project page?

We were asked to build an app which solves the given tasks. You were OK for whatever code/tools/method to use as long as it works, there the “industry standard” didn’t show up ironically!!!

Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

In the same industry that I work - we build the dockers and give it for prod push.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Dear Sir,  
I got log with error as /bin/sh: 1: [/root/.local/bin/uv,: not found.  
I debugged that I had a small issue in the dockerfile that was submitted and it is  
CMD [“/root/.local/bin/uv”, “run”, “app.py”] has an **invisible Unicode non-breaking space** (`U+00A0`) between `"run", "app.py"` instead of a regular space. This causes the shell to misread the command.  
I know it’s very late for the submission to reconsider, but this small mistake spoiled my hard earned project which got local score 8/25 which could finally get converted to 12 marks. I made this change and pushed it to docker and github repository. Considering this, I request you to please evaluate my submission if possible, because I don’t want to lose the marks which i tried my level best to score. I already have good score in GA’s and ROE. Expecting a positive response from your end.

---

sir, but before submission i run evluate.py and it gave me 8/10 in task A. after submission i also got result mail stating that i got 8/20.  
image description : The image is a screenshot of a terminal or log file displaying the results of a series of tests, likely related to data processing or web requests. The display is a mix of text, status indicators (like "FAILED" with an "X" mark), and HTTP request details.
image text: HTTP Request: GET http://localhost:8265/read?path=/data/b7.png "HTTP/1.1
X B7 FAILED
B8 failed: not all arguments converted during string formatting
X B8 FAILED
Running task: Convert https://raw.githubusercontent.com/octocat/Spoon-Knife/d0dd1f61b33d64e29d8bc1372a94ef6a2fee76a9/README.md to HTML and save it to `/data/b9.html`
HTTP Request: POST http://localhost:8265/run?task=Convert+https%3A%2F%2Fraw.githubusercontent.com%2Foctocat%2FSpoon-
Knife%2Fd0dd1f61b33d64e29d8bc1372a94ef6a2fee76a9%2FREADME.md+to+HTML+and+save+it+to+%60%2Fdata%2Fb9.html%60 "HTTP/1.1 200 OK"
HTTP 200 {
"message": "B9 Task 'Convert https://raw.githubusercontent.com/octocat/Spoon-Knife/d0dd1f61b33d64e29d8bc1372a94ef6a2fee76a9/README.md to HTML and save it to `/data/b9.html`'
executed successfully"
}
HTTP Request: GET http://localhost:8265/read?path=/data/b9.html "HTTP/1.1 404 Not Found"
B9 failed: Cannot read /data/b9.html
X B9 FAILED
Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background.
From `tickets count the number of rows where `type` is "Bronze" using
http://localhost:8001/ticket-sales.csv?sql=SELECT COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22
and save it to /data/b10.csv.
Then stop the datasette server.
HTTP Request: POST http://localhost:8265/run?task=Run+datasette+via+%60uvx+datasette+%2Fdata%2Fticket-sales.db+--
port+8001%60+in+the+background.%0AFrom+%60tickets%60+count+the+number+of+rows+where+%60type%60+is+%22Bronze%22+using%0Ahttp%3A%2F%2Flocalhost%3A8001%2Fticket-
sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM%2Btickets%2BWHERE%2Btype%2B%3D%2522Bronze%2522%0Aand+save+it+to+%2Fdata%2Fb10.csv.%0AThen+stop+the+datasette+server.%0A
"HTTP/1.1 400 Bad Request"
HTTP 400 {
"detail": "HTTPConnectionPool (host='localhost', port=8001): Max retries exceeded with url: /ticket-sales.csv?sql=SELECT COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22
(Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7e835ef27bf0>: Failed to establish a new connection: [Errno 111] Connection refused'))"
}
HTTP Request: GET http://localhost:8265/read?path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 8/20
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
---  
also this mail result Earlier i got From your side. ![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=14 ":frowning:")

---

Sir, I realized that I mistakenly submitted the image tag `"abhay227/version1"` instead of the correct image ID. The correct image ID is `4db729a03f74`, which is part of version1 and is already present and publicly available.  
Unfortunately, I didn’t receive any notification about this issue after submission. Receiving this mail at this stage feels disheartening after all the effort I’ve put into the project. I kindly request you please consider this correct image ID.

---

image description: The image is a checklist of pre-requisites. The text includes checks for the existence and public status of a Docker repo and a Github repo with a timestamp before 18th of Feb, and the presence of a LICENSE file (MIT License) and Dockerfile. Each check has a corresponding value of 1.
image text: Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1

Hi, all my pre-requisites have been fulfilled, and the evaluation logs say I have a score of 10/25. But I have gotten a score of 0, saying ‘Task A module missing’. This is a kind request to confirm the scores.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Here's a description of the image:
The image is a screenshot of a Google Sheets document titled "p1\_evaluation\_error\_logs". The spreadsheet contains data in columns labeled "A" and "B", with rows containing error log information. The information includes timestamps, email addresses, and descriptions of the errors encountered. The text includes error messages like "taskA module missing", "app module missing", "SyntaxError: unmatched '}'", and issues with container binding.
image text: p1\_evaluation\_error\_logs File Edit View Insert Format Data Tools Extensions Help 100% View only M 23f1001524 0 of 0 A1 fx email A B 55 23f1000049@ds.study.iitm.ac.in taskA module missing 56 23f1000337@ds.study.iitm.ac.in app module missing 57 23f1000625@ds.study.iitm.ac.in application running on 5000 port 58 23f1000718@ds.study.iitm.ac.in taskA module missing 59 23f1000799@ds.study.iitm.ac.in SyntaxError: unmatched '}' 60 23f1000879@ds.study.iitm.ac.in flask module missing 61 23f1001029@ds.study.iitm.ac.in Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside (host os) 62 23f1001156@ds.study.iitm.ac.in npx not found 63 23f1001232@ds.study.iitm.ac.in taskA module missing 64 23f1001472@ds.study.iitm.ac.in env file missing 65 23f1001645@ds.study.iitm.ac.in taskA module missing 66 23f1001995@ds.study.iitm.ac.in taskA module missing 67 23f1002010@ds.study.iitm.ac.in taskA module missing 68 23f1002144@ds.study.iitm.ac.in taskA module missing 69 23f1002223@ds.study.iitm.ac.in flask module missing 70 23f1002363@ds.study.iitm.ac.in taskA module missing 71 23f1002368@ds.study.iitm.ac.in openai module missing 72 23f1002534@ds.study.iitm.ac.in PhaseA module missing 73 23f1002558@ds.study.iitm.ac.in taskA module missing 74 23f1002571@ds.study.iitm.ac.in taskA module missing
  
image description: The image displays a file explorer window in a Windows operating system. The window is focused on the "Downloads" folder, and it appears to be searching for a specific file or folder using the search term "23f1001524". The search results indicate that no items match the search criteria. The left-hand side of the window has a navigation pane with several options, including "Home", "Gallery", "OneDrive - Perso", "Desktop", "Downloads", "Documents", "Pictures", "Music", "Videos", "Bsc Ds", and "iitm".
image text: 23f1001524 - docker\_logs.zip
X
+
23f1001524 - docker\_logs.zip
>
Downloads
>
docker\_logs.zip
New
४
Name
N Sort
=View
Extract all
Type
Compressed size
Password p... Size
Home
Gallery
>
OneDrive - Perso
No items match your search.
Desktop
↓ Downloads
Documents
Pictures
Music
Videos
Bsc Ds
iitm
Ratio
Date modified
X
23f1001524
X
Q
Details
  
Here's a description of the image:
The image shows a file explorer window open on a computer. The window is displaying the contents of a zip file named "evaluation\_logs.zip," which is located in the "Downloads" folder. The window shows the standard columns for file information (Name, Type, Compressed Size, etc.) but states "No items match your search." The user is viewing the file via the Downloads folder which is selected in the left panel. The title bar indicates the file name is "23f1001524" with a search bar on the right.
image text:
23f1001524 - evaluation\_logs.z
New
Name
Home
Gallery
OneDrive - Perso
Desktop
Downloads
Documents
Pictures
Music
Videos
Bsc Ds
iitm
←
>
Downloads
evaluation\_logs.zip
Type
Compressed size
Password p...
No items match your search.
Extract all
Size
Ratio
Date modified
23f1001524
Details

I cannot find my docker\_logs nor evaluation\_logs and nor anything on the forms . The mail I got says that i received 0 in project tasks but clearly my project is not evaluated. Please look into this. during earlier evaluation i got 7 marks but this time it is 0.  
Here's a brief description of the image:
The image appears to be a document or report related to a software project evaluation. It provides information on GitHub and Docker repositories, pre-requisite checks with associated scores, and a scoring summary. There are tables with entries marked as 0. At the end there is information about task score, bonus and p1 score.
image text: Your final t score calculation is based on
MIN (20, (task score + bonus))
Github repo submitted: https://github.com/veershah1231/tds\_proj\_1
Docker repo submitted: veershah1231/tdsproject1final
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
0 0 0 0 0 0 0 0 0 0
B1 B2 B3 B4 B5 B6 B7 B8 B9 B10
0 0 0 0 0 0 0 0 0 0
C1 C2 C3 C4 C5
0 0 0 0 0
Your task score is: 0
Your bonus is: 1
Your P1 score is: 1
We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.
You will only have an evaluation log if your API service actually started working within 5 minutes. Otherwise you will have only a docker log.

My roll number is 23f1001524 .

---

[@carlton](/u/carlton) and [@Jivraj](/u/jivraj) , for Task A i had tested before and all the test cases passed, but all my A tasks has failed with 0, In the evaluation logs, i could see that all task A tests failed due to datagen.py not available.

Could you rerun the test ?

---

Respected Sir,

Thank you for your response and for providing the steps to replicate the test environment.  
Steps Taken to Replicate the Test Environment  
I cloned my repository using:

```
bash
git clone <my_repo_url>
cd <my_repo_directory>
I built the Docker image using:

bash
docker build -t.
I ran the Docker container with:

bash
docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000

I ensured that datagen.py and evaluate.py were placed in the same folder as instructed.

Finally, I ran the evaluation script using:

bash
uvicorn evaluate.py --email=<any_email> --token_counter 1 --external_port 8000

```

Issue with Original Submission  
After reviewing the evaluation logs, I identified that the issue with my original submission was caused by binary incompatibility between pandas (version 2.0.3) and NumPy (version 1.24.3). These versions worked perfectly during development on my local machine and were tested multiple times across both Linux and Windows platforms before submission. Even after pulling the submitted Docker image from Docker Hub post-submission, it worked without any issues locally.

However, during your evaluation, this incompatibility caused the container to fail.  
I acknowledge this issue, have fixed it in my updated submission, and previously conveyed this in my earlier message.

Action Taken  
To address this issue, I made a small adjustment to my requirements.txt file to explicitly fix these versions for compatibility across all environments. This was the only change made to my submission. After rebuilding the container with this updated file, I tested it again thoroughly in your replicated test environment, and it worked as expected:

The application initializes correctly on port 8000 within 5 minutes.

It responds to requests within the required timeframe.

I have pushed this updated image to Docker Hub under the same repository:  
Docker Hub URL: santoshsharma003/tds-project-one-1:latest

Request for Re-Evaluation  
I kindly request that you pull the latest version of my Docker image from Docker Hub and re-run the evaluation process. I understand that deployability is being tested, and I have taken every necessary step to ensure that my submission now works in any environment, including replicating your test setup exactly.

Previous Message for Reference  
For your convenience, here is my earlier message explaining this issue in detail:

"Greetings, Sir,

I would like to bring to your notice a problem with my original submission of the Docker container. During evaluation, a binary incompatibility between pandas and numpy caused the container to fail. To my surprise, the same versions (pandas==2.0.3 and numpy==1.24.3) were working fine while developing on my local machine. I also tested it with the same Dockerfile on both Linux and Windows platforms using these versions, and it was functioning correctly before pushing and submitting it. I checked the other day after pulling the Docker image from Docker Hub following the submission, and it worked at that time as well.

To resolve this issue, I adjusted the Dockerfile to explicitly fix these versions, rebuilt the container, and conducted further testing locally. The application now correctly initializes on port 8000 and returns expected responses within the required 5-minute timeframe.

I’ve pushed the updated image to Docker Hub (santoshsharma003/tds-project-one-1:latest). Could you please ensure that the latest version of my image is pulled from Docker Hub before rerunning the evaluation? I appreciate your time and effort in reviewing my submission again.

Thank you for your assistance!"

---

same for me  
my roll number is 23f1003094

---

Same with me sir [@carlton](/u/carlton)

---

There are no evaluation logs for you, I am not sure which evaluation log you are referring to. Your docker image fails to run the required task because your Dockerfile is misconfigured. Did you follow the test environment setup mentioned in this post before posting your query?

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that
> import requests
> import pandas
> DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")
> url = f"https://api.github.com/repos/{owner}/{repo}/commits"
> try :
> response = requests.get(url,headers=github\_headers, timeout=60)
> fetch\_commit = None
> if response.status\_code == 200:
> commits = response.json()
> for commit in commits:
> sha = commit["sha"]
> …

Because if you did, you will realise why your evaluation failed.  
You must replicate the test environment and then if you submission works, you have a legitimate appeal. Otherwise we will not consider it. Please replicate the issue using the test environment as detailed in the post link.

Kind regards

---

You can take it up with [@s.anand](/u/s.anand)  
I did not come up with the standard.  
And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.

> Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.

Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand if we could make the allowance. He made the decision to enforce this protocol.

Kindest regards.

---

[@carlton](/u/carlton)  
image description: The image is a screenshot of a terminal or log file. The text provides information on data processing tasks and their results. Errors are indicated with red icons.
image text: README.md to HTML and save it to /data/b9.html 23f2001390@ds.study.iitm.ac.in\_evaluation.log ... B9 failed: Cannot read /data/b9.html B9 FAILED Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background. From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv?sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv. Then stop the datasette server. HTTP Request: POST http://localhost:8369/run?task=Run+datasette+via+%60uvx+datasette+%2Fdata%2Fticket-sales.db+-- port+8001%60+in+the+background.%0AFrom+%60tickets%60+count+the+number+of+rows+where+%60type%60+is+ %22Bronze%22+using%0Ahttp%3A%2F%2Flocalhost%3A8001%2Fticket- sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM%2Btickets%2BWHERE%2Btype%2B%3D%2522Bronze%2522%0Aand+save+it+to+ %2Fdata%2Fb10.csv.%0AThen+stop+the+datasette+server.%0A "HTTP/1.1 400 Bad Request" HTTP 400 { "detail": "HTTPConnectionPool (host='localhost', port=8001): Max retries exceeded with url: /ticket-sales.csv? sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7c9f911c0b60>: Failed to establish a new connection: [Errno 111] Connection refused'))" } HTTP Request: GET http://localhost:8369/read?path=/data/b10.csv "HTTP/1.1 404 Not Found" B10 failed: Cannot read /data/b10.csv B10 FAILED Score: 7 / 20 HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
  
Respected Sir,  
see the above image its from the scores we got from mail just before the latest one, in that I had got 7/20 and now new mail shows I got 0?? how is this possible…  
the link for evaluation in which i got 7/20 is : [23f2001390@ds.study.iitm.ac.in\_evaluation.log - Google Drive](https://drive.google.com/file/d/1cNVy9KSfSITZg_KGLF2_wwLWjzNl8mb5/view)  
image description: The image is a screenshot of a webpage displaying the results of a system check or evaluation. It includes details of submitted GitHub and Docker repositories, pre-requisite checks, and a score breakdown. The image also contains a table with various sections labeled A1 to C5, all having a value of "0". There is also informational text at the bottom about evaluation logs.
image text: Github repo submitted: https://github.com/23f2001390/IImagent
Docker repo submitted: 23f2001390/llmagent
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
0 0 0 0 0 0 0 0 0 0
B1 B2 B3 B4 B5 B6 B7 B8 B9 B1C
0 0 0 0 0 0 0 0 0 0
C1 C2 C3 C4 C5
0 0 0 0 0
Your task score is: 0
Your bonus is: 1
Your P1 score is: 1
We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.
You will only have an evaluation log if your API service actually started working within 5 minutes. Otherwise you will have only a docker log.
  
MOST importantly mail shows :  
**Your final t score** calculation is based on

MIN (20, (task score + bonus))

**Github repo submitted:** [GitHub - 23f2001390/llmagent](https://github.com/23f2001390/llmagent)

**Docker repo submitted:** 23f2001390/llmagent

**Pre-requisites check: (1 for pass, 0 for fail)**

Docker repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo exists and is public (should have a timestamp before 18th of Feb): 1

Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1

Gihub repo check - Dockerfile exists: 1  
Your task score is: 0  
Your bonus is: 1  
Your P1 score is: 1

---

So according to the above, I passed the pre-requisites and also in mail u have mentioned that:  
We have attached the docker logs and the evaluation logs for everyone who passed the pre-requisites.

but I don’t find my mail id or roll number in the docker\_logs.zip or evaluation\_logs.zip that has been given in the mail(latest), if I passed the pre requisites my logs should be there in the zip files included in this latest mail right, my roll number is 23f2001390 and email id is 23f2001390@ds.study.iitm.ac.in  
and nor do i find my id in the p1\_evaluation\_error\_logs so please help sir  
Thank you  
image description: The image is a screenshot of a file explorer window. The window is open to the "docker\\_logs.zip" file in the "Downloads" folder. The search bar in the upper right corner has text. In the main area of the window, it shows "No items match your search".
image text:
> This PC > Downloads > docker\\_logs.zip
Name
Type
Compressed size
Password p...
No items match your search.
23f2001390
X
Select a file to preview.
  
image description: A screenshot of a file explorer window, likely on a Windows operating system, showing the contents of a zip file named "evaluation\_logs.zip". The window displays a "This PC" path leading to the "Downloads" folder. There is a search box with the text "23f2001390". The central content area shows "No items match your search" and the right area has the text "Select a file to preview.".
image text:
↑> This PC > Downloads > evaluation\_logs.zip
Name Type Compressed size Password p...
No items match your search.
23f2001390
Select a file to preview.
  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of a Google Sheets spreadsheet titled "p1\_evaluation\_error\_logs." The spreadsheet contains two columns: "email" and "error\_reason," with several rows of data. The "error\_reason" column contains error messages related to module missing issues, application issues, and file path issues.
\*\*image text:\*\*
p1\_evaluation\_error\_logs
email error\_reason
21f1000589@ds.study.iitm.ac.in requests modue missing
21f1002560@ds.study.iitm.ac.in application running on 5000 port
21f1004148@ds.study.iitm.ac.in functions module missing
21f1006922@ds.study.iitm.ac.in Usage: /app/start.sh <email>
21f2000304@ds.study.iitm.ac.in /bin/sh: 1: [/root/.local/bin/uv,: not found
21f2000555@ds.study.iitm.ac.in app module missing
21f3000031@ds.study.iitm.ac.in nest\_asyncio module missing
21f3000245@ds.study.iitm.ac.in whisper module missing
21f3000591@ds.study.iitm.ac.in taskA module missing
21f3001093@ds.study.iitm.ac.in SyntaxError: unmatched ']'
21f3001194@ds.study.iitm.ac.in taskA module missing
21f3002753@ds.study.iitm.ac.in taskA module missing
21f3003255@ds.study.iitm.ac.in taskA module missing
22ds2000091@ds.study.iitm.ac.in taskA module missing
22f1000696@ds.study.iitm.ac.in taskA module missing
22f1000703@ds.study.iitm.ac.in taskA module missing
22f1000770@ds.study.iitm.ac.in taskA module missing
22f1001651@ds.study.iitm.ac.in flask\_cors module missing
22f1001972@ds.study.iitm.ac.in error: Failed to spawn: `app.py', Caused by: No such file or directory (os error 2)
22f2000429@ds.study.iitm.ac.in taskA module missing
22f2000467@ds.study.iitm.ac.in taskA module missing
22f2000770@ds.study.iitm.ac.in taskA module missing
22f2001048@ds.study.iitm.ac.in Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside (host os)
22f2001103@ds.study.iitm.ac.in taskA module missing
22f3000099@ds.study.iitm.ac.in taskA module missing
22f3000276@ds.study.iitm.ac.in phaseA module missing

---

[@carlton](/u/carlton)  
Same for sir. I have made my post similarly, roll number is 23f2001390 and email is 23f2001390@ds.study.iitm.ac.in

---

[@carlton](/u/carlton)  
i also not found anything in this form , but i got mail to score=0  
image description: This is a screenshot of a Google Sheets document titled "p1\_evaluation\_error\_logs". The spreadsheet contains data with two columns, labeled "A" and "B". Column A appears to contain email addresses and column B contains error messages. The document is "View only".
image text:
p1\_evaluation\_error\_logs
File Edit View Insert Format Data Tools Extensions Help
A1
fx email
A
B
89
23f2001286@ds.study.iitm.ac.in taskA module missing
90
23f2001305@ds.study.iitm.ac.in pydub module missing
91
23f2001738@ds.study.iitm.ac.in taskA module missing
92
23f2002090@ds.study.iitm.ac.in taskA module missing
93
23f2002285@ds.study.iitm.ac.in could't import module app
94
23f2002286@ds.study.iitm.ac.in Could not import module "MAIN".
95
23f2002745@ds.study.iitm.ac.in flask module missing
96
23f2003448@ds.study.iitm.ac.in PhaseA module missing
97
23f2003680@ds.study.iitm.ac.in Attribute "app" not found in module "app"
98
23f2004278@ds.study.iitm.ac.in ImportError: cannot import name 'logger' from 'app.utils.logger'
99
23f2004318@ds.study.iitm.ac.in taskA module missing
100
23f2004395@ds.study.iitm.ac.in taskA module missing
101
23f2004462@ds.study.iitm.ac.in Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside (host os)
102
23f2004675@ds.study.iitm.ac.in taskA module missing
103
23f2004770@ds.study.iitm.ac.in taskA module missing
104
23f2004941@ds.study.iitm.ac.in SyntaxError: unterminated string literal (detected at line 306)
105
23f2004979@ds.study.iitm.ac.in taskA module missing
106
23f2005067@ds.study.iitm.ac.in taskA module missing
107
23f2005141@ds.study.iitm.ac.in Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside (host os)
108
23f2005275@ds.study.iitm.ac.in Container was bound to 127.0.0.1 instead of 0.0.0.0 which is why docker container port 8000 is not accessible outside (host os)
109
23f2005325@ds.study.iitm.ac.in pytesseract module missing
110
23f2005327@ds.study.iitm.ac.in ImportError: libGL.so.1: cannot open shared object file: No such file or directory
111
23f3000264@ds.study.iitm.ac.in RuntimeError: Cannot install on Python version 3.12.9; only versions >=3.6, <3.10 are supported.
![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14 ":smiling_face_with_tear:")

---

Hi Hari,

Your docker failed to build.

Did you try to replicate the test environment as mentioned in

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that
> import requests
> import pandas
> DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")
> url = f"https://api.github.com/repos/{owner}/{repo}/commits"
> try :
> response = requests.get(url,headers=github\_headers, timeout=60)
> fetch\_commit = None
> if response.status\_code == 200:
> commits = response.json()
> for commit in commits:
> sha = commit["sha"]
> …

If you tried you would find that it will not build. Thats why you have no logs.  
90 such cases are there where the image could not be built from your repo.

The specific error in your case is:  
tried copying requirements.txt which doesn’t exists

Thats why there are no logs.  
Kind regards

---

Hello [@carlton](/u/carlton) Sir, please reply to my query

---

We cannot allow changes to repos. This is a blanket rule for everyone. No exceptions. Since the only way to get your project to work is to make changes to it, we cannot score you for changes.

Kind regards

---

Thanks for the response. We can go on endless discussions using “nice words” “professionally” with the number of questions we have. Finally we are at the receiving end as students in this setup.

What’s the take away for everyone? Let’s move on. This isn’t the end.

Positive or Negative - Real world outside will make everyone realise and everyone change their opinions (including me) as the time and environment changes.

---

What I observed is that most of the repositories appear to be copied from a single source. This original repository contains several issues, such as an incorrectly named Dockerfile and missing instructions to copy all necessary data. Unfortunately, many students seem to have uploaded it blindly without reviewing or fixing these problems.

---

Hi I have my Dockerfile saved as dockerfile, given 0 for project 1 due to this. This doesn’t seem to be a big issue to grade me 0 for this. Kindly correct the score please.

---

Most common reason for during running docker image was `taskA module was missing` which is because a lot of students blindly copied from someone with building and running image, if they would have done that they could have corrected it at early stage.

---

For you check failed because of the naming of Dockerfile(It was named as dockerfile(d in small).

---

This is error that you got while building docker image using docker file in your github repo tried copying requirements.txt which doesn’t exists

In your Dockerfile you are trying to copy requirements.txt but it doesn’t exists in the directory where Dockerfile is located

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/mitali_r/48/66886_2.png) MITALI\_R:

> 23f1003094

While running docker image create by your github repo, we got following error `taskA module missing`

For regenerating it follow steps that are mentioned here : [Tds-official-Project1-discrepencies - #316](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

For you naming of MIT License was not correct.  
This shows naming criteria for adding License.  
[Adding a license to a repository - GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository)

---

Sir actually my project doesn’t have requirements.txt, instead it installs automatically  
when:  
`uv run app.py` is run and for docker image it installs while building and I had submitted the docker image with all libraries required(the dockerfile below, in that it installs while building).  
my dockerfile from the repo:

```
FROM python:3.12-slim-bookworm

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Download and install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:$PATH"

# Set up the application directory
WORKDIR /app
# Copy application files
COPY *.py /app/
COPY .env /app/

# Explicitly set the correct binary path and use `sh -c`
CMD ["/root/.local/bin/uv", "run", "app.py"]

```

here u can see it installs using pip install …

here it’s requiring `.env` file to be present in the project folder because my project when I was uploading to both git and docker had `.env` file for AIPROXY\_TOKEN and I uploaded to docker with that `.env` file but as git doesn’t allow upload of `.env` file I couldn’t upload`.env` to git

the project will still work after downloading the repository when we upload AIPROXY\_TOKEN as environment variable but to again build the docker image for replicating the test environment, my docker image could not be built because`.env` file doesn’t upload to GIT, so when I downloaded the repository from the above method, it didn’t have the `.env` file so it didn’t build so I had to create the `.env` file now to create the docker image, and for the dockerimage I had submitted, I built it with the `.env` file(it supports both`.env` file and environment variable one)

---

After filling form you didn’t double check form.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/abhay222/48/66780_2.png) Abhay222:

> I kindly request you please consider this correct image ID.

We can’t reconsider it.

---

Yes problem was missing `.env` file, Your repo, was supposed to run in a test environment.

---

Yes sir, please help me

---

Sorry We can’t do any help, we won’t be considering for eval.

---

But sir, It was supposed to run right…

---

It Should build in any test environment using Dockerfile from your github repo.

---

[@Jivraj](/u/jivraj) please tell me what was my mistake?

---

It was named wrongly.  
You named it LICENCE but it should be LICENSE or LICENSE.md.

---

But sir, just because the repository doesn’t have .env file it couldn’t build the dockerimage, the docker image will build in any test environment as u said but it requires the .env to be included which the git didn’t have(it doesn’t allow upload of it ofcourse), don’t rerun the evaluation again but please sir atleast give me those 7/20 marks along with the pre-requisite bonus(1mark) that was mailed earlier to me along with logs…this is my primary degree after 12th, I’m also not asking any extra marks just the marks that i got earlier:  
image description: The image is a screenshot of a log file that appears to be related to data processing or a similar task. The log contains a series of messages indicating the status of various operations. There are several "HTTP Request" entries that detail attempts to fetch data. Some requests failed as indicated by error messages "400 Bad Request" and "404 Not Found".
image text:
HTTP Request: GET http://localhost:8369/read?path=/data/b9.html "HTTP/1.1 404 Not Found"
B9 failed: Cannot read /data/b9.html
X B9 FAILED
Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background.
From `tickets` count the number of rows where `type` is "Bronze" using
http://localhost:8001/ticket-sales.csv?sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22
and save it to /data/b10.csv.
Then stop the datasette server.
HTTP Request: POST http://localhost:8369/run?task=Run+datasette+via+%60uvx+datasette+%2Fdata%2Fticket-sales.db+--
port+8001%60+in+the+background.%0AFrom+%60tickets%60+count+the+number+of+rows+where+%60type%60+is+
%22Bronze%22+using%0Ahttp%3A%2F%2Flocalhost%3A8001%2Fticket-
sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2BFROM%2Btickets%2BWHERE%2Btype%2B%3D%2522Bronze%2522%0Aand+save+it+to+
%2Fdata%2Fb10.csv.%0AThen+stop+the+datasette+server.%0A "HTTP/1.1 400 Bad Request"
HTTP 400 {
"detail": "HTTPConnectionPool (host='localhost', port=8001): Max retries exceeded with url: /ticket-sales.csv?
sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 (Caused by NewConnectionError('<urllib3.connection.HTTPConnection
object at 0x7c9f911c0b60>: Failed to establish a new connection: [Errno 111] Connection refused'))"
}
HTTP Request: GET http://localhost:8369/read?path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 7 / 20
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/vl/embeddings "HTTP/1.1 200 OK"

---

Hi [@23f2002600](/u/23f2002600) [@21f1005908](/u/21f1005908)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) [Tools in Data Science](/c/courses/tds-kb/34)

> You can take it up with [@s.anand](/u/s.anand)
> I did not come up with the standard.
> And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.
> Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.
> Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

Runned for you, it A1 Fails.

---

Your docker image and github repo are not consistent, your docker image was not built with the latest code before 18th feb that’s present in your github repo.

---

We can’t consider any changes after deadline.

---

Your docker image and github repo are not consistent.

While running docker image we got following error: `flask module missing`  
For regenerating this error follow steps mentioned in below post.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that
> import requests
> import pandas
> DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")
> url = f"https://api.github.com/repos/{owner}/{repo}/commits"
> try :
> response = requests.get(url,headers=github\_headers, timeout=60)
> fetch\_commit = None
> if response.status\_code == 200:
> commits = response.json()
> for commit in commits:
> sha = commit["sha"]
> …

---

Anything after deadline we can’t consider any changes, it was just a matter of time, you didn’t tests running evaluate.py on docker container that was created, otherwise you would have spotted this mistake and rectified it.

---

In your github repo, Dockerfile should be named as Dockerfile(D caps).

---

I don’t know reason behind it, earlier evaluation was done by pulling docker image.  
Latest one was done through github repo, if code in github repo is not consistent with docker image it might cause problems.

LLM won’t provide same results every time, for that reason we have give bonus marks.

---

[@carlton](/u/carlton) [@jivraj](/u/jivraj) sir it is my humble request to do something. We are losing our marks because of small negligence or mistakes like i fogot to commit my requirements.txt in my github repository. Already the course has taken tolls on our mind. Please give partial marks for the correct run of the docker image or please evaluate my latest commit with the requirements.txt. Because of this project I will lose my cgpa and the hardwork that I have done till this term. A small mistake is causing me my full marks and grades. Atleast consider partial marking for the docker image which does the tasks. I have maintained 9+ cgpa in the diploma and I took other subjects which are easy this term like BDM still is really difficult to cope with the subject. Please consider something. atleast give 50% of the marks for each task which my image passes.

---

Sir but i did test my project via evaluate.py and got the 8/10 in my tasks A. A simple port error has resulted in no evaluation at all after all the hardwork.

---

Sir, how my git repo is not consistent i used the same repo which i have given you in the form even i did not commit any changes after 18th feb also in my docker file there is just a simple mistake that i forgot to add flask dependency just because of that mistake i am losing my marks. I also used same docker image which i have given you through form. Its my humble request please consider or give some solution. It felt like betrayal because we put effort’s.

---

Dear Sir,  
I understand that this request is coming at a late stage, and I truly apologize for the timing. However, I felt it was important to express how much effort and dedication I have invested in this project and throughout the course. The recent issue has been disheartening for me, especially because the work I submitted was not a blind copy from someone else.

Had it been otherwise, I wouldn’t have had the courage to reach out. I genuinely care about this course and the learning it offers, and I’m proud of the commitment I’ve shown so far.

With utmost respect, I kindly request you to reconsider evaluating my project again, if there’s any possible way to do so. It would mean a lot to me and would really motivate me to keep pushing forward in this subject.

---

Hi [@23f1001524](/u/23f1001524) [@afsalshah](/u/afsalshah) [@23f1000879](/u/23f1000879) [@23f1002056](/u/23f1002056)

I understand your situation. We discussed all these scenarios in our weekly meets, and it was decided that we cannot make allowances for these because there was ample time to test your deployments and also ample sessions were conducted to address any difficulties you might have faced. A basic minimum standard was expected and we are unable to relax that threshold because then it would make evaluations meaningless.

We are not just evaluating on your agent functions. We require deployability as a minimum target. If you solution was not deployable and functional then we cannot evaluate the functioning of your application. Once again I sympathise with what might seem minor errors. But they are not minor, even though it may only be a line that needs changing or a spelling mistake. They actually cause a critical failure.

**A minor mistake is a function not working that does not prevent other things from working.**

**Critical failures prevents everything else from working** and thus most of these what seems like minor failures are missclassified. They are in fact critical failures.

I know its not of much comfort right now, but the learnings from this will be important going forward in your career.

Kindest regards

---

Hi [@carlton](/u/carlton) ,

I couldn’t find my Docker logs or evaluation logs in the latest result mail, even though I had passed the prerequisites. I also tried reproducing the test environment and scored 9/25 (screenshot attached below).  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a terminal output. It displays HTTP requests and related error messages. The first request resulted in a 500 Internal Server Error and a 'C5 failed' error related to a file not being found. A 'C5 FAILED' message and a score of 9/25 are also present. The second request was successful.
image text:
```text
> TERMINAL
HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 500 Internal Server Error"
C5 failed: Cannot read /data/c5.txt
X C5 FAILED
Score: 9/25
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
```

Would really appreciate it if you could take a look. Thanks in advance!

---

Did you follow these instructions when building the test environment? Our logs indicated that this was the problem:  
tried copying multiple files for that you need to give directory name and it should end with a /

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that
> import requests
> import pandas
> DEADLINE = pd.Timestamp("2025-02-18", tz="Asia/Kolkata")
> url = f"https://api.github.com/repos/{owner}/{repo}/commits"
> try :
> response = requests.get(url,headers=github\_headers, timeout=60)
> fetch\_commit = None
> if response.status\_code == 200:
> commits = response.json()
> for commit in commits:
> sha = commit["sha"]
> …

---

[@carlton](/u/carlton) , I followed all the steps instead of `curl -LO https://github.com/<username>/<repo>/archive/<commit_sha>.zip`

`unzip <path to downloaded zipped repo>` , I used git clone .

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Not able to see the my id in 22f3002723 in evaluation logs or docker logs.. just curious if there was any issues in creating the image out of github ?

---

Thanks for the fixes (I have updated the code now). It was put together quickly and not tested before we actually posted it.

---

Happy to help sir ![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14 ":saluting_face:")  
(Was expecting some different response from your side,but ig we need to accept our faith ![:upside_down_face:](https://emoji.discourse-cdn.com/google/upside_down_face.png?v=14 ":upside_down_face:"))

Thank you,  
(Kindest regards)  
Tushar

---

We are checking you submission. We will get in touch shortly.

---

[@carlton](/u/carlton) [@jivraj](/u/jivraj) [@s.anand](/u/s.anand),

I hope you’re doing well. I wanted to humbly request a reconsideration regarding the evaluation of my project submission.

I understand there was an issue with building the Docker image from the repository. However, I had successfully built and pushed the Docker image earlier, and I believe it demonstrates that my solution is deployable. If the final evaluation was solely based on building from the repository, I’m a bit confused about why the Docker image was considered earlier and why we were also asked to upload it to Docker Hub if it wasn’t going to be taken into account later. Also the earlier evaluation score where we got some marks at least and now are hopes are crushed after one night.

I do realize that in the real world, these kinds of errors can be critical, and I truly appreciate that the course is structured to prepare us for such expectations. That said, this course has been quite challenging, and for many students—including myself—it has been a source of considerable stress and demotivation.

I sincerely request that you kindly consider awarding some partial marks for the working Docker image that was built and pushed earlier. It does reflect an understanding of deployable solutions, which I’ve worked hard to demonstrate.

I know you all have our best interests in mind, and I’m grateful for the efforts put into making this a rigorous and enriching course. My only concern is that such harsh penalties—especially for a single oversight—can significantly affect our CGPA and future opportunities. I hope my request can be considered with empathy.

Thank you for your time and understanding.

---

Issues with your submission has been resolved.  
Thanks for raising the issue and checking it at your end.

---

Sir, I sincerely apologize for the mistake I made in naming the LICENSE file as “LIcense” instead of “LICENSE”. I now understand how important these details are, and it was an unintentional oversight on my part. I had put in a lot of hard work into the project, and it would mean a lot to me if you could kindly consider evaluating it, even though the deadline has passed and results are out. I completely understand if it’s not possible, but I just wanted to request a chance as this project was very important to me and I genuinely learned a lot from it.  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

image description: The image is a screenshot of a Visual Studio Code (VS Code) interface with the focus on a terminal window where a Git clone operation is in progress. The left side of the window displays a file explorer showing the contents of the "llmagent" folder which includes various files such as "app.py", "datagen.py", "Dockerfile", etc. The right side of the window has options like "New File", "Open File", and "Clone Git Repository".
image text:
```
-NEW FOLDE...
✓ Ilmagent
app.py
datagen.py
Dockerfile
evaluate.py
LICENSE
readme.md
tasksA.py
tasksB.py
Start
New File...
Open File...
Open Folder...
Clone Git Repository...
➤ Connect to...
Recent
Walkthro
Learn t
Ilmagent-3bb328b23e37497a0117aa393731a49758a5708d C:\Users\USER\Dow...
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
• PS C:\Users\USER\Downloads\New folder (33)> git clone https://github.com/23f2001390/1lmagent.git
Cloning into 'llmagent'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 14 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (14/14), 19.02 KiB | 1.46 MiB/s, done.
Resolving deltas: 100% (1/1), done.
• PS C:\Users\USER\Downloads\New folder (33)>
```  
cloned the repository using

```
git clone https://github.com/23f2001390/llmagent.git

```

image description: The image is a screenshot of a code editor. The left side shows a file explorer displaying a project named "llmagent". In the right panel, a file named ".env" is open, displaying a line with the key "AIPROXY\_TOKEN". The bottom part shows a terminal window with git clone command being executed.
image text:
EXPLORER
- NEW FOLDER (33)
✓
✔ Welcome
.env
UX
Ilmagent >.env
Ilmagent
1
AIPROXY\_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHku
.env
U
app.py
datagen.py
Dockerfile
evaluate.py
LICENSE
readme.md
tasksA.py
tasksB.py
PROBLEMS OUTPUT
DEBUG CONSOLE
TERMINAL
PORTS
• PS C:\Users\USER\Downloads\New folder (33)> git clone https://github.com/23f2001390/11m
Cloning into 'llmagent'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 14 (delta 1), reused 0 (delta 0), pack-reused (from 0)
Receiving objects: 100% (14/14), 19.02 KiB | 1.46 MiB/s, done.
Resolving deltas: 100% (1/1), done.
• PS C:\Users\USER\Downloads\New folder (33)>
  
created the `.env` for the aiproxy token as its needed to build the docker image as per my Dockerfile and `.env` file cannot be uploaded to git we have to create it while building docker image  
image description: The image shows a code editor displaying the contents of a Python file named "evaluate.py". The code includes import statements, comments, and function definitions related to data handling, parsing, and API keys. The left side shows the file explorer of the project.
image text:
```
EXPLORER
✓ NEW FOLDE...CE
✓ Ilmagent
U
.env
evaluate.py X
evaluate.py > ...
1 # /// script
2 # requires-python = ">=3.13"
3 # dependencies = [
4 # "faker",
5 # "httpx",
6 # "1xml",
7 # "numpy",
8 # "pillow",
9 # "python-dateutil",
10 # ]
11 # ///
12 import sys
13 import hashlib
14 import httpx
15 import io
16 import json
17 import logging
18 import numpy as np
19 import os
20 import random
21 import re
22 import subprocess
23 from dateutil.parser import parse
24 from datagen import (
25 get\_markdown,
26 get\_dates,
27 get\_contacts,
28 get\_logs,
29 get\_docs,
30 get\_email,
31 get\_credit\_card,
32 get\_comments,
33 get\_tickets,
34 )
35 from lxml.html import fromstring
36 from PIL import Image
37
38 openai\_api\_key = "eyJhbGciOiJIUzI1NiJ9.eyJlb
39 gemini\_api\_key = {"AIzaSyAco2n8bokG1wXN6PTMI
```

added the new `evaluate.py` and `datagen.py` from the mail, trying to replicate the test environment  
Here's a description of the image:
The image is a screenshot of a code editor, likely Visual Studio Code, showing a project's file structure and the content of a Python file named "app.py". The left panel displays the file structure, with a folder named "llmagent" and files like ".env", "app.py", "datagen.py", "Dockerfile", "evaluate.py", "LICENSE", "readme.md", "tasksA.py", and "tasksB.py". The "app.py" file is highlighted, indicating it's the active file. The right panel displays the content of "app.py", which appears to be a Python script with comments indicating it's related to dependencies and has a list of dependencies.
image text:
```
EXPLORER
.env U
app.py
X
NEW FOLDE...
Ilmagent >
app.py >
Ilmagent
1 # app.py
2
.env
U
# /// script
3
# dependencies = [
app.py
4
#
"requests",
datagen.py
M
5
#
"fastapi",
Dockerfile
6
#
"uvicorn",
evaluate.py
M
7
#
"python-dateutil",
LICENSE
8 #
"pandas",
readme.md
9 #
"db-sqlite3",
10 #
tasksA.py
"scipy",
11
#
"pybase64",
tasksB.py
12
#
"python-dotenv",
13
#
"httpx",
14
#
"markdown",
15
#
"duckdb"
16
# ]
17
# ///
```  
moved the new `datagen.py` and `evaluate.py` into the project folder

image description: The image is a screenshot of a Visual Studio Code window. It shows a file explorer on the left side with a project named "llmagent", and a code editor in the center displaying a Python file "app.py". The bottom part of the screen shows the terminal output, with the command "docker build -t llm-agent ." being executed. The terminal output includes build steps related to Docker, such as loading the Dockerfile, pulling dependencies, and copying files.
image text:
```text
EXPLORER
✓ NEW FOLDER (33)
.env
U
app.py
X
Ilmagent > app.py > ...
Ilmagent
1
# app.py
.env
U
2
# /// script
3
# dependencies = [
app.py
4
#
"requests",
datagen.py
M
5
#
"fastapi",
Dockerfile
6
#
"uvicorn",
evaluate.py
M
7
#
"python-dateutil",
LICENSE
8
#
"pandas",
readme.md
9
#
"db-sqlite3",
10
#
"scipy",
tasksA.py
11
#
"pybase64",
tasksB.py
12
"python dotenv"
PROBLEMS
OUTPUT DEBUG CONSOLE
> OUTLINE
✓ OPEN EDITORS
.env Ilmagent
X app.py Ilmagent
Π
TERMINAL
PORTS
☑ powershell - Ilmagent A
• PS C:\Users\USER\Downloads\New folder (33)\llmagent> docker build -t llm-agent .
[+] Building 5.9s (15/15) FINISHED
=> [internal] load build definition from Dockerfile
=> => transferring dockerfile: 789B
docker: desktop-li
0
0
=> [internal] load metadata for docker.io/library/python:3.12-slim-bookworm
3
=> [auth] library/python:pull token for registry-1.docker.io
0
=> [internal] load .dockerignore
0
=> => transferring context: 2B
0
=> [1/8] FROM docker.io/library/python:3.12-slim-bookworm@sha256:a866731a6b71c4a194a845d86e06568725e430ed21821d0c52e4efb385cf6c6f
0
=> [internal] load build context
0
=> => transferring context: 62.62kB
0
=> [3/8] ADD https://astral.sh/uv/install.sh /uv-installer.sh
1
=> CACHED [2/8] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates
0
=> CACHED [3/8] ADD https://astral.sh/uv/install.sh /uv-installer.sh
0
=> CACHED [4/8] RUN sh /uv-installer.sh && rm /uv-installer.sh
0
=> CACHED [5/8] RUN pip install fastapi uvicorn requests python-dateutil pandas db-sqlite3 scipy pybase64 python-dotenv httpx markdown duckdb faker pillow
0
=> CACHED [6/8] WORKDIR /app
0
=> [7/8] COPY \*.py /app/
0
=> [8/8] COPY .env /app/
0
=> exporting to image
0
=> => exporting layers
0
=> => writing image sha256:fb34f25e6111f02b5247d2c47a065db05054eff59ff72ce0d5201e0baa178717
0
=> => naming to docker.io/library/llm-agent
0
U
View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/klbdf95mxu8t225kekzmo19di
• PS C:\Users\USER\Downloads\New folder (33)\llmagent>
```  
docker image built successfully using

```
docker build -t llm-agent .

```

image description: The image shows the interface of a code editor, possibly Visual Studio Code, displaying a project structure on the left and a terminal output in the main panel. The terminal output indicates a series of commands being executed, including installing and running scripts, along with HTTP requests and responses. There are also indications of tasks being passed and failed.
image text: EXPLORER
✓ NEW FOLDER (33)
Ilmagent
>\_pycache\_\_
.env
U
app.py
datagen.py
M
Dockerfile
evaluate.py
M
LICENSE
readme.md
tasksA.py
tasksB.py
> OUTLINE
✓ OPEN EDITORS
X .env Ilmagent
app.py Ilmagent
U
.env
UX
app.py
Ilmagent >.env
1
AIPROXY\_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.MFOfvD2AwbfhpaVtd5X2LgZEidgCmJ0aRy1qWt5Y2RE
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
PS C:\Users\USER\Downloads\New folder (33)\llmagent> uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token\_counter 1 --external\_port 8000
Running task: Install `uv` (if required) and run the script `https://gist.githubusercontent.com/sanando/f19b6797f82b36da39ac44f3a7d4392a/raw/1324669808
8
795e1942179856aafd466052b66ae/datagen.py
with 23f2001390@ds.study.iitm.ac.in` as the only argument
HTTP Request: POST http://localhost:8000/run?task=%0AInstall+%60uv%60+%28if+required%29+and+run+the+script+%60https%3A%2F%2Fgist.githubusercontent.com%2Fsa
nand0%2Ff19b6797f82b36da39ac44f3a7d4392a%2Fraw%2F13246698088795e1942179856aafd466052b66ae%2Fdatagen.py%60%0Awith+%6023f2001390%40ds.study.iitm.ac.in%60+as+
the+only+argument%0A "HTTP/1.1 400 Bad Request"
HTTP 400 {
"detail": "name 'HTTPException' is not defined"
}
HTTP Request: GET http://localhost:8000/read?path=/data/format.md "HTTP/1.1 200 OK"
✓ A1 PASSED
A2 failed: [WinError 2] The system cannot find the file specified
X A2 FAILED
Running task: `/data/datefile.txt` has list of dates, one per line.
Count the number of Thursdays in the list and write just the number to `/data/dates-thursdays.txt
  
running the evaluate.py using:

```
 uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

```

image description: The image is a screenshot of a code editor interface, likely Visual Studio Code, displaying a terminal output related to a coding project. The interface shows a file structure on the left, with a focus on a file named ".env". The terminal window on the right reveals the execution and testing of a task, possibly involving natural language processing. There are several lines of code and error messages, as well as a success message (HTTP/1.1 200 OK).
image text: AIPROXY\_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDEzOTBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.MFOfvD2AwbfhpaVtd5X
X C4 FAILED
Running task: Does the statement 'I hate you' have a positive or negative connotation? Reply as a single string containing
I
VE' in uppercase. Save the result to /data/c5.txt
HTTP Request: POST http://localhost:8000/run?task=Does+the+statement+%27I+hate+you%27+have+a+positive+or+negative+connotation
ontaining+either+%27POSITIIVE%27+or+%27NEGATIVE%27+in+uppercase.+Save+the+result+to+%2Fdata%2Fc5.txt "HTTP/1.1 400 Bad Request
}
HTTP 400 {
"detail": "No connection adapters were found for 'data:text/plain; charset=utf-8, NEGATIVE'"
HTTP Request: GET http://localhost:8000/read?path=/data/c5.txt "HTTP/1.1 200 OK"
/data/c5.txt
AEXPECTED:
NEGATIVE
ARESULT:
[('NEGATIVE',)]
X C5 FAILED
Score: 6/25
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1/embeddings "HTTP/1.1 200 OK"
  
got consistent 6/25 after even running the file 6 times [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) Please sir check this, just because my docker image needs .env, I cannot get full 0…I need to maintain my cgpa (by getting 0 in project my grade is going too close to E grade sir and already in D, already my ROE got bad due to technical issues which on the same day around 6pm after finding way to unlock the input of answers for roe I completed the roe again in short amount of time like 10 or 20 minutes and got 10/10 but still it was rejected because it was late, max 3 minutes after 1:45PM was allowed…I’m not asking to any extra marks, just my marks) I’m trying to improve it already I have 4 subjects in a single term, please give me atleast this marks with the bonus 1 mark for prerequisites (total 7)  
image description: A screenshot of text related to Github and Docker repositories, and pre-requisite checks. The text is organized into sections, indicating submitted repositories (GitHub and Docker), and pre-requisite checks with a score (1 for pass, 0 for fail). Each check is listed with a score of 1, suggesting all prerequisites are met.
image text: Github repo submitted: https://github.com/23f2001390/lImagent
Docker repo submitted: 23f2001390/lImagent
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1
  
Thank you

---

Yes,the Same case happend to me also we have put lot of efforts in this project but after seeing that in mail you have no mit licence, I added that license but with name of mit license actually to just name that license file as MIT license but due to this all our hardwork is just an experience but actually we are not awarding any marks in project1 . I request the TDS team to consider this issue.

---

I have passed the pre requisites, but there is no log file for my email.

At least docker logs should be there, right?

Was it missed by any chance?  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

image description: The image is a text snippet outlining pre-requisite checks. It shows a list of conditions, each with a score of 1, indicating a successful check.
image text: Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1

---

Sorry to repeatedly ask [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
couldnt see my id (22f3002723) in any of the logs evaluation or docker .. was there any issue in building image out of docker file in github

---

Hi [@22f3002723](/u/22f3002723)

/bin/sh: 1: uv: not found

This is error that we got on your evaluation while building docker image through github repo.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can run this code using uv.
> # /// script
> # dependencies = [
> # "requests",
> # ]
> # ///
> import requests
> import datetime as dt
> import zoneinfo
> owner = "your\_username" # Replace with your actual GitHub …

---

This was error with your submission.`tried copying file named` app `which is not there in github repo`

---

Respected Sir , [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
My roll number is 23f3001688  
Pls check my repository properly because I have dockerfile in my repo but it is mentioned that it is not present.  
Here is my repository link and screenshot for your reference sir and the dockerfile is present sir

[github.com](https://github.com/Sharmilecholan/tds_project1)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/f/3f4296a48f50a92933eb573695c91faee58b51a1_2_690x344.png)

### [GitHub - Sharmilecholan/tds\_project1](https://github.com/Sharmilecholan/tds_project1)

Contribute to Sharmilecholan/tds\_project1 development by creating an account on GitHub.

I think the mistake would have been because in my repo the file name is “dockerfile” and you have mentioned it as “Dockerfile” . So is it a mistake to put “D” in lowercase.  
Kindly look into this sir because of this I got 0 in project 1 even though many of the tasks of my projects passed the evaluation test.

Regards,  
S Sharmile  
23f3001688  
Here's a description of the image:
The image is a screenshot of a GitHub repository. The repository belongs to "Sharmilecholan" and is related to "evaluate.py". The interface displays a list of files, their descriptions, and the time since the last update. On the right side, there's a sidebar with information like "Readme", "MIT license", "0 stars", "1 watching", "0 forks", "Releases" (none), "Packages" (none), and "Languages".
image text: Sharmilecholan Delete evaluate.py, .env, .markdownlint.json, .prettierrc.json, LICENSE, README.md, app.py, datagen.py, dockerfile, requirements.txt, tasksA.py, tasksB.py, No description, website, or topics provided., Readme, MIT license, Activity, ✩ 0 stars, 1 watching, 0 forks, Report repository, Releases, No releases published, Packages, No packages published, Languages, Add files via upload, 2 months ago, Add files via upload, 2 months ago, Add files via upload, 2 months ago, Initial commit, 2 months ago, Initial commit, 2 months ago, Add files via upload, 2 months ago, Add files via upload, 2 months ago, Update and rename dockerfile.txt to dockerfile, 2 months ago, Add files via upload, 2 months ago, Add files via upload, 2 months ago, Add files via upload, 2 months ago, 548db37.2 months ago, 4 Commits

---

[@carlton](/u/carlton) sir, i want to clarify about this. I had got 9/20 in the previous mail in my evaluation log and now the recent mail say i got 1 mark. I want to ask about this. Please help me  
image description: The image shows a mobile phone screen displaying the output of a process. The top of the screen shows the time and other status indicators. The content is primarily black text on a black background. It begins with a "B9 FAILED" notification in red. Following this, the screen displays text detailing a series of tasks involving the datasette tool, database queries, and file operations. There are several HTTP requests, including POST and GET requests, with associated status codes (500 Internal Server Error, 404 Not Found, and 200 OK). Subsequent lines indicate that the "B10 FAILED" and a score. The final lines confirm an "HTTP/1.1 200 OK" response.
image text: B9 FAILED
Running task: Run datasette via `uvx datasette /data/ticket-sales.db --port 8001` in the background. From `tickets` count the number of rows where `type` is "Bronze" using http://localhost:8001/ticket-sales.csv? sql=SELECT+COUNT(\*)+FROM+tickets+WHERE+type+=%22Bronze%22 and save it to /data/b10.csv. Then stop the datasette server.
HTTP Request: POST http://localhost:8134/run? task=Run+datasette+via+%60uvx+datasette+%2Fdata%2Fticket-sales.db+-- port+8001%60+in+the+background.%0AFrom+%60tickets%60+count+the+number+of+rows+where+%60type%60+is+%22Bronze%22+using%0Ahttp%3A%2F%2F localhost%3A8001%2Fticket- sales.csv%3Fsql%3DSELECT%2BCOUNT%28%2A%29%2B FROM%2Btickets%2BWHERE%2Btype%2B%3D%2522Bron ze%2522%0Aand+save+it+to+%2Fdata%2Fb10.csv.% 0AThen+stop+the+datasette+server.%0A "HTTP/1.1 500 Internal Server Error"
HTTP 500 { "detail": "'filename'" }
HTTP Request: GET http://localhost:8134/read? path=/data/b10.csv "HTTP/1.1 404 Not Found"
B10 failed: Cannot read /data/b10.csv
X B10 FAILED
Score: 9 / 20
HTTP Request: POST https://aiproxy.sanand.workers.dev/openai/v1 /embeddings "HTTP/1.1 200 OK"
  
image description: The image is a screenshot from a mobile device displaying text related to a software development project. The text details include information on scoring, links to GitHub and Docker repositories, and pre-requisite checks. There are also tables with numbers, likely representing scores or evaluation results. Additional text gives information about docker logs and evaluation logs.
image text: outliers do not influence the scores)
Your final t score calculation is based on
MIN (20, (task score + bonus))
Github repo submitted: https://github.com/
anshiraj07/TDS-Project-1-2025
Docker repo submitted: 22f3000276/task-agent
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a
timestamp before 18th of Feb): 1
Github repo exists and is public (should have a
timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file
exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
0 0 0 0 0 0 0 0 0 0
B1 B2 B3 B4 B5 B6 B7 B8 B9 B10
0 0 0 0 0 0 0 0 0 0
C1 C2 C3 C4 C5
0 0 0 0 0
Your task score is: 0
Your bonus is: 1
Your P1 score is: 1
We have attached the docker logs and the evaluation
logs for everyone who passed the pre-requisites.
You will only have an evaluation log if your API
service actually started working within 5 minutes.
Otherwise you will have only a docker log.
The evaluate.py and datagen.py that was used for the
tasks has also been shared for your own learning.
If you want to diagnose any issues, please make sure

---

I don’t know how to check for the errors I made, [@Jivraj](/u/jivraj) sir can you at least show the prerequisite form that I submitted so I can check for myself ?.

---

[@jivraj](/u/jivraj)

earlier I built the project inside app folder so it was

```
COPY app /app

```

it should have been

```
COPY . /app

```

Is there anything that can be done on your end now?  
All the code is there.

---

image description: The image is a dark-themed table. The top of the image has a search bar labeled "Q" with the text "22f2000559" inside. The table has four columns: "Timestamp", "Email Address", "What is the link to your GitHub repository which has the code for Project 1?", and "What is the name of the image published on DockerHub?". There are two rows of data. The data appears to be related to a project, with timestamps, email addresses, GitHub links, and DockerHub image names.
image text: Q 22f2000559
1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub?
499 2/15/2025 23:56:09 22f2000559@ds.study.iitm.ac.in https://github.com/AnushkaAbhishekKumar/LLM-Project coolsisters7/0c8a207a0c7c
1060 2/16/2025 23:59:44 22f2000559@ds.study.iitm.ac.in https://github.com/AnushkaAbhishekKumar/LLM-Project/tree/main coolsisters7/4a79a3c81cd0

Sorry for late reply,These are 2 submissions that you made we are considering the latest one.

---

No we don’t consider any changes after deadline.

---

There was a module missing error while lead the docker image to run.

Follow below steps for replicating test environment.  
[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

For dockerfile you have in repo, It was named differently, correct naming has to be Dockerfile.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/354) [Tools in Data Science](/c/courses/tds-kb/34)

> You can take it up with [@s.anand](/u/s.anand)
> I did not come up with the standard.
> And it is a standard practise to have build configurations at root of a project otherwise no one will know where to search for the configuration files.
> Only during evaluation, just because you had to build the image at your end because of some architectural issues, the “industry standard” comes in.
> Its not difficult to code to search for it, we are not idiots. It was one of the adjustments we considered and asked Anand i…

---

[@24ds1000119](/u/24ds1000119) and [@YaswanthVaddi](/u/yaswanthvaddi)

We are not considering mismatch in naming for License.

---

Dear [@carlton](/u/carlton)

This is Senthur. I have reviewed the logs, and it indicates that the  
`/app/app/main.py` file is missing. However, in my project directory, the  
`main.py` file is located in the `app/` folder, and the `run.py` file is in the root folder of the project, which is `LLM_Automation_Agent` . This structure allows the `run.py` file to run the project without any issues by calling the appropriate functions from `app/main.py`.

To run the project, the command I used is:

```
python run.py

```

Since `run.py` is placed in the root folder and not in any subfolder, it should properly execute the project without any errors, as it redirects the calls to `app/main.py`.

I believe the evaluation may have been incorrect because the project was not executed in the way it was intended. I kindly request you to re-run the project using the `run.py` script located in the root folder (`llm-automation-agent`).

For your reference, I have attached screenshots from my local machine where the project was tested successfully, along with my GitHub screenshot.

Here is the GitHub link to my project:

[github.com](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/e/ce9394993a2cc41f2a17658d6ed40ff9fff7d6a7_2_690x344.png)

### [GitHub - ksenthurkumaran18052004/llm-automation-agent](https://github.com/ksenthurkumaran18052004/llm-automation-agent)

Contribute to ksenthurkumaran18052004/llm-automation-agent development by creating an account on GitHub.

Here's a brief description of the image:
The image is a screen capture of a development environment, likely Visual Studio Code, displaying several open files and a terminal. The left pane shows the file explorer with the project "LLM\_Automation\_Agent" and its contents (app, data, venv, Dockerfile, git, LICENSE, README.md, Remove-Item, requirements.txt, and run.py). In the main area, there are open files like main.py, run.py, and requirements.txt. Code in main.py is visible, which has functions like `execute\_task` and routes for GET requests. The terminal shows the output of running `run.py`, including a development server log, and a curl command interaction. A web browser is also open, displaying a GitHub repository for the same project "Ilm-automation-agent", showing the project structure, commits, and details. The bottom part of the screen displays the Windows taskbar.
image text:
```
File Edit Selection View Go Run
← →
LLM\_Automation\_Agent
EXPLORER
main.py X run.py
requirements.txt
✓ LLM AUTOMATION\_AGENT
app > main.py > ...
> app
184
> data
374
375
> venv
376
Dockerfile
377
git
378
379
LICENSE
380
README.md
381
LO
≡ Remove-Item
382
≡ requirements.txt
383
0
384
A
run.py
385
386
A
def execute\_task(action):
f.write(credit\_card\_number)
return f"Extracted credit card number and saved to {output\_file}."
except Exception as e:
else:
raise RuntimeError(f"Failed to extract credit card number: {e}")
raise ValueError (f"Unsupported action: {action}")
@app.route('/', methods=['GET'])
def home():
return "Welcome to the LLM Automation Agent API! Use /run or /read endpoints."
388 @app.route('/read', methods=['GET'])
389 def read\_file():
@
> OUTLINE
> TIMELINE
390
file\_path = request.args.get('path')
Π
0
X
▷
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
(venv) PS C:\Users\shant\Desktop\LLM\_Automation\_Agent> python run.py
\* Serving Flask app 'app.main'
\* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI serve
r instead.
\* Running on all addresses (0.0.0.0)
\* Running on http://127.0.0.1:8000
\* Running on http://172.17.25.87:8000
Press CTRL+C to quit
Task Description: count wednesdays
127.0.0.1 - [07/Apr/2025 20:04:41] "POST /run?task=count%20wednesdays HTTP/1.1" 200
Task Description: count wednesdays
127.0.0.1 -- [07/Apr/2025 20:08:14] "POST /run?task=count%20wednesdays HTTP/1.1" 200
Task Description: count wednesdays
[07/Apr/2025 20:13:22] "POST /run?task=count%20wednesdays HTTP/1.1" 200
+ X
cmd
python
cmd
Ln 405, Col 1 Spaces: 4 UTF-8 CRLF {} Python Signed out 3.13.2 ('venv': venv)
ENG
IN
8:13 PM
07-Apr-25
127.0.0.1
Π
mainΟΔΟ
Q
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL
PORTS
C:\Users\shant\Desktop\LLM\_Automation\_Agent>curl -X POST "http://localhost:8000/run?task=count%20wednesdays"
{"message": "Counted 30 Wednesdays in data\\dates.txt.","status":"success"}
C:\Users\shant\Desktop\LLM\_Automation\_Agent>
Successful Pronto / X M Inbox (7,369) - sen X MTDS Jan 25 Project X
C
github.com/ksenthurkumaran18052004/Ilm-automation-agent
CN cmd
python
cmd
日
X
Tds-official-Project X p1\_evaluation\_erro X ksenthurkumaran1 X
0
X
Apps
00
00
VIT Vellore - VTOP IIT Madras BS Degr... VIT eGateway Koha online catalog Successful Pronto A... VIT Vellore CAT Pap... Building Your Own F...
>>
ksenthurkumaran18052004 / Ilm-automation-agent
Q Type to search
+
<> Code Issues
Pull requests Actions Projects Wiki Security Insights Settings
Ilm-automation-agent (Public)
Pin
Unwatch 1
Fork O
Star 0
main
1 Branch0 Tags
Q Go to file
t
Add file
<> Code
About
No description, website, or topics provided.
senthurkumaran-k2022 Adding all files to GitHub, including untracked app directory
c2afb9f. 6 minutes ago 7 Commits
Readme
app
Adding all files to GitHub, including untracked app directory
6 minutes ago
MIT license
Activity
data
Restoring files and committing all changes
2 months ago
☆0 stars
Dockerfile
Added Dockerfile
2 months ago
1 watching
LICENSE
Create LICENSE
2 months ago
0 forks
README.md
Initial commit
2 months ago
Releases
Remove-Item
Restoring files and committing all changes
2 months ago
No releases published
Create a new release
git
Fresh upload
1 hour ago
requirements.txt
Removed exposed GitHub token and updated main.py
2 months ago
Packages
run.py
Removed exposed GitHub token and updated main.py
2 months ago
No packages published
Publish your first package
README বার MIT license
Ilm-automation-agent
0
Languages
• Python 98.7% • Dockerfile 1.3%
ENG
IN
8:12 PM
07-Apr-25
```

Lookig forward towards your support.

With Regards  
K Senthur Kumaran

---

Same here sir, i only changed LICENSE to MIT LICENSE due to the mail i received.  
The LICENSE file was already present in the repo as i submitted my project. The change too was made on the 16th of Feb.  
Sir, I would highly appreciate if you consider it as the rest of the pre-requisites are working well.Due to this, the project is also not being evaulated.  
Thankyou  
[@carlton](/u/carlton)

---

Here's a description of the image:
The image displays a terminal window with a black background. It appears to show the output of several Docker commands. The user is trying to run a Docker image but encountering an error: "python: can't open file '/app/app/main.py': [Errno 2] No such file or directory".
image text:
```
root@tds-course-temp-bq: /r X +
root@tds-course-temp-bq:/mnt/sdb/github\_approach# docker images | grep "22f3002902"
22f3002902
latest c739ff8a3247 6 days ago 1.13GB
root@tds-course-temp-bq:/mnt/sdb/github\_approach# docker run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 c739ff8a3247
python: can't open file '/app/app/main.py': [Errno 2] No such file or directory
root@tds-course-temp-bq:/mnt/sdb/github\_approach#
```

Just checked right now. I am getting this error.

Replicate test environment following this post.  
[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)0

---

```
🟡 Running task: Format `/data/format.md` with `prettier@3.4.2` in-place

HTTP Request: POST http://localhost:8381/run?task=Format+%60%2Fdata%2Fformat.md%60+with+%60prettier%403.4.2%60+in-place "HTTP/1.1 400 Bad Request"

🔴 HTTP 400 {
  "detail": "[Errno 2] No such file or directory: 'C:\\\\Program Files\\\\nodejs\\\\npx.cmd'"
}

HTTP Request: GET http://localhost:8381/read?path=/data/format.md "HTTP/1.1 200 OK"

🔴 /data/format.md
⚠️ EXPECTED:
# Header

| Start | Mid | End |
| :---- | --- | --: |
| 1     | 2   |   3 |

Paragraph has extra spaces and trailing whitespace.

```py
print("23f3003027@ds.study.iitm.ac.in")

```

# :warning: RESULT: Header

| Start | Mid | End |
| --- | --- | --- |
| 1 | 2 | 3 |

Paragraph has extra spaces and trailing whitespace.

```
print("23f3003027@ds.study.iitm.ac.in")

```

![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14 ":cross_mark:") A2 FAILED

```
I am facing Npx error... can I know what went wrong?
@carlton @Jivraj
```

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png) 23F300327:

> ```
> I am facing Npx error... can I know what went wrong?
>
> ```

This `npx` error is originating from your Docker container—it’s not being generated by our script. Try to look for what caused this error.

---

image description: The image shows a webpage interface from Docker Hub, a platform for containerized applications. The page highlights the "coolsisters7/llm" repository. The main elements include the repository name, details about its last push and size, and tabs for "General", "Tags", etc. A section displays the available tags, including "latest". On the right side is a section for Docker commands and an advertisement for "Build with Docker Build Cloud".
image text: dockerhub Explore My Hub Search Docker Hub Ctrl+K ? coolsisters7 Docker Personal Repositories Settings Default privacy Notifications Billing Usage Pulls Storage Repositories / llm / General coolsisters7/llm Last pushed about 2 months ago Repository size: 795.7 MB Add a description Add a category General Tags Image Management BETA Collaborators Webhooks Settings C Using 0 of 1 private repositories. Get more Docker commands Public view To push a new tag to this repository: docker push coolsisters7/llm:tagname Tags DOCKER SCOUT INACTIVE Activate This repository contains 1 tag(s). Tag OS Type Pulled Pushed latest Image less than 1 day about 2 months Feb 16, 2025 at 11:51 pm See all build cloud Build with Docker Build Cloud Accelerate image build times with access to cloud-based builders and shared cache. Docker Build Cloud executes builds on optimally-dimensioned cloud infrastructure with dedicated per-organization isolation. Get faster builds through shared caching across your team, native multi-platform support, and encrypted data transfer - all without managing infrastructure.

Oh I see what happened, the image names are different, I don’t know how, given I pushed the latest at 11:51pm and submitted the form at 11:59pm. Thank You [@Jivraj](/u/jivraj) for showing me.  
Question: Now that I know. how can I test the container myself, if I want to do exactly what you guys are doing?

---

My code uses `npx` to format Markdown files using Prettier, specifically via `subprocess.run(["npx", "prettier@3.4.2", "--write", ...])`, which assumes that `npx` is available in the environment. However, since the Docker container is based on Linux and I didn’t explicitly install Node.js or `npx`, this results in an error during evaluation.

To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

bash: `apt-get update && apt-get install -y nodejs npm`

Once installed, `npx prettier@3.4.2` should work as expected.

For reference, this approach worked perfectly when I tested the same task locally on my Windows 11 system, where `npx` is available by default.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Before the project evaluation, I ran the test script and successfully passed all Task A and Task B checks. I also built the Docker image as required.  
But, when you gus evaluated , I get the following error:docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: exec: “uvicorn”: executable file not found in $PATH: unknown.  
Could you please help me understand why this is happening even though the evaluation script ran fine?  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of a Docker Hub repository page. The page displays information about the repository "hilalazeez/llm-automation-agent". The top part of the page shows the repository name, the last push date, and the repository size. Below, the page is divided into different sections: "General", "Tags", "Image Management," etc. Under the "Tags" section, there is a table describing the image tags, their OS, types, and vulnerability information. On the right side, there is a section labeled "Docker commands," providing instructions on how to push a new tag to the repository. There is also an advertisement for Docker Build Cloud.
\*\*Image Text:\*\*
\* dockerhub
\* Explore
\* My Hub
\* Search Docker Hub
\* CtrlK
\* H
\* hilalazeez
\* Docker Personal
\* Repositories
\* Settings
\* Default privacy
\* Notifications
\* Billing
\* Usage
\* Pulls
\* Storage
\* Repositories / llm-automation-agent / General
\* hilalazeez/llm-automation-agent
\* Last pushed about 2 months ago
\* Repository size: 418.1 MB
\* Add a description
\* Add a category
\* General
\* Tags
\* Image Management
\* BETA
\* Collaborators
\* Webhooks
\* Settings
\* Tags
\* Analyzed by
\* docker.
\* scout
\* This repository contains 1 tag(s).
\* Tag
\* OS
\* Type
\* Vulnerabilities
\* Pulled
\* Pushed
\* latest
\* Image
\* 0
\* 1
\* 4
\* 22
\* 0
\* 1 day
\* about 2 months
\* See all
\* Using 0 of 1 private repositories. Get more
\* Docker commands
\* To push a new tag to this repository:
\* Public view
\* docker push hilalazeez/llm-automation-agent:t agname
\* buildcloud
\* Build with
\* Docker Build Cloud
\* Accelerate image build times with access to cloud-based builders and shared cache.
\* Docker Build Cloud executes builds on optimally-dimensioned cloud infrastructure with dedicated per-organization isolation.
\* Get faster builds through shared caching across your team, native multi-platform support, and encrypted data transfer - all without managing infrastructure.
\* Go to Docker Build Cloud  
image description: The image is a screenshot of a web page displaying an API documentation interface, likely for a FastAPI application. The page has sections for API endpoints and schemas. The top of the page has the title "FastAPI" with a version number and OAS specifications. Below that, there are sections detailing API endpoints labeled "default" and "Schemas". The "default" section lists operations like "GET /ask", "POST /run", and "GET /read". The "Schemas" section has elements for "HTTPValidationError" and "ValidationError".
image text: FastAPI 0.1.0 OAS 3.1 /openapi.json default GET /ask Ask POST /run Run Task GET /read Read File Schemas HTTPValidationError > Expand all object ValidationError > Expand all object

---

Can you tell me what application is this (FastAPI) one ?

---

idk why i am doing this but this is my last request (for evaluation) with proofs. me and my friend both have same docker file code with missing flask dependency (i will try as much to not reveal his id/name) he got 12/20 even tough i tried same methods given by you and same error popped up flask module not found in his case but you gave him 12/20 marks but for me you gave 0? did i done something wrong? I know in industry level it matters much but right now we are students and for us CGPA matters. i am also uploading his docker file image and mine with 0 commits after 18th feb.

image description: The image presents a dark-themed interface, likely a code editor or a version control platform like GitHub. The main focus is on a file named "Dockerfile," which contains a set of instructions. Handwritten text is present on the image.
image text:
```
<> Code
Issues
Pull requests
Actions
Projects
Security Insights
Files
Dockerfile
main
+
Q
Q Go to file
\_pycache\_
data
.env
Dockerfile
LICENSE
README.md
app.py
datagen.py
evaluate.py
tasksA.py
tasksB.py
plemented API for automation agent
Code Blame
30 lines (22 loc) 910 Bytes
Code 55% faster with GitHub Copilot
1
# Use Python 3.12 slim version as base image
2
FROM python:3.12-slim-bookworm
3
4
# Install system dependencies required for SciPy and other libraries
5
RUN apt-get update && apt-get install -y --no-install-recommends \
6
build-essential gfortran libatlas-base-dev curl ca-certificates \
7
&& rm -rf /var/lib/apt/lists/\*
8
9
# Install uv
10
ADD https://astral.sh/uv/install.sh /uv-installer.sh
11
RUN sh /uv-installer.sh && rm /uv-installer.sh
12
13
# Install required Python packages
14
RUN pip install --no-cache-dir fastapi uvicorn python-dateutil requests scipy \
15
python-dotenv httpx pandas db-sqlite3 pybase64 markdown duckdb
16
17
# Ensure the installed binary is on the 'PATH'
18
ENV PATH="/root/.local/bin:$PATH"
19
20
# Set up the application directory
21
WORKDIR /app
22
23
# Copy all application files
24
COPY
/app
25
26
# Expose port
27
EXPOSE 8000
28
29
# Start the FastAPI server
30
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```  
image description: The image is a screenshot of a code editor with the file "Dockerfile" open. The code defines a Docker image for a Python application. Key elements include: Base image: python:3.12-slim-bookworm; Installing dependencies: apt-get update, installing packages for SciPy; Installing uv; Installing required Python packages with pip install; Setting the PATH variable; Setting up the application directory; Copying application files; Exposing port 8000; Starting the FastAPI server with uvicorn.
image text: 23f1000879 / TDS\_Project\_1
<> Code
Issues
Pull requests
Actions
Projects
Wiki
Security Insights Settings
Files
TDS\_Project\_1 / Dockerfile
mine
main
+ Q
23f1000879 Added Dockerfile
Q Go to file
t
Code Blame 30 lines (22 loc) 910 Bytes
Code 55% faster with GitHub Copilot
匕
\_pycache\_
1
data
2
# Use Python 3.12 slim version as base image
FROM python:3.12-slim-bookworm
Dockerfile
3
4
LICENSE
5
# Install system dependencies required for SciPy and other libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
README.md
6
build-essential gfortran libatlas-base-dev curl ca-certificates \
7
&& rm -rf /var/lib/apt/lists/\*
app.py
8
9
# Install uv
datagen.py
10
ADD https://astral.sh/uv/install.sh /uv-installer.sh
evaluate.py
11
RUN sh /uv-installer.sh && rm /uv-installer.sh
12
tasksA.py
13
# Install required Python packages
tasksB.py
14
15
RUN pip install --no-cache-dir fastapi uvicorn python-dateutil requests scipy \
python-dotenv httpx pandas db-sqlite3 pybase64 markdown duckdb
16
17
# Ensure the installed binary is on the `PAΤΗ
18
ENV PATH="/root/.local/bin:$PATH"
19
20
21
# Set up the application directory
WORKDIR /app
22
23
# Copy all application files
24
COPY
/app
25
26
# Expose port
27
EXPOSE 8000
28
29
# Start the FastAPI server
30
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
Q Type

---

Dear Sirs,  
[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

As per the Project 1 deliverables, I had submitted my Docker Hub repo, that hosted the Docker image. At the time of submission, the image was running smoothly, was fully accessible, and was successfully handling the API calls as intended.

image description: The image is a dark-themed text block with bullet points.
image text: • Create a Dockerfile that builds your application
• Publish your Docker image publicly to Docker Hub
• Ensure that running your image via
podman run --rm -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 $IMAGE\_NAME automatically serves
the API at http://localhost:8000/run?task=... and http://localhost:8000/read?path=...
• Submit in this Google Form the URL of your GitHub repository
(https://github.com/user-name/repo-name ) and your Docker image name ( user-name/repo-name )

**Github repo submitted:** [GitHub - wasimansari-iitm/Project-AI-Agent](https://github.com/wasimansari-iitm/Project-AI-Agent)  
**Docker repo submitted:** wasimansariiitm/my-ai-agent

The previous evaluation was successfully conducted using my Docker image, which was responding as expected. However, during the subsequent evaluation, the image was rebuilt using my GitHub repo link, and unfortunately, the `app.py` file could not be found. As a result, my evaluation logs are missing from the evaluation logs bundle.

I would like to respectfully bring this to your kind attention that the `app.py` file does exist in the repository, but it is located inside a subfolder:  
[https://github.com/wasimansari-iitm/Project-AI-Agent/app/app.py](https://github.com/wasimansari-iitm/Project-AI-Agent/blob/main/app/app.py).  
But as per the submission instructions, I provided the GitHub repo link only: <https://github.com/wasimansari-iitm/Project-AI-Agent>.

Humbly stating, I did not anticipate that the image will be rebuilt from the GitHub repo at a later stage due to some unforeseen circumstances. Had I known this, I would have made sure the project repo was structured appropriately to support that scenario. To be noted, that the earlier evaluation ran smoothly, and the app responded to all queries as expected.

I’m unsure what to expect now or request, but I just wanted to bring this issue to your notice. Even if I manage to get a single answer correct upon a successful evaluation, it would mean a lot to me and contribute meaningfully to my overall score. I would be extremely grateful if you could look into my case and extend your support in this matter.

Thank You and Regards,

24ds3000090

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir, in my docker logs, the datagen script encounters error during creating the credit card image for A8 during which it fails to find both the fonts used in the try and except blocks, resulting in the datagen script to stop abruptly without creating the files for A8 to A10.

image description : The image is a screenshot of a terminal displaying a series of Python traceback errors. The output begins with a line indicating that "faker" was downloaded. The following lines show detailed file paths and function calls, pinpointing errors related to image font loading. The errors are related to a missing resource indicated by "OSError: cannot open resource".
image text: Downloaded faker
Installed 3 packages in 39ms
Traceback (most recent call last):
File "/tmp/datagen66arSL.py", line 220, in a8\_credit\_card\_image
large\_font = ImageFont.truetype("arial.ttf", size=60)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 880, in truetype
return freetype(font)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 877, in freetype
return FreeTypeFont (font, size, index, encoding, layout\_engine)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 285, in \_init\_
self.font = core.getfont(
font, size, index, encoding, layout\_engine=layout\_engine
)
OSError: cannot open resource
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/tmp/datagen66arSL.py", line 303, in <module>
a8\_credit\_card\_image()
File "/tmp/datagen66arSL.py", line 224, in a8\_credit\_card\_image
large\_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=60)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 880, in truetype
return freetype(font)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 877, in freetype
return FreeTypeFont (font, size, index, encoding, layout\_engine)
File "/root/.cache/uv/environments-v2/ffad51b5c0487eb6/lib/python3.13/site-packages/PIL/ImageFont.py", line 285, in \_init\_
self.font = core.getfont(
font, size, index, encoding, layout\_engine=layout\_engine
)
OSError: cannot open resource

I actually want to know if this could have been avoided by some changes in my code or is it an issue in the datagen.py script, because as the situation currently stands, my app wasn’t even tested properly for tasks A8 to A10 as the datagen.py script failed to create the required files because it could not find a font which as far as I knew was not specified that it must be included in my own code or image somehow.

Edit 1: I just realized that the datagen script looked for the fonts in python 3.13/site-packages/…  
But my docker image is using the python:3.12-slim-bookworm. Could that be an issue? There was nothing specified about required python version or required python image to be used in docker in the project 1 requirements.

Edit 2:  
Even if the font not being available is somehow my fault, A9 and A10 still should not be penalized for A8 without proper checking.  
image description: The image presents Python code. It begins with an 'if' statement and imports 'argparse'. The code then defines an argument parser, adds arguments for 'email' and '--root', and parses the arguments. It sets up configurations for 'email' and 'root', and prints a disclaimer. Several function calls such as a2\_format\_markdown(), a3\_dates(), etc. follow.
image text:
```python
if \_\_name\_\_ == "\_\_main\_\_":
import argparse
parser = argparse.ArgumentParser()
parser.add\_argument("email")
parser.add\_argument("--root", default="/data")
args = parser.parse\_args()
config["email"] = args.email
config["root"] = os.path.abspath(args.root)
os.makedirs(config["root"], exist\_ok=True)
print("DISCLAIMER: THIS SCRIPT WILL CHANGE BEFORE THE EVALUATION. TREAT THIS AS A GUIDE.")
print("Files created at", config["root"])
a2\_format\_markdown()
a3\_dates()
a4\_contacts()
a5\_logs()
a6\_docs()
a7\_email()
a8\_credit\_card\_image()
a9\_comments()
a10\_ticket\_sales()
```  
Though an error occured in A8, A9 and A10 still could have worked if each of these function calls were enclosed in their own try-except blocks, ensuring independent checks for each task. But the current datagen.py script fails as error propagates to main, where it is not handled and causes abnormal termination without executing the functions for creating files for A9 and A10 as well.

Thank you.  
Regards,  
Shivaditya

---

Hi Haricharan

Your Dockerfile does not build the repo. Its misconfigured.  
This is the error when building it:

```
=> ERROR [8/8] COPY .env /app/                                                                                                                         0.0s
------
 > [8/8] COPY .env /app/:
------
Dockerfile:20
--------------------
  18 |     # Copy application files
  19 |     COPY *.py /app/
  20 | >>> COPY .env /app/
  21 |     
  22 |     # Explicitly set the correct binary path and use `sh -c`
--------------------
ERROR: failed to solve: failed to compute cache key: failed to calculate checksum of ref 468faeeb-6d46-4aeb-a590-25bae24a84d5::y52oingx9lezoq9kjiwp6v58m: "/.env": not found

```

Here's a description of the image:
The image displays a code snippet on a dark background. The code outlines steps to set up an application directory and copy files. An arrow points to the line "COPY .env /app/", which is highlighted with a red outline.
image text:
```
# Set up the application directory
WORKDIR /app
# Copy application files
COPY \*.py /app/
COPY .env /app/
```

This is because if you look at your Dockerfile .env does not exist in your repo.  
Therefore it does not build.  
Your docker is supposed to take the AIPROXY token from our environment not from yours.  
This is passed dynamically at runtime of the Docker.

Since it fails to build, we cannot evaluate it.

Kind regards

---

Your docker failed to build from your Dockerfile

```
 => ERROR [4/7] RUN uv --version                                                                                                                        0.1s
------
 > [4/7] RUN uv --version:
0.078 /bin/sh: 1: uv: not found
------
Dockerfile:25
--------------------
  23 |     
  24 |     # Verify uv installation
  25 | >>> RUN uv --version
  26 |     
  27 |     # Set working directory inside the container
--------------------
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127

```

Since we cannot build your docker from your Docker manifest file we cannot evaluate it.

---

Your container failed to run after building it.

```
docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: exec: "uv": executable file not found in $PATH: unknown

```

Thats why we cannot evaluate it.

---

There is **clearly** *some difference* between both the applications. That is up to you to figure out. I can only tell whats wrong with yours. After building it and trying to run it this is the error we get. It fails to run as a result and we cannot evaluate it.

```
Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 412, in main
    run(
  File "/usr/local/lib/python3.12/site-packages/uvicorn/main.py", line 579, in run
    server.run()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 66, in run
    return asyncio.run(self.serve(sockets=sockets))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 70, in serve
    await self._serve(sockets)
  File "/usr/local/lib/python3.12/site-packages/uvicorn/server.py", line 77, in _serve
    config.load()
  File "/usr/local/lib/python3.12/site-packages/uvicorn/config.py", line 435, in load
    self.loaded_app = import_from_string(self.app)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 22, in import_from_string
    raise exc from None
  File "/usr/local/lib/python3.12/site-packages/uvicorn/importer.py", line 19, in import_from_string
    module = importlib.import_module(module_str)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 999, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/app/app.py", line 23, in <module>
    from tasksB import *
  File "/app/tasksB.py", line 83, in <module>
    from flask import Flask, request, jsonify
ModuleNotFoundError: No module named 'flask'

```

---

Noted your concerns wrt Edit 1 and Edit 2 (and datagen.py running latest python version): Will raise it with [@s.anand](/u/s.anand) during our Wednesday meeting. Once we have an update, we will inform you of the outcome.

Kind regards

---

Hi,

Please let me know the reason on why I have not got any bonus marks.

Here's a description of the image:
\*\*image description:\*\* The image presents a report card or checklist. It details a score calculation and checks for certain conditions related to a project submission. It includes the final score calculation which is based on MIN (20, (task score + bonus)). The image displays the submitted Github and Docker repositories. Then there is a section for pre-requisites checks. Followed by three tables containing rows labeled A, B, and C and columns from 1 to 10. Finally, it provides a task score, bonus, and P1 score at the bottom.
\*\*image text:\*\*
Your final t score calculation is based on
MIN (20, (task score + bonus))
Github repo submitted: https://github.com/swati-iitm/project1\_final
Docker repo submitted: swatiiitm/project1\_final
Pre-requisites check: (1 for pass, 0 for fail)
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo exists and is public (should have a timestamp before 18th of Feb): 1
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1
Gihub repo check - Dockerfile exists: 1
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
1 0 0 0 1 0 0 0 0 0
B1 B2 B3 B4 B5 B6 B7 B8 B9 B10
0 0 1 0 0 0 0 0 0 0
C1 C2 C3 C4 C5
0 0 0 0 0
Your task score is: 3
Your bonus is: 0
Your P1 score is: 4

Here's a brief description of the image:
The image is a webpage displaying a GitHub repository titled "project1\_final," with the branch "master" selected. It indicates that the branch is 8 commits ahead of "main." It displays a list of files and folders within the repository, their descriptions, and update times.
image text: project1\_final Public
Pin Unwatch 1 Fork 0 Star 0
master 2 Branches 0 Tags
Q Go to file t Add file <> Code About
No description, website, or topics provided.
This branch is 8 commits ahead of main. Contribute MIT license
swati-iitm last\_minut 7d08160 · 2 months ago 9 Commits Activity
\_pycache\_ version\_latest 2 months ago ✩ 0 stars
data version\_latest 2 months ago 1 watching
Dockerfile updated, relative path 2 months ago 0 forks
LICENSE Initial commit 2 months ago Releases
app.py last\_minut 2 months ago No releases published
Create a new release
datagen.py updated relative path 2 months ago
Packages
evaluate.py version\_latest 2 months ago No packages published
Publish your first package
llm\_code.py last\_minut 2 months ago

---

We used some internal parameters with weights to auto calculate the bonus. Unless your submission met that threshold of 0.5 after scaling you would not get any bonus. Your score was normalised so instead of 3 you got 4 (3.75 got rounded up). But the metrics used to evaluate the quality of your submission only scored you at 0.007 which is far below the threshold required to get a bonus.

---

Respected Sir,

* Yes Sir, I said the same, `.env` was not able to be uploaded to repo as .env file was not allowed to be uploaded
* when we download the repository it doesn’t have the `.env` file,
* for docker image to build we need to add `.env` with `AIPROXY_TOKEN`
* after that docker image will build, I had given about this in previous message
* As you said Sir that you will use separate `AIPROXY_TOKEN`…you can put that in `.env` file and build the docker image
* after that Sir its optional to pass `AIPROXY_TOKEN` again while running the docker Image
* just the `.env` file required, even without token in that it will work as project has support for both AIPROXY token in .env file and as environment variable

and when I uploaded to repository the .env file was not allowed to upload so had submitted that way, I actually forgot to add step for running the docker image in the previous message, the steps which I used:

```
git clone https://github.com/23f2001390/llmagent.git

```

adding `.env` with AIPROXY token and replacing `evaluate.py` and `datagen.py` with new ones according to test environment

```
docker build -t llm-agent .

```

```
docker run -p 8000:8000 llm-agent
or
docker run -e AIPROXY_TOKEN=token -p 8000:8000 llm-agent

```

and in another terminal

```
uv run evaluate.py --email=23f2001390@ds.study.iitm.ac.in --token_counter 1 --external_port 8000

```

Thank you  
Kind regards

---

Respected sir  
I understand it’s my mistake sir and I apologize for that sir, but please consider this time sir since because of this my entire project score went from 9/20 to 0, which would make me difficult to pass this course and continue my diploma.  
Please consider this request sir, sorry sir and this would never be repeated in future. My project evaluation was 9/20 initially sir, but later it came down to 0 because of this issue. Kindly consider sir please.

Regards,  
S Sharmile  
23f3001688

---

Thanks for relentless efforts [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

I tested the docker file in docker playground again.. Please find the screenshot of the docker build command and the log output of the docker build.. It went thru without issues..

Was the latest docker file used from git lab? Because as explained on March 30 i had to remove the hardcoded http/https proxies of my office environment,

Here's a brief description of the image:
The image is a screenshot of a web application. The main area is taken by a window displaying information about a container. Some elements include the IP address, memory, SSH access information, and buttons labeled "DELETE" and "EDITOR". At the bottom is a terminal.
image text: labs.play-with-docker.com/p/cvqlfo0l2o9000cd7ic0#cvqlfo0l\_cvqlfsol2o9000cd7icg
want sir Attit...
G sadhguru anything...
(42) Reciprocating si... 1272572-disha5.jpg...
disha%20patani%20...
BIGGEST Announce...
:44:22
cvqlfool\_cvqlfsol2o9000cd7icg
LOSE SESSION
IP
TANCE
192.168.0.13
OPEN PORT
Memory
SSH
ssh ip172-18-0-93-cvqlf001209000cd7ic0@direct.labs.play-
DELETE
EDITOR
CK
[node1] (local) root@192.168.0.13 ~
$ docker build -t tdsproject1:latest
CPU
> tds-projlbuild.log

build output

```
#0 building with "default" instance using docker driver

#1 [internal] load build definition from Dockerfile
#1 transferring dockerfile: 694B done
#1 DONE 0.0s

#2 [internal] load metadata for docker.io/library/python:latest
#2 DONE 0.5s

#3 [internal] load .dockerignore
#3 transferring context: 2B done
#3 DONE 0.0s

#4 [1/6] FROM docker.io/library/python:latest@sha256:aaf6d3c4576a462fb335f476bed251511f2f1e61ca8e8e97e9e197bc92a7a1ee
#4 DONE 0.0s

#5 [internal] load build context
#5 transferring context: 33B done
#5 DONE 0.0s

#6 [4/6] RUN uv --version
#6 CACHED

#7 [2/6] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#7 CACHED

#8 [3/6] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
#8 CACHED

#9 [5/6] COPY execute.py /
#9 CACHED

#10 exporting to image
#10 exporting layers done
#10 writing image sha256:2919fe6ce0097ae2fc33aebaba327dbd6a35d256b6d946c97c310fd992944add done
#10 naming to docker.io/library/tdsproject1:latest done

```

Here's a description of the image:
The image shows a commit log entry.
image text: Commits on Mar 30, 2025
Update Dockerfile removed hard coded proxies
rsjay1976 authored last week
Verified
a71e3a8

---

Here's a description of the image:
\*\*Image Description:\*\*
The image shows a terminal window with a command-line interface. The user is building a Docker image. The output shows a series of commands being executed, including `apt-get update` and `curl`, and subsequent failures. An error message "ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127" is displayed, indicating a problem running the 'uv --version' command within the Docker build process. The Dockerfile is referenced, with the line `RUN uv --version` highlighted as the source of the error.
\*\*Image text:\*\*
```text
root@tds-course-temp-bq:/r X
+
root@tds-course-temp-bq:/mnt/sdb/github\_approach# cd github\_repos/
root@tds-course-temp-bq:/mnt/sdb/github\_approach/github\_repos# cd 22f3002723/
root@tds-course-temp-bq:/mnt/sdb/github\_approach/github\_repos/22f3002723# cd TDS-Project1-Jan25-622ed8adf432b6c539321e6519d62da09248a
542/
root@tds-course-temp-bq:/mnt/sdb/github\_approach/github\_repos/22f3002723/TDS-Project1-Jan25-622ed8adf432b6c539321e6519d62da09248a542#
docker build -t 22f3002723:latest .
[+] Building 8.7s (8/10)
docker:default
=> [internal] load build definition from Dockerfile
0.0s
=> => transferring dockerfile: 895B
0.0s
=> [internal] load metadata for docker.io/library/python:latest
0.0s
=> [internal] load .dockerignore
0.0s
=> => transferring context: 2B
0.0s
=> CACHED [1/7] FROM docker.io/library/python:latest
0.0s
=> [internal] load build context
0.1s
=> => transferring context: 347.68kB
0.0s
=> [2/7] RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && apt-get clean && rm -rf 7.6s
=> [3/7] RUN curl -sSfL https://astral.sh/uv/install.sh | sh
0.7s
=> ERROR [4/7] RUN uv --version
0.3s
> [4/7] RUN uv --version:
0.240 /bin/sh: 1: uv: not found
Dockerfile:25
23 |
24 | # Verify uv installation
25 | >>> RUN uv --version
26 |
27 | # Set working directory inside the container
ERROR: failed to solve: process "/bin/sh -c uv --version" did not complete successfully: exit code: 127
root@tds-course-temp-bq:/mnt/sdb/github\_approach/github\_repos/22f3002723/TDS-Project1-Jan25-622ed8adf432b6c539321e6519d62da09248a542#
```

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

> Was the latest docker file used from git lab

No, we are not allowing any changes to repo after deadline, this is consistent rule for every student. We pulled your github repo latest commit before 18th feb, I am getting following error.

---

follow the steps mentioned in post below ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14 ":slight_smile:")

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f300327/48/91361_2.png) 23F300327:

> To test the functionality correctly, `npx` must be installed inside the running container. This can be fixed by entering the container and installing Node.js and npm using:

That destroys the purpose of containerization, your container should run anywhere anytime, all the dependencies must be preinstalled.

---

Thanks [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
As mentioned earlier, the pre Feb 18 dockerFile commited in GIT had my office proxy url’s set as http\_proxy and https\_proxy.. It worked in my office envuironment and i tested everything in my office environment but based on the results which came on March last week realised that the proxies were preventing the uv to be installed in other environments.

Post that realised we have cloud based "docker playground’ utility where docker builds can be tested agonistic of any environment.. The good thing with playground is our instances last for only 3 hrs and next day we try we are kind of gauranteed of fresh environment without any caches,

Now after March 30th checkin validated the same in docker playground and ensured that the image got tagged and createdd successfully..

It would be great if the March 30th checkin could be considered, Again appreciate all your help so far.

---

**Subject:** Request for Verification of Dockerfile and Reevaluation of Marks for Project 1  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir,  
Regarding the recent feedback on **Project 1** for **TDS**, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named **`dockerfile`** (not **`Dockerfile`**). Please verify the repository again with this in mind.

Additionally, my Docker image architecture is *linux/amd64* (64-bit **x86**). I have also filled out the **Architecture Information Collector** form as requested.

**Pre-requisites check: (1 for pass, 0 for fail)**  
Docker repo exists and is public (should have a timestamp before 18th of Feb): 1  
Github repo exists and is public (should have a timestamp before 18th of Feb): 1  
Github repo check - LICENSE or LICENSE.md file exists (MIT License): 1  
Gihub repo check - Dockerfile exists: 0  
image description: The image is a screenshot of a GitHub repository titled "task\_agent\_api" with the owner "23f1001822". The repository contains files and folders like .myenv, \_pycache\_, .env, LICENSE, README.md, app.py, datagen.py, dockerfile, evaluate.py, and requirements.txt. The image highlights the "dockerfile" entry. The right side panel provides repository information, including a description, license, activity, stars, watchers, and forks. It also shows the "Releases", "Packages", and "Contributors" sections.
image text: 23f1001822 / task\_agent\_api
task\_agent\_api Public
main 1 Branch 0 Tags
23f1001822 dockerfile update
.myenv dockerfile update
\_pycache\_ dockerfile update
.env first commit
LICENSE Initial commit
README.md Initial commit
app.py first commit
datagen.py first commit
dockerfile dockerfile update
dockerfile
evaluate.py first commit
requirements.txt dockerfile update
tasksA.py first commit
About
No description, website, or topics provided.
Readme
MIT license
Activity
✩0 stars
1 watching
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors

Here’s the link to my GitHub repository:

[github.com](https://github.com/23f1001822/Task_agent_api)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/d/8/d83b83eaf69931596b2cddbbfea39884f17e047a_2_690x344.png)

### [GitHub - 23f1001822/task\_agent\_api](https://github.com/23f1001822/Task_agent_api)

Contribute to 23f1001822/task\_agent\_api development by creating an account on GitHub.

**Docker repo submitted:** *sakshamumate/task\_agent\_api*

I kindly request a **reevaluation of my project marks** based on these clarifications.

Thank you for your attention to this matter. Please let me know if you need any further information or clarification.

Best regards,  
Saksham Umate ,  
23f1001822@ds.study.iitm.ac.in

---

Sir, I had posted the query on A8 and datagen exception. Is this a reply to that?

---

oh yeah sorry, hit the reply to the wrong button, but yes its to your post.

---

I’ve got good news for you and 30 other students. Thanks to your diligent debugging effort that we were able to find this bug. For now the fix is that we will not evaluate you on a8 and catch the datagen exception so as to not cause cascading failures.

Thanks and kind regards.  
We will let you know the outcome of the evaluations soon.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
any way out for my earlier query ?

---

[@carlton](/u/carlton)  
Thank you for the reply .But it was working when i ran the initial evalaute.py .If you don’t mind could you tell what may have caused this to happen.

---

Hi Hilal,

You have to recreate the test environment as shown in this post

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316) [Tools in Data Science](/c/courses/tds-kb/34)

> To replicate the test environment:
> Fetch the github repo’s latest commit before 18th feb use below code for that. You need to have github cli installed on your system and need authentication for certain github api enpoint access. Once authenticated and providing the appropriate repo details you can run this code using uv.
> # /// script
> # dependencies = [
> # "requests",
> # ]
> # ///
> import requests
> import datetime as dt
> import zoneinfo
> import argparse
> import os
> import zipfile
> parser = argparse.…

That way you will be able to identify why the error was occuring.

The specific error itself means:  
Docker is trying to run the command uv inside your container, but it can’t find the uv executable — it’s not installed or not in the system PATH inside the container.

If you did not run evaluate.py as specified in our live sessions by recreating the test environment and then running evaluate.py then it would not have reflected how your dockerised application would work.

Kind regards

---

sir for my project 1 i got a mail stating that the docker file isn’t public and that’s why prerequisite failed. but i checked it and it seemed absolutely perfect to me. Please look into this issue as my docker repo is public and absolutely as per the requirement. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Hi [@22f3003083](/u/22f3003083)

Following was your submission, which is not a valid dockerrepo.  
Here's a description of the image:
The image is a table, likely representing data or a log. The top portion has navigation elements like "Preview", "Code", "Blame" followed by size information. There's a search bar with "22f3003083/v1" in it. The table includes columns like "Timestamp", "Email Address", "What is the link to your GitHub repository which has the code for Project 1?", and "What is the name of the image published on DockerHub?". There is one row of data.
image text:
Preview Code Blame 1069 lines (1069 loc) 127 KB
Q 22f3003083/v1
1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub?
932 2/16/2025 23:20:17 22f3003083@ds.study.iitm.ac.in https://github.com/22f3003083/TDS\_Project\_1 22f3003083/v1

---

Now I feel so good getting 0.  
0 is best.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
As requested earlier, Could you please reevaluate my submission. The only change that had to be done post Feb 18 checkin was to remove my office proxies on Mar 30 from the docker file to make it work in all environments.. It would be great if this could be accomodated..

---

Hi Jayaram,

Unfortunately, we are not able to relax restrictions on changes to your repo, regardless of the reason. We have kept this rule uniform for everyone. If we allow this change, then everyone has a legitimate reason to request changes and would make the rule meaningless because then everyone will be able to make corrections to their submission. We do not even allow spelling changes.

Kind regards

---

Thanks for the response [@carlton](/u/carlton) .. just a small suggestion, to avoid scenarios like what i faced and also with softwares like docker/podman not being too windows friendly, i think students can find it easier if a dev/mock linux env is provided for course term duration, instead of everyone having to figuring out with AWS/Azure and all providers.. Anyway thanks and appreciate all the help

---

Sir, I have done everything for my project, but I am getting zero. I have uploaded my Docker file, but the email says it is not public. Sir, this is affecting my grades — please help me out. [@Carlton](/u/carlton)

---

These are your project 1 responses,  
image description : The image is a dark-themed table containing data about a project. It contains the search bar in the top left corner which has the search term "23f1001236". The table has columns for timestamp, email address, GitHub repository link, and DockerHub image name.
image text:
Q 23f1001236
1 Timestamp Email Address What is the link to your GitHub repository which has the code for Project 1? What is the name of the image published on DockerHub?
203 2/15/2025 20:29:39 23f1001236@ds.study.iitm.ac.in https://github.com/MaheshSingh01/tds\_proj.git maheshsingh01/tds-proj
758 2/16/2025 21:28:12 23f1001236@ds.study.iitm.ac.in https://github.com/MaheshSingh01/tdsrepos.git maheshsingh01/tdsrepos
1012 2/16/2025 23:53:46 23f1001236@ds.study.iitm.ac.in https://github.com/MaheshSingh01/tdsrepos.git maheshsingh01/tdsrepos

We are considering latest submission which have docker repo `maheshsingh01/tdsrepos`   
which is not accessible publically.  
Image description: The image is a screenshot of a webpage displaying a 404 error page on Docker Hub. The page features a large blue circle in the center with the number "404" in white, followed by "Oops!" and the text "The page you have requested was not found". Below the text, there is an illustration of a person looking at a computer. The Docker Hub logo and navigation bar are visible at the top.
image text: dockerhub
https://hub.docker.com/r/maheshsingh01/tdsrepos/tags
Explore / maheshsingh01 / tdsrepos
Search Docker Hub
404
Oops!
The page you have requested was not found
Ctrl+K
?
Update
Sign in
Sign up

---

Sir, could you please check it once more? I think the issue has been resolved. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Since repo was not public during evaluation, we won’t be rechecking, or reevaluating.

---

[@Jivraj](/u/jivraj) I’ve completed all the required steps, but I’m still getting 0, It was working fine before. Could you please help me identify what might be going wrong?

---

Hi [@21f3003107](/u/21f3003107)

You need to look it up yourself, We have sent out evaluation log and docker log files, check those out.  
Evaluation script and other scripts that we have used are there in github repository over here.  
[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/1)  
If there is some mistake from our end let us know about it.

To replicate test environment follow steps provided below.

[Tds-official-Project1-discrepencies - Courses / Tools in Data Science - IITM-DSA](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/316)

---

[@carlton](/u/carlton) Requested sir  
This is to request that in my evaluation a got 0 cause of the use of lowercase d instead of uppercase D but I have already submitted the docker file in my git hub repo also.  
image description: The image is a screenshot of a file directory, likely from a code repository platform like GitHub or GitLab. The directory contains various files, including .dockerignore, .gitattributes, .gitignore, LICENSE, README.md, app.py, datagen.py, Dockerfile, evaluate.py, requirements.txt, tasksA.py, and tasksB.py. Each file is listed with its status ("added") and the time since its last modification ("2 months ago"). The user associated with these changes is "wag28".
image text: wag28 added eff178a · 2 months ago .dockerignore added 2 months ago .gitattributes Initial commit 2 months ago .gitignore added 2 months ago LICENSE added 2 months ago README.md added 2 months ago app.py added 2 months ago datagen.py added 2 months ago dockerfile added 2 months ago evaluate.py added 2 months ago requirements.txt added 2 months ago tasksA.py added 2 months ago tasksB.py added 2 months ago

---

[@carlton](/u/carlton)  
Thank you i found my mistake in my docker file i wrote this CMD [“uv”, “run”, “app.py”] instead of  
CMD [“uvicorn”, “main:app”, “–host”, “0.0.0.0”, “–port”, “8000”].Now i think everything works fine

---

Sir my repo was public

---

Sir any news on this? Did my score increase at all? My dashboard still shows the old score.

---

[@carlton](/u/carlton) sir, my project 1 marks have still not increased even though while during evaluation it shows 4/10 for the task 1. It was said that the docker image prerequisite will be removed and without that the evaluation would be done, but there is still no change in my marks. please look into it once, as my dashboard currently reflects 0 for project 1.

---

These evals are being handled separately. They have not yet been completed. Kindly bear with us till they are complete.

---

Same here [@carlton](/u/carlton) in my evaluation logs i have scored 10 while marks being reflected are not the same neither on mail nor on site

---

I looked at your evaluation logs and it says 1 score instead of 10.

---

Good evening!  
[1000092114|690x198](/uploads/short-url/30ijyIo5UiUUEVvnPZklfYVY2mI.jpeg)

I am writing to you to request you please relook into the evaluation.

The docker image which I share is working at my end. The size of the image is 6 GB which may take more than 5 minutes to load as I wasn’t aware of the infra level restrictions.

I request you to kindly consider my request and please re-evaluate the assignment as I have contributed a lot of effort into it.

Thanks,  
Garima

---

Sir, so will my score get updated because now it is marked as 0.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir,  
I am Saksham Umate and my project 1 was to be re-evaluation because of docker file not found in root ,but it was their so you had given me confirmation that it will re-evaluate after end term. I had already shared my docker file systems configuration at docker hub

So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it

Tell me if any information is needed about project from my side  
Thank you!

Best regards,  
Saksham

My docker repo details in previous post:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) [Tools in Data Science](/c/courses/tds-kb/34)

> Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1
> [@carlton](/u/carlton) [@Jivraj](/u/jivraj)
> Sir,
> Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind.
> Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested.
> P…

Here's a description of the image:
\*\*Image Description:\*\*
The image shows an email from Carlton D'Silva with information for a "Dear Learner". The email is about a project P1 submission. It clarifies that the P1 submission will be looked at separately and the end term only. It also talks about a script that runs and searches for the Dockerfile, any changes after Feb 18th are not accepted and no spelling deviations will be accepted.
\*\*image text:\*\*
Carlton D'Silva 9 Apr
to bcc: me
Dear Learner,
Your P1 had failed a pre-requisite because
our script could not locate Dockerfile in the
base of the root directory of your github
repo. We are relaxing this requirement.
Your P1 submissions will be looked at
separately after the end term only.
We will run a script to do a directory tree
search for Dockerfile in your github.
No changes to the github repo after Feb
18th will be considered.
No spelling deviations will be accepted for
the required files.
All other prerequisites will still have to be
met.
Your docker image has to build without
errors from the Dockerfile.
After building it, your docker container has
to become operational within 5 minutes of
starting.
Then evaluations will be carried out exactly
according to the test environment that was
specified.
99+
4

---

Evaluations are done for such cases where Dockerfile(with name of Dockerfile as `Dockerfile`) was present inside other folders than root folder of your github repo.

---

[@carlton](/u/carlton) sir, any info on outcome of [this bug in P1 datagen.py](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451) ?

---

Did Mark’s are updated or being update for this students ?

---

Hi [@22f3000819](/u/22f3000819)

We had updated datagen.py(try block for task) which affected 30 students, but scores changed only for 4 students, for others it remained the same.

---

We will be pushing marks today.

---

I probably wasn’t 1 of the 4, right? Anyways thanks for paying attention to the matter.

Regards,  
Shivaditya

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Respected Sir,

I hope you are doing well.  
This is with reference to your confirmation mail that my project 1 will be re-evaluated after end term  
I would like to sincerely apologize for the oversight in my Project 1 submission. Upon reviewing my GitHub repository, I realized that the file was named `dockerfile` (with a lowercase ‘d’) in the Github root repo instead of the required `Dockerfile` (with an uppercase ‘D’).

While the contents of the file were correct and my project passed several evaluation tests, I understand that the evaluation script could not detect the Dockerfile due to this naming issue. I genuinely did not intend to deviate from the standard, and I now fully understand the importance of following naming conventions precisely.

I humbly request you to kindly consider this as an honest mistake and allow a one-time exception, Please sir. This issue has unfortunately resulted in my project score being reduced to 0, which puts my overall course performance at risk. I assure you that I have learned from this experience and such an error will not occur again in the future.  
So, I hope you will look at this and re-evaluate my project as I put lots of efforts to complete it.  
Thank you very much for your time and consideration.

Warm regards,  
S. Sharmile  
Roll No: 23f3001688

---

Sir, my marks still did not get updated, please help me in that regard.

---

Hi Everyone,

We have sent the updated marks to Operations. At this time of the term they are very busy with lots of updates, so it will take time for them to push it to the dashboard. As soon as they inform us that the scores have been pushed, we will send out a discrepancy form if you find any issues with your score.

Thanks & Kind regards

---

Sir, my project 1 marks are still 0 even though I had passsd few cases. Please help me sir as my final score is coming as 69.8 , it will be very valuable for me if it crosses 70, please sir help me with this regard

---

[@carlton](/u/carlton)  
Hi Sir,  
I hope you’re doing well. I just wanted to let you know that I put a lot of effort into completing **Project1**, but I accidentally named the **Dockerfile** as `dockerfile` (with a lowercase ‘d’).  
Could you please consider evaluating it with that name? I’d really appreciate it.  
Thank you!  
My discourse post for more information:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1001822/48/66833_2.png)
[Tds-official-Project1-discrepencies](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/447) [Tools in Data Science](/c/courses/tds-kb/34)

> Subject: Request for Verification of Dockerfile and Reevaluation of Marks for Project 1
> [@carlton](/u/carlton) [@Jivraj](/u/jivraj)
> Sir,
> Regarding the recent feedback on Project 1 for TDS, it was mentioned that there is no Dockerfile in my GitHub repo. However, the Dockerfile is named dockerfile (not Dockerfile). Please verify the repository again with this in mind.
> Additionally, my Docker image architecture is linux/amd64 (64-bit x86). I have also filled out the Architecture Information Collector form as requested.
> P…

---

