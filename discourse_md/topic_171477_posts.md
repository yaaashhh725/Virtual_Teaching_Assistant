# project-1-evaluation-second-mail-is-not-correct-and-reports-files-missing-while-they-are-present

Mail I received Yesterday:  
image description: The image is a text-based document that outlines the prerequisites for Project 1. It starts with a greeting, followed by a list of requirements, including a publicly accessible GitHub repository, a LICENSE file with the MIT license, a Dockerfile, and a publicly accessible Docker image. The document also contains a list of evaluations for the project prerequisites.
image text: Dear Learner,
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

Previous Correct Evaluation Mail:  
image description: This is a document providing feedback on a docker image submission for a project. It includes instructions, explanations, and links to files for evaluation. It also gives the ID of the docker image evaluated and notes about the scoring process and the deadline for reporting issues.
image text: Dear Learner,
We have evaluated your project 1 docker image submission. Please find the following files.
MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us.
MISSING files will result in a score of 0.
Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud compute unit. So performance of the server
was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster than the fastest domestic internet.
1. Evaluation log file. https://drive.google.com/file/d/1BaAw9x6g2YBRDgf-GoZSe1UbGSSBafnO/view?usp=drivesdk This contains your performance report on your individual tasks.
2. Docker log file. https://drive.google.com/file/d/1aFya6jG3YF1UrahQu7qnCbEOaDh4JW27/view?usp=drivesdk This provides the technical performance of your container.
3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests.
4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism.
5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks.
6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the required environment variables that will
be required by your container to function and the port mappings for communications.
7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core concepts of LLMs to achieve the
desired result.
This is the id of the docker image that was evaluated: 48299f48f66b
These scores are not final but they indicate what our current evaluation standards will score you.
If you have discovered a bug in our scripts or have a discrepancy to report with how the various scripts functions then we are happy to address your concern and where necessary make amendments to your score.
You will have until Tuesday to report any problems. After which the score will be considered final. We will listen to feedback and then come up with a final marking schema.
We will also look at the highest scores (including the score of the sample script we shared) to decide the mark on which the rest of the scores will be normalised.
We look forward to your feedback and apologise for the delay in providing you with the scores.
Post all your concerns on this discourse thread

Good Morning Sir,

This is my github repo: [GitHub - kohliaryan/TDS\_Project\_1](https://github.com/kohliaryan/TDS_Project_1) ()You can verify that it is public, MIT License is present and Dockerfile is also present.)

I also got a mail 2 days ago in which everything is mentioned correctly but the mail I got yesterday worry me. Sir, I have worked really hard for project 1. Please look into this matter.  
[@carlton](/u/carlton)

---

[@Jivraj](/u/jivraj) Sir, Please look into in this matter, no reply from your side till now and 2 days have been passed.

---

Apologies for that,

The second email was an automated script that used a stricter criteria. You have passed evaluation and also have a score. So dont worry. We will push scores over this weekend. We are currently doing normalisation.

Kind regards

---

Hi [@carlton](/u/carlton),

I’m experiencing the same issue mentioned in this thread regarding Project 1 evaluation emails:

1. The first email I received confirmed all requirements were met (public repo, MIT License, Dockerfile, etc.)
2. The second email incorrectly flagged missing files despite their presence in my repository

Here are screenshots of both emails showing the discrepancy:

image description: The image is a screenshot of an email from "22t1 se2002" to "me". The subject is "TDS Jan 25 Project 1 Scores". The email informs the recipient about the evaluation of their project 1 docker image submission. It lists several files (evaluation log, docker log, server start log, evaluation script, data generation, docker orchestration, and solution script) with links or references to attachments. The email also provides information on how the scoring works, the meaning of "MISSING" files, and deadlines for reporting issues.
image text: TDS Jan 25 Project 1 Scores Inbox x
22t1 se2002 <se2002@study.iitm.ac.in>
to me
Dear Learner,
We have evaluated your project 1 docker image submission. Please find the following files.
MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us.
MISSING files will result in a score of 0.
Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud compute
unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which is nearly 5 times faster
than the fastest domestic internet.
1. Evaluation log file. https://drive.google.com/file/d/1h0HJ-yKj5t1ud42\_b8mktmuF7bMLzsvs/view?usp=drivesdk This contains your performance report on your individual tasks.
2. Docker log file. https://drive.google.com/file/d/1xSRVWb53I-RNO400SYQ4rX4T\_lxq\_M79/view?usp=drivesdk This provides the technical performance of your container.
3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests.
4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism.
5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks.
6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the
required environment variables that will be required by your container to function and the port mappings for communications.
7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the core
concepts of LLMs to achieve the desired result.
This is the id of the docker image that was evaluated: b0d89eee9b17
These scores are not final but they indicate what our current evaluation standards will score you.
If you have discovered a bug in our scripts or have a discrepancy to report with how the various scripts functions then we are happy to address your concern and where necessary make
amendments to your score.
You will have until Tuesday to report any problems. After which the score will be considered final. We will listen to feedback and then come up with a final marking schema.
  
Here's a description of the image:
\*\*Image Description:\*\*
The image is an email notification regarding the scores of a project. The sender is "22t1 se2002" and the subject is "TDS Jan 25 Project 1 Scores". The email lists pre-requisite checks and their evaluations.
\*\*Image Text:\*\*
TDS Jan 25 Project 1 Scores Inbox x
22t1 se2002 <se2002@study.iitm.ac.in>
to me
Dear Learner,
Project 1 requires you to pass some pre-requisite checks as detailed on the TDS Project 1: Evaluation page:
1. Your GitHub repository exists and is publicly accessible
2. Your GitHub repository has a LICENSE file with the MIT license
3. Your GitHub repository has a valid Dockerfile
Tue, Apr 1, 1:25 AM (3 days ago)
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

My GitHub repo remains publicly accessible with all required components:  
[GitHub repo](https://github.com/23f2000345/TDS_final)

Could you please confirm this was an automated error and that my submission will be evaluated based on the actual repository contents? Your clarification would be greatly appreciated.

Thank you for your time and assistance!

---

Hi,

Prerequisite checks have passed. But your docker image was missing a dependency that you forgot to copy into the image. so it failed to evaluate because it failed to run.

---

You talking about me or [@23f2000345](/u/23f2000345) ?

---

Good Morning Sir, Actually even I got the mail regarding Project-1 Evaluation, where I got the message like the prerequisites were not met. But, sir actually I have uploaded my MIT License file, requirements.txt file, my Project.py file and the Dockerfile. Sir, and when I sent a request to my API from my device, it worked sir. I have got 0 in my project 1 sir, but I have met the pre-requisites Can you please check this once sir?

My GitHub repository for Project-1: [GitHub - sudhishssn134/project\_1\_tds](https://github.com/sudhishssn134/project_1_tds)

Thanking You

Just attaching the mail I recieved.  
image description: The image is a screenshot of an email, with the sender being "22t1 se2002" and the subject "TDS Jan 25 Project 1 Scores". The email discusses the evaluation of a docker image submission. It includes information about missing files, scoring, and links to evaluation logs. There are also attachments.
image text: TDS Jan 25 Project 1 Scores Inbox x
22t1 se2002
to me
Dear Learner,
We have evaluated your project 1 docker image submission. Please find the following files.
MISSING indicates that the file is not available because the evaluation did not run or the docker image was misconfigured. If you feel this is in error you can still contact us.
MISSING files will result in a score of 0.
Your docker image is supposed to become responsive in 5 minutes from launch. If it does not, then we will not consider it. The images were all run on an 8 core Xeon Google Cloud
compute unit. So performance of the server was not a bottleneck for your docker image. Also each docker image had 1 Gigabit of dedicated network bandwidth available which
is nearly 5 times faster than the fastest domestic internet.
1. Evaluation log file. https://drive.google.com/file/d/1LNtZ6bGYNUCudn4A0ZtRE-NqaQIRDPQK/view?usp=drivesdk This contains your performance report on your individual
tasks.
2. Docker log file. https://drive.google.com/file/d/1K5KRIS2dpMNMpR1iLU0-WGnLRT-6yazq/view?usp=drivesdk This provides the technical performance of your container.
3. Server start log file (separate logs for arm vs x86) (See attachment). If your docker service did not start or respond to attempts to our requests.
4. Evaluation script file (separate logs for arm vs x86) (See attachment). This file has the actual tests that were run against your submission and the scoring mechanism.
5. Data generation file (See attachment). The evaluation file depends on this file to create the data for the tasks.
6. Docker orchestration file (See attachment). This file handles the retrieval of your docker image from docker hub and launching of your container instance. It also sends the
required environment variables that will be required by your container to function and the port mappings for communications.
7. Solution script (See attachment zip). This file solves the entire project 1 using prompt engineering only. This is a sample example of what can be achieved by leveraging the
core concepts of LLMs to achieve the desired result.
This is the id of the docker image that was evaluated: 7382b3277180
These scores are not final but they indicate what our current evaluation standards will score you.
If you have discovered a bug in our scripts or have a discrepancy to report with how the various scripts functions then we are happy to address your concern and where necessary
make amendments to your score.
You will have until Tuesday to report any problems. After which the score will be considered final. We will listen to feedback and then come up with a final marking scheme.

---

Your Dockerfile was misconfigured. When we try to build the docker image from your github repo, we get this error:

`tried copying parent folder(COPY failed: forbidden path outside the build context: .. ())`

You have to replicate the test environment. If it works when you follow this test setup then you should get in touch with us.

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

---

Oh OK Sir. I will try it out. Thank You so much sir

---

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below  
Here's a brief description of the image:
The image displays a terminal output, likely from a Docker build process. It shows steps like extracting layers, copying files, installing dependencies using pip, and exporting the image. Following this is a Docker run command and output related to starting a server, and some informational messages are shown.
image text:
```
=> => sha256:74018f7cfa8f2965fd86b13c38f71417bc846e071a5f5bb5ae569ccb5a6e7248 3.51MB / 3.51MB
=> => sha256:8a628cdd7ccc83e90e5a95888fcb0ec24b991141176c515ad101f12d6433eb96 28.23MB / 28.23MB
=> => extracting sha256:8a628cdd7ccc83e90e5a95888fcb0ec24b991141176c515ad101f12d6433eb96
=> => extracting sha256:74018f7cfa8f2965fd86b13c38f71417bc846e071a5f5bb5ae569ccb5a6e7248
=> => extracting sha256:a0b0cfc480ce03c723a597904bcfbf28c71438c689e6d5097c2332835f67a40c
=> => extracting sha256:97d21b95fb00ac3b08975ab6f8709f3a7e35a05d75e2f9a70fa95348279dac27
=> [internal] load build context
=> => transferring context: 9.24kB
=> [2/5] WORKDIR /app
=> [3/5] COPY ./app
=> [4/5] COPY requirements.txt /app/
=> [5/5] RUN pip install --no-cache-dir -r requirements.txt
=> exporting to image
=> => exporting layers
=> => exporting manifest sha256:fd9582b91eda6f81ed41cf9450ea7821e8576779e7dc678ee94ad1f27b3e8a6a
=> => exporting config sha256:8b2fd7d92ec5907553593d1f5489e77f427e7118fe7b35e898133cb5bdf61c2d
=> => exporting attestation manifest sha256:852a716f978368ac94d509fdbcad7180252c34f4f8ab126d9fc9e6764fb10921
=> => exporting manifest list sha256:b5e540509d0c663a681f4a6c2246e44acac9a3fca50d0fda2b89b35b4b2702dd
=> => naming to docker.io/library/sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49
=> => unpacking to docker.io/library/sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49
View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/4btzhep5n0ttsar3bibf4z96c
1.5s
2.8s
0.5s
0.1s
0.3s
0.0s
0.1s
0.0s
0.1s
0.0s
0.0s
5.1s
1.4s
1.0s
0.0s
0.0s
0.0s
0.0s
0.0s
0.2s
C:\SSNFun\IITM\sudhishssn134-project\_1\_tds-b240fec>docker run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 sha256:9739a6
07cecceea347fade8e485cb7c372b86608284aaa852144ebb755586b49
INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Sir, But I couldn’t run the last command you gave,

```
uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

```

As I dont have evaluate.py

But, the DockerImage is built and is running without error sir.  
Please guide me after this sir  
Thank You So much sir

---

Sir, I have extracted the files from the GitHub Repository, built my DockerFile withe the DockerImage I have posted. The build is successful and the dockerimage is also running sir. I have attached the screen shot below

image description: The image is a terminal output that shows the progress of building and running a Docker image. The output begins with several lines that describe the extraction of sha256 files. Subsequent lines detail actions such as transferring context, setting the working directory, and copying files. The terminal then runs commands like installing dependencies and exporting the image. Towards the bottom, there are lines about the server process starting, waiting for application startup, and completion, along with the Uvicorn server running on a specific port.
image text:
```
=> => sha256:74018f7cfa8f2965fd86b13c38f71417bc846e071a5f5bb5ae569ccb5a6e7248 3.51MB / 3.51MB 1.5s
=> => sha256:8a628cdd7ccc83e90e5a95888fcb0ec24b991141176c515ad101f12d6433eb96 28.23MB / 28.23MB 2.8s
=> => extracting sha256:8a628cdd7ccc83e90e5a95888fcb0ec24b991141176c515ad101f12d6433eb96 0.5s
=> => extracting sha256:74018f7cfa8f2965fd86b13c38f71417bc846e071a5f5bb5ae569ccb5a6e7248 0.1s
=> => extracting sha256:a0b0cfc480ce03c723a597904bcfbf28c71438c689e6d5097c2332835f67a40c 0.3s
=> => extracting sha256:97d21b95fb00ac3b08975ab6f8709f3a7e35a05d75e2f9a70fa95348279dac27 0.0s
=> [internal] load build context 0.1s
=> => transferring context: 9.24kB 0.0s
=> [2/5] WORKDIR /app 0.1s
=> [3/5] COPY . /app 0.0s
=> [4/5] COPY requirements.txt /app/ 0.0s
=> [5/5] RUN pip install --no-cache-dir -r requirements.txt 5.1s
=> exporting to image 1.4s
=> => exporting layers 1.0s
=> => exporting manifest sha256:fd9582b91eda6f81ed41cf9450ea7821e8576779e7dc678ee94ad1f27b3e8a6a 0.0s
=> => exporting config sha256:8b2fd7d92ec5907553593d1f5489e77f427e7118fe7b35e898133cb5bdf61c2d 0.0s
=> => exporting attestation manifest sha256:852a716f978368ac94d509fdbcad7180252c34f4f8ab126d9fc9e6764fb10921 0.0s
=> => exporting manifest list sha256:b5e540509d0c663a681f4a6c2246e44acac9a3fca50d0fda2b89b35b4b2702dd 0.0s
=> => naming to docker.io/library/sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586649 0.0s
=> => unpacking to docker.io/library/sha256:9739a607cecceea347fade8e485cb7c372b86608284aaa852144ebb755586649 0.2s
View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/4btzhep5n0ttsar3bibf4z96c
C:\SSNFun\IITM\sudhishssn134-project\_1\_tds-b240fec>docker run -e AIPROXY\_TOKEN=$AIPROXY\_TOKEN -p 8000:8000 sha256:9739a6
07cecceea347fade8e485cb7c372b86608284aaa852144ebb755586649
INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

Sir, But I couldn’t run the last command you gave,

```
uv run evaluate.py --email <any email> --token_counter 1 --external_port 8000

```

As I dont have evaluate.py

But, the DockerImage is built and is running without error sir.  
Please guide me after this sir  
Thank You So much sir

---

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png)
[URGENT ATTN REQ: technical discrepancy and inconsistency in the evaluation scripts of graded assignment and project 2](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-req-technical-discrepancy-and-inconsistency-in-the-evaluation-scripts-of-graded-assignment-and-project-2/173172/32) [Tools in Data Science](/c/courses/tds-kb/34)

> Project 1 : You tried to copy parent folder(Ref:line number 8 in your [Dockerfile](https://github.com/sudhishssn134/project_1_tds/blob/main/Dockerfile)) but there is no parent folder with respect to github repo’s root folder, so it fails evaluation.
> Project 2 : Response we received through google form was <http://127.0.0.1:8000/api> which is local host url not a vercel endpoint.

---

