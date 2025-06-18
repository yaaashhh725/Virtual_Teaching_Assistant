# project-2-tds-solver-discussion-thread

Please post any questions related to [Project 2 - TDS Solver](https://tds.s-anand.net/#/project-2).

Deadline: Monday, March 31, 2025 6:29 PM

---

---

If someone Scrapes the GA Questions with Answers , Can you Please Send them , All of us have might have different GAs (a lil bit maybe), so more data more helpful. PLEASE HELP…

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f1002382/48/68945_2.png)
[Project 2 - TDS Solver - Shared Data Pool](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-shared-data-pool/169045) [Tools in Data Science](/c/courses/tds-kb/34)

> Project 2 - TDS Solver - Discussion Thread
> Creating this Thread to share answers and questions from your respective assignments
> Why? ![interrobang](https://emoji.discourse-cdn.com/google/interrobang.png?v=12 "interrobang")![thinking](https://emoji.discourse-cdn.com/google/thinking.png?v=12 "thinking")
> If we can Train the LLM with these Questions already, we can easily do well?
> Too many Questions for LLM ![nerd_face](https://emoji.discourse-cdn.com/google/nerd_face.png?v=12 "nerd_face")![nerd_face](https://emoji.discourse-cdn.com/google/nerd_face.png?v=12 "nerd_face")![nerd_face](https://emoji.discourse-cdn.com/google/nerd_face.png?v=12 "nerd_face")
> True we can use embeddings, map that stored in-system dictionary and use relevant questions from in-system data to send as context with answer
> What We need from YOU 🫵🏽
> Get to scraping your respective Gra…

@all

---

is it possible to have written solutions to all 5 assignments , instead of just live sessions. I have certain pending questions from the first 5 assignements.

---

Please quickly arrange a live TDS session to explain this project. There are a lot of doubts and questions in our minds.

---

Please also give access to the answers for GAs. So that we can evaluate our api with the correct answers.

---

[@carlton](/u/carlton) sir, is there any bonus marks for code uniqueness and extra tasks like project 1

---

If we use ngrok to create a tunnel to our API or Llamafile server, for how long should our terminal remain running? Should it be active only at the time of submission, or must it be continuously available until evaluation is completed?

---

Is it like only the questions from the portal will be sent to the api?

If yes, is this project just about finding which question is asked and accordingly match the answer send the answer as response?

---

Here's a description of the image:
The image is a web page section with a dark background, the title says "Deploy your application", and is followed by a description stating how to deploy an application to a public URL.
image text: Deploy your application
Deploy your application to a public URL that can be accessed by anyone. You may use any platform, including
Vercel.
  
Hello Sir,

I understand that we can deploy on vercel. Can it be deployed on Heroku as well? I believe both serve the same purpose. Wanted to know your thoughts on the same sir.

Thanks and Regards  
Shalini

---

If you use ngrok, ensure that it is running continuously until you get your results

---

Any question from first 5 Ga’s can be there and you would need to analyze which question it is, you can use function calling or prompting as well. Function calling is better approach here.

---

Hi [@24f2006531](/u/24f2006531)

You can deploy it anywhere, just test how it works on Heroku, if it works(send request to api endpoint to your application and it should respond with answer)

Kind regards

---

will the asked question be same which was asked in my GAs (i mean there were variations in problem statements for diff-diff students.)  
[@Jivraj](/u/jivraj) sir

---

Was the variation because of the datasets? Or even the problem statement?

---

Mostly problem statement like different cities etc

---

Then it comes down to what the project demands, as in what kind of questions the llm will be tested on (like you said). Hope the team can give us a test set like in the first project.

---

my question is some graded assignments have image files as a answer, so should our api return files as the answer or like can you clarify what type of answers we need to work on?

---

I guess yes, our APIs should return photos if required

---

@all

Keep posting your doubts here we will have answers to all of your doubts In Thursday’s session.

Kind regards

---

Sir will it answer deployment question? like what will be output link or anything else?

---

[@Jivraj](/u/jivraj)  
Could we have a tutorial-type session, similar to the one provided for Project 1, just before the deadline?

---

There are a total of 57 questions in all 5 GAs(18+10+9+10+10).  
Due to so many different formats of accepting questions and solving them, my main question is:  
Is the main essence of this project related to deciphering cryptic js code in order to scrape it?

Some other doubts are

1. Some questions ask for you to access some hidden divs in the html page and use that for solving (like week 1 q11)
2. Some questions ask you for AIPROXY TOKENs (like week 3 q9)
3. Some questions required manual correction to get correct answers (like week 4 q2)
4. Some questions require file output (like week 2 q2)

How do we account for this? [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) [@carlton](/u/carlton)

---

I have few questions just going through the Project 2 problem statement.

1. Are we supposed to use OpenAI api’s or locally/private hosted one?
2. Many of the questions need files or images or audio files as input, same api is expected to handle those also?
3. Can we work in a team and submit the project together?
4. If we are to use locally hosted llm system, our systems are not strong enough to run most of the good ones locally
5. Is it possible to get a TA to collaborate in our project as an observer?

awaiting a response.

Thank you…

---

LLM is god, if you dont know how to use llm in your work, you are failed students. unnecessary project statement.

---

Is it okay if my api only answers the questions which were asked in my GAs ? [@carlton](/u/carlton) sir [@Saransh\_Saini](/u/saransh_saini)

---

please confirm this query sir [@Jivraj](/u/jivraj) because most of them are very hard to make automated.

---

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Dear Sir,  
I have few questions. It is written in the [Tools in Data Science](https://tds.s-anand.net/#/project-2) that we can expose the api using vercel (the example given also uses vercel). But I don’t think vercel can handle/allow many operations, some of them are listed below.

1. In GA 1 ques 13 and GA 2 Ques 7, we have to create github repo, then creating github actions and then retrieve the raw github file url. We can accomplish this using Github CLI `gh` which we have to install in the vercel instance using `apt` package manager.  
   But, Vercel does not provide sudo access which is required to install packages.
2. In GA 2 ques 10, we have to use local LLM (Llamafile), will vercel allow that?  
   Also after that, we have to give answer as the ngrok public url for which we have to first install `ngrok` package.
3. In GA 2 ques 8, uploading an image to Dockerhub requires `docker` package installed.
4. In GA 2 ques 6, Deploy a Python API to Vercel in a Vercel instance?
5. Many ques require writing and running FastAPI server to serve data with CORS enabled. Can Vercel allow/do that?
6. And many more

Most tasks mentioned above like installing packages etc. requires sudo privilages or may face restrictions set by Vercel.  
Vercel does not provide sudo access or any form of root access to its hosting environment which is required to perform the above tasks.

Many of these task can be done in our local systems (exposing to internet using cloudflare tunnels/ngrok), but we cannot run our systems 24\*7 during evaluation.

I can see only one option left that is renting a VPS from server providers like digitalocean, gcp, aws etc, which will provide us sudo access and 100% uptime.

Also, some ques requires external toolings like

1. In GA1 ques 5, it is written to explicitly use Excel and this will only work in Office 365.
2. In GA1 ques 6, we have to use Devtools to show/find the hidden element in the question. Now, the question parameter in the POST request will be plain text, so how the element can hide there?
3. GA 2 ques 4 and GA 2 ques 5 uses Google Colab specific python libraries like google.colab which can’t be installed locally.

How to solve these above questions that require explicit usage of external tools.

Also, handling POST request for some questions are not clear like

1. In GA 2 ques 2, we have to compress the image and upload the image as answer. So, now how to response such answer in json object. Should we encode the resultant compressed image as base64 string or Image URL or Data URI.
2. Some ques have images in them. For those images in GAs, I right clicked and used “Save as” to save the images and then done the required computations. So, now when this question will be sent as POST request, will the image be included as the base64 encoded string in the question parameter of the POST request itself or as an optional file attachment?

Another concern is regarding the OpenAI API TOKEN, unlike Project 1, Project 2 does not have an API\_TOKEN parameter in the POST request. Hence, the API TOKEN provided from <https://aiproxy.sanand.workers.dev> will be also used during evaluation. Now, what will happen if our API TOKEN credits gets end during evaluation. The LLM will throw errors then.

Please advise what we should do. please clarify Sir.

---

Can you provide with an evaluation file like we had for Project 1.

---

Can we have groups for this please? [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

If you are talking about the parameters of those questions, then it would be better if you make your API capable of working with different parameters.

---

Well if your API is capable of solving those questions in your GAs with the expected answer, then that’s sufficient validation.

---

If you are indicating towards working collaboratively then,  
Yes, we encourage you to collaborate with others and collectively work towards solving this project. Even if you are going for the relatively easiest approach of Function Calling, it would require you to code about 50 functions to solve all your tasks. Which is why it is sensible to work collectively.

---

Hello Sir,

I have a few questions. Would like your thoughts and suggestions over the same.

1. Currently answers that we have entered for GA’s 1 to 4 are not available and only for GA5 its available. It would be helpful for the project (when running the Curl command for each of the question) if the assignments can display the answers we’ve entered as well for verification purposes.
2. The first question of GA1 q1 needs for us to run vs code but when executing it through vercel its not possible because vercel is a serverless environment. In this case, is it okay to manually enter the answer in the code, so when the question is triggered it takes the manual output from the code.
3. Can you provide some clarity as to how the question is supposed to be and structured ? Or should the code be able to handle multiple variants of the question? To address this concern, i tried to implement sentence\_transformers using a lightweight model but the vercel application build failed saying that the data is too long and that Vercel serverless function deployment size exceeds the limit of 250 MB. Should i consider deploying elsewhere or change the approach?
4. How do we handle questions pertaining to Devtools - creating input box etc.

Thanks and Regards  
Shalini

---

What does it mean to solve the question?  
Everyone is asking that?  
Do you yourself know what to do and to go about it?  
Or just pull out something from your hAtSS at the last moment?

“and responds with the answer to enter in the assignment.”  
From my understanding only those questions that are solved with a program and give an answer are to be considered… For example it states in the project that ![:backhand_index_pointing_down:t3:](https://emoji.discourse-cdn.com/google/backhand_index_pointing_down/3.png?v=13 ":backhand_index_pointing_down:t3:")  
" The response must be a JSON object with a single text (string) field: `answer` that can be directly entered in the assignment. For example:"  
If you all still have not responded, then I’m honestly not sure if this is what y’all meant.  
Last project was not clear to some extent, This time its even more vague.

I understand that y’all want to give different projects to help High Order Thinking skills, but if not executed properly, no one actually learns anything and we(I) just end by debugging the project statement code and question with no relevance to the project. If we wanted to do that, I could just go random GitHub repos and solve and create pull requests for a specific bug. Also we end up losing interest thinking most if the course instructors don’t what they are doing. I understand Anand Sir is extremely busy(like really busy lol), but what are the course instructors doing?

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)  
Sir is it possible to extend the deadline of this project 2 to Arpil. Because of Quiz2 and Vivas of project should be completed in march only as I am degree potential student. Extending the deadline wont be disadvantage also, project2 will be like ET preparation

Please consider this request sir

Thanks

---

I just want to know if you prefer using an existing language model application where we utilize an LLM (Large Language Model), train it, and format the output. For instance, I used the Gemini API key, integrated it with Python, and then formatted the results with the help of Copilot to achieve the desired outputs.

Alternatively, do you want us to create a new LLM model and train it with questions from graded assignments? I’m curious about your preference.

Additionally, would you like the LLM to provide specific answers regarding computer specifications, or should it give general specifications? For example, in Graded Assignment 1, there is a question about the editor: Visual Studio Code.

Your editor is the most important tool in your arsenal; that’s where you’ll spend most of your time, so make sure you’re comfortable with it.

Visual Studio Code is, by far, the most popular code editor today. According to the 2024 Stack Overflow Survey, almost 75% of developers use it. We recommend you learn it well. Even if you use another editor, you’ll likely work with others who use VS Code, so having some exposure is beneficial.

To get started, you can watch these introductory videos (totaling 35 minutes) from the Visual Studio Docs:

* Getting Started: Set up and learn the basics of Visual Studio Code (7 min)
* Code Editing: Learn how to edit and run code in VS Code (3 min)
* Productivity Tips: Become a VS Code power user with these productivity tips (4 min)
* Personalize: Personalize VS Code to make it yours with themes (2 min)
* Extensions: Add features, themes, and more to VS Code with extensions (4 min)
* Debugging: Get started with debugging in VS Code (6 min)
* Version Control: Learn how to use Git version control in VS Code (3 min)
* Customize: Learn how to customize your settings and keyboard shortcuts in VS Code (6 min)

## AI Editors: Copilot, Cursor

Note: AI editors like Cursor, Cody, and GitHub Copilot use LLMs to help you write code faster. These tools are built on top of VS Code and have become standard in every developer’s toolkit. Please make sure to use them.

To install and run Visual Studio Code, open your Terminal (or Command Prompt) and type `code -s`, then press Enter. Copy and paste the entire output below.

What is the output of `code -s`? The output of `code -s` cannot be universally answered because it depends on the user’s system and the specific version of VS Code installed. The question requests the output of a command that is unique to each user.

As for the part about getting answers from the LLM model, I believe that may require using an AI agent. I am currently searching for a solution for this, and I would like to know your thoughts on it.

image description: The image displays a webpage with the title "IIT Madras Assignment Helper." It includes a section to "Ask a Question" where a user can input a query related to data science assignments. There is an optional file upload, and a "Get Answer" button. The answer section displays a SQL query.
image text:
-->
IIT Madras Assignment Helper
Welcome to the Assignment Helper! This tool helps you find answers to IIT Madras Data Science graded assignment
questions.
Ask a Question
onigi-perring posts.
Write a DuckDB SQL query to find all posts IDs after 2025-01-16T06:36:30.367Z with at least 1 comment with 5
useful stars, sorted. The result should be a table with a single column called post\_id, and the relevant post
IDs should be sorted in ascending order.
Check the console for the result of your query.
Upload assignment file (optional): Choose File No file chosen
Get Answer
Answer:
sql SELECT post\_id FROM social\_media WHERE timestamp >= 2025-01-16T06:36:30.367Z AND EXISTS(
SELECT 1 FROM json\_each(comments) WHERE json\_extract(value, $.stars.useful)::INT > 5 ) ORDER BY
post\_id;

---

can we make this type of solution for above project

[yantravid-git-main-vicky-kumars-projects-5400c012.vercel.app](https://yantravid-git-main-vicky-kumars-projects-5400c012.vercel.app/)

### [IIT Madras Assignment Helper](https://yantravid-git-main-vicky-kumars-projects-5400c012.vercel.app/)

---

and this is also working with simple question  
![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/b/3b2f71bedf5d8b246e6da38b5f7016c193083daa.png)

---

image description: The image is a terminal window displaying a command-line interface. The command-line interface is set on a dark background and presents a series of commands and their outputs. The first command is a curl POST request to a specified URL. Following the command, are some lines with "More?" and some file operations. The image shows a shell session, likely in Bash, with curl command and the output.
image text: D:\Yantravid\yantravid>curl -X POST "https://yantravid-git-main-vicky-kumars-projects-5400c012.vercel.app/api/" ^
More? -F "question=Download qmove.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all file
s replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt. What does running grep \* | LC\_ALL=C sort |
sha256sum in bash on that folder show?" ^
More? -F "file=@D:\Yantravid\yantravid\test\_data\qmove.zip"
{"answer":"text\ne086115d65479e8562262a61e17e4568880561732b2d6e81117e041681883191"}

---

Sir, for GA-5 question number 3 the file is too large to send via request to vercel  
possible solution is uploading on google drive or smth like that but how will u guys send such long files plus the project only mention sending files not url …Kindly clarify regarding this.

---

Here's a description of the image:
image description: The image is a text-based instruction or explanation presented on a dark background. It gives instructions for an API endpoint. The instructions include information about POST requests and multipart/form-data for file attachments.
image text:
Your application exposes an API endpoint. Let's assume that it is at https://your-app.vercel.app/api/.
The endpoint must accept a POST request, e.g. POST https://your-app.vercel.app/api/ with the question
as well as optional file attachments as multipart/form-data.
  
Here, the questions entered after the endpoint will be exactly same as the GAs or be similar as the GAs ??

---

[@Saransh\_Saini](/u/saransh_saini) please look into my matter and please clear my doubt

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
I received this mail from TDS Google Group Announcement this morning at 10:30 am. The Project 2 submission date mentioned in the mail i.e. 15 March 2025 contradicts with submission date mentioned in [Tools in Data Science](https://tds.s-anand.net/#/project-2) and  
[Project 2 - TDS Solver - Discussion Thread](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029) i.e. 31 March 2025. Please clarify.

Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of an email about "Tools in Data Science" course from study.iitm.ac.in. The email discusses the eligibility to attend the end-term exam and course grades, including the grading criteria with formulas. The email also provides details of assessments like "Remote Online Exam 1", "take home project 1", and "take home project 2".
\*\*image text:\*\*
```
From
donot\_reply@study.iitm.ac.in
To 25t1\_se2002-announce@study.iitm.ac.in
Subject Tools in Data Science - Eligibility to write the final exam
List-ID <25t1\_se2002-announce.study.iitm.ac.in>
Dear Learners,
Eligibility to attend the end term exam: Average of best 2 out of the first 5 weekly assessment
scores >= 40/100
Eligibility to get the course grade: Attending end-term exam
Assessment
Open date
Submission date
Peer Review
Date
ROE1
Remote Online Exam 1 Sunday, March
2, 2025 13:00
Hrs IST
(45 mins, open
internet, Objective
assessments)
Sunday, March 2, 2025
13:45 Hrs IST
P1
take home project 1
(open internet)
Friday, January
17 February 7,
2025
Monday Saturday
February 15 17, 2025
Tuesday,
February 25,
2025
P2
take home project 2
(open internet)
Friday,
February 21
Wednesday Monday,
March 15 12, 2025
Monday,
March 17,
28, 2025
2025
GAA = score in best 4 of 7 weekly assignments on the portal (open internet, MCQs)
F = Final end term exam (no internet, in-person, mandatory).
P1 and P2 will have two components - Submissions and peer reviews with weightage 80:20.
Final course score T = 0.1GAA + 0.2 ROE1 + 0.2 P1 + 0.2P2 +0.3F
Final course score T = 0.15GAA + 0.2 ROE1 + 0.2 P1 + 0.2P2 + 0.25F
Please refer the grading documents for the further details.
Regards,
IITM BS Team
You received this message because you are subscribed to the Google Groups "Announcement list for
Jan 2025 - Tools in Data Science" group.
To unsubscribe from this group and stop receiving emails from it, send an email to 25t1\_se2002-
announce+unsubscribe@study.iitm.ac.in.
```
  
image description: The image presents information about a project titled "Project 2 - TDS Solver." It details the project's deadline, announcement date, and provides a link for questions. It also includes a background section describing a scenario involving a student in a data science course.
image text: Project 2 - TDS Solver
This project is due on 31 Mar 2025 EOD IST. Results will be announced by 15 Apr 2025.
For questions, use this Discourse thread.
Background
You are a clever student who has joined IIT Madras' Online Degree in Data Science. You have just enrolled in the
Tools in Data Science course.
To make your life easier, you have decided to build an LLM-based application that can automatically answer any
of the graded assignment questions.
  
image description: The image shows a discussion thread titled "Project 2 - TDS Solver". It is about a course project. The thread is started by "s.anand" with a request to post questions. The deadline is set for March 31, 2025, at 11:59 PM. There are details about views, likes, links, and users. It also indicates it was pinned on March 3.
image text: Project 2 - TDS Solver - Discussion Thread
■ Courses Tools in Data Science announcement term1-2025 tds-project-2
s.anand Course\_faculty
Please post any questions related to Project 2 - TDS Solver 71.
Deadline: Monday, March 31, 2025 11:59 PM
530 32 3 24
views likes links users
Pinned on Mar 3
9d
5
Reply
6 min
read

---

The deadline is 31st March for Project 2. Please ignore the announcement email. We apologise for the confusion.

Kind regards

---

Is there any proxy\_Ai token as provided earlier for the project 1..

---

Hi Ayush,

Just go the AI Proxy token issue page and re-issue it or use the same one. The limits get reset.  
Kind regards

---

My Approach , is to

1. scrape and parse all the current question
2. create embeddings , of the questions.
3. create a test endpoint , just to check if i am able to correctly identify the questions
4. segregate numerical , string and json responses and see if these can be answered part of phase 1
5. Phase 2 , experiment with url based answers. need to see if an MCP server can come in handy  
   to deploy a server and return an url

---

Since the token is limited, I have thought to use the run llms locally, to check for the accuracy of solving the question.

1. I want to know which LLM will be more closer to the one used for evaluating our project.
2. Does the model used for evaluation is capable for handling raw files, or we need to pass it in the text format..(As as I am to recall, the models are capable enough to handle the files..)  
   Thanks!

Does anyone willing to work with me..?  
contact: whatsapp(8697454203)

---

Should we answer the questions and return the response to enter in the answer box(as stated in the question) or should we just provide instructions on how to go about solving the question? Some of the questions include pictures and we cannot use LLM for pictures.

---

Did you just Post your number on a public forum?

---

They(instructors) only don’t what to do it looks like, Anand Sir will tell them and they will tell you (with 25-50 percent lossy communication), just wait and keeping tagging Anand Sir. He will explain clearly, Ask everyone to push for a live session with Anand Sir , that 40 mins he explains will be worth its weight in gold, Hope he does that. Flattery gets me everywhere (not really, I really think Anand Sir is OP. Check out his YT ![:fire:](https://emoji.discourse-cdn.com/google/fire.png?v=14 ":fire:")![:fire:](https://emoji.discourse-cdn.com/google/fire.png?v=14 ":fire:")![:saluting_face:](https://emoji.discourse-cdn.com/google/saluting_face.png?v=14 ":saluting_face:"))! [@s.anand](/u/s.anand)

---

A good video, with working code for OpenAI agents api .. <https://www.youtube.com/watch?v=0Z7u6DTDZ8o>

---

should we make the functions on the basis of the GAs or should we make it general so it will be able to perform the task but the data provided will be different.  
[@s.anand](/u/s.anand) [@carlton](/u/carlton)

---

The key learning objective for Project 2 is for you to be absolutely comfortable interacting with APIs and understanding how they work to perform tasks.

So there is very little need for the use of LLMs or agents.

1. Identify the the question being asked (how you do this is upto you, you can be as simplistic as using regex to look for some key words, or you can be clever and create embeddings out of the original question and calculate the similarity from the request)
2. Create a function that solves the question with the required parameters and inputs. Remember this does not have to be fancy. Just compute the answer. You do not need to do the task as the GA required. You ONLY want the answer. No tools required. Just a computed answer.
3. Give the answer back as specified.

Kind regards

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png) carlton:

> You do not need to do the task as the GA required.

Does this mean this type of question won’t be paramaterized?

![Screenshot 2025-03-18 at 5.17.35 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/3/8/3800f4aa4cc2ec09122cedf8c48a015520153fa9_2_690x46.png)

Like instead of `code -s` there won’t be any other command, otherwise it would require installation of VS Code inside a container to find the answer or this type of questions won’t be part of evaluation at all?

The same confusion is for these type of questions as well:  
image description: The image presents two sections, each containing a prompt related to writing formulas in Google Sheets and Excel. The first section involves a Google Sheets formula, and the second focuses on an Excel formula. Both prompts instruct the user to type the provided formula and enter the result.
image text: Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
=SUM(ARRAY\_CONSTRAIN (SEQUENCE (100, 100, 15, 6), 1, 10))
What is the result?
Check
5 Use Excel (0.25 marks)
Let's make sure you can write formulas in Excel. Type this formula into Excel.
Note: This will ONLY work in Office 365.
=SUM(TAKE (SORTBY({3,14,6,10,3,12,9,6,3,12,15,4,11,11,4,14}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 9))
What is the result?
Note: If you get #NAME? you have the wrong version of Excel. Find a friend for whom this works.
Check

A bit more clarity would be helpful. Thanks in advance.  
[@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> Like instead of `code -s` there won’t be any other command, otherwise it would require installation of VS Code inside a container to find the answer or this type of questions won’t be part of evaluation at all?

there will not be any other command. This question can be solved with a hardcoded answer

Excel and Google sheet questions can be solved by just using python . No excel or google sheets required.

The question WILL be parameterised however. So the numbers might be different. You should just understand what the question is asking and solve it programatically to get the answer.

---

Guys, I have designed a new version of this project. Please ask questions related to the graded assignment and let me know if you observe any errors.  
[AI Question Answering](https://regulations-contributing-millions-angela.trycloudflare.com/)

---

Means no github, image related, vs-code, vercel, etc. will be there

---

And the answer will be in string format ??

---

I am not sure how you came to that conclusion!

For example vercel question still requires a vercel endpoint that will respond.

What I said is some questions might not need you to use those specific tools. Your answers should still be legitimate answers that one can paste into the text box of a GA and still get it correct.

The only question that will not be asked is the LLM say yes question.

A github account would still need you to commit a file to it and provide the url that is reachable.

etc.

---

[@carlton](/u/carlton) 1 small request.. can we have 2-3 more examples in the project2 description.. so that it gets a bit more clear

---

**Prof. Anand Live Session Alert!**

* ![🕘](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/1/31e5418a6753391681e46eae2fc2ab7e4b8c0096.png) **Date & Time:** Wednesday, March 19, 2025 · 9:00 – 10:00 PM (IST)
* ![🎤](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/9/b9484a4812e4e431a40e97e94907a9c654456ebb.png) **Speaker:** Professor Anand
* ![📌](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/d/5d0b610f9487ac70603819651fb2c472635c17de.png) **Topic:** Project 2 Q&A + General Course Queries
* ![🔗](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/a/da3d7fa22946354584e940fd75549ae249ce39b9.png) **Google Meet Link:** [Join Here](http://url237.study.iitm.ac.in/ls/click?upn=u001.FrsGe6wgnGFQ7SeE9RgsnXyC7-2Bs5DCMDnB4XkxqFd3k2eEoGdOWtgYm0Vj3Y-2FyatYygA_TaYffKNLhcpM10MCY1PnqDJT-2FNuZ61KkdeQdP748DgJIHBveqWN7MW2nmp9Bjx3duSmBjg5OoK74k-2F4xXBO6V3n3qhKMKwd0wpwWDd1QTRcmufGhDej3Jovut9eB2B-2FKQIczKSgdTkzhLVDn2NzWdOijAjfGATgpHFSMVaNhH2r4WMYxY1yuBcM8h-2FC87c600hzYnZAH0tDDLBwNuOAfytRmwndVDxR5uLxLZIPV8KA-3D) (<https://meet.google.com/jdr-pquo-vza>)
* Or from the TDS Google Calendar

@all

---

## Just to be clear the special Session is tonight Wed, 19th March at 9pm.

---

my small piece of code to evaluate the GA number parsing, it may be useful for some

```

import httpx, os
import json
import logging
import random

async def run(task: str):
    async with httpx.AsyncClient(timeout=30) as client:
        logging.warning(f"🟡 Running task: {task.strip()}")
        data = {
                "question": task
            }
        files = {}
        response = await client.post("http://localhost:8000/api/parse", data=data, files=files)
        try:
            response_text = response.json()
        except json.JSONDecodeError:
            response_text = response.text
        if response.status_code < 400:
            logging.info(f"🟢 HTTP {response.status_code} {response_text}")
        else:
            logging.error(f"🔴 HTTP {response.status_code} {response_text}")
        return response.status_code, response_text
    
async def evaluate(use_case: str):
    # file exists under test_data directory
    file_path = f"test_data/{use_case}.txt"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task = file.read()
        status_code, response_text = await run(task)
        if status_code != 200:
            return False
        
        # check the returned json matches the use case
        if "GA_No" in response_text and response_text["GA_No"] == use_case:
            return True
        else:
            return False
    else:
        #print("File does not exist.")
        return False

async def main():
    use_cases = [
        "GA1.1", "GA1.2", "GA1.3", "GA1.4", "GA1.5", "GA1.6", "GA1.7", "GA1.8", "GA1.9", "GA1.10", "GA1.11", "GA1.12", "GA1.13", "GA1.14", "GA1.15", "GA1.16", "GA1.17", "GA1.18",
        "GA2.1", "GA2.2", "GA2.3", "GA2.4", "GA2.5", "GA2.6", "GA2.7", "GA2.8", "GA2.9", "GA2.10",
        "GA3.1", "GA3.2", "GA3.3", "GA3.4", "GA3.5", "GA3.6", "GA3.7", "GA3.8", "GA3.9",
        "GA4.1", "GA4.2", "GA4.3", "GA4.4", "GA4.5", "GA4.6", "GA4.7", "GA4.8", "GA4.9", "GA4.10",
        "GA5.1", "GA5.2", "GA5.3", "GA5.4", "GA5.5", "GA5.6", "GA5.7", "GA5.8", "GA5.9", "GA5.10"
    ]
    use_cases = random.sample(use_cases, 5)
    a_score, a_total = 0, 0
    for use_case in use_cases:
        a_total += 1
        try:
            success = await evaluate(use_case)
        except Exception as e:
            logging.error(f"🔴 {use_case} failed: {e}")
            success = False
        if success:
            logging.info(f"✅ {use_case} PASSED")
        else:
            logging.error(f"❌ {use_case} FAILED")
        a_score += 1 if success else 0
        
    logging.info(f"🎯 Parsed: {a_score} / {a_total}")

if __name__ == "__main__":
    import asyncio
    import argparse

parser = argparse.ArgumentParser(description="Evaluate GA No with configurable logging")
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    parser.add_argument("--log-level", default="INFO", choices=levels, help="Set logging level")
    args = parser.parse_args()
    logging.basicConfig(level=args.log_level, format="%(message)s\n")
    
    asyncio.run(main())

```

---

Hi TAs,

I attended the meet which happened today. But I don’t clearly get one thing.

Most of the questions have a **question text** and a **file: csv,zip,json,etc**

My doubt is, will the request to the end point be :

```
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file=https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;template=results;type=batting"

```

> my doubt :  
> Is this the only format or can there be other too ?

---

Hi [@23f2000573](/u/23f2000573)

Yes this is correct format for the question, It will have 2 fields question and file.

You can send a file from local machine like this `-F "file=@abcd.zip"` so here `abcd.zip` must be in current working directory.

Kind regards

---

Fine sir, this is clear. I have a few doubts in the file formats. When free, kindly address these to. I will try to cover most common doubts, so that you wouldn’t need to answer similar doubts again. Sorry if some of the doubts are basic / written incorrectly.

## FILES

The data file sent to the api will always be in the **requester’s** local machine. When the api server receives the request, the file will be in binary format?

Or

Sometimes the api server receives the file in byte and some times, it will recieve a link like this : <https://exam.sanand.workers.dev/shapes.png>

This link was take from GA2 Question 2

## HTML AND TABLE

Some questions have `html` and `tables`. In this case will these two be in a file encoded in binary, or will it be a string.

Example for string. Consider the table

| Col 1 | Col 2 |
| --- | --- |
| Row 1, Col1 | Row 1 Col 2 |
| Row 2, Col 1 | Row 2 Col 2 |

Will this be something like this

```
"|Col 1| Col 2|\n|-|-|\n|Row 1, Col1 | Row 1 Col 2|\n|Row 2, Col 1|Row 2 Col 2|"

```

or something like

```
"<table>\n<thead>\n<tr>\n<th>Col 1</th>\n<th>Col 2</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>Row 1, Col1</td>\n<td>Row 1 Col 2</td>\n</tr>\n<tr>\n<td>Row 2, Col 1</td>\n<td>Row 2 Col 2</td>\n</tr>\n</tbody>\n</table>
"

```

## HIDDEN BLOCK AND ANSWER : 2 TASKS

In one question, there were two tasks.

* Find the answer to the question
* Enable the `disabled` text block

In this question, what will the answer type be?

Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block

## MORE THAN ONE FILE

Some questions have more than one file. For example, the last question of GA5, it has a png file in this link <https://exam.sanand.workers.dev/jigsaw.webp> and a table.

In this case, how will the curl request be? Is it some thing like this

```
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question text" \
  -F "file= Image file" \
  -F "file= table file/ string"

```

## CORS HEADERS

Will the CORS headers asked in the question be the same or can it be different?

---

Hi,  
In GA 2, q5, this is the code i got in the question.

```
import numpy as np
from PIL import Image
from google.colab import files
import colorsys

# There is a mistake in the line below. Fix it
image = Image.open(list(files.upload().keys)[0])

rgb = np.array(image) / 255.0
lightness = np.apply_along_axis(lambda x: colorsys.rgb_to_hls(*x)[1], 2, rgb)
light_pixels = np.sum(lightness > 0.554)
print(f'Number of pixels with lightness > 0.554: {light_pixels}')

```

Is this the code for others as well?  
Thanks

---

So I was thinking to create the project 2 together and I was looking for collaboration, and for that we would require the following:

→ the set of question-answers pairs at first  
→ All the questions of 2 distinct students to see which parameters changes in each questions  
→ Make the solution functional and parameterised based on previous step.

Till now I have created the following:

→ Identification of the question, using embeddings  
→ extraction of parameters using llm for that particular question  
→ Implementation of 3 questions using this approach

If we come together, we all can reduce the workload and complete it on time.

\*Those who resonate with my approach or have any different approach feel free to leave a DM. I might not respond immediately as I might not be online all the time ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=14 ":slight_smile:")

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> The data file sent to the api will always be in the **requester’s** local machine. When the api server receives the request, the file will be in binary format?
>
> Or
>
> Sometimes the api server receives the file in byte and some times, it will recieve a link like this : <https://exam.sanand.workers.dev/shapes.png>

file format will be exactly same as corresponding GA.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> ```
> "<table>\n<thead>\n<tr>\n<th>Col 1</th>\n<th>Col 2</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>Row 1, Col1</td>\n<td>Row 1 Col 2</td>\n</tr>\n<tr>\n<td>Row 2, Col 1</td>\n<td>Row 2 Col 2</td>\n</tr>\n</tbody>\n</table>
>
> ```

This is correct html table format.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> Should it just be the answer or should it be the html string which will have the disabled block enabled and also the answer string sitting inside the block

It will be just answer.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> Some questions have more than one file. For example, the last question of GA5, it has a png file in this link <https://exam.sanand.workers.dev/jigsaw.webp> and a table.
>
> In this case, how will the curl request be? Is it some thing like this
>
> ```
> curl -X POST "https://your-app.vercel.app/api/" \
>   -H "Content-Type: multipart/form-data" \
>   -F "question=question text" \
>   -F "file= Image file" \
>   -F "file= table file/ string" 
>
> ```

In last question of GA5 there is only one file(image), table is not coming through file, it will be kept same for project2.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> Will the CORS headers asked in the question be the same or can it be different?

I didn’t get this question, could you point to exact question?

---

Hi [@22f3001307](/u/22f3001307)

yes it’s same code.

---

Sir, a few things are not yet clear .

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> file format will be exactly same as corresponding GA.

Some questions have **clickable html buttons**. When we click that, the zipfile or json file, or csv gets downloaded

Some questions have **image attached to the text**. For this, we have to use **right click → download the image**. Here, the image is take from some url. For example. in GA2, q2, the image displayed is taken from <https://exam.sanand.workers.dev/shapes.png>.

My doubt is, what will be the value of file attribute in curl command

Will it be

* “file=binary of zipfile/csv/json” for the first type and
* “file=<https://exam.sanand.workers.dev/shapes.png>” for the second type

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> This is correct html table format.

Will this table be in the “question” attribute of curl or “file” attribute

![](https://avatars.discourse-cdn.com/v4/letter/j/b9bd4f/48.png) Jivraj:

> In last question of GA5 there is only one file(image), table is not coming through file, it will be kept same for project2.

so, can I assume that the table will be given as a html element in the “question” attribute and the image in the “file” attribute?

---

Sir  
[@Jivraj](/u/jivraj) was yesterday (March 19) 's google meet recorded and  
available for replay..

---

[@22f3002723](/u/22f3002723)

[![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/3/e/3efcd748f78a7c057c71077f79d7b0858622b9ff.jpeg "Live Session - TDS")](https://www.youtube.com/watch?v=RToHBe6yB_4)

---

thanks a lot [@23f1001231](/u/23f1001231)

---

Hi [@23f2000573](/u/23f2000573)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> Will it be
>
> * “file=binary of zipfile/csv/json” for the first type and
> * “file=[https://exam.sanand.workers.dev/shapes.png”](https://exam.sanand.workers.dev/shapes.png%E2%80%9D) for the second type

Files will be exactly same as GA assignment, if there is url then it will be a url and if it get’s downloaded by clicking then it will come from requester’s machine.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> so, can I assume that the table will be given as a html element in the “question” attribute and the image in the “file” attribute?

For questions that have table they will either come as html code or as markdown. Keep a if else condition for identifying which case it is, if it’s a html then beautiful soup should be able to find table tag, if it’s markdown table then it can be identified with `|` characters.

Kind regards

---

For GA 1, question 2  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a dark grey box with text and code snippets related to HTTP requests using the "httpie" package. There is an instruction to use the package to send a HTTPS request. The provided JSON output of the command is also displayed. Finally, there's a "Check" button at the bottom.
\*\*Image Text:\*\*
Running uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the
URL.
Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to
21f2000709@ds.study.iitm.ac.in
What is the JSON output of the command? (Paste only the JSON body, not the headers)
{ "args": { "email": "21f2000709@ds.study.iitm.ac.in" }, "headers": {
"Accept": "\*/\*", "Accept-Encodir
Check
  
The portal accept answers in strict json with double quotes. Now in the project we need to return the answer in string value which again has double quotes, so the best answer I could get is using `\"` inside the answer like this.

![Screenshot 2025-03-21 at 4.25.02 PM](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/e/1e4550c6e2637e7cf226d943eb61ccb0a8f96770.png)

But still the GA portal marks it as invalid json. What to do in this case?  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Hi [@21f2000709](/u/21f2000709)

image description: The image is a screenshot of a Python code execution environment, showcasing a series of commands and their outputs. The code appears to be manipulating a JSON object. The first few lines define a variable `jobj` and display its string representation. Subsequently, the `json.loads()` function is used to parse the JSON string, demonstrating how it is converted into a Python dictionary. Finally, the `type()` function is called on `jobj` to determine its data type which is 'str'.
image text:
In [28]: jobj
Out [28]: "{'name':'jivraj'}"
In [29]: jobj = '{"name":"jivraj"}'
In [30]: jobj
Out[30]: '{"name":"jivraj"}'
In [31]: json.loads(jobj)
Out [31]: {'name': 'jivraj'}
In [32]: json.loads(jobj)['name']
Out [32]: 'jivraj'
In [33]: type(jobj)
Out [33]: str
In [34]: |

This works, just send a string which can be loaded as json object.

---

The correct answer has to be with the escape sequence otherwise you cannot send a valid response back.  
We never feed your response to the GA by copy pasting.

Here's a description of the image:
The image appears to be a code snippet, likely in Python, demonstrating JSON serialization and deserialization. The code defines a `response` object, serializes it to a JSON string, prints the JSON string, and then deserializes the JSON string back into a Python object. It also prints the answer and then prints a statement. The code is displayed on a dark background with a monospaced font.
image text:
```
response = {
"answer": '{ \"args\":{\"challenge\": \"How can TDS ever hope to solve this problem?\" } }'
}
import json
send\_response = json.dumps(response, indent=2)
print (send\_response)
✔ 0.0s
{
"answer": "{ \"args\": {\"challenge\": \"How can TDS ever hope to solve this problem?\" } }"
}
tds\_evaluator = json.loads(send\_response)['answer']
print (tds\_evaluator)
✔ 0.0s
{ "args": {"challenge": "How can TDS ever hope to solve this problem?" } }
print ("OH MY GOODNESS! I CAN'T BELIEVE IT! THIS IS AMAZING!")
✔ 0.0s
OH MY GOODNESS! I CAN'T BELIEVE IT! THIS IS AMAZING!
```

---

So the questions expecting JSON will be jsonified separately before passing to the evaluator because in the current implementation in the text field idk why it is failing to load the json with `\"` however I could load the exact thing using json.loads in python.

---

hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj) !  
could you please provide us with the correct answers for all the 57 GA questions, so that it would be really helpful for us to cross check if our app is returning the correct answer for each question. please consider sharing the correct answers for all the questions as they are not available in the seek portal as well

---

Hi [@23f2003413](/u/23f2003413)

We won’t be sending codes for any of the questions, regarding validation part you can submit answer to portal and if that works.

All first 5 GA’s were conducted on anand sir’s proxy server portal, so just enable check answers button and you can test answers.

---

can u please let me know on how to enable the check answers button? and which proxy server portal are you talking about. please help me out!

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir

image description : The image shows a dark-themed webpage with text and a few interactive elements. The top portion of the screen displays a header with information such as time, network connectivity, and a website address. Below that is the body of the webpage which has instructions about Github pages with associated text and the email address 22f3000819@ds.study.iitm.ac.in, along with guidance on how to format an email address and a place to input GitHub Pages URL, followed by a "Check" button and a final instruction.
image text:
12:30
M.
TDS 2025 Ja...
sanand.workers.dev
Publish a page using GitHub Pages that
showcases your work. Ensure that your email
address 22f3000819@ds.study.iitm.ac.in
is in the page's HTML.
GitHub pages are served via CloudFlare which
obfuscates emails. So, wrap your email
address inside a:
<!--email\_off-->22f3000819@ds.study.i
What is the GitHub Pages URL? It might look
like: https://[USER].github.io/[REPO]/
If a recent change that's not reflected, add ?
v=1, ?v=2 to the URL to bust the cache.
Check
4
Use Google Colab (0.5 marks)
  
For questions like this (there’s a similar one in GA1 too, will the user send the USER and REPO of their GitHub account as parameters too?  
Even if they do, my script may not get necessary authentication to create repo and make commit in their repository. In this case, would I have to implement GitHub OAuth flow?  
If they don’t send those details but just the email and I am expected to just change the email in my own repo and commit, in the worst case making the same change repeatedly may be misconstrued as a DDoS attack by an automated script which may lead to my GitHub account being suspended, which does not seem ideal.  
Can you please at least hint at a solution?

Edit: Same query for the GitHub actions question (GA2 Q7)

Another edit: A similar query for GA2 Q8. Repeated dockerimage pushes to Dockerhub with different tags.

---

Use the following script to enable answer boxes and check answers buttons:

```
inputs = document.querySelectorAll('input')
textboxes = document.querySelectorAll("textarea")
buttons  = document.querySelectorAll("button")
inputs.forEach(input => input.removeAttribute('disabled'));
buttons.forEach(input => input.removeAttribute('disabled'));
textboxes.forEach(input => input.removeAttribute('disabled'));

```

This was provided with the Mock ROE2 mail.

---

For GA-1 question 10,  
we need to get the hash of the json, from the site [JSON Hash](https://tools-in-data-science.pages.dev/jsonhash),  
I found that underneath it using sha-256 in a function inside the encrypt.js file but still when I implemented the same in python, it is giving a different hash. Can we get the hashing code in python?

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

Update:

* I was successful in getting the hash in js.

---

You won’t be required to update someone else’s repo.  
Any github name, repo name is fine.  
Just that it should have github pages with that particular email address.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> Same query for the GitHub actions question (GA2 Q7)

Same for GA2 Quetion7 as well, you github url is required.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> If they don’t send those details but just the email and I am expected to just change the email in my own repo and commit, in the worst case making the same change repeatedly may be misconstrued as a DDoS attack by an automated script which may lead to my GitHub account being suspended, which does not seem ideal.  
> Can you please at least hint at a solution?

In evaluation we will only send request one worst case twice or thrice if it fails from our end, so no issues with that.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000709/48/134907_2.png) 21f2000709:

> I was successful in getting the hash in js.

I was thinking of same solution it would definetly work in js.

---

Okay. Thank you sir. I’ll just do this after the rest for now.

Another question .. In GA1 Q6, will the hidden element be sent as an html file or will the tag be included in the question parameter?

---

[@carlton](/u/carlton) and [@jivraj](/u/jivraj),

Hello.. I am facing issue with zip file extraction function which is in many GA1 questions. e.g., for GA1 Q15, if I use 7-zip to extract files, it shows the correct total size when using Postman for local server. If I use python built-in function, it calculates a different value (which is incorrect). So, I used 7-zip. But I (with help from copilot agent) am not able to make 7-zip work on the vercel deployment. Can we just hard code the answers to GA1 questions, or is there a way to take answer from local server and use it for response in vercel (sorry, it doesn’t even make sense to me, but a lot of things are hard to understand anyway)? Or how do we resolve this 7-zip issue. Python built-in extraction did not work correctly even after hours of trying..

I have another question. Due to lack of time, if I just submit the Project 2, with question/answers to GA1, (and if these all work as expected on vercel), how much approx score can we get if I am not able to do other GAs at all for Project 2. Edit after posting: I can hard code questions and other answers from GA2 upto GA4 (I missed GA5, so don’t have those answers). Thank you.

---

I too want to know like by 5 questions at random, is it 1 random question per GA or 5 random questions from the entire 5 GAs?

In the later case, there would be no certainty unless all of our questions works and there aren’t any unexpected surprises at the evaluation.

---

in the GA 4 question 5 ( Find the bounding box of a city ) Will the OSM\_id ending digits be provided. In the question body they are not there but on submission they come like in the attached screenshot.  
image description: The image is a white background text, the title is "Impact". There are listed points after the title "By automating the extraction and processing of bounding box data, UrbanRide can:". The next part is a question and an answer with an error below it.
image text: Impact
By automating the extraction and processing of bounding box data, UrbanRide can:
• Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs.
• Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents.
• Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements.
• Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality.
What is the minimum latitude of the bounding box of the city Tianjin in the country China on the Nominatim API? Value of the minimum latitude
38.566
Error: Incorrect latitude. Check OSM ID ending with 2077

---

[github.com](https://github.com/Tusharisme/TDS_Project_2)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/6/b6b0ba3cab8056213814184ce412198bd670c7fd_2_690x344.png)

### [GitHub - Tusharisme/TDS\_Project\_2](https://github.com/Tusharisme/TDS_Project_2)

Contribute to Tusharisme/TDS\_Project\_2 development by creating an account on GitHub.

This is my project github repo link.I just wanted your guys suggestion with this…like am I going correct

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

I faced the same issue. Initially, I used `geopy.geocoders` to solve the question, and it provided the correct answer during the assignment submission. However, the same approach is now giving an incorrect result.

Instead of using `geopy`, try using this URL directly: <https://nominatim.openstreetmap.org/search> .  
This worked for me.

---

1. I have a doubt like when I pass answers in string and in the questions about markdown will the \n characters be properly parsed before checking the correctness of the markdown or will it be directly checked for valid markdown? Because the raw string when pasted in the text box of the GA isn’t getting the markdown.
2. In case of image compression question, should I return the base64 encoding of the compressed image?  
   [@Jivraj](/u/jivraj)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
**Respected TDS Team,**

I currently have Three doubts regarding **Project 2**:

1. As per the 19th March session, it was mentioned that the files would be the same for everyone, and only the parameters in the questions would vary. However, I have noticed that the files can actually be different. To support this, I’m attaching screenshots of the CSV files for GA5 Q1—one is mine, and the other belongs to a batchmate.  
   image description: The image shows a spreadsheet table with columns for TransactionID, Customer Name, Country, Date, Product/Code, Sales, and Cost. The table is populated with data, including customer names, countries, dates, product codes, sales amounts in USD, and corresponding costs in USD.
   image text: TransactionID Customer Name Country Date Product/Code Sales Cost
   0001 John Doe France 10-13-2023 Eta/fzflrq 2021 USD 1973 USD
   0002 Frank Thomas United States 2022/10/14 Alpha/f2yscp 6855 USD 4866 USD
   0003 Bob Brown FRA 09-06-2023 Theta/xvwf8u 5644 USD 3504 USD
   0004 Bob Brown IND 01-27-2022 Zeta/4rk2rx 9273 USD 1235 USD
   0005 Charlie Davis United Arab Emirates 09-26-2022 Theta/0ylj7e 5699 USD 1847 USD
   0006 Charlie Davis US 2022/05/25 Kappa/bquhwf 7897 USD 3424 USD
   0007 Bob Brown AE 2023/09/20 Iota/0t6cym 8680 USD
   0008 John Doe United States 2022/09/06 Gamma/mb4cm9 8501 USD 4820 USD
   0009 Alice Johnson U.A.E 01-11-2022 Iota/vhfsw5 7582 USD 4491 USD
   0010 Eve Wilson United Kingdom 2022/07/13 Kappa/yyzmfh 630 USD 557 USD
   0011 Charlie Davis AE 03-30-2022 Alpha/ixogpm 2199 USD 1104 USD
   0012 Frank Thomas FR 01-16-2022 Beta/py2nmk 1479 USD 489 USD
   0013 Eve Wilson FRA 08-10-2022 Epsilon/vl58sf 1076 USD 2928 USD
   0014 Bob Brown UAE 05-29-2023 Zeta/dljl2j 1534 USD 4803 USD
     
   image description: The image is a table with columns for TransactionID, Customer Name, Country, Date, Product/Code, Sales, and Cost. Each row represents a transaction. The data includes customer names, countries, transaction dates, product codes, sales amounts in USD, and costs in USD.
   image text:
   TransactionID Customer Name Country Date Product/Code Sales Cost
   0001 Frank Thomas IND 12-01-2022 Delta/tbakf3 7164 USD 2062 USD
   0002 Eve Wilson US 08-10-2023 Alpha/hknae9 2457 USD 3439 USD
   0003 Jane Smith US 2022/09/04 Theta/mjrd4g 3924 USD 4544 USD
   0004 Charlie Davis IN 08-26-2023 Alpha/b3x7ax 6883 USD 2091 USD
   0005 John Doe United Kingdom 2023/02/24 Eta/6e491r 335 USD 2095 USD
   0006 John Doe Ind 2022/08/01 Theta/ehv1v9 8669 USD
   0007 John Doe Fra 2022/07/13 Delta/0yr2zu 403 USD 2617 USD
   0008 Alice Johnson AE 2022/10/09 Beta/fuaz1n 192 USD
   0009 Charlie Davis AE 2022/03/11 Zeta/4jyhlz 1936 USD
   0010 John Doe IND 10-01-2023 Kappa/xbuc0j 7623 USD 661 USD
   0011 Alice Johnson United Kingdom 2023/05/10 Theta/1dh7jm 1239 USD 995 USD
   0012 Alice Johnson U.S.A 11-18-2023 Theta/d3mi7o 8460 USD 3430 USD
   0013 John Doe AE 2022/05/13 Theta/Osjjwl 4874 USD 2020 USD
   0014 Bob Brown IND 2023/01/05 Zeta/xxgvro 3990 USD 2953 USD
   0015 Frank Thomas FRA 12-05-2023 Alpha/cw7cbz 1712 USD 4823 USD
   0016 Eve Wilson U.K 08-21-2022 Zeta/wmyow7 507 USD 824 USD
   0017 Alice Johnson Bra 2023/01/09 Alpha/lfxddg5 9914 USD 415 USD
     
   During the session, it was said that uploading files would take time, and the suggested solution was to pre-download the files on the server since they are supposed to be the same. But since the files are not identical for all students, this issue needs to be addressed.
2. In **GA4 Q2**, my task is to retrieve movie information from IMDb for all films with a rating between 3 and 5. I am scraping the correct movie names(for example 6th movie in given image), but the portal is accepting them differently. All movie names are provided in English, but the portal seems to be accepting some titles in other languages—Spanish, Dutch, I believe.  
   Here's a description of the image:
   The image shows a section of a webpage, likely related to data validation or code testing. The top portion features a text field displaying JSON data. Below this, an error message highlights a discrepancy in a title. Further down, there's a suggestion regarding manually translating titles. A blue "Check" button is at the bottom.
   image text: What is the JSON data?
   ```json
   "id": "tt30422937",
   "title": "6. Nadaaniyan",
   "year": "2025",
   "rating": "3.0"
   },
   ```
   Error: At [5].title: Values don't match. Expected: "6. Naadaniyaan". Actual: "6. Nadaaniyan"
   IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.
   Check
     
   image description: The image shows a list of movies or TV shows. The top of the image has a description about an FBI agent and Florida State officer investigating unsolved murder cases. The next entry is for "6. Nadaaniyan", with details about its release year, runtime, rating, and a brief synopsis of the plot. There is a rating icon next to it. The bottom part of the image is for "7. Watson". image text: An FBI agent and Florida State officer team up to investigate a string of unsolved murder cases. 6. Nadaaniyan 2025 1h 59m TV-14 3.0 (14K) Rate ⓘ A privileged Delhi socialite hires a middle-class student to pose as her boyfriend to maintain her social status. Their pretense becomes complicated when genuine feelings develop between them. 7. Watson
     
   Please check the issue in the images provided. How to handle this question.
3. In **GA4 Q10**, very few students were able to solve the question using LLMs or Python during the assignment. Most of us ended up solving it manually. At that time, [@carlton](/u/carlton) sir had mentioned that the question would be revised.  
   Here is the [thread link](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106) for reference.  
   How should we handle this question now?

Thankyou

---

```
// GA1 question 9:
    //     curl -X POST "http://localhost:8000/api/" -H "Content-Type: multipart/form-data" -F "question=Sort this JSON array of objects by the value of the age field. In case of a tie, sort by the name field. Paste the resulting JSON below without any spaces or newlines. 
    // [{\"name\":\"Alice\",\"age\":92},{\"name\":\"Bob\",\"age\":28},{\"name\":\"Charlie\",\"age\":16},{\"name\":\"David\",\"age\":56},{\"name\":\"Emma\",\"age\":70},{\"name\":\"Frank\",\"age\":67},{\"name\":\"Grace\",\"age\":36},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Ivy\",\"age\":44},{\"name\":\"Jack\",\"age\":53},{\"name\":\"Karen\",\"age\":65},{\"name\":\"Liam\",\"age\":23},{\"name\":\"Mary\",\"age\":97},{\"name\":\"Nora\",\"age\":68},{\"name\":\"Oscar\",\"age\":57},{\"name\":\"Paul\",\"age\":88}]"
    {
        "answer": "[{\"name\":\"Charlie\",\"age\":16},{\"name\":\"Liam\",\"age\":23},{\"name\":\"Bob\",\"age\":28},{\"name\":\"Grace\",\"age\":36},{\"name\":\"Ivy\",\"age\":44},{\"name\":\"Jack\",\"age\":53},{\"name\":\"David\",\"age\":56},{\"name\":\"Oscar\",\"age\":57},{\"name\":\"Karen\",\"age\":65},{\"name\":\"Frank\",\"age\":67},{\"name\":\"Nora\",\"age\":68},{\"name\":\"Emma\",\"age\":70},{\"name\":\"Paul\",\"age\":88},{\"name\":\"Alice\",\"age\":92},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Mary\",\"age\":97}]"
    }

```

Is it ok for GA 1 Question 9 answer output to look like this because it matches with the answer just it has the extra back slash…What should i do

```
def sort_json_array(json_array: str, sort_keys: list) -> str:
    """
    Sort a JSON array based on specified criteria

Args:
        json_array: JSON array as a string
        sort_keys: List of keys to sort by

Returns:
        Sorted JSON array as a string
    """
    try:
        # Parse the JSON array
        data = json.loads(json_array)

# Sort the data based on the specified keys
        for key in reversed(sort_keys):
            data = sorted(data, key=lambda x: x.get(key, ""))

# Return the sorted JSON as a string without whitespace
        return json.dumps(data, separators=(",", ":"))

except Exception as e:
        return f"Error sorting JSON array: {str(e)}"

```

```
{
            "type": "function",
            "function": {
                "name": "sort_json_array",
                "description": "Sort a JSON array based on specified criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "json_array": {
                            "type": "string",
                            "description": "JSON array to sort",
                        },
                        "sort_keys": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of keys to sort by",
                        },
                    },
                    "required": ["json_array", "sort_keys"],
                },
            },
        },

```

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
![sad me](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/2/e/2e577720e007a687c9e3aeecd301efb7b64eb222.gif)

---

Hi [@23f2003751](/u/23f2003751)

### Short Answer: No

### Long Answer:

Backslashes are usually not a problem when converting a string to JSON. But somehow the evaluation script isn’t taking this into consideration. Check this out.  
This is my response  
image description: The image shows a segment of code. It presents a JSON object that appears to be sorted. It has been assessed as correct, as indicated by the checkmark.
image text: Sorted JSON:
[ { "name": "Bob", "age":11 }, { "name": "Emma", "age": 11 }, { "name": "Grace", "age":14 }, { "na ✓
Correct

which is shown incorrect just after adding 2 backslashes

## Here's a description of the image: The image shows a snippet of JSON data with an error message. The JSON data appears to be an array of objects, each representing a person with "name" and "age" properties. The text reads "Sorted JSON:" followed by a snippet of JSON data, showing an error. image text: Sorted JSON: [{ {"name": "Bob", "age": 11 }, { "name": "Emma", "age": 11 }, { "name": "Grace", "age": 14 }, { "r SyntaxError: Expected property name or '}' in JSON at position 16 (line 1 column 17)

### Note: It would be better to check your responses on the TDS portal before finalising the script. You can access the answer box and check button by removing the disable attribute.

---

[@Saransh\_Saini](/u/saransh_saini)

it can’t be fixed actually, you would need the answer in the json format

`{"answer": "actual_answer"}`

but if the actual\_answer needs to be string and if it happens to be of json type, it has to be represented using `\"`

---

Do we require open\_api key like project 1 for this one too ? if yes from where we can get that?

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> As per the 19th March session, it was mentioned that the files would be the same for everyone, and only the parameters in the questions would vary. However, I have noticed that the files can actually be different. To support this, I’m attaching screenshots of the CSV files for GA5 Q1—one is mine, and the other belongs to a batchmate.
>
> image description: The image is a spreadsheet table containing transactional data, displaying information across various columns. The columns include "TransactionID," "Customer Name," "Country," "Date," "Product/Code," "Sales," and "Cost." The rows contain specific data points, such as customer names, countries, dates, product codes, sales amounts, and associated costs.
> image text:
> TransactionID Customer Name Country Date Product/Code Sales Cost
> 0001 John Doe France 10-13-2023 Eta/fzflrq 2021 USD 1973 USD
> 0002 Frank Thomas United States 2022/10/14 Alpha/f2yscp 6855 USD 4866 USD
> 0003 Bob Brown FRA 09-06-2023 Theta/xvwf8u 5644 USD 3504 USD
> 0004 Bob Brown IND 01-27-2022 Zeta/4rk2rx 9273 USD 1235 USD
> 0005 Charlie Davis United Arab Emirates 09-26-2022 Theta/0ylj7e 5699 USD 1847 USD
> 0006 Charlie Davis US 2022/05/25 Kappa/bquhwf 7897 USD 3424 USD
> 0007 Bob Brown AE 2023/09/20 lota/0t6cym 8680 USD
> 0008 John Doe United States 2022/09/06 Gamma/mb4cm9 8501 USD 4820 USD
> 0009 Alice Johnson U.A.E 01-11-2022 lota/vhfsw5 7582 USD 4491 USD
> 0010 Eve Wilson United Kingdom 2022/07/13 Kappa/yyzmfh 630 USD 557 USD
> 0011 Charlie Davis AE 03-30-2022 Alpha/ixogpm 2199 USD 1104 USD
> 0012 Frank Thomas FR 01-16-2022 Beta/py2nmk 1479 USD 489 USD
> 0013 Eve Wilson FRA 08-10-2022 Epsilon/vl58sf 1076 USD 2928 USD
> 0014 Bob Brown UAE 05-29-2023 Zeta/dljl2j 1534 USD 4803 USD
>
> Here's a description of the image:
> The image displays a table with data organized in rows and columns. The columns represent: TransactionID, Customer Name, Country, Date, Product/Code, Sales, and Cost. Each row seems to represent a transaction with the corresponding details. The data consists of various names, dates, product codes, sales figures in USD, and costs also in USD.
> image text:
> TransactionID Customer Name Country
> Date
> Product/Code Sales
> Cost
> 0001
> Frank Thomas
> IND
> 12-01-2022 Delta/tbakf3
> 7164 USD
> 2062 USD
> 0002
> Eve Wilson
> US
> 08-10-2023 Alpha/hknae9
> 2457 USD
> 3439 USD
> 0003
> Jane Smith
> US
> 2022/09/04 Theta/mjrd4g
> 3924 USD
> 4544 USD
> 0004
> Charlie Davis
> IN
> 08-26-2023 Alpha/b3x7ax
> 6883 USD
> 2091 USD
> 0005
> John Doe
> United Kingdom
> 2023/02/24 Eta/6e491r
> 335 USD
> 2095 USD
> 0006
> John Doe
> Ind
> 2022/08/01 Theta/ehv1v9
> 8669 USD
> 0007
> John Doe
> Fra
> 2022/07/13 Delta/0yr2zu
> 403 USD
> 2617 USD
> 0008
> Alice Johnson
> AE
> 2022/10/09 Beta/fuaz1n
> 192 USD
> 0009
> Charlie Davis
> AE
> 2022/03/11 Zeta/4jyhlz
> 1936 USD
> 0010
> John Doe
> IND
> 10-01-2023 Kappa/xbuc0j
> 7623 USD
> 661 USD
> 0011
> Alice Johnson
> United Kingdom
> 2023/05/10 Theta/1dh7jm
> 1239 USD
> 995 USD
> 0012
> Alice Johnson
> U.S.A
> 11-18-2023 Theta/d3mi7o
> 8460 USD
> 3430 USD
> 0013
> John Doe
> AE
> 2022/05/13 Theta/Osjjwl
> 4874 USD
> 2020 USD
> 0014
> Bob Brown
> IND
> 2023/01/05 Zeta/xxgvro
> 3990 USD
> 2953 USD
> 0015
> Frank Thomas
> FRA
> 12-05-2023 Alpha/cw7cbz
> 1712 USD
> 4823 USD
> 0016
> Eve Wilson
> U.K
> 08-21-2022 Zeta/wmyow7
> 507 USD
> 824 USD
> 0017
> Alice Johnson
> Bra
> 2023/01/09 Alpha/Ifxdg5
> 9914 USD
> 415 USD
>
> During the session, it was said that uploading files would take time, and the suggested solution was to pre-download the files on the server since they are supposed to be the same. But since the files are not identical for all students, this issue needs to be addressed.

The file is just 341kb. it should take less than a second. So you do not have to pre download this file. Only very large ones that are not parameterised you can have a hard copy of.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> In **GA4 Q2**, my task is to retrieve movie information from IMDb for all films with a rating between 3 and 5. I am scraping the correct movie names(for example 6th movie in given image), but the portal is accepting them differently. All movie names are provided in English, but the portal seems to be accepting some titles in other languages—Spanish, Dutch, I believe.

Questions that require manual intervention will be graded very liberally. In other words those questions will not have as strict a grading criteria as in the GA portal.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> In **GA4 Q10**, very few students were able to solve the question using LLMs or Python during the assignment. Most of us ended up solving it manually. At that time, [@carlton](/u/carlton) sir had mentioned that the question would be revised.  
> Here is the [thread link](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/106) for reference.  
> How should we handle this question now?

Same as above.

Kind regards

---

the problem is not the url , if we provide the ending digits of osm\_id then only we can match it as multiple cities are there in same country but osm\_id is unique

---

image description: The image presents a code snippet. The top text describes the use case and the requirement to run it. The text underneath is the code itself. The last line asks what the result will be and indicates it should be a 5-character string.
image text: Let's make sure you can access Google Colab. Run this program on Google Colab, allowing all required access to your email ID: 23f1001524@ds.study.iitm.ac.in.
import hashlib
import requests
from google.colab import auth
from oauth2client.client import GoogleCredentials
auth.authenticate\_user()
creds = GoogleCredentials.get\_application\_default()
token = creds.get\_access\_token().access\_token
response = requests.get(
"https://www.googleapis.com/oauth2/v1/userinfo",
params={"alt": "json"},
headers={"Authorization": f"Bearer {token}"}
)
email = response.json()["email"]
hashlib.sha256(f"{email} {creds.token\_expiry.year}".encode()).hexdigest()[-5:]
What is the result? (It should be a 5-character string)
  
How to parameterise this function? It is really difficult to do this function with other parameter, please help. what is approach other than hardcoding it?

---

Did you get a solution for the Markdown question? I have the same issue.

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
image description: The image is a screenshot of a text file containing a step analysis report. The report includes an introduction explaining that the analysis examines the number of steps walked each day over a week and compares the results over time. The report includes a data table with days of the week and corresponding step counts. It also features a code for step analysis written in Python.
image text: {"answer":"# Step Analysis Report\n\n## Introduction\n Tracking daily steps is an \*\* analysis examines the number of steps walked each day over a week and compares the results over time ata was collected using a fitness tracker and recorded daily. The following steps were taken:\n\n ed daily steps with previous weeks.\n 3. Compared steps with friends to analyze trends.\n\n ga fitness device.\n - Data was logged into a spreadsheet.\n - Weekly trends were cal |- | Monday | 8,500 |\n | Thursday | 10,000 |\n | Friday | 9,600 |\n | Saturd ## Code for Step Analysis\n To analyze the step data, we used Python:\n ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], \n | Steps Walked |\n |\n df = pd.DataFrame(data)\n print(df.describe())\n \*Monday\*.\n - The highest step count was recorded on \*\*Sunday\*\*.\n arison with Friends\n > \"Walking together keeps us motivated!\" \n\n Alice: \*\*10,500\*\* steps/day average\n Bob: \*\*9,800\*\* steps/day average\n improvements\n Some ways to improve step count tracking:\n - \*\*Increase daily goals\*\* tive throughout the day.\n - Track steps using an advanced fitness tracker.\n me](https://www.healthline.com/health/how-many-steps-a-day)\n\n ## Visualization\n ## Re ![9  
Can we rather do PlainTextResponse for the markdown question?

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

# Questions Requiring Clarification/Manual Intervention for Evaluation (As Discussed in Tuesday’s Session)

Respected TDS Team,

As per the discussion during the Tuesday session, and following [@Saransh](/u/saransh)’s suggestion, I am creating this post to list the questions that may require manual intervention or are facing issues potentially due to portal-side behavior. Kindly verify these points before evaluation.

---

## :red_exclamation_mark: Questions Requiring Manual Intervention / Portal-Side Issue

1. GA3 Q8

* Issue: The question doesn’t mention all required queries. Although all mentioned queries were added, the portal seems to check for additional queries not stated, resulting in an incorrect answer flag.
2. GA3 Q9

* Issue: This question asks to create an LLM prompt, but upon submission, a pop-up requests the AIPROXY\_TOKEN.
   * Clarification needed: How are we supposed to handle token-based inputs for evaluation?
3. GA4 Q2 & Q10

* Issue: Previously encountered issues have been resolved.
   * Reference: [GA4 Q2 and Q10 resolution](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/98)
4. Output Formatting (Multiple Questions)

* Issue: When using plain text, the answer is accepted. However, in JSON format, newline characters (\n) and backslashes are added.
   * Note: As per the project requirement, the output should be in JSON like {“answer”: “result”}. But directly copy-pasting such a result with special characters leads to rejection by the portal.
5. Vercel / Docker Hub / Ngrok Deployment Questions

* Issue: Some deployment-related questions require a \*\*live-running server, which needs real-time manual deployment using platforms like Vercel or Ngrok.
   * Clarification needed: How is this expected to be evaluated?

---

## Deployment-Related Issues (To Be Included in Thursday’s Session)

Please include discussion and solutions for the following deployment issues:

1. Platform Capability for GA Tasks

* Which cloud platform (Azure, DigitalOcean, etc.) can handle all GA tasks reliably?
   * Note: Some platforms have limitations that block certain tasks or token usage.
2. File Upload Example via Platform API

* Request: Please provide examples for both small and large file uploads using API from a cloud-deployed app.
   * This would help validate deployments for assignment questions involving file input.
3. General Observations on GA1-5  
   Output Accuracy: Approximately 80% of the questions in GA1-5 return correct output when tested on a local machine. However, about 20% either have portal-side issues or deployment-related problems.

---

Kindly review these points before final evaluation, and let us know if any additional clarification is required from our side.

---

Thanks a lot [@23f2005702](/u/23f2005702), we’ll try to answer these questions in Thursday’s session.

---

Is their any way to solve this issue. [@Jivraj](/u/jivraj)

---

[@carlton](/u/carlton) ( [@Saransh\_Saini](/u/saransh_saini) ) [@Jivraj](/u/jivraj) , is it possible to extend the deadline by 2 days April 1st, since we can use the LLM api a little more and Most people(me atleast) have Their OPPEs and its combined syllabus (and the OPPE 1 did not go well, partly due to my inadequacies) , which has much more to cover, since this project involves more involved coding compared to the last project(ideally project one should have taken not more than a day , still messed it up though xD). Asking for extension for 2 days, if possible. Really need it not even want, like **need**

**Summary: Please extend Project 2 deadline by 2 days(April 1st),**  
*(actually 1 day extension is April 1st)*

---

Hi [@23f1002382](/u/23f1002382) ,  
Unfortunately it’s not possible for us to extend the deadline. Project 2 was released almost a month back, and that can be considered ample amount of time to complete the project. I can understand it must be hard to deal with it along with an upcoming OPPE, but this is what it is. Even if you are not able to cover all the 58 questions, try to cover the majority of them, as the evaluation involves sending just 1-3 questions for evals.

All the best for your OPPE and your Project 2 ![:victory_hand:](https://emoji.discourse-cdn.com/google/victory_hand.png?v=14 ":victory_hand:")

---

[@21f2000709](/u/21f2000709) [@23f2003751](/u/23f2003751)  
Yes you are absolutely right. I confirmed this with Carlton and Anand sir, and yes you have to send the JSON responses as strings, which will automatically add those backslashes(\). I apologies for causing this confusion, and I hope I was able to clarify it.

---

Yes, your response seems correct. It should be a single string containing all the markdown.

---

[@Saransh\_Saini](/u/saransh_saini) can you please confirm 5 Qs at random means 5 random Qs from entire 58 Qs or 1 random Q/GA for the evaluation of TDS Project 2.

---

Hi [@21f3001993](/u/21f3001993)  
You can use the `zipfile` library to extract and access zip files pretty easily. You can even make it so that you don’t even have to download the sent file either zip/csv/etc, in order to access it. All this will be discussed in Thurday’s [27-03-2025] Live Session. Kindly attend the session if you want a deeper understanding of it.

---

It can be any 5 questions.

---

It can be 1-5 random questions from all 58 question. Its not like a random question each from each GA. It’s even possible to get all those 5 questions from one single GA.

---

For GA 2 Question 10, how do we host an LLM on a free vm with very limited resources?

---

Ok, thanks. I won’t be able to attend the session live, but will watch the recording. Thanks for offering to discuss this in live session.

---

just to clarify if the llm is giving the output like this the evaluation script will mark it correct.

```
{
 "answer": "[{\"name\":\"Charlie\",\"age\":16},{\"name\":\"Liam\",\"age\":23},{\"name\":\"Bob\",\"age\":28},{\"name\":\"Grace\",\"age\":36},{\"name\":\"Ivy\",\"age\":44},{\"name\":\"Jack\",\"age\":53},{\"name\":\"David\",\"age\":56},{\"name\":\"Oscar\",\"age\":57},{\"name\":\"Karen\",\"age\":65},{\"name\":\"Frank\",\"age\":67},{\"name\":\"Nora\",\"age\":68},{\"name\":\"Emma\",\"age\":70},{\"name\":\"Paul\",\"age\":88},{\"name\":\"Alice\",\"age\":92},{\"name\":\"Henry\",\"age\":94},{\"name\":\"Mary\",\"age\":97}]"
 }

```

[@Jivraj](/u/jivraj)

---

Yes, it will. Just make sure that doing a json.loads() on this string should give you the desired output.

---

The GA portal marks it as wrong unless I manually insert new lines. I hope that won’t be an issue, will it?

---

Your markdown must have newline characters or spaces wherever necessary. Otherwise we will not be able to check if your answer is correct. Our parser will only work if encodings for the formatting are present in the response. If there are no encodings (invisible or visible) then we will not have the correctly formatted file.

Please review module 1 for a better understanding about how text is encoded. Especially invisible characters.

The browser is designed for user friendliness. Thats why the characters are invisible when you copy paste string with newlines. But it exists.

The programmatic strings show invisible encodings as escaped characters. (Usually)

To check if a string has invisible characters,

```
# Multi-line string
my_string = """Hello
World    with    spaces 
and some newlines
and a tab	"""

# Print ASCII values of each character
print([ord(c) for c in my_string])

```

e.g., newline = 10, tab = 9

This is a great way to check what we are receiving when you send us some response,

```
import requests
import json

# This is just an example server to see what we see.

url = "https://httpbin.org/post"

my_multiline_string_answer = """This is a multiline
string that spans
multiple lines    with    spaces 
and some newlines
and a tab	as well."""

response_to_send_to_tds_evaluator = {
"answer": my_multiline_string_answer
}

# Send the JSON data
response = requests.post (url, json=response_to_send_to_tds_evaluator)

# Check the response
print (response.status_code)
print (response.json ())
print (response.text)

# Do other checks as necessary...

```

See what happens when I print the result

```
print (json.loads (response.text)['json']['answer'])

```

image description: The image shows a terminal window with a multi-line string displayed after running a python script.
image text: .venvcarland@Carlton-MacBook-Pro tds % /User
tds/test.py
This is a multiline
string that spans
multiple lines
and some newlines
and a tab
with spaces
as well.
.venvcarland@Carlton-MacBook-Pro tds %

Its a proper multiline correctly formatted text! The encodings are invisible just like in the original as well as in your clipboard when you copy paste into the GA.

Here is a json example:

```
json_answer = {
    "mary": "poppins",
    "age": 42
}

stringed_json = json.dumps (json_answer)
response_to_send_to_tds_evaluator = {
"answer": stringed_json
}

response = requests.post (url, json=response_to_send_to_tds_evaluator)

print (json.loads (response.text)['json']['answer'])

```

Look at the response. A perfect json.  
![Screenshot 2025-03-27 at 3.30.17 pm](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/f/df98b9abfbf5f7d32de578c727f25b166a564560.png)

If you do not want spaces in the response then strip the spaces before you send the stringified response.

Kind regards

---

I would request the TDS team to please consider making the evaluation criteria for project 2 a bit more liberal.  
5 random Questions with 4 marks each is quite harsh. I request you to make it more balanced like 2 Qs from each GA with 2 marks each or so. So that even if we can’t exhaustively cover the whole number of questions, it gives mercy for the partial completion.

5 random question is a kind of lottery or luck based unless our app is perfect. Thanks

[@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

Hey guys, I have designed the code, and it currently works for the first 11 GA1 questions and the sixth and third questions of GA2. I have accounted for all edge cases. Please check the code at this link:  
<https://4e52-43-230-106-58.ngrok-free.app/>.  
Let me know your thoughts!

---

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

1. **GA2 - Question 3: Publish a Page Using GitHub Pages**

* As part of the requirement, I successfully published a webpage using GitHub Pages that includes my email address `21f3001076@ds.study.iitm.ac.in` in the HTML content. The page functions correctly and becomes accessible on my local system.
* To automate the publishing process, I implemented a delay function that checks for the page’s availability after 5 seconds. Based on testing, GitHub Pages typically take around 10–20 seconds to go live after repository creation and HTML deployment. As a result, the complete process—from initiating the API call to verifying that the page is live—takes approximately 30 seconds locally. This setup works reliably on my local machine.
* However, when deploying the same process on Azure, I encountered an issue. Without the delay, the API responds too quickly—before the GitHub Pages site is actually live—resulting in a broken or non-functional link on the assignment portal. On the other hand, including the delay function causes Azure to throw a **502 Bad Gateway** error, likely due to Azure’s request timeout limitations. The additional wait time slightly exceeds the platform’s allowed response duration.

2. **GA4 - Question 9: Process PDF Files**

* A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a **502 Bad Gateway** error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.
* Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.

Currently, I am using Azure for deployment, and for the majority of tasks, it works reliably. Although these specific tasks face timeout issues, shifting to another deployment platform is not feasible at this point. I am not certain if alternative platforms will work consistently across all questions, and making such a change could introduce failures in other parts of the assignment where Azure performs well.

Below Image is showing response of local machine api request for GA2 Q3 which works fine.

image description: The image is a screenshot of a web interface or a development tool. It's divided into two main sections. The left side focuses on "Request URL" and "Server response". It shows the URL being accessed, server response code (200), response body with a JSON string, and response headers. The right side includes text about GitHub pages, email obfuscation, and an example GitHub Pages URL.
image text: http://127.0.0.1:8000/api/, 200, "answer": "https://21f3001076.github.io/github-pages-20250327144836/", access-control-allow-credentials: true, access-control-allow-origin: \*, content-length: 70, content-type: application/json, date: Thu, 27 Mar 2025 09:18:35 GMT, server: uvicorn, GitHub pages are served via CloudFlare which obfuscates emails. So, wrap your email address inside a: <!--email\_off-->21f3001076@ds.study.iitm.ac.in<!--/email\_off--, https://[USER].github.io/[REPO]/, https://21f3001076.github.io/github-pages-20250327144836/, Correct, If a recent change that's not reflected, add ?v=1, ?v=2 to the URL to bust the cache.

---

[@s.anand](/u/s.anand)  
[@carlton](/u/carlton)  
[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

### **Final Thoughts on Project 2**

Project 2 has been a valuable yet challenging experience. I’d like to share a few reflections—not as criticism, but as constructive feedback with the intention to contribute positively to future iterations.

1. **Organization & Structure:**  
   The project felt a bit unstructured at times, which may be expected given that this is possibly the first time such an initiative is being carried out. I’m not blaming anyone—just sharing my thoughts. I hope positive insights can be drawn from this feedback.
2. **Deployment & Portal Limitations:**  
   There are noticeable limitations on the deployment side (e.g., timeouts, platform constraints) and occasional issues on the assignment portal. While frustrating, these also led to some deep technical learning.
3. **Time Constraints:**  
   Balancing this project with ongoing coursework and other responsibilities has been quite demanding. The deadline of March 31st adds pressure, making it difficult to thoroughly test all 57 questions across different environments.
4. **Sessions & Support:**  
   The sessions conducted were helpful in addressing specific topics, but in many areas, I had to rely heavily on GPT and self-guided exploration to move forward.
5. **Deployment Variability:**  
   Each GA’s questions seemed to expose different limitations depending on the deployment platform. This inconsistency made it hard to predict which questions would work reliably.
6. **Effort Acknowledgment:**  
   I sincerely appreciate the efforts of the TAs and instructors—it’s clear that a lot of hard work went into enabling and supporting this project. However, it’s also a bit disappointing that we, as students, are unsure which questions are expected to work and which may fail—even the team might not have full visibility over this at the moment.
7. **Feasibility in the Given Timeline:**  
   Even for someone with a technical background, it’s difficult to troubleshoot and experiment across so many cases within the current timeline. Trying different approaches per question isn’t always feasible before the deadline.

---

I genuinely hope someone is able to complete **all 57 questions** successfully—I’d love to learn from their experience and solutions.

Again, this post is meant in a positive and constructive spirit. If anything I said seems inappropriate or off the mark, please let me know—I’m happy to edit or delete the post if needed.

**Thank you for the learning opportunity**

---

I have implemented till GA 4 q8 with few questions here and there like one with the llamafile, etc. If someone have the functions of GA 5 ready please ping me for collaboration.

---

[@carlton](/u/carlton) How to do the GitHub Actions questions as it is a cron job based but need manual trigger for the eval script to verify. If done without cron job the portal complains.

---

If there is any plan for extension, I request the TDS team to announce it in advance as people would rush and submit, then, they come hear about the extension when they had submitted it already.

Happened to me like almost every time. We have OPPE this weekend, so if there is slightest possibility, I request to announce it in advance.

Thanks

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)  
Can someone reply to this? ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14 ":sweat_smile:")

---

image description: The image is a set of instructions or a task description. The text describes the structure and format of an Apache web log file and outlines specific tasks to be performed on the log data, including filtering and aggregation.
image text: Your Task
This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.
Each row has these fields:
• IP: The IP address of the visitor
• Remote logname: The remote logname of the visitor. Typically "-"
• Remote user: The remote user of the visitor. Typically "-"
• Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
• Request: The request made by the visitor. E.g. GET /blog/HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
• Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
• Size: The size of the response in bytes. E.g. 1234
• Referer: The referer URL. E.g. https://s-anand.net/
• User agent: The browser used. This will contain spaces and might have escaped quotes.
• Vhost: The virtual host. E.g. s-anand.net
• Server: The IP address of the server.
The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)
All data is in the GMT-0500 timezone and the questions are based in this same timezone.
1. Filter the Log Entries: Extract only the requests where the URL starts with /malayalammp3/. Include only those requests made on the specified 2024-05-15.
2. Aggregate Data by IP: Sum the "Size" field for each unique IP address from the filtered entries.
  
Dear Sirs,

I have a question regarding Q3 and Q4 of GA5. When calling the API, should we pass the `.gz` file directly, or will the API accept a Google Drive link from which it can download the `.gz` file?

Specifically, will the API call be structured as follows?

Essentialy, will the API call look like so?

> curl -X POST “<http://127.0.0.1:5000>”   
> -H “Content-Type: multipart/form-data”   
> -F "question=Bandwidth Analysis for Regional Contents - [anand.net](http://anand.net) is a personal website that had region-specific music content. One of the site’s key sections is tamilmp3, which hosts music files and is especially popular among the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server load, and content engagement. By analyzing the server’s Apache log file, the author can identify heavy users and take measures to manage bandwidth, improve site performance, or even investigate potential abuse. Your Task: This GZipped Apache log file has 258,074 rows. Each row is an Apache web log entry for the site [s-anand.net](http://s-anand.net) in May 2024. Each row has these fields:
>
> IP: The IP address of the visitor.  
> Remote logname: The remote logname of the visitor. Typically ‘-’.  
> Remote user: The remote user of the visitor. Typically ‘-’.  
> Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Note that this is not quoted, and you need to handle this.  
> Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has three space-separated parts:  
> (a) Method: The HTTP method. E.g. GET.  
> (b) URL: The URL visited. E.g. /blog/.  
> (c) Protocol: The HTTP protocol. E.g. HTTP/1.1.  
> Status: The HTTP status code. If 200 <= Status < 300, it is a successful request.  
> Size: The size of the response in bytes. E.g. 1234.  
> Referer: The referer URL. E.g. <https://s-anand.net/>.  
> User agent: The browser used. This will contain spaces and might have escaped quotes.  
> Vhost: The virtual host. E.g. [s-anand.net](http://s-anand.net).  
> Server: The IP address of the server.
>
> The fields are separated by spaces and quoted by double quotes (‘-’). Unlike CSV files, quoted fields are escaped via \" and not ‘-’. (This impacts 41 rows.)
>
> All data is in the GMT-0500 timezone, and the questions are based on this same timezone.
>
> Filter the Log Entries: Extract only the requests where the URL starts with /tamilmp3/. Include only those requests made on the specified 2024-05-23.
>
> Aggregate Data by IP: Sum the ‘Size’ field for each unique IP address from the filtered entries.
>
> Identify the Top Data Consumer: Determine the IP address that has the highest total downloaded bytes. Report the total number of bytes that this IP address downloaded.
>
> Across all requests under tamilmp3/ on 2024-05-23, how many bytes did the top IP address (by volume of downloads) download?"   
> -F “file=@s-anand.net-May-2024.gz”

I would appreciate your clarification on whether the `.gz` file should be directly included in the API request or if a Google Drive link should be provided instead.

Thank you for your time and assistance.

---

Hello Everyone i have cread solution now just for graded 1 and graded 2

[a240-43-230-106-58.ngrok-free.app](https://a240-43-230-106-58.ngrok-free.app/)

### [TDS - Tools for Data Science](https://a240-43-230-106-58.ngrok-free.app/)

ask question there is only one problem in one question like in one question my code unable to match desired function so giving other function output

---

The endpoint a240-43-230-106-58.ngrok-free.app is offline.

---

Now Online check it is online

---

so I have a doubt whatever output my code gives for the ga question , if i copy it one to one and paste in the ga page and it says correct .Would it mean the same would happen with the evaluation method ? or is there any extra things i must add?  
{  
“answer” : “answer inside string”  
}

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> 2. **GA4 - Question 9: Process PDF Files**
>
> * A similar issue occurs in GA4 Question 9, where the task involves processing PDF files. While this works perfectly in the local environment, it leads to a **502 Bad Gateway** error on Azure. This is due to the relatively long time required to parse and analyze the PDFs, which again exceeds Azure’s execution time limit.
> * Moreover, pre-processing the PDF files is not an option because the input varies for each user. Therefore, the PDFs must be processed dynamically, which adds to the delay and contributes to the timeout problem.

[@carlton](/u/carlton)  
I watched the last session. In that session, regarding the specific PDF question, you mentioned that the PDF is the same for everyone, so it can be preprocessed beforehand. However, I checked and found that the PDF is actually different for each user. So, we need to fetch it from the API endpoint.  
How should we handle the timeout issue on the deployment platform? I even tried upgrading the plan, but it didn’t help.

[@s.anand](/u/s.anand)  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Also, many questions and doubts were addressed in the last two sessions. I can improve a lot and add the remaining questions, but the constraint is the 31st March deadline. Most students, including myself, will only get time after 30th March due to Viva and OPPE.  
It would be really helpful if the TDS team could extend the deadline.

I believe it would strike a good balance—team made us wait for the Project 1 results, but extending the Project 2 deadline would make up for that for some extent. Its request nothing else.

---

Hello sir,

My question is, the questions my endpoint will be evaluated are they the exact same ones with same parameters for my respective email as on the assignment portal ?

Essentially I am trying to understand there are certain questions where I don’t have to solve the question again and just return the hardcoded answers, would that be correct ?

---

Anyone please respond and also for ga 1 q 8 for instance where we have:

Let’s make sure you know how to use JSON. Sort this JSON array of objects by the value of the `age` field. In case of a tie, sort by the `name` field. Paste the resulting JSON below without any spaces or newlines.

```
[{"name":"Alice","age":67},{"name":"Bob","age":53},{"name":"Charlie","age":34},{"name":"David","age":89},{"name":"Emma","age":92},{"name":"Frank","age":37},{"name":"Grace","age":4},{"name":"Henry","age":49},{"name":"Ivy","age":30},{"name":"Jack","age":2},{"name":"Karen","age":2},{"name":"Liam","age":5},{"name":"Mary","age":32},{"name":"Nora","age":56},{"name":"Oscar","age":19},{"name":"Paul","age":22}]

```

Sorted JSON:

here would question be sent as text only or text + json file seperately?

---

Can Somebody please share the answers for GA 3 and 4, as I have missed those? Thank you

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

Hi [@adi3](/u/adi3),  
The `.gz` file would be sent along with the API request. You can even read the file directly without even downloading it.

---

The API request would be sent containing the question text and the JSON file/files as a binary stream.

---

Hi [@22f3002933](/u/22f3002933)  
Files are less likely to change, but parameters are. For instance, GA1\_Q12, the zip file is less likely to change but the symbols to perform the aggregate on would be changed.

---

Hi [@lakshaygarg654](/u/lakshaygarg654),  
Yes for GA4\_Q9 the PDF files are different for everyone, but the workflow is exactly the same. Its a basic tabula read, with no particular need of any preprocessing. So, yeah you have to fetch it from the API request.  
Unfortunately, we can’t extend Project 2 deadline, it was released on 3rd of March, and we believe ample amount of time was given for it. If you are lagging far behind in the race, we would encourage you to collaborate with other and get the project done.

---

Thanks for the answer sir.

I remember being told on the last session, that the question will be exactly the same we have on the assignment portal for my respective case, and the answer on the portal can be the same here as well.

Actually I am exploring a hardcoded answer route where if i return the answer which I already got after solving the questions on the portal (in certain qns with dynamic functions) , so thought of asking if method is alright.

---

Yes sending your GA answer as text as the JSON response can work if the question was not parameterized. I hope you are aware that parameters for some questions will be changed, resulting in different answers.

---

Thanks for your reply [@Saransh\_Saini](/u/saransh_saini)  
I’ve figured out the solution to that particular question.  
The deadline is still a concern, as many issues were only resolved during recent sessions—similar to the project 1 workflow—and This time there are many other things in the pipeline ( viva’s and oppe’s )  
Anyway, I will complete this course with valuable learnings, but many others have been seriously affected by it.

---

Hi [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) ,

In the sample curl command  
i.e.

```
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
  -F "file=@abcd.zip"

```

It is given that only one file arguement is passed , can there be a usecase where multiple files are sent , for example GA-5 10th question Image reconstruction where there could be one file be the image another could be separate file with mapping, Although mapping can be given with question as well,  
But still can you please confirm if there will be only one file or there can be multiple files send to API?

---

Multiple files can be sent in the API requestion. They would be sent as a list of files.

---

But in q10 will it be passed as the part of question only??

---

[@carlton](/u/carlton) in GA 5 q10 the mappings table is sent as part of the question text or any other separate file?  
[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

Query about Week2 Q3 and Q7 Publishing a page or action takes time to reflect the site or action performed in github. how to solve this timing issue ? Github repo creation and file /action addition completes immediately but publishing of file /action takes time causing the resulting URL to return 404 for a long time before it returns the correct 200 status and content in response.

---

Hello Sir,

I want to express my gratitude for the opportunity to work on this project. I have developed a mini chatbot backend using `vicky_server.py`, which handles question matching and execution internally, producing appropriate responses. `My mini chatbot is capable of creating its own API using REST and can manage tasks such as image compression, repository management, workflows, and web scraping related to graded assignments. It can even calculate total marks for subjects like physics and convert PDFs into markdown content. Additionally, it is capable of downloading the Llama model and creating a tunnel using ngrok. Essentially, it can address the first four assignment questions.`

However, there are some limitations to this project. Currently, it processes my local files instead of the uploaded PDFs. I am working on resolving this issue, but I have some confusion regarding the internal handling of uploaded files. When I pass a PDF or file through an upload method, how should the system proceed? I want to ensure that the file is treated as a PDF for the user rather than just being referenced as “question.pdf.” How can I effectively manage this problem?

Furthermore, there is an issue with question matching. At times, the system incorrectly identifies questions containing the word “code” and executes `first.py` for GA1.

Thank you for the opportunity to work on this project!

Best regards,  
vicky kumar

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
my model at [Vicky kumar tds](https://310c-43-230-107-168.ngrok-free.app/)

---

In GA5\_Q10 the mappings would be sent as either a HTML or Markdown file along with the image. Both files would be send as a List.

---

[@carlton](/u/carlton)  
I am bit confused about answer evaluation process. Can you tell which one is correct process.  
1st process ( I used json.dumps() to get my\_response as json formatted string)  
image description: The image shows a code execution environment. The code imports the 'json' library, defines a string 'my\_response', and prints a specific element. The result of the code execution "26272" is also visible.
image text: import json
my\_response = "{\"answer\": \"26272\"}"
print(json.loads(my\_response)["answer"])
26272

2nd process ( This one is Json object)  
image description : The image shows code snippets of Python code and its output.
image text:
[14]
import json
my\_response = {"answer": "26272"}
print(my\_response["answer"])
26272

or both are incorrect?

This is one more example of 1st process after json.loads() it gave me correct format for assignment portal answer:  
image description : The image displays Python code. The code imports the 'json' and 'httpx' libraries, then defines a string variable 'my\_response' which holds a JSON string. The JSON string seems to be used to interact with an API, likely the OpenAI API. The code then extracts the 'answer' part of the JSON string. The following code is executed: `print(json.loads(my\_response) ["answer"])`
image text: import json
my\_response = "{\"answer\": \"import httpx\\n\\ndef analyze\_sentiment():\\n
url = \\\"https://api.openai.com/v1/chat/completions\\\"\\n
{\\n
headers
=
\\\"Authorization\\\": \\\"Bearer dummy\_api\_key\\\",\\n
\\\"Content-Type\\\": \\\"application/json\\\"\\n }\\n data = {\\n
\\\"model\\\": \\\"gpt-40-mini\\\",\\n
\\\"messages\\\":[\\n
{\\\"role\\\": \\\"system\\\", \\\"content\\\": \\\"Analyze the sentiment of
the given text and classify it as GOOD, BAD, or NEUTRAL.\\\"},\\n
{\\\"role\\\": \\\"user\\\", \\\"content\\\": \\\"\\\"\\\"P5I 3P1xw aE
WvYHB6zc5xB SY4QzV 0bM8tDP7e o MOG4R9\\\"\\\"\\\"}\\n
response = httpx.post(url, json=data, headers=headers)\\n
raise\_for\_status()\\n result = response.json()\\n\\n
Execute the function and print the result\\nif \_name
\\\"\_main\_\\\":\\n
\\n
try:\\n
print(sentiment\_result)\\n
(f\\\"Error: {e}\\\")\"}"
print(json.loads(my\_response) ["answer"])
==
]\\n }\\n\\n
response.
return result\\n\\n#
sentiment\_result = analyze\_sentiment()
except Exception as e:\\n
print

This is one more example of 2nd process without use of json.loads() it gave me correct format for assignment portal answer:  
image description: The image shows a code snippet written in Python, likely used for sentiment analysis. The code uses libraries like 'json' and 'httpx' to interact with an external API. The core function, 'analyze\_sentiment()', sends a request to an OpenAI API endpoint.
image text:
```python
import json
my\_response = {
"answer": "import httpx\n\ndef analyze\_sentiment():\n url = \"https://api.\n openai.com/v1/chat/completions\"\n headers = {\n \"Authorization\": \n \"Bearer dummy\_api\_key\", \n \"Content-Type\": \"application/\n json\"\n }\n data = {\n \"model\": \"gpt-4o-mini\",\n \"messages\":[\n {\"role\": \"system\", \"content\": \"Analyze\nthe sentiment of the given text and classify it as GOOD, BAD, or NEUTRAL.\"}, \n {\"role\": \"user\", \"content\": \"\"\"P513P1xw aE WvYHB6zc5xB\nsY4QzV 0bM8tDP7e o MOG4R9\"\"\"}\n ]\n }\n\n response = httpx.\n post(url, json=data, headers=headers)\n response.raise\_for\_status()\n result = response.json()\n\n return result\n\n# Execute the function and\nprint the result\nif \_\_name\_\_ == \"\_\_main\_\_\":\n try:\n sentiment\_result = analyze\_sentiment()\n print(sentiment\_result)\n except Exception as e:\n print(f\"Error: {e}\")"
}
print(my\_response ["answer"])
```

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
The vercel api question in GA2, does the endpoint that we give you have to be a vercel url or just hosting it in anyway is alright?

---

[@Saransh\_Saini](/u/saransh_saini) the field name “file” would remain same, I mean it won’t be “files” right?

---

I am trying to create a student account on Microsoft Azure using my IIT Madras email ID (**23f2004705@ds.study.iitm.ac.in**), but I am encountering an issue. The system is showing a message that my email domain is not currently registered with them, and it is asking me to use another verification method.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Could you please guide me on how to proceed with the verification or if there is an alternative method to access Azure’s student benefits?  
Here's a description of the image:
The image is a screenshot of a Microsoft Azure webpage.
\* \*\*Top:\*\* The top bar displays the Microsoft Azure logo and user account information, including an email address and a "Sign out" option.
\* \*\*Content:\*\* The main part of the screen presents a form related to "Academic Verification." It has a warning message that the email domain isn't registered and a suggestion to select another verification method.
image text: Microsoft Azure
Your email domain is not currently registered with us. You can choose another verification method.
Academic Verification
Start by entering your name as per the school records. Select your school's country and enter your school's name. Enter your date of birth as per the school records. The email address may be used to reach you if we have trouble verifying your application, so please enter your school provided email address.
23f2004705@ds.study.iitm.ac.in Sign out

---

Same goes with me also when I try for Academic Verification .  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Please look into it .

---

sir im having the same issue, i have tried so many times.  
sir azure was asking me to fill in the last name which i didnt register in my academic records.  
i have just used my first name while starting this course . can this be a problem while verifying this azure bcz it says last names field is must to fill in. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
sir if the last name was not the issue then pls find us a soln as soon as possible bcz the deadline is in just two days …  
image description: The image is a screenshot of a form with the title "Academic Verification". The form contains fields to input first name, last name, country, school name, and date of birth. The first name field is pre-filled with "shashikumar". The last name field is labeled as "This field is required" in red. The country field has a drop-down menu, and the school name field is pre-filled with "Indian Institute of Technology Madras (Chennai, Tamil Nadu)". There is a text at the top indicating that the email domain is not currently registered.
image text: Your email domain is not currently registered with us. You can choose another verification method.
Academic Verification
Start by entering your name as per the school records. Select your school's country and enter your school's name. Enter your date of birth as per the school records. The email address may be used to reach you if we have trouble verifying your application, so please enter your school provided email address.
First name
shashikumar
Last name
This field is required
Country
India
If your country is not listed, the offer is not available in your region. Learn More
School name
Indian Institute Of Technology Madras (Chennai, Tamil Nadu)
School name will help provide Microsoft with additional information for verification. If available, please enter it here.
Date of birth

---

In Web Scrapping Question The Website will change or it will be same website but the parameters will change of scrapping? [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

bro ur also direct entry diploma student? bcz im also having the same issu..  
i guess the direct entry to diploma students have this problem in comman

---

Was the project hosting session recording posted? Carlton sir said he would post it. [@carlton](/u/carlton)

---

Hi [@lakshaygarg654](/u/lakshaygarg654)  
In both the scenarios you laid out, the second implementation is correct. Your response to our API request should be a JSON object `{"answer" : "YOUR RESPONSE AS STRING"}`. In any case the value of the `"answer"` key should be a string.

---

Hosting it anywhere is fine. Try to deploy on vercel first, if that doesn’t succeed you can use any other hosting technique.

---

This is a basic prototype function we would be using to send requests to your URL.

```
def run(question, file_path):
    url = "http://127.0.0.1:8080/api"
    questions = {'question': question}
    files = [
        ('file', open("abcd.zip", 'rb')),
        ('file', open("dcba.img", 'rb'))
    ]
    response = requests.post(url, data=questions, files=files)
    return response

```

or

```
curl -X POST "http://127.0.0.1:8080/api" \
  -H "Content-Type: multipart/form-data" \
  -F "question=question" \
  -F "file=@abcd.zip" \
  -F "file=@dcba.img"

```

***NOTE**: This is not the evaluation script.*

---

HI [@ripusudan](/u/ripusudan)  
This has been a problem with all direct entry students. Unfortunately, there is no way we can help you with this problem. The best way out is asking a friend who is not a TDS student for this term to create a Azure VM for you.

---

Yes the websites would be the same.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png) Saransh\_Saini:

> This is a basic prototype function we would be using to send requests to your URL.
>
> ```
> def run(question, file_path):
>     url = "http://127.0.0.1:8080/api"
>     questions = {'question': question}
>     files = [
>         ('file', open("abcd.zip", 'rb')),
>         ('file', open("dcba.img", 'rb'))
>     ]
>     response = requests.post(url, data=questions, files=files)
>     return response
>
> ```

I couldn’t find this function on the Project Doc and I made the project based on the curl function calling.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png) Saransh\_Saini:

> ```
> curl -X POST "http://127.0.0.1:8080/api" \
>   -H "Content-Type: multipart/form-data" \
>   -F "question=question" \
>   -F "file=@abcd.zip" \
>   -F "file=@dcba.img"
>
> ```

At this moment it can’t be changed as I am occupied with other things. Please keep the question parameter as “question” and file parameter as “file” in the evaluation which is on the Project 2 page and the content type as multipart/form-data.

To clarify if I can handle any one of these 2 methods, I will be fine?

Edit:  
Just now discovered that the field names are indeed “question” and “file” only in both the cases. Sorry for the oversight.

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
I have a few queries. Even a yes/no response for each would suffice.

GA1:  
Q13 - Use GitHub: Since the parameter is just my email, this question *WILL NOT* be tested against any other email, right? So I can just have a repo with my email in it, right?

GA2:  
Q2 - Compress an image: Should my app’s response be like this

```
{
     "answer": "base64_encoding_of_compressed_image"
}

```

Q3 - Host your portfolio on GitHub Pages, Q7 - Create a GitHub action, Q8 - Push an Image to Docker Hub: Similar to GA1 Q13, these too have my email or roll number as parameter. These too **WILL NOT** be checked against any other email, right?

GA3:

Can you please give an example of how questions of this GA will be sent in the request, especially any of Q1 or Q2 or Q5 or Q6 or Q7 or Q8 which have code-blocks containing text crucial to the question? I just want to decide whether regex or function-calling would be more appropriate here.

GA4:

The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?

GA5:

No particular questions at the moment.

Please help me out by answering these asap

---

if you use github student account then no need to verfiy this and you can directly verify through github student account and got credit i think 150 dollar so you can chose this path also

---

Hello [@22f3001307](/u/22f3001307), there is an error in the code that needs to be fixed as part of the question:  
image = Image.open(list(files.upload().keys)[0]  
with  
image = Image.open(list(files.upload().keys())[0])

---

Sir but i am not a direct entry students

---

[@Saransh\_Saini](/u/saransh_saini)  
As per your reply time, I was in TDS session at that time.  
And asked same doubt, [@Jivraj](/u/jivraj) said 1st implementation they will use. ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14 ":sweat_smile:")

[Session link](https://drive.google.com/file/d/1ftan66I-2BlfDzVkOfdQcyeTwEXZM8wD/view?usp=drivesdk) ( watch at 26:55)

Kindly clarify this.

---

What Jivraj agreed was stringifying the answer and putting it in as the value of the `"answer"` key in the JSON object.  
`{ "answer" : "YOUR_STRINGIFIED_ANSWER" }`

Just check the Project 2 page on the portal. It’s clearly mentioned a JSON object has to sent not a strigified version of the entire JSON object.  
image description: The image is a code snippet demonstrating how a JSON object should be formatted. It instructs that the response be a JSON object with a single text field labeled "answer" which contains a string of the number "1234567890". The text "json" is at the top right corner.
image text: The response must be a JSON object with a single text (string) field: answer that can be directly entered in the assignment. For example:
{
"answer": "1234567890"
}
json

---

[@Jivraj](/u/jivraj) kindly add-in your thoughts on this.

---

Response from api should be a string, which if we load using json.loads it should load json object with answer key.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> Q13 - Use GitHub: Since the parameter is just my email, this question *WILL NOT* be tested against any other email, right? So I can just have a repo with my email in it, right?

Check with other student if they have a different email then it is a parameter and can change.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> Q2 - Compress an image: Should my app’s response be like this
>
> ```
> {
>      "answer": "base64_encoding_of_compressed_image"
>
> ```

This is correct, make sure you test decoding base64 string before deadline.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> Q3 - Host your portfolio on GitHub Pages, Q7 - Create a GitHub action, Q8 - Push an Image to Docker Hub: Similar to GA1 Q13, these too have my email or roll number as parameter. These too **WILL NOT** be checked against any other email, right?

Same answer as Q13 GA1

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000819/48/66738_2.png) 22f3000819:

> Can you please give an example of how questions of this GA will be sent in the request, especially any of Q1 or Q2 or Q5 or Q6 or Q7 or Q8 which have code-blocks containing text crucial to the question? I just want to decide whether regex or function-calling would be more appropriate her

We will take Q1 in this format, which is just copy pasting from portal```  
One of the test cases involves sending a sample piece of meaningless text:

```
au7BK3 33 H 5   lKz6y4n  oQmbgoX 0  hNW3JH  68Q1u

```

Write a Python program that uses `httpx` to send a POST request to OpenAI’s API to analyze the sentiment of this (meaningless) text into GOOD, BAD or NEUTRAL. Specifically:

1. Make sure you pass an Authorization header with dummy API key.
2. Use `gpt-4o-mini` as the model.
3. The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories.
4. The second message must be **exactly** the text contained above.

This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications.

**Note**: This uses a dummy `httpx` library, not the real one. You can only use:

1. `response = httpx.get(url, **kwargs)`
2. `response = httpx.post(url, json=None, **kwargs)`
3. `response.raise_for_status()`
4. `response.json()`

```

[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

[quote="22f3000819, post:173, topic:169029"]
The links to the website are hyperlinks in the questions. When the question will be sent to my app, will the link of the website to be scraped be written as a full link in the question itself or will it be sent in some other way?
[/quote]

Full link will be part of question.
```

---

Thanks for the help [@Jivraj](/u/jivraj) sir

---

Dear Sir  
Is there any limite for request on tokens. because now my model does not generate any output. for any question also not showing any error. could you please explain.  
When i hit request on this (curl -X POST “<http://localhost:8000/api/>”   
-H “Content-Type: multipart/form-data”   
-F "question=Let’s make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won’t work in Excel)

=SUM(ARRAY\_CONSTRAIN(SEQUENCE(100, 100, 1, 9), 1, 10))  
What is the result?") this is not showing any kind of output or error not only on this request any other also.

---

As per the portal, we have to return a JSON object as a response from the API. However, if we load a JSON object directly using `json.load()`, it will throw an error. We need to first convert it into a JSON string and then load it using `json.loads( )`. For clarity I add image below.

This question has been stretched for too long—it’s not that big.

I guess [@Jivraj](/u/jivraj) is right.

image description: The image presents Python code snippets with a focus on JSON processing. It begins with a dictionary `my\_response` containing a key-value pair ("answer": "26272"). The code then attempts to load and print the "answer" using `json.loads()`. However, a `TypeError` is raised, indicating that the input to `json.loads()` must be a string, bytes, or bytearray. The error traceback pinpoints the issue, as the original `my\_response` is a dictionary, not a string. The subsequent code corrects this by first converting `my\_response` to a JSON string using `json.dumps()` before loading and printing the answer, which successfully outputs "26272".
image text:
```
import json
my\_response = {
"answer": "26272"
}
print(json.loads(my\_response) ["answer"])
```
```
TypeError
Traceback (most r
<ipython-input-1-28ad5ba89266> in <cell line: 0>()
4 }
5
----> 6 print(json.loads(my\_response) ["answer"])
/usr/lib/python3.11/json/\_init\_.py in loads(s, cls, objec
337 else:
338 if not isinstance(s, (bytes, bytearray)):
--> 339 raise TypeError(f'the JSON object must
340 f'not {s.\_\_class\_\_.\_\_name\_\_}
341 s = s.decode(detect\_encoding(s), 'surrogate
TypeError: the JSON object must be str, bytes or bytearray,
```
```
import json
my\_response = {
"answer": "26272"
}
#converting json object to string as "{\"answer\": \"26272\"
my\_response= json.dumps(my\_response)
print(json.loads(my\_response) ["answer"])
```
```
26272
```

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Hi,  
while trying to creating podman image of my application, it is being created as 7.2GB file. Any idea what should i do?

Also, I can sign up for azure student pack, are there any way to deploy my application?

Thanks

---

Subject: Request for Uniform Evaluation Process in Project 2 - TDS Solver.  
Hello [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) sir.  
We truly appreciate the effort you put into designing and evaluating our graded assignments and projects. We understand that any five random questions will be selected for evaluation, and we fully respect this approach.

However, we kindly request that the same set of five questions be used for all students to ensure a uniform and unbiased evaluation process. This way, the difficulty level remains consistent across all evaluations, providing a fair assessment of our understanding.

Thank you for considering our request. We appreciate your guidance and support.

Best regards,  
Digvijaysinh Chudasama.

---

image description: The image is a set of instructions for a task. It starts with the heading "Your Task" and then lists the steps. The first step instructs the user to utilize IMDb's advanced web search at a given URL. The second step requires filtering movie titles based on their ratings. The third step requires extracting specific details from up to 25 titles and formatting them into a JSON structure. An example of the desired JSON format is provided. The last step tells the user to submit the JSON data in a text box.
image text: Your Task
1. Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to
access movie data.
2. Filter: Filter all titles with a rating between 2 and 8.
3. Format: For up to the first 25 titles, extract the necessary details: ID, title, year, and
rating. The ID of the movie is the part of the URL after tt in the href attribute. For
example, tt10078772. Organize the data into a JSON structure as follows:
[
{ "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
{ "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },
// ... more titles
]
4. Submit: Submit the JSON data in the text box below.
  
For this question, The answer which we get is not same as the expected answer which the portal fetch through proxy fetch  
Here's a description of the image:
The image shows code snippets written in a programming language. The code appears to be parsing and extracting data from HTML content, likely related to retrieving information about movies or TV shows from IMDb. The structure includes function definitions, conditional statements, variable assignments, and the use of DOM manipulation to select and retrieve specific elements from the HTML.
image text:
```
r> n && ([n,r] = [r, n]);
lets, dasync g => { g = "[\n {\n \"id\": \"tt13406094\",\n \"title\": \"1. The White Lotus\",\n \"year\": \"2021-\",\n \"rating\": \"8.0\"\n },\n {\n
if (!s) {
leth = await fetch('/proxy/https://www.imdb.com/search/title/?user\_rating=${r}.${n}');
if (h.ok)
s = await h.text();
else
throw new Error('I wasn't able to get the IMDb data to verify. Please try again. Response: ${h.status} ${h.statusText}')
}
let l [...new DOMParser().parseFromString(s, "text/html").querySelectorAll(".ipc-metadata-list-summary-item")].map(h => { l = Array(25)
let m = h.querySelector(".ipc-title-link-wrapper").getAttribute("href").match(/(tt\d+)/) [1]
let b = h.querySelector(".ipc-title\_text").textContent
let S = h.querySelector(".dli-title-metadata-item").textContent
let w = h.querySelector(".ipc-rating-star--rating").textContent;
return {
id: m,
title: b,
year: S,
rating: w
```  
let h = await fetch('/proxy/…) ------------> here  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir because of this mismatch we have to edit manually after clicking check button again and again

please guide me how to solve this

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) I just wanted to bring to your attention that in GA4 question 2, the answer evaluation script expects the movie title as “17. Kraven: The Hunter” but it is actually listed on the IMDb page as “17. Kraven the Hunter”, resulting in the correct one being marked wrong.  
No questions here just wanted to bring it to attention so that it does not affect the project evaluation script.

---

Its unusual to have a docker container worth 7 GBs of space. Here is what you can do

* Remove unused libraries from your `requirements.txt`. Sometimes having resource demanding libraries like `SentenceTransformers` can install large sub-dependency packages.
* Exclude your virtual environment folder from the container creation
* Create a `.containerignore` file to have an exception for those folders you want to skip.
* Clear your package cache and any vscode cache you might have.

---

Hi [@21f2000588](/u/21f2000588),  
Your concerns sound genuine and we will put this point up during our discussion sessions. Whatever would be the decision we will inform you guys.  
Regards,  
Saransh Saini

---

In the previous replies, you’ve mentioned that for Github questions → actions, pages (GA2) that if the email changes for everyone it means that its parameterised. However, in one of the live sessions this week, Carlton had mentioned that for these questions, it wont be parameterised as this is very individual specific. The same goes for the docker hub question of GA2 as well. KIndly clarify on the same.

For GA2 Q9 → I have given an input file via post request and my fastapi server can handle get requests and its as follows. Kindly confirm if my url is good to go for this specific question.  
Here's a description of the image:
The image shows a user interface for an API endpoint. It includes a POST request to "/api/upload-csv". The interface allows users to upload a CSV file and filter data by class. It also displays the curl command generated, the request URL, and the server response, including the response body containing student data.
image text: POST /api Upload Csv
Accept a CSV file and return student data. Optional class filters via query string: /api?class=1A&class=1B
Parameters
Name
Description
class
array<string>
|
| null)
1A
(array<string> 1B
(query)
Add string item
Request body required
file \* required
Choose file q-fastapi.csv
string($binary)
Responses
Execute
Clear
Curl
curl -X 'POST' \
'https://b3cc-223-178-84-140.ngrok-free.app/api?class=1A&class=1B' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'file=@q-fastapi.csv;type=text/csv'
Request URL
https://b3cc-223-178-84-140.ngrok-free.app/api?class=1A&class=1B
Server response
Code
Details
200
Response body
{
"students": [
{
"studentId":233,
"class": "1B"
},
{
"studentId": 344,
"class": "1A"
},
Cancel
Reset
multipart/form-data

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Sir, in GA4 Question 7, the portal gives the boundary of ultra-new user as the exact time when it was opened, right?  
Here's a brief description of the image:
The image is a dark gray/blue background with white text describing strategies related to recruitment and market research. There are bullet points on Competitive Intelligence, Efficiency and Data-Driven Decisions. Below the bullet points, there's a request to enter a date in ISO 8601 format related to when the newest user joined GitHub, followed by instructions for searching and a timestamp.
image text:
• Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly.
• Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building.
• Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research.
Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
Search using location: and followers: filters, sort by joined descending, fetch the first url, and enter the created\_at field. Ignore ultra-new users who JUST joined, i.e. after
3/30/2025, 7:21:18 PM.
  
So, will this boundary for ultra-new user be sent as parameter in the question or can my app use datetime.now() to set the ultra-new user boundary?

---

Hi [@22f3000819](/u/22f3000819)  
Thanks for bringing this into light, we’ll keep this in mind while creating the evaluation script.

---

This will be sent as a parameter in along with the API request.

---

Okay sure, thank you so much. I hope you take this into consideration.  
Thanks and Regards  
Digvijaysinh Chudasama

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)  
For GA4, Q9 on Tabula - Tabula requires Java Runtime to install. How to deploy it on Vercel?

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Please give us some clarification on this query

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) please give us some clarification on this query.

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) please clarify

---

please provide clarification on this as deadline is close.  
[@carlton](/u/carlton) , [@Saransh\_Saini](/u/saransh_saini) , [@Jivraj](/u/jivraj)

---

[@jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
same issue… What are your final thoughts?

---

sir GA10 i have designed it as this output of that quesiton is Successfully reconstructed the image. Saved to: E:\data science tool\GA5\output\reconstructed\_jigsaw.png

is this correct or we have to show image directory or folder or image

---

You have to return the image output as base64 encoded data

---

image description: A futuristic cityscape with tall buildings, flying vehicles, and neon lights. Roads are filled with vehicles. The overall mood of the image is high-tech and futuristic.
image text: none
  
through this i got this image in my file output directly  
and is your internal server capable of extracted from given location or we have to handle this internally

---

I am going to clarify this once and for all  
The response should be a **JSON Object** with the value of the `"answer"` key as a string.

```
{ "answer" : "YOUR_ANSWER_AS_STRING" }

```

This is the way we are expecting your responses.  
However, due to the heavy confusion among students and will be considering responses with entire JSON objects stringified. We don’t want anyone to loose their marks for such a miniscule error.  
So,

```
"{\"answer\": \"YOUR_ANSWER\"}"

```

is also valid.

---

means {‘answer’:‘E://data science too//GA5/output/vicky.jpg’} right or we have to do you said output as base64

---

[@Algsoch](/u/algsoch) We should receive your images as base64 encoded within your response JSON object.

---

No, we won’t be able to access your images from your local machine address.

---

i cannot use github as file goes to 18gb what is solution for it as you are asking for github  
but i created repo there is only main file vicky\_server.py,copy\_tds.py  
can you explain how to solve this problem and i will use ngrok so we have to open that till you check and how i know that you will check my api that time or when  
as vercel don’t supported it

---

[@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Sir, I have an issue in GA5 Q3

What is the number of successful GET requests for pages under **/telugu/** from **11:00** until before **20:00** on Mondays?

For this, I have used two python scripts to get the answer, one written completely by me and another from someone else’s solution; both give the same answer - **2698**

However, the portal says it’s incorrect. No modifications resulting in different answer are being accepted either and the modifications themselves seem to break the bounds of the question.

Please check the scripts and tell me where I am going wrong.

My script:

```
import subprocess
from datetime import datetime

def isDay(dtobj, day):
  return dtobj.weekday() == day

def isTime(dtobj, l, u):
  return l <= dtobj.hour < u

step1 = subprocess.run("cat data | grep -i 'GET /telugu/'", capture_output=True, shell=True, text=True)
subprocess.run("rm -f forstep2.txt", shell=True)
with open('forstep2.txt', 'a') as f:
  for line in step1.stdout.splitlines():
    try:
      status = int(line.split()[8])
    except Exception as e:
      status = 400
    if 200 <= status < 300:
      f.write(line + '\n')
step2 = subprocess.run("cat forstep2.txt | cut -d ' ' -f4", capture_output=True, shell=True, text=True)
count = 0
for line in step2.stdout.splitlines():
  log_datetime = datetime.strptime(line.strip('['), "%d/%b/%Y:%H:%M:%S")
  if(isDay(log_datetime, 0) and isTime(log_datetime, 11, 20)):
    count += 1

count

```

I had extracted and uploaded the `data` after extraction using gzip into colab and then executed the script.

The other script:

```
import pandas as pd
import gzip
import re
import os
from datetime import datetime
import hashlib
from google.colab import files

# Function to compute SHA-256 hash
def compute_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Function to parse Apache log entries
def parse_log_line(line):
    log_pattern = (r'^(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (.*?) (\S+)" (\d+) (\S+) "(.*?)" "(.*?)" (\S+) (\S+)$')
    match = re.match(log_pattern, line)
    if match:
        return {
            "ip": match.group(1),
            "time": match.group(4),
            "method": match.group(5),
            "url": match.group(6),
            "protocol": match.group(7),
            "status": int(match.group(8)),
            "size": match.group(9),
            "referer": match.group(10),
            "user_agent": match.group(11),
            "vhost": match.group(12),
            "server": match.group(13)
        }
    return None

# Upload file
uploaded = files.upload()
file_path = list(uploaded.keys())[0]  # Get uploaded file name

# Load and parse the log file
def load_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()

parsed_logs = []
    with gzip.open(file_path, 'rt', encoding='utf-8') as f:
        for line in f:
            parsed_entry = parse_log_line(line)
            if parsed_entry:
                parsed_logs.append(parsed_entry)
    return pd.DataFrame(parsed_logs)

# Convert time format
def convert_time(timestamp):
    return datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S %z")

df = load_logs(file_path)

if not df.empty:
    df["datetime"] = df["time"].apply(convert_time)
    df["day_of_week"] = df["datetime"].dt.strftime('%A')
    df["hour"] = df["datetime"].dt.hour

# Filter conditions
    filtered_df = df[
        (df["method"] == "GET") &
        (df["url"].str.startswith("/telugu/")) &
        (df["status"] >= 200) & (df["status"] < 300) &
        (df["day_of_week"] == "Monday") &
        (df["hour"] >= 11) &
        (df["hour"] < 20)
    ]

# Compute hash of the result
    result_hash = compute_hash(str(len(filtered_df)))

# Output the count and hash
    print("Successful GET requests for /telugu/ on Mondays (11:00-7:59 AM):", len(filtered_df))
else:
    print("No log data available for processing.")

```

Both give the same output: 2698. Please help me identify the error, if any.

---

can anyone help me ,  
image description: The image is a screenshot of a web form for academic verification. The form includes fields for first name, last name, country, and school name. The user has entered "VIKASH" as the first name and "PRASAD" as the last name. The country selected is "India," and the school name entered is "Indian Institute Of Technology Madras (Chennai, Tamil Nadu)". Above the form, a message states that the user's email domain is not currently registered and suggests choosing another verification method.
image text: Your email domain is not currently registered with us. You can choose another verification method.
Academic Verification
Start by entering your name as per the school records. Select your school's country and enter your
school's name. Enter your date of birth as per the school records. The email address may be used to
reach you if we have trouble verifying your application, so please enter your school provided email
address.
First name
VIKASH
Last name
PRASAD
Country
India
If your country is not listed, the offer is not available in your region. Learn More
School name
Indian Institute Of Technology Madras (Chennai, Tamil Nadu)
School name will help provide Microsoft with additional information for verification. If available, please enter it here.
  
Here's a description of the image:
The image shows a text input field for a school email address.
image text:
School email address
21f3002277@ds.study.iitm.ac.in

---

Hi,  
i deployed the application the application in render. It is free for 750 hours per month. But it is saying if the application is inactive mode, it will be go spin-off mode and take some 50 seconds to respond to the first query from inactive mode.  
is that ok?  
[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

do we have additional sample question request formats available then what is listed on the project description page? kindly assist. thank you.

---

image description: This image shows a section for configuring inbound port rules, specifically for selecting which ports are accessible from the public internet. The interface offers two options for public inbound ports: "None" or "Allow selected ports". If "Allow selected ports" is chosen, a dropdown menu appears with an option to select "SSH (22)". A warning message below clarifies that allowing all IP addresses is only recommended for testing and suggests using advanced controls in the Networking tab for limiting inbound traffic.
image text: Inbound port rules
Select which virtual machine network ports are accessible from the public internet. You can specify more limited or granular
network access on the Networking tab.
Public inbound ports \* (i)
None
Allow selected ports
Select inbound ports \*
SSH (22)
This will allow all IP addresses to access your virtual machine. This is only
recommended for testing. Use the Advanced controls in the Networking tab to
create rules to limit inbound traffic to known IP addresses.
  
is the port is correct [@Jivraj](/u/jivraj)

---

[@s.anand](/u/s.anand)

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

Respected Sir,

We kindly request a one-day extension for Project 2, as we finished with vivas and OPPE yesterday only. The circumstances this time have been more challenging than in Project 1, making it difficult to meet the deadline.

We would be extremely grateful if you could consider this request. Your support would be highly appreciated.

Thank you for your time and consideration.

Best regards

---

Yes please extend the deadline for project 2, as it was very lengthy and we have other exams as well with that.  
[@s.anand](/u/s.anand) ,  
[@carlton](/u/carlton)  
[@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)  
Respected Sirs,  
Please consider the extension for Project 2 submission…

---

Good morning sir,  
Could you please extend the deadline for Project 2 as today(31/03/2025) is the last day of submission and it clashes with “Eid al-Fitr”. I have small portion of work left but it won’t be possible as there is frequent visit of guests and friends. Could you please extend the deadline till 02/04/2025, this will give us enough amount of time to complete the project after our festival.  
Thank you

---

[@carlton](/u/carlton), please this much support we deserve from you

---

Pls sir extend the deadline it’s very hectic schedule for all of us to complete by today. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

Sir, could you please extend the deadline by one day? I’m facing some issues with deployment, and with Eid celebrations at home, it’s been a bit difficult to manage everything. I would really appreciate your consideration. Thank you!  
[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

Sir many of us had OPPEs and Programming projects due this weekend and thus an extension in the deadline will be helpful

---

hi sir. Im also on the same boat.

---

hello please say on ngrok i want to share ngrok method ‘’ but i have to open all days right on

---

Hi. I got a new laptop and was wondering how to recover my AIPROXY token. How do I get it? If I remember correctly it has something to do with my iiim email

---

[@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

What is the request timeout for each question, especially for the question on YouTube video transcription? I request the timeout to be at least 40-60 seconds as yt-dlp and faster-whisper take take to download the audio, load the model and run it on cpu and get the transcription.  
For 259.7 to 351.8 seconds, it is taking around 1.5 mins, but it is giving the correct answer.

So I request you to shorten the length of the audio or increase the request timeout or both in moderation.

Question —> the “question” sent to the api will have the youtube video link, right? Or since the video is same for everyone, can I just have the audio file ready in the project? Will the api be tested against any YouTube video other than the Mystery Story Audiobook link given in the GA question?

Edit: Even with a preprocessed audio file (mp3, speech optimized, 32K), what’s taking the longest time is joining the transcribed sentences into a single string. That alone is taking >50 seconds. Please suggest a way to make it faster.

Regards,  
Shivaditya

---

For the FastAPI type questions, my endpoints are like <http://ip>:port/endpoint. But while testing using the portal it expects HTTPS instead of http. But nothing of that sort is given in the question. Will the evaluator also expect a https url or is a http url enough for it to hit the endpoint?

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Yes we’ll take that into consideration.

---

For GA 5 - Q10 - do we have to return base64 encoded image or the url of the image?

---

Base64 encoded string

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

q-vercel-python.json will be same or different?

image description: The image is a black and white text-based document. It instructs to create a Python app on Vercel, which will have a JSON response based on input. The Vercel URL for the final product is provided at the end.
image text: Download this q-vercel-python.json which has the marks of 100 imaginary students.
Create and deploy a Python app to Vercel. Expose an API so that when a request like https://your-app.vercel.app/api?name=X&name=Y is made, it returns a JSON
response with the marks of the names X and Y in the same order, like this:
{ "marks": [10, 20] }
Make sure you enable CORS to allow GET requests from any origin.
What is the Vercel URL? It should look like: https://your-app.vercel.app/api
https://vercel-tds-one.vercel.app/api

Will the llamafile be same?  
image description: The image is a block of text on a dark background, likely a code snippet or a set of instructions. The text provides steps on how to run a specific model using Llamafile and create a tunnel using ngrok. The text highlights the URL that can be used.
image text: Download Llamafile. Run the Llama-3.2-1B-Instruct.Q6\_K.llamafile model with it.
Create a tunnel to the Llamafile server using ngrok.
What is the ngrok URL? It might look like: https://[random].ngrok-free.app/
https://aafb-2405-201-4007-c068-eb1d-b640-5d42-2493.ngrok-free.app

---

hello i want to know about this currently I am using approach like you provide HTML page URL and my internal approach and run hidden value or you provide URL website

Here's a description of the image:
The image shows a text-based puzzle or quiz. It presents the question: "Just above this paragraph, there's a hidden input with a secret value. What is the value in the hidden input?" Below the question, there is a blank input field for the user to enter their answer, and a blue "Check" button is placed below the input field.
image text: Just above this paragraph, there's a hidden input with a secret value.
What is the value in the hidden input?
Check

---

hello for this question i am using approach like initially i login and saved seession now it is giving output like it login internally to website of college ga1 and then find  
image description: The image is a screenshot from a web-based learning environment. It contains a question related to CSS selectors.
image text: Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes? Sum of data-value attributes: Check

---

I asked this question in the gmeet. They said html will be provided in the question and u have to find the hidden input from there. Same for css selectors

---

Here's the image description:
The image displays a table containing information about concert tickets. The table has columns for "type," "units," and "price," with example rows showing data for "bronze," "silver," and "SILVER" tickets. Below the table, there's a question about calculating the total sales for "Gold" tickets, prompting the user to write SQL code. The area below the question is a dark rectangle.
image text: There is a tickets table in a SQLite database that has columns type, units, and price. Each
row is a customer bid for a concert ticket.
type
units
price
bronze
297
0.6
Bronze
673
1.62
Silver
105
1.26
Silver
82
0.79
SILVER
121
0.84
...
What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it.
  
do you know answer of this that time i got answer

---

but i got wrong answer

---

[@carlton](/u/carlton)  
Could you please consider the above request for an extension? There are still many updates needed, and the project is close to completion. I am confident you will be pleased with the final results.

---

Here's a description of the image:
The image is a UI for an AI assignment solver. It allows users to upload a file or ask a question.
image text:
Al Assignment Solver
Upload a File
Choose File No file chosen
Upload
No file uploaded.
Ask a Question
Enter your question here
Answer will appear here.
Submit
  
Sir, I have created the frontend app like an html page with the fastapi utilizing the chatgpt-o3 , instead of Api key. I managed to get api keys but ended up in only text mining without file handing (not able to do multipart-form data). So, I have made to use the model and designed a frontend which also takes the input from the file uploaded, So, it will be ideal for assignment solver, Isn’t it , Sir? [@carlton](/u/carlton) [@Karthik\_POD](/u/karthik_pod)

---

image description: A document with text on a gradient purple background. The text presents a list of numbers and a calculation to determine the total value of complaints.
image text: - 2,400.00
- 0.00
- 1,234.00
- 10,000.00
- 20.00
- 2,000.00
- 0.00
- 0.00
- 20,03,030.00
- 1,000.00
- 1,000.00
- 1,000.00
- 1,000.00
- 1,000.00
Now, let's calculate the total:
- 1,233.00
- 56,767.00
- 2,400.00
- 1,234.00
- 10,000.00
- 20.00
- 2,000.00
- 20,03,030.00
- 5,000.00 (total of subsequent similar entries)
Summing these values:
1,233.00 + 56,767.00 + 2,400.00 + 1,234.00 + 10,000.00 +
20.00 + 2,000.00 + 2,003,030.00 + 5,000.00 = 2,073,684.00
Thus, the total value of complaints is \*\*2,073,684.00\*\*.
  
This is the output Sir [@carlton](/u/carlton) [@Karthik\_POD](/u/karthik_pod) . Also my project-1 has not been scored .. till now .. Please review that also. [Project 2 - TDS Solver - Discussion Thread - #240](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/240)

---

Hi [@22f3000370](/u/22f3000370)  
We appreciate the efforts you have put in. But, for the project we aren’t expecting a full-stack app with an integrated frontend. We just need an API endpoint on which we would be able to send requests in the given format. For more info check the TDS course page. [Tools in Data Science](https://tds.s-anand.net/#/project-2)

---

[@Saransh\_Saini](/u/saransh_saini) Is answer in this form acceptable..  
image description: The image shows a section of code and its output. The first part shows a curl command with several options. Below that, there's the "Request URL" field and the URL used. The "Server response" section presents a code 200 with its details. The main body contains a JSON response, including an "answer" key. The answer is a Python function calculating cosine similarity between embeddings.
image text: curl -X 'POST' \
'http://127.0.0.1:8000/api/' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=ShopSmart is an online retail platform that places a high value on customer feedback. Each month, the company receives hundreds of comments
Request URL
http://127.0.0.1:8000/api/
Server response
Code
Details
200
Response body
{
"answer": "Here's a Python function that calculates the cosine similarity between each pair of embeddings and returns the pair of phrase
s that has the highest similarity:\n\n```python\nimport numpy as np\nfrom itertools import combinations\n\ndef cosine\_similarity(vec\_a, ve
c\_b):\n \"\"\"Calculate the cosine similarity between two vectors.\"\"\"\n dot\_product = np.dot(vec\_a, vec\_b)\n norm\_a = np.linal
g.norm(vec\_a)\n norm\_b = np.linalg.norm(vec\_b)\n \n if norm\_a == 0 or norm\_b == 0: # Handle zero division\n
return 0.0\n
return dot\_product / (norm\_a \* norm\_b)\n\ndef most\_similar(embeddings):\n \"\"\"Find the pair of phrases with the highest cosine simila
rity.\"\"\"\n max\_similarity = -1\n most\_similar\_pair = (None, None)\n
phrases = list(embeddings.keys())\n vectors = lis
t(embeddings.values())\n \n for (phrase\_a, vec\_a), (phrase\_b, vec\_b) in combinations(zip (phrases, vectors), 2):\n
sim = cosin
max\_similarity = sim\n
most\_similar\_pair = (phrase\_a,
e\_similarity(vec\_a, vec\_b)\n
if sim > max\_similarity:\n
\n
phrase\_b)\n \n return most\_similar\_pair\n\n# Example usage\nembeddings = {\n \"Packaging was excellent.\": [-0.01674579456448555,
-0.06481242924928665, -0.24050545692443848, 0.042519159615039825, \n
683, 0.1299005150794983, 0.17366009950637817, \n
23444, -0.015152188017964363, \n
1757946, \n
0.14857585728168488, -0.11343036592006
-0.12356054037809372, 0.049548257142305374, 0.230582013726
-0.06047092750668526, -0.08428027480840683, 0.140513077378273, 0.033095341
0.15987755358219147, -0.13982394337654114, -0.1899235099554062, 0.0849694088101387, \n
0.10901995003223419, 0.023171907290816307, 0.1423737108707428, -0.010603947564959526, \n
-0.123629450798034
0.13754981756210327, 0.0631929785013
0.5634305477142334, 0.003012778703123331, -0.154226705431
0.10013020783662796, 0.05392421782016754, 0.10895103961229324, -0.017710573
67, -0.02598010189831257, 0.04410415142774582, -0.0650191679596901,\n
1989, 0.2340276539325714, -0.1448545753955841,\n
93817, -0.10137064009904861, \n
0.0405896008014678
971271515, \n
-0.0018617206951603293, 0.01796899549663067, 0.0550268217921257, 0.251669317483902, \n
-0.005680993665009737, 0.12080402672290802, -0.08173050731420517, 0.1045406237244606, \n
96, 0.1787596344947815],\n \"Shipping costs were too high.\": [-0.02132924273610115, -0.05078135058283806, 0.24659079313278198, 0.03407
837450504303, \n
-0.031469374895095825, 0.04534817487001419, -0.14255358278751373, 0.0284838192164897

---

what is the problem in my Dockerfile it’s not working and crashing my system

```
# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables
ENV PYTHON_VERSION=3.11

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    python3-dev \
    git \
    curl \
    wget \
    ffmpeg \
    imagemagick \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Ensure python3.11 is the default python version
RUN ln -sf /usr/bin/python3.11 /usr/bin/python

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get install -y nodejs && \
    node -v && \
    npm install -g prettier@3.4.2

# Copy dependencies file first to leverage caching
COPY re.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r re.txt

# Install `uv` package manager from Astral
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create and set working directory
WORKDIR /app

# Copy application files
COPY main.py .
COPY llm_functions.py .
COPY llm_tools_functions_calls.py .
COPY server.py .

# Set default command to start the FastAPI server with `uv`
CMD ["uv", "run", "main.py"]

```

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Here's a brief description of the image:
The image is a webpage of a web service, specifically "TDS-Project-2". It shows information about the deployment status, including a note that free instances will spin down with inactivity, potentially delaying requests. There's a deployment log showing the date and time, and a progress indicator. The page contains options to upgrade the instance or cancel the deploy.
image text:
WEB SERVICE
TDS-Project-2 Python 3 Free Upgrade your instance →
Connect
Manual Deploy
23f3001764 / TDS-Project-2 main
https://tds-project-2-pnlm.onrender.com
Your free instance will spin down with inactivity, which can delay requests by 50 seconds or more.
Upgrade now
March 31, 2025 at 4:38 PM In Progress
5989351 Final Commit
Cancel deploy
All logs Search
Live tail GMT+5:30
↑
  
I have deployed the project on render so the first request in evaluation takes around 50 to 60 second is that okay

---

I deployed my API using Railway.app, but Jio ISP is blocking requests to `.up.railway.app`. I tested it with five other ISPs, and the API endpoint works perfectly. Could you please consider that some ISPs may be blocking certain domains?

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

Error code: 401 - {‘error’: {‘message’: ‘Your authentication token is not from a valid issuer.’, ‘type’: ‘invalid\_request\_error’, ‘param’: None, ‘code’: ‘invalid\_issuer’}}

This error is persisting despite many attempts.

---

you have given diffrent variable name in environment and in app

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Can you pls confirm on timeline  
since azure take money so till when do we have to turn on our deployment portal services

---

Also if we are using ngrok , how long do we have to keep it running

---

Yup, this is correct. All we need is the JSON object.

---

We’ll try to keep this in consideration while developing the evaluation script. But to be on the safer side keep sending requests to your server on such intervals that it doesn’t go inactive.

---

[@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

#### Please extend the deadline for TDS Project 2. The MAD 1 project and two OPPEs have taken up all my time. I have completed my TDS project up to the Week 3 assignment solutions, and only two weeks remain to complete Weeks 4 and 5.

![Description of the GIF](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/e/2/e260c5b2643d3c609e92b14c16c5a3c714596166.gif)

---

We won’t be able to extend deadline, if we do, then evaluations will get delayed.

---

I completely understand the need to keep evaluations on schedule. In that case, would it be possible to grant just a one-day extension? I’ve completed up to Week 3 and just need a little extra time to wrap up Weeks 4 and 5 properly. A single day would really help me submit a more polished project without causing significant delays

---

I think it should be given many had their OPPE also

---

Sir, please reply. Otherwise, all my hard work up to Week 3 assignment will go to waste.

---

Even Im getting the same error. Did you find a resolution for this?

---

are you sure api requests are going through the IITM AI Proxy and not OpenAI directly?

---

I am facing this issue can any one help

image description: The image shows an error message indicating that a serverless function has crashed. The text highlights that the connection and Vercel are working correctly. It presents a 500: INTERNAL\_SERVER\_ERROR, with a code and ID for the error. The message provides instructions for visitors and owners on how to proceed. image text: This Serverless Function has crashed. Your connection is working correctly. Vercel is working correctly. 500: INTERNAL\_SERVER\_ERROR Code: `FUNCTION\_INVOCATION\_FAILED` ID: `bom1::48ghr-1743430791127-d99a1b77819a` - If you are a visitor, contact the website owner or try again later. - If you are the owner, learn how to fix the error and check the logs.

---

Please check the logs.

---

Hi [@s.anand](/u/s.anand) and [@carlton](/u/carlton) Sir,  
It would be really great if the deadline for submission could be extended by one more day. While we understand your reasons, we kindly request you to consider our situation as well.

---

Trailing Slash redirect error (Used next.js)

---

Questions that have access hidden divs, how would the parameters be provided  
? [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

Sometimes the server shuts down, what would happen then? [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

For this the HTML file would be provided to you and you have to find the given element.

---

[@Saransh\_Saini](/u/saransh_saini) can you provide us the time frame for evaluation so that we know when to run ngrok. Vercel isn’t an option right now as i’m having issues deploying.

---

Sir, I sincerely request an extension of the deadline by just one day. I have completed the coding part, but I am facing some issues with the deployment of the project. I would really appreciate your consideration.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

![OnePieceStrawhatsGIF](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/2/a2ca53960e1ef9d9566dd1648096df09332e6310.gif)

Stay tuned @all

---

What issues are you having? I am having an issue deploying due it either using up all the memory while installing dependencies or hitting some other limit. I gave up and am now hosting it on render.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)  
URGENT IMPORTANT QUESTION : should the link we will submit in the gform have /api in it or not :,) [ PLS DONT SCOLD IF ITS A SILLY QUESTION ]

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png) Saransh\_Saini:

> this the HTML file would be provide

same  
PLEASE INFORM

S  
S  
S  
S

---

please tell how long approx will evaluations will last

---

it depends on what ur post endpoint is , if its (“/api” ) then give that

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) same question

---

same here , It worked fine for a while and once the dependencies grew and varied it started showing serverless function crashed though it was running fine locally

---

I noticed that ngrok disconnects after two hours, so I’m wondering if we can continue using it.

If your team was aware of this, I’d like to understand why it was allowed to deploy on ngrok. I typically use Vercel for deployment, but as you know, Vercel doesn’t support certain features.  
what to do now

---

Just extend the deadline for one day please it will be a great help for many students

---

ngrok will give me 0 marks right because when ever your system try to evaluated it get offline message

still i am very thankful for this project i created mini chatgpt  
without using any llm api  
instead of prompt engineer

---

pls sir extend the deadline by 1 day

---

it wont disconnect in 2hours , if u login using ur id to ngrok and start ur server with auth id , it will keep running as long as ur pc is on

---

use screen package to keep it running

---

yes me too  
*Thank You for some sleepless nights(now I have some dark-circles😑) and this wonderful experience*[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

![DoolwindTheOfficeGIF](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/5/054b78122fc9aed3a2a9138ef0839a109dee8001.gif)

---

Thank you [@21f2000709](/u/21f2000709) [@trebhuvansb](/u/trebhuvansb) [@ItsMeAlex](/u/itsmealex)  
without you guys, i don;t know what i would have done. THANK YOU

---

Ah, the true mark of a dedicated developer—when even your dreams come with syntax errors! ![:laughing:](https://emoji.discourse-cdn.com/google/laughing.png?v=14 ":laughing:") This project was a rollercoaster of caffeine, code, and existential debugging at 3 AM. But hey, we survived, and now even my subconscious is running `python main.py` on repeat. On to the next adventure… after some well-earned sleep (hopefully bug-free)!

---

Hello Sir,  
I hope you’re doing well. On behalf of all the students in our course, I wanted to request a deadline extension for the project 2. We’re all putting in our best effort, but we need a little more time to complete it properly.

If it’s possible to grant an extension, we would really appreciate it. Please let us know if you can consider this request.

Thank you for your time and understanding!  
Saksham

Please sir !  
image description: A cat with its paws in front of its mouth, as if it's pondering. The cat's coat is grey and white, and it has a cute expression. The background is a wooden floor.
image text: None.

---

yess sir same with me can u just extend 2hrs like that

---

i used ngrok. i need to change it to vercel or someother thing. so sir kindly extend the deadline for a day… please sir. this is a kind request from every student

---

anybody there?..???..???..???..?

---

Respected Sir,

I kindly request a deadline extension of at least 3 minutes for the project submission, similar to what was done for ROE. Due to slow internet connectivity and the absence of WiFi, my submission took longer than usual. As a result, I was only able to upload it at 12:01 AM instead of the regular 11:59 PM deadline.  
PLEASE Sir, As I’m a standalone student and this is my primary degree after 12th, please do accept it.

Thank you  
Here's the image description:
The image features Tom from Tom and Jerry, in a kneeling prayer pose with eyes closed. The cat is dark gray with a lighter gray belly, chest and paws. The background shows a blurred outdoor setting with green and brown hues.
image text: None

---

sir kindly extend the deadline for a day sir, kind request from tds students. kindly consider our pleadings.

---

sir i was trying to upload it but due to net issue it got submitted at 12:01.  
the google form is saying the response is recorded. so my response is recorded right?

---

Hi [@s.anand](/u/s.anand) and [@carlton](/u/carlton) Sir,  
It would be really great if the deadline for submission could be extended by one more day. While we understand your reasons, we kindly request you to consider our situation as well.

---

Hi [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

I have submitted my fastapi endpoint without the /api at the end.

Would this be a problem?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)  
Sir i also didn’t addd /api/ at the end of the url. Will this cause a peoblem?

---

My project is hosted on render, because vercel refuses to cooperate with me, as a result the free version of render takes a minute to respond, and not only that but might also give internal server error until the 2nd or 3rd try. There is nothing I can do to change this except for maybe sending requests every now and then like it was suggested for another student using render. I just want to know if this is okay for evaluation.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) sir,  
I also have submitted my fastapi endpoint without /api at the end, please reply if this would be a problem?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)

Can you please say when the project 2 be evaluated?? since i am using ngrok it is very hard to keep my laptop running and also the result time is given as 15th. no possile way i could run my laptop more than a couple day. kindly provide a solution for ngrok users or please extended a day or so to change from ngrok to someother. this is a kind request. and kindly reply as soon as possible.

---

me too ,please inform how long will it take .

---

are we free to edit the google response , to update the ngrok link if it changes cuz in the free version if the laptop restarts so will the link

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)  
Yesterday, I don’t mention /api at the end of my dns while submitting the form and I come to know to day we have to add /api at the end of the it. So I edited my response please consider the latest one.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

I have a curious question.  
I have my project running from azure and code in GitHub repository.

What is stopping me from making further change to my deployment because my end point will be same. Anyway my code checksum for the deployment and GitHub code won’t match as I haven’t pushed the token to GitHub.

Thanks,  
Vinil

---

I did the same mistake and I am just realising it. Will my submission be discarded in that case? Please clarify.  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

I reuesting to all my teachers [@s.anand](/u/s.anand), [@carlton](/u/carlton), [@Jivraj](/u/jivraj), [@Saransh\_Saini](/u/saransh_saini) please reply me.

What is this going on? Is it joking? Our teachers don’t have enough time to make a separate video for project to explain what to do and how to do? I already have done two project courses and they taught us, even they made 2 - groups just only for discussions in which one is personal and also made a YouTube playlist especially for project. They explained what should be your approach? How to make project? And here, they took only one session just only for show off. And they organised that single session when too many student requests too many times? Are we studying in IIT - The top institute of India or in a cheap and lower than third class government schools. It is the responsibility of our teachers to explain the project, but they are just showing off. Even they never provided the solutions for assignments also. Is it not our right to get solutions so that we can know where we did mistake? They don’t have time to make solutions, they just made an assignment checker which checks the assignments automatically. I don’t think so that they really made any effort in our course. In project-2 also, we need solutions for all graded assignments and so many students request for solutions but our the great teachers ignores the request and didn’t provide the solutions. I think they provide the projects whatever comes in their dreams during sleeping. In weekly study material, don’t have their notes, even they have a very few videos made by them, they just render to other YouTuber’s Youtube videos and online websites. Are we paid just only for these YouTube videos ? If we can understand everything just only from YouTube then why we are studying from the India’s top Engineering institute - The IIT Madras? I have much more better videos than that are provided on YouTube and created by other YouTubers. They only have some points copy pasted from documentations, but they never tried to explain them. Just read, copy and paste in your program. What is it, why it is used for, don’t ask anything.

Some students request for extending the time limit of [roject-2 just only for one day, but what was their excuse- "We won’t be able to extend deadline, if we do, then evaluations will get delayed. ". I want to ask them, where is the result of Project-1? The first date of result declaration was 26-Feb, then their another date was 16-March, but until now on 2-Apr, we do not get our results. It is more than 45 days, what is this going on? Nobody tried to ask with our great teachers. But on extending the deadline of project-2 just only for one day, their evaluation will be late. In project-2, we have to continue running our project until they will not evaluate, whether they take more than 1, 2 or more months. Either we have to host online by paying or run our own system for 24x7 unto when, we also don;t know as their result date is also not fixed, it is just a combination of letters and numbers showing on portal. It is our tales it is my right to get solutions for every weekly assignment, but don’t ask them to make efforts. Just pay and do assignments at own risk even you have not understand anything from the copy-pasted material. Just use AI’s or read whatever and wherever you want to read.

It is my kind request, our term is going to be completed, but please make some efforts in next term.

Thankyou to all my respected ‘The Great Teachers’.

---

hi,

I dont share your views.

i feel it was one of the best course in whole of Diploma.

I have learned a lot in these projects and even in ROE preparation.

all the things we are learning here are open in market and the course contents are great direction towards learning and practicing them.

I agree it is stessful, my whole team were in a 9-hour g-meet call on Saturday night. but we have found solutions, shared ideas, try-outs, made fun of each other.

but at the end of the day we all agree that we have learnt lots of new things.

Regarding Project1 delay: if we think, atleast 1GB of docker image per students for 700+ students. even if parallalize the execution 5 students at a time you still need a very powerfull system to download and amount of data downloading etc… At the end of the day we got a very good result and report with logs to verify

for GA’s: it is upto you to copy solutions or learn something out of each GA sections

All in all I am happy with the course.

---

Totally Agree with [@23f2004837](/u/23f2004837)  
Best course so far from learning POV.

---

Dear Shahzada,

You joined Discourse almost a year ago Jun 8th, 2023. In all that time you have read 832 posts. And never interacted with anyone on discourse. You finally decided to interact once and that was today and this is your first post (your second if we count that you deleted your first post)

The first step to receiving help is communication. If you do not communicate, no one can help you.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> What is this going on? Is it joking?

I am not sure what your question is. I am not sure what you are referring to. Please be clear in your questions.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> Our teachers don’t have enough time to make a separate video for project to explain what to do and how to do?

We have made **several hours of videos** on Project 2 and have demonstrated multiple ways to solve it. However, we are not going to ever create it for you. We do teach you all the core technologies you can leverage to create it yourself.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> I already have done two project courses and they taught us, even they made 2 - groups just only for discussions in which one is personal and also made a YouTube playlist especially for project.

Not sure which courses you are referring to, but those are standalone courses. Here project is part of the course and is meant to take you roughly a few days to create. We gave students more than one month for Project 1 and the solution for it takes a few hours to create. (which we have shared)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> They explained what should be your approach? How to make project?

Yes these were explained if you

1. either took part in any live session or
2. watched the recorded video

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> And here, they took only one session just only for show off. And they organised that single session when too many student requests too many times?

I am not sure what you are referring to because several sessions were conducted for Project 2 spanning nearly 2 weeks.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> It is the responsibility of our teachers to explain the project, but they are just showing off.

Project 2 was explained. I can summarise it in these words:  
Create a server api that receives a request.  
The request would be any question from the first 5 GAs.  
The response has to be a json response as specified in the Project page.

Multiple demonstrations were done of this workflow in sessions.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> Even they never provided the solutions for assignments also. Is it not our right to get solutions so that we can know where we did mistake?

Since this is your first post, you’ve never ever asked for solutions to any assignments. We have never provided solution notebooks for TDS. It defeats the learning process.

If you want solutions, there are several options:

1. Ask for help (since you have never posted before, you missed the opportunity to receive it)
2. Collaborate with others (a bigger goal of TDS, because in the real world one man bands almost certainly fail with extremely high probability, barring a few exceptions, human progress is built on collaboration)
3. Join live sessions, where we have provided solutions to almost every assignment question that students have asked (and not asked)
4. Watch the live sessions, we have even created neat Q & A summaries for them on the TDS portal (something which no other subject does at the moment)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> They don’t have time to make solutions, they just made an assignment checker which checks the assignments automatically.

This is one of the most loved features by our students. No other GA in any other course gives you the option to check your answers in real time and better yet correct them before submitting.

The biggest clue for solutions is in this nugget. If you take the opportunity, and enterprise and get some fellow students together, you are actually able to obtain the solution script from the GA page itself. It takes some effort, but that is how learning occurs… with effort. Studies repeatedly show that zero effort results in nearly zero learning.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> Are we paid just only for these YouTube videos ? If we can understand everything just only from YouTube then why we are studying from the India’s top Engineering institute - The IIT Madras? I have much more better videos than that are provided on YouTube and created by other YouTubers.

If you had better resources available, you have hardly been the paragon of virtue, because we always encourage people to share their learnings. We learn from you, just as you learn from us. If someone makes a better video than us and give it for free, we are happy enough to learn from them. Why should we reinvent a video that is poor quality and force students to watch it when there are better videos? We are not so egoistic to take that approach and worse it does not benefit our students to satisfy our ego. There are a million videos out there on you Tube, how do you find the best one? We curate it. So that you do not have to spend hours finding a good video.

But feel free to find better videos. More power to you, but what would be even better? Share with others so that we can build each other up.

What are the best videos to learn linear algebra? Probably MIT. Why bother with substandard videos when you can just get the best for free? Its just that watching MIT videos will not give you an undergraduate degree from MIT. And it costs Rs. 2.7 crores, provided you even get a seat in the first place. Here you get a 4 year degree for Rs 3.5 lakhs. So you are paying for that.

I absolutely 100% agree with you, if you think you can get a better degree for Rs 3.5 Lakhs then definitely do that. There is no point in wasting time and money on something that is not delivering good value to you.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> They only have some points copy pasted from documentations, but they never tried to explain them. Just read, copy and paste in your program. What is it, why it is used for, don’t ask anything.

Reading documentation is a skill you have to pick up. **Having said that, we have always explained something that students have asked.** Just ask anyone who attended the sessions. More significantly, most of the new things we learnt, were self taught. Unless you pick up this lifelong habit, you will struggle in the real world.

Now is a good time to start.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> Some students request for extending the time limit of [roject-2 just only for one day, but what was their excuse- "We won’t be able to extend deadline, if we do, then evaluations will get delayed. "

That is correct. We do not want to evaluations for Project 2 to be delayed as end term is very close. Is your complaint that you want evaluations to be delayed? Also its not an excuse. Its a fact. Delaying submissions, delays evaluations. Its just basic logic.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> I want to ask them, where is the result of Project-1?

They have already been sent to all those who passed the prerequisites. Yours did not pass the first time.

**Luckily for you,** our first priority is always to do our best for students. So not being satisfied with the validation script that was run which was stricter, we created a new one that was more forgiving. You should get a 0 based on the stricter criteria, but you passed on our more lenient check and now you will soon be getting a normalised 7/20 score (we have not decided the normalisation yet because its a matter of deciding how lenient to be).

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> The first date of result declaration was 26-Feb, then their another date was 16-March, but until now on 2-Apr, we do not get our results. It is more than 45 days, what is this going on? Nobody tried to ask with our great teachers.

If you had attended the live session you would have seen Anand explain the reason for the delay. And we do not mind when students ask why and we freely tell them why. So I do not understand how you came to this conclusion.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> In project-2, we have to continue running our project until they will not evaluate, whether they take more than 1, 2 or more months. Either we have to host online by paying or run our own system for 24x7 unto when, we also don;t know as their result date is also not fixed, it is just a combination of letters and numbers showing on portal.

Anand invited students to write the evaluation script in his live session. And since you claim it is so easy you could have written it and gotten full marks. I am not sure why you did not take this easy option. You complained about it, but decided not to create a solution?

Also if you watched the sessions, we never asked you to run your server for 2 months or 1 month etc. Its generally a bad idea to make assumptions that have no basis in reality. Project 2 is easy to evaluate. We expect it will take a few days, possibly by this weekend to finish evaluation and push a score. So why you came to the conclusion it would take months, is a mystery, given that you already rightfully explained that its easy to write a script.

But validation takes time. We want to make sure there are no bugs and errors and a lot of edges are possible when students are running various deployments. So we want to give them the best chance of actually scoring. Unless you prefer we do a rush job and give them zeros. You would have received a zero in your project 1 had we not caught a few edge cases in our testing regime.

You can take a poll and ask fellow students if they prefer your approach. We are always happy to make changes based on feedback.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2002668/48/66999_2.png) 23f2002668:

> It is my kind request, our term is going to be completed, but please make some efforts in next term.
>
> Thankyou to all my respected ‘The Great Teachers’.

I am glad you decided make a kind request, although by all the personal insults and attacks and your ending sign off its clear that neither `respect` nor `kindness` is evident in your post.

But thank you for your feedback.

One final note: Do interact more, its healthy. We make mistakes, and we learn. There are many things we want fix for next term. Its not at all our desire to delay evaluations. The complexity of project 1 evaluations was unexpected. So we do apologise for that. We have done so repeatedly, even in our sessions and in discourse posts. The scripts that we released for everyone, probably showed how challenging it was to get it right so that everyone who could get a score, got a score.

And when writing posts or emails or any communication, try to stay on point and professional. We are always happy to learn what we can change and improve.

Kind regards,  
TDS team

---

Hi, I have a few things to say

## My background :

I have completed all the courses in diploma except TDS. I have secured reasonably good grades in all the courses. However, I failed TDS the last term and I am likely to fail in this term too. The reason is, I got bad marks in both ROE and I have never submitted any project, i.e., I have not submitted 3 TDS projects in the last two terms and did badly in the first project of the previous term.

## My Initial Disappointments with this Course

In one of the orientation session, I heard Andrew sir say this (subject to correction):

> The video lectures are the primary content. It is not compulsory to attend the live sessions, but it is highly recommended.

* Here, the most important resource are the live sessions. I did not like it. Till now, I have managed all the courses with faculty lectures alone. I rarely watch live sessions. I didn’t like watching live sessions. I felt it was against what is pointed out in the previous paragraph
* ROE is just for forty five minutes, with around 10 questions. I felt that this is rubbish and unthoughtful.
* There are not many videos explaining the tools (from IIT side). Only a few videos. Most of the tools are explained through text. I felt that a the purpose of a college course is to explain things in a simple way so that we can learn it easily.

## Why did I fail?

### Last Term

I dumped myself with a 3 more courses, projects and nptel courses. I didn’t practice the GAs properly. So I failed ROE. I will come to the projects soon.

## This term.

I made sure that I do all the GAs properly. But I did better than last time in ROE but still bad. This time because, other than GAs, I didn’t allocate time for ROE. Also, I didn’t submit both the projects.

In both the terms I didn’t collaborate with anyone. I felt that I shouldn’t earn my marks be talking help from someone. I felt it is not fair.

## Me Understanding about the Course Now

This one line changed my view about ROE.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png)[On another topic](/t/99838/2)

> **What does this RoE evaluate?** Implicit learning.

I am reasonably ok with python and all the tools in this course. But in ROE, I was not able to write a nested for loop, which was needed for some question. It is not that I don’t know how to write a simple nested loop. I discovered the fact that I have not coded enough.

I scored 100 in all the OPPEs : python, java, PDSA, DBMS. I knew the concepts. But the questions were not difficult and the time was ample. This is not the case in TDS.

Now I realize that I am not good in SQL or DSA. It is just the questions were easy and was accompanied with ample time.

In MLP, I score just 40 in OPPE 1, this was because of me not practicing `SKLearn`. Then I practiced and got 90 in the second OPPE.

This course has made me realise that till I need to learn relearn these things in an ***implicit*** way.

This is the exact reason why I have not been able to complete the projects. I still know most of the things required for project 1 and 2. But I was not able to practically sit and write the code.

I have understood that this is not a traditional course. I feel that we must expect something different from this course. Especially not just marks

I have understood that the limited amount of recorded lectures for is a way to make the students to practically go through the documentation. Understand the complex phrasing of some functionalities, etc.

I am most likely to take this course again. I feel extremely bad to have wasted 15000 rupees. But this course has been a wake up call for me. I still feel that I have the potential to do this course way better than this. What I would have to do is a lot more coding of what I have already learnt.

From the other project courses, I had a wrong assumption that projects are about applying what we have learnt. This was also a reason why I didn’t do my projects in TDS. I felt that the course team didn’t cover all the essentials of a projects. I have now realized that projects are about applying what we know and also learn new things which will enhance our projects.

Since this is not a traditional course, I also feel that it is fine to collaborate and seek help, at the same time, strive to contribute to others too.

Thanks to [@s.anand](/u/s.anand) , [@carlton](/u/carlton) , [@Jivraj](/u/jivraj) and [@Saransh\_Saini](/u/saransh_saini)

> Just two suggestions

* I feel that MAD 2 and MLP should be corequisites.
* While introducing the projects, kindly include a video where the flow of the project is explained. Also, address few questions in the video itself which are likely to be asked by us.

---

true but I wish they can inform how quickly they can evaluate for those using paid platforms / ngrok

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Hello Carlton,

When are you guys likely to test the API endpoints for Project 2?  
I have hosted it on Microsoft Azure, and I only have $92 left out of the free $100 credit. It would be great if you could do this within a week. It is decreasing rapidly.

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) same issue  
I only have $80 left out of the free $100 credit. It would be great if you could do this within a week.

---

[@parthivn28](/u/parthivn28) [@Harshjayswal-2003](/u/harshjayswal-2003) [@23f2004912](/u/23f2004912)  
Evaluations will start before this weekend, with some sampling done possibly even tonight and most evaluation runs tomorrow.

Also we will prime the target first by sending a dummy request so it gets “warmed up” because some of you have reported time to respond to first request takes time for the server to spin up.  
Then once we know its responding, we will send requests for evaluation.

Kind regards

---

[@carlton](/u/carlton) lord carlton ![:ok_hand:](https://emoji.discourse-cdn.com/google/ok_hand.png?v=14 ":ok_hand:")

---

Yess, I too did the same , previously submitted on 11.55 and edited my response on 12.01 with /api . Hope u will consider it . [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

hello can you share ip address whenever you hit our api then we know you hitting it please

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand) sir, I have noticed that sometimes our vm based application gets stuck and on verifying every request using FastApi have noticed that best way to check is run and get your answer post that RESET it back and then run another query and it works perfectly fine, not sure have other faced this issue or not, but it would be great if you could take note of this while evaluating just for safety.

Hope you take note of this and take this into consideration.  
Thanks & Regards,  
Digvijaysinh Chudasama

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) yes same issue

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)  
Sirs, I too am facing this issue..

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000588/48/478_2.png) 21f2000588:

> check is run and get your answer post that RESET it back and then run another query

I couldn’t get what this part means?

---

Okay so basically sometimes what happens is while verifying on FASTApi – it gives errors like missing paramaters like… So basically sometimes it needs resetting the request parser and then it works perfectly fine.

```
{
  "detail": "execute() missing 1 required positional argument: 'file_bytes'"
}

```

Which is incorrect, so if we press the RESET button and execute it works properly.

Here's a description of the image:
\*\*Image Description:\*\*
The image shows a form or interface with several input fields and buttons. The top section has "Parameters" as the heading and a cancel and reset button. It has a "Request body" section with a dropdown selection of "multipart/form-data". Below, there is a section with a text field labeled "question" which also states that it is required, along with a "Download and use multi-cursors and convert it into a single" prompt, a file upload labeled "file" with a "Choose File" button and a file name, "q-multi-cursor-json.txt". There's also a checkbox for "Send empty value". Buttons for "Execute" and "Clear" are located at the bottom. There is also a section called "Responses" with "Curl" as the heading.
\*\*image text:\*\*
Parameters
No parameters
Request body required
multipart/form-data
question \* required
string
Download and use multi-cursors and convert it into a single
file
string | (string |
null) ($binary)
Choose File q-multi-cursor-json.txt
Send empty value
Responses
Curl
Execute
Clear
Cancel
Reset

Correct output image –  
Here's a description of the image:
The image is a screenshot of a web interface. The top part indicates "Server response" with "Code" and "Details" listed below. The code shows "200" and the details section displays "Response body" with a json response. There is a "Download" button.
image text:
Server response
Code Details
200
Response body
{
"answer": "7a5955793fe63e199d0677d33f0053c50110d66589253280b1be96c598df24d8"
}
Download

Hope you get my point which i’m trying to convey sir.

---

[@23f2004912](/u/23f2004912)

Just a brother trying to help students gain valuable skills.  
Nothing more brother.

The success of students’ future, is the best reward.

Sometimes it takes a bit longer because some lessons are harder than others. And we all make mistakes. But if you’ve learnt something valuable on the journey, then you are better prepared for what comes next regardless of whether you could clear the obstacle the first time or not.

Kindest regards,  
Just Carlton  
(nothing more).

---

The way we test your api is **not through a front end.**

We send a request to the endpoint directly. We have demoed it in live sessions.

We have even posted on discourse snippets of what this looks like.

As long as your endpoint responds to a request that we send, it will be fine.

Kind regards

---

sir [@carlton](/u/carlton) currently iam facing an issue sir. just now in order check weather my api is working fine or not . i just tried curl some question but unexpectedly i got timeout error from vercel. i have deployed my app in vercel only. when i checked out i found that in vercel for free account the request timeout is 10s. what to do sir some times gpt take more time to respond. The same endpoint after an hour i tried works fine . will this be an issue sir .

---

[@carlton](/u/carlton)  
i also edited my form due to /api/ after deadline on monday  
can u tell atleast whats the status on this query

---

Dear [@Carlton](/u/carlton) and [@S.Anand](/u/s.anand),  
I successfully deployed my project on Vercel, and it works perfectly when tested using curl commands. Each task installs its required packages and runs as expected. However, I encountered an issue with Vercel’s free version, which has a 250MB limit. While my project’s size without installed packages is approximately 34MB, the size exceeds the limit once packages like Pandas, NumPy, Pillow, Whisper, and Uvicorn are installed, causing the server to crash.  
Could you kindly suggest any alternatives or solutions for this issue? I would greatly appreciate your guidance, as I fear all my hard work might go to waste without a resolution.

---

We are in the processing pipeline. You will have to wait till it completes. Basically if your endpoint works when we send it a request you will be evaluated. We will use the timestamp of your latest endpoint before the deadline.

Hope that answers your question.

---

The alternative is to use vercel purely as an endpoint service that processes most things without large libraries, and for more heavy duty backend work forwards the request to another system that handles it and sends it back to your vercel function which then relays the answer to the request.

---

in spreadsheet edit response modify previous response with timestamp, how you can access that timestamp response?? So how can u have my end point before deadline one since i updated it after deadline.  
Also the before deadline one end point is  
/api which i changed to /api/ after deadline so if u somehow have access to my old url pls consider adding 1 (slash) / :')

---

gform allows multiple submissions. i would have to check with [@s.anand](/u/s.anand) if its been enabled, i almost certain he has configured it for multiple submissions.

---

I understand your point but what I am saying is that when I edited my end point after deadline it changed my timestamp to after deadline one so that is my concern that my submission might not be even considered

---

you can have multiple submissions with multiple timestamps in gform. (unless you chose to edit your response, in that situation i have not tested what actually happens).

---

I have edited after deadline from /api to /api/  
I did not resubmit

---

:

---

# :graduation_cap: From Problem to Platform: Building “Vicky” – A Smart Data Science Assistant for TDS @ IIT Madras

![:rocket:](https://emoji.discourse-cdn.com/google/rocket.png?v=14 ":rocket:") **Project Demo Website**: <https://app.algsoch.tech>

During our college course *Tool for Data Science (TDS)* at **IIT Madras**, we were tasked with a challenging but exciting project: **to build a platform that can take in natural language questions and execute corresponding solutions through an API**.

## :brain: The Mission:

Create a tool that behaves like a **chatbot**, accepts **user queries (text or file-based)** via **web or API**, processes them intelligently, **executes the appropriate code**, and returns accurate results—like a real data science assistant.

---

## :counterclockwise_arrows_button: The Journey: From Fails to Final

At first, the natural choice was to try **LLM agents**—they sounded magical. But in real-world usage, they were slow, unreliable, and lacked precision. Most failed to parse or execute even moderately dynamic queries. ![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14 ":cross_mark:")

Then I thought—what if I manually mapped questions and answers using a **static JSON structure**? That quickly broke when users passed **different parameters, different files**, or queried in **non-standard formats** like “code -s” or “code -v”.

The next idea: write **individual Python scripts per question** from our Graded Assignments (GA1–GA5). But that lacked flexibility and reusability. Creating multiple files became unmanageable and non-scalable. ![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14 ":cross_mark:")

---

## :wrench: The Breakthrough: Dynamic Function Mapping

After multiple iterations and failed prototypes, I finally found the right architecture:

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Centralized engine in `vicky_server.py`  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Uses **regex-based pattern matching** to detect question types, extract parameters, and identify the correct solution  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Each solution is a structured Python function like `ga1_first_solution(query=None)`  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Supports dynamic parameter injection, command-line variations, file-based queries, and more  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Acts like a **mini compiler for data science tools**

---

## :globe_with_meridians: Presenting Vicky – The Mini Chatbot for TDS :fire:

Vicky is a **smart, modular chatbot** built specifically for **Tool for Data Science at IIT Madras**. It’s packed with real functionality—not just templates.

### Key Features:

![:brain:](https://emoji.discourse-cdn.com/google/brain.png?v=14 ":brain:") **Graded Assignment Solver**  
Handles dynamic, real-world questions from GA1 to GA5 like:

* `code -s` / `code -v` → VS terminal commands
* Create FastAPI API for CSV with filtering/searching
* GitHub automation: repo creation, GitHub Actions setup
* Data cleaning, scraping from IMDb, image compression

![:open_file_folder:](https://emoji.discourse-cdn.com/google/open_file_folder.png?v=14 ":open_file_folder:") **File Upload with Query Matching**  
Users can upload a file (CSV, JSON, Excel) and ask file-specific queries. The system understands context and dynamically links the query to the uploaded file.

![:globe_showing_europe_africa:](https://emoji.discourse-cdn.com/google/globe_showing_europe_africa.png?v=14 ":globe_showing_europe_africa:") **HTML Viewer + Base64 Decoder**

* View any website in rendered & source format using CORS proxy
* Upload Base64 string → Get original image back

![:robot:](https://emoji.discourse-cdn.com/google/robot.png?v=14 ":robot:") **Webhooks Integration**

* Live notifications via **Discord** & **Slack** whenever `/api` endpoints are accessed
* Monitors **server status (online/offline)** and sends real-time updates

![:spouting_whale:](https://emoji.discourse-cdn.com/google/spouting_whale.png?v=14 ":spouting_whale:") **LLM Download + Auto Tunneling**

* Downloads LLaMA models
* Dynamically finds available ports
* Creates and exposes tunneled endpoints

![:chart_increasing:](https://emoji.discourse-cdn.com/google/chart_increasing.png?v=14 ":chart_increasing:") **Live Web UI at [app.algsoch.tech](https://app.algsoch.tech)**

* Ask any TDS question
* Upload and query with files
* Image decoder
* Graded assignment slider navigation
* HTML viewer
* API health status

---

## :man_technologist: Built With:

* **FastAPI** for blazing fast APIs
* **Regex & Pattern Matching** for dynamic input detection
* **GitHub Copilot** + my Python debugging and architectural thinking
* Full webhook and status monitoring system
* Modular backend (`vicky_server.py`) and web frontend (`vicky_app.py`)

I want to extend a huge thank you to [@s.anand](/u/s.anand) for their guidance on this project. I’ve learned what prompt engineering is and how we can leverage large language models (LLMs). One interesting takeaway is that while these technologies won’t replace our jobs—especially for those who understand programming—they will create new job opportunities instead.  
Now I am capable of how fastapi work and more things and how to structure code and how to design code and most important what to think for project

---

Dear Sir,  
I would like to clarify the situation regarding my previous submission. Initially, I provided an ngrok link, but due to an error with ngrok, it stopped working. I then found an alternative solution using Cloudflare with a custom domain that I obtained through the GitHub Student Pack. I successfully created a tunnel, and it is currently functional. I can shut down my laptop, and it still works with the same URL when I restart.  
I hope you will consider my case. I submitted my work at that time because I learned about this solution from a fellow student on Discord. I only changed the URL and made no other modifications.  
Thank you for your understanding

---

Hi [@carlton](/u/carlton)

The same issue has affected several of us. During the last Google Meet session, we explained the situation to [@Saransh\_Saini](/u/saransh_saini).

It seems that when we edit our responses, the timestamp with other values updates not submitted as new response. However, the position of the response in the form remains unchanged. For instance, we submitted our response at 11:30 PM on March 31st, and someone else submitted theirs at 11:45 PM. Even after editing our response the next day, our entry still appears above theirs.  
We just wanted to clarify: Will responses edited or submitted on April 1st still be considered, given that the form remains open? If not, is there any way we can show proof of our original submission? Currently, we have email confirmations for both the initial and the edited responses.

We hope this won’t be a major issue, especially not on the level of Project 1 concerns. Looking forward to a positive resolution from the TDS team.

Thank you  
Lakshay

---

Dear [@carlton](/u/carlton) [@s.anand](/u/s.anand) Sir  
“I’ve deployed my project to Microsoft Azure through GitHub, and my Azure for Students account was verified today. Could you kindly review this project instead of the previous link I shared? While I did not make any changes to the code, you can access and review it directly on GitHub.”

---

My Azure credits are burning out. It is giving me unwanted pressure.

Here's a description of the image:
The image is a screenshot from a webpage, likely a Microsoft Azure sponsorship dashboard. The page displays information about a sponsored account.
image text:
SPONSORED
Active - Offer expiring in 349 days
USED
26 USD
TOTAL CREDIT
100 USD
REMAINING
74 USD
18 Mar 2025 - 18 Mar 2026 \*Based on usage through 4/4/2025
23f2004837@ds.study.iitm.ac.in
SUBSCRIPTIONS
1 ACTIVE
Subscription Usage
3def2d44-91a8-495d-81ff
Azure for Students

Please evalute the project early.

we can help in writing evaluation script, that also would be a learning for us.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

Dear Sir [@carlton](/u/carlton),

Sir, please note that after the deadline I haven’t resubmitted the form but I have edited it (as the form was allowing editing till then). Now what exactly have I edited is just added a “/” at the end and that’s it and nothing more. Highlighting it again, I haven’t resubmitted the form but edited it on the very next morning after the deadline.

So now my question is: My edited response will be accepted right in this case?  
Sir, please throw some light on my doubt.

Warm Regards,  
Tensed TDS Student

---

[@carlton](/u/carlton) . Hi sir, I also edited the form after deadline. I just added /ask in the end…

---

any update on this would be appreciated [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

I would like to clarify something, I had gotten a couple of get requests on my ngrok api endpoint .(but I had set it up for post req as per the P2 details) .Wanted to know if this is requests from ur side. Thank you

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a terminal output with log entries. Each line starts with a timestamp and includes information about TDS python processes and HTTP requests. The log entries show various HTTP methods, status codes (200 OK, 404 Not Found, 405 Method Not Allowed), and requested paths like "favicon.ico", ".env", and "logincheck". There's also a "WARNING" log for an "Invalid HTTP request received".
image text: Apr 05 14:19:25 TDS python[79249]: INFO: 162.243.238.100:0 - "GET /t4 HTTP/1.0" 404 Not Found
Apr 05 14:19:27 TDS python[79249]: INFO: 162.243.238.100:0 - "GET /favicon.ico HTTP/1.0" 200 OK
Apr 05 14:19:27 TDS python[79249]: INFO: 162.243.238.100:0 - "GET / HTTP/1.0" 200 OK
Apr 05 14:19:28 TDS python[79249]: INFO: 162.243.238.100:0 - "GET /teorema505?t=1 HTTP/1.0" 404 Not Found
Apr 05 14:29:32 TDS python[79249]: INFO: 34.89.64.89:0 - "GET / HTTP/1.0" 200 OK
Apr 05 14:35:51 TDS python[79249]: INFO: 45.148.10.172:0 - "GET /.env HTTP/1.0" 404 Not Found
Apr 05 14:36:09 TDS python[79249]: INFO: 154.81.156.10:0 - "PROPFIND / HTTP/1.0" 405 Method Not Allowed
Apr 05 14:51:05 TDS python[79249]: INFO: 154.81.156.10:0 - "PROPFIND / HTTP/1.0" 405 Method Not Allowed
Apr 05 14:53:52 TDS python[79249]: INFO: 172.172.245.144:0 - "GET /autodiscover/autodiscover.json?@zdi/Powershell HTTP/1.0" 404 Not Found
Apr 05 14:59:42 TDS python[79249]: INFO: 195.211.191.127:0 - "GET /.env HTTP/1.0" 404 Not Found
Apr 05 15:06:20 TDS python[79249]: INFO: 194.163.152.77:0 - "GET /.git/config HTTP/1.0" 404 Not Found
Apr 05 15:51:28 TDS python[79249]: INFO: 84.201.151.18:0 - "GET / HTTP/1.0" 200 OK
Apr 05 15:56:14 TDS python[79249]: INFO: 103.175.163.104:35562 - "GET /.env HTTP/1.1" 404 Not Found
Apr 05 16:05:16 TDS python[79249]: INFO: 154.81.156.10:0 - "PROPFIND / HTTP/1.0" 405 Method Not Allowed
Apr 05 16:27:40 TDS python[79249]: INFO: 81.213.175.254:0 - "GET / HTTP/1.0" 200 OK
Apr 05 16:40:17 TDS python[79249]: INFO: 185.180.140.106:0 - "GET / HTTP/1.0" 200 OK
Apr 05 16:44:11 TDS python[79249]: WARNING: Invalid HTTP request received.
Apr 05 16:47:28 TDS python[79249]: INFO: 85.255.108.243:0 - "GET / HTTP/1.0" 200 OK
Apr 05 16:51:30 TDS python[79249]: INFO: 20.163.15.217:0 - "GET /actuator/health HTTP/1.0" 404 Not Found
Apr 05 17:13:31 TDS python[79249]: INFO: 161.35.235.64:34746 - "GET /.env HTTP/1.1" 404 Not Found
Apr 05 17:13:32 TDS python[79249]: INFO: 161.35.235.64:34756 - "GET /.git/config HTTP/1.1" 404 Not Found
Apr 05 17:20:32 TDS python[79249]: INFO: 181.188.166.178:0 - "GET / HTTP/1.0" 200 OK
Apr 05 17:24:00 TDS python[79249]: INFO: 181.188.166.178:0 - "POST /logincheck HTTP/1.0" 404 Not Found
azureuser@TDS:~$
  
something’s cooking… ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=14 ":sweat_smile:") And it doesn’t seem like good news for us — at least from the initial visuals.

---

[@carlton](/u/carlton) I’m noticing frequent requests from globally scattered IPs—mostly from cloud or bulletproof hosts like DigitalOcean, Contabo, and Azure—targeting sensitive paths like `/t4`, `/logincheck`, `/.env`, and `/.git/config`. These include IPs from places like New York (162.243.238.100), London (34.89.64.89), Amsterdam (45.148.10.172), Moscow (84.201.151.18), Jaipur (103.175.163.104), and Vilnius (85.255.108.243). It really seems like automated vulnerability scanning or botnet activity. Carlton, what can I do??

---

Several students have made the exact same problem. We are looking into it.

---

The evaluation script is ready and the evaluations are going on. So have no worries, your $75 are enough to carry out several evaluations.

---

My server shut down can you ask me to run the server again? [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

---

I’m running the servers now, i got a bunch hits from random ip s what is the ip address i add a verification if need be

---

INFO: Shutting down  
INFO: Waiting for application shutdown.  
INFO: Application shutdown complete.  
INFO: Finished server process [15355]  
INFO: Stopping reloader process [11917]

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) .

23f1002382@ds.study.iitm.ac.in@tdsproj2:~/tds-solver\_NEW$ ps -a  
PID TTY TIME CMD  
24617 pts/0 00:00:01 python3  
24619 pts/0 00:00:00 python3  
24620 pts/0 00:00:01 python3  
24645 pts/0 00:00:00 ps

ran it again. You can see from the process id that was actually a process that was started long back

---

Also a better evaluation strat would be to submit the GitHub repo in the form(Else they can make changes to the repo, who checks the commit history?) and maybe conduct a 2 min demo where the student clones the repo and then you run the script?  
I know many students are there but other subjects do it for project courses?

Maybe a helpful tip for next time

If i do fail and repeat this course. Hopefully not XD

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) I too faced the same issue, I received a bunch of hits from random ip addresses and it got shut down.

image description: The image is a black and white terminal output, containing logs. The logs show HTTP request details. It has warning and info messages including messages like "Invalid HTTP request received", "404 Not Found" and "Shutting down".
image text: WARNING: Invalid HTTP request received.
INFO: 104.234.115.27:34430 - "GET / HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:34434 - "GET /manage/account/login HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:36174 - "GET /admin/index.html HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:36184 - "GET /index.html HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:36186 - "GET /%2BCSCOE%2B/logon.html HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:36190 - "GET /cgi-bin/login.cgi HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:36200 - "GET /login.htm HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:44582 - "GET /login.html HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:44586 - "GET /login.jsp HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:43564 - "GET /login HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:43572 - "GET /doc/index.html HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:48112 - "GET /remote/login HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:47634 - "GET //admin/login.asp HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:47648 - "GET /web/ HTTP/1.1" 404 Not Found
INFO: 104.234.115.27:47204 - "GET //webpages/login.html HTTP/1.1" 404 Not Found
INFO: 154.81.156.35:54334 - "GET / HTTP/1.1" 404 Not Found
INFO: 114.33.166.218:60327 - "GET / HTTP/1.0" 404 Not Found
INFO: 192.210.187.85:55602 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 221.144.32.29:57561 - "GET / HTTP/1.0" 404 Not Found
INFO: 156.229.233.88:56664 - "POST /goform/set\_LimitClient\_cfg HTTP/1.1" 404 Not Found
INFO: 106.71.57.84:38617 - "GET / HTTP/1.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 123.57.165.38:48810 - "GET /.env.bak HTTP/1.1" 404 Not Found
INFO: 123.57.165.38:51206 - "GET /.env HTTP/1.1" 404 Not Found
INFO: 123.57.165.38:51212 - "GET /containers/json HTTP/1.1" 404 Not Found
INFO: 123.57.165.38:51214 - "GET / HTTP/1.1" 404 Not Found
INFO: 154.81.156.35:53364 - "GET / HTTP/1.1" 404 Not Found
INFO: 172.172.245.91:56766 - "GET /hudson HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 89.44.131.187:52847 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 154.81.156.35:52966 - "GET / HTTP/1.1" 404 Not Found
INFO: Shutting down
INFO: Waiting for application shutdown.
INFO: Application shutdown complete.
INFO: Finished server process [1320]

I started it once again. Can you please reevaluate it now if it hasn’t been done yet. I actually tested it till 3rd of April and it was working fine. I don’t know what actually happened. Please do consider.

Actually in the free tier there are many issues. These issues are beyond our control and I request the TDS team to please consider this issue and please consider re-evaluating it if it has not been done yet as we had put in a lot of efforts.

---

i havent recieved any pings yet . Has it pinged everyone or is it still coming batch by batch

---

Now my token is expired?

---

They revoked token access?

---

My env only shut down its running again lol

You have used 11 requests this month (2025-04), costing 0.01 USD.

so maybe you guys have not hit my server yet im guessing

---

154.81.156.35:57962 this ip keeps pinging , is this the teams? [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

Just do a geographic search on the ip

---

Even am getting random requests from US,Netherlands, Singapore etc… what might be the reason ![:thinking:](https://emoji.discourse-cdn.com/google/thinking.png?v=14 ":thinking:")

---

Hi [@23f1002382](/u/23f1002382)  
I re-ran evaluation on your endpoint, and it completed successfully.

---

They are malicious probes. A global cyber war is going on. So anything that can be compromised is being probed.

---

[@carlton](/u/carlton) sir

A lot of us have hosted on Azure and other platforms and were wondering by when we could expect project 2 marks so that we can take this down ? Could we have rough idea as to when the results will be available ?

---

[@Carlton](/u/carlton), I believe you all have evaluated it. For me, there are some requests from a known IP with the following location details:

```
{'status': 'success', 'country': 'India', 'countryCode': 'IN', 'region': 'TN', 'regionName': 'Tamil Nadu', 'city': 'Chennai', 'zip': '600042', 'lat': 13.0895, 'lon': 80.2739, 'timezone': 'Asia/Kolkata', 'isp': 'IIT Madras', 'org': 'IITM', 'as': 'AS141340 IIT Madras', 'query': '103.158.43.17'}

```

This request was made at 4:38:19 IST.  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a terminal window displaying log entries and a command prompt. The log entries show timestamps, process information (TDS, python, and process ID), and HTTP request details with IP addresses and status codes. The last line shows the command prompt.
\*\*image text:\*\*
Apr 06 10:10:28 TDS python[79249]: INFO: 103.158.43.17:0 - "GET /favicon.ico HTTP/1.0" 200 OK
Apr 06 11:08:19 TDS python[79249]: INFO: 103.158.43.17:0 - "POST /api HTTP/1.0" 200 OK
Apr 06 11:08:19 TDS python[79249]: INFO: 103.158.43.17:0 - "POST /api HTTP/1.0" 200 OK
Apr 06 11:08:19 TDS python[79249]: INFO: 103.158.43.17:0 - "POST /api HTTP/1.0" 200 OK
Apr 06 11:08:19 TDS python[79249]: INFO: 103.158.43.17:0 - "POST /api HTTP/1.0" 200 OK
Apr 06 11:08:19 TDS python[79249]: INFO: 103.158.43.17:0 - "POST /api HTTP/1.0" 200 OK
azureuser@TDS:~$ |

---

Are the evaluations done by any chance? I havent received any requests from an Indian IP address yet…

---

Evals are going on. I just checked my logs, it seems like we ran evaluation on your endpoint, but it looks like your server wasn’t running.

---

But i tried and its working can you let me know what I can do?  
image description: The image is a screenshot of a POST request in a web application (likely Postman or a similar tool) used for API testing. The request is directed to the URL "4.213.61.248:8080/api". The image captures the "Body" section of the request, with the form-data option selected. There is a "question" key with the text "what is output of -s?". Below is the JSON response showing version and other details.
image text:
```json
{
"answer": "Version: Code 1.96.2 (fabdb6a30b49f79a7aba0f2ad9df9b399473380f, 2024-12-19T10:22:47.216Z)\nOS Version: Darwin arm64 24.2.0\nCPUs: Apple M1 (8 x 2400)\nMemory (System): 8.00GB (0.09GB free)\nLoad (avg): 2, 6, 6\nVM: 0%\nScreen Reader: no\nProcess Argv: --crash-reporter-id ca90dba9-1235-4414-b9a6-6a7e9b4e613b\nGPU
Status: 2d\_canvas: enabled\n canvas\_oop\_rasterization: enabled\_on\n gpu\_compositing: direct\_rendering\_display\_compositor: disabled\_off\_ok\n multiple\_raster\_threads: enabled\_on\n rasterization: opengl: enabled\n raw\_draw: disabled\_off\n video\_decode: skia\_graphite: enabled\n video\_encode: enabled\n"
}
```  
image description: The image is a terminal output, likely from a software development environment. It displays JSON-formatted data and command-line information. The text is predominantly white against a black background. The data describes function calls, model usage, and cost metrics related to an API interaction. The terminal output includes details like prompt tokens, completion tokens, and various cost-related figures.
image text: Loaded embeddings from cache file
1 0.37612552369709695
[{'type': 'function', 'function': {'name': 'solver\_1', 'description': 'Gives output of a specific command in VS code', 'parameters': {'type': 'object', 'properties': {'command': {'type': 's
tring', 'description': 'the command whose output is required'}}, 'required': ['command'], 'additionalProperties': False}, 'strict': True}}]
{'id': 'chatcmp1-BJK7nbeTemPJrZ1AttZaXXqHBCkwG', 'object': 'chat.completion', 'created': 1743945291, 'model': 'gpt-4o-mini-2024-07-18', 'choices': [{'index': 0, 'message': {'role': 'assista
nt', 'content': None, 'tool\_calls': [{'id': 'call\_IND10amENHPbPbhTmsTqBIf3', 'type': 'function', 'function': {'name': 'solver\_1', 'arguments': '{"command":"-s"}'}}), 'refusal': None, 'annot
ations': []}, 'logprobs': None, 'finish\_reason': 'tool\_calls'}], 'usage': {'prompt\_tokens': 63, 'completion\_tokens': 18, 'total\_tokens': 81, 'prompt\_tokens\_details': {'cached\_tokens': 0, 'a
udio\_tokens': 0}, 'completion\_tokens\_details': {'reasoning\_tokens': 0, 'audio\_tokens': 0, 'accepted\_prediction\_tokens': 0, 'rejected\_prediction\_tokens': 0}}, 'service\_tier': 'default', 'sys
tem\_fingerprint': 'fp\_b376dfbbd5', 'monthlyCost': 0.007031520000000004, 'cost': 0.000297, 'monthlyRequests': 34, 'costError': 'crypto.createHash is not a function'}
{'command': '-s'}
INFO: 54.86.50.139:41710 - "POST /api HTTP/1.1" 200 OK
23f2000599@ds.study.iitm.ac.in@TDS-PROJECT:~/tds-solver$

---

I have been doing this the entire day even yest and getting the output. Can you please check again ![:sob:](https://emoji.discourse-cdn.com/google/sob.png?v=14 ":sob:")

---

It seems like your server went offline for some reason when we ran evaluations on it. Keep your server running for the next 2 hours, we’ll run a re-evaluation.

---

Yes sure thank you so much. It is running right now

---

[@Saransh\_Saini](/u/saransh_saini)  
The same thing happened to me.  
I have not received request from Indian ip as far as I can see on the logs.  
Can you please check if my server responded or not ?  
I am using Google cloud and the VM was running continuously…

---

I just now checked it ran! all 5 qs thank you so much!

---

Your submission was complete successfully. Even your score card has been generated.

---

Thank you so much sir…

---

[@Saransh\_Saini](/u/saransh_saini) - This is 24f1001631  
The same thing has happened to me as the mentioned above. I also have not received request from Indian IP as far as I can see on the logs. I am using the azure VM itself.  
I rechecked and maybe the server went offline, so I re-ran the script anyway and checked a few questions now and it works.  
I think after a certain while it timed out for me(not entirely sure tho)… but i fixed it.

ga1 q1  
image description: The image shows a network request with the details of a "question" and its "answer" displayed in JSON format. The request is a POST method to an API endpoint.
image text: TDS-Project2-Testing-Again / ga1 / q1-working-now
POST
104.211.116.95:8080/api
Save
Share
Send
Params Authorization Headers (9) Body Scripts Settings
Cookies
O none form-data x-www-form-urlencoded raw binary GraphQL
Key Value Description Bulk Edit
✔ question Text Install and run Visual Studio Code. In your Terminal (or......
file File Select files
Key Text Value Description
Body Cookies Headers (4) Test Results
{} JSON ▷ Preview Visualize
200 OK 3.86 s 2.08 KB Save Response
1 {
2 "answer": "Version: Code 1.96.2 (fabdb6a30b49f79a7aba0f2ad9df9b399473380f, 2024-12-19T10:22:47.216Z)\nOS Version: Darwin arm64 24.2.0\nCPUs: Apple M1 (8 x 2400)\nMemory (System): 8.00GB (0.09GB free)\nLoad (avg): 2, 6,
6\nVM: 0%\nScreen Reader: no\nProcess Argv: --crash-reporter-id ca90dba9-1235-4414-b9a6-6a7e9b4e613b\nGPU Status: 2d\_canvas: canvas\_oop\_rasterization: disabled\_off\_ok\n gpu\_compositing: enabled\_on\n multiple\_raster\_threads: enabled\n rasterization: enabled\n raw\_draw: disabled\_off\n direct\_rendering\_display\_compositor: enabled\n opengl: enabled\n video\_encode: enabled\n skia\_graphite: enabled\n video\_decode: enabled\n webgpu: disabled\_off\n webg12: enabled\n\nCPU %\tMem MB\t PID\tProcess\n 115 t 1439\tcode main\n 0 t 49\t 1443\t gpu-process\n 0 t 16 t 1444\t utility-network-service\n 0 t 188 t

ga5 q5  
image description: The image is a screenshot of a POST request in a tool like Postman. It displays the details of an API call, including headers, body, and the response. The request is targeting an API endpoint at "104.211.116.95:8080/api". The body of the request is in "form-data" format. The key-value pairs in the body include "question" with the value "Sales Analytics at GlobalRetail Insights" and "file" with the value "q-clean-up-sales-data (7).json". The response section shows the JSON output, indicating a status code of 200 OK.
image text: POST
104.211.116.95:8080/api
Params
Authorization
Headers (9)
Body Scripts Settings
Cookies
none
form-data
x-www-form-urlencoded
raw
binary GraphQL
Key
Value
Description
Bulk Edit
question
Text
Sales Analytics at GlobalRetail Insights
file
File
▲ q-clean-up-sales-data (7).json
Key
Text
Value
Description
Body
Cookies
Headers (4)
Test Results
{} JSON
Preview
Visualize
1
{
2
"answer": "10887"
3
}
200 OK
3.68 s 143 B
Save Response

---

[@Saransh\_Saini](/u/saransh_saini)  
Hi sir, can you check and say if my server has been evaluated?  
roll no.23f3000975  
thank you in advance

---

Yes you have been evaluated.

---

You have been evaluated [@ItsMeAlex](/u/itsmealex)

---

Thanks Saransh.  
PS: Just wanted to know how did u automate the testing of something like this?(Postman?)

---

Create a shell script that loops through the list of API endpoints and uses `curl` to send requests to each. You can pass headers, authentication tokens, or data as needed.

---

[@Saransh\_Saini](/u/saransh_saini)  
Hi sir, just wanted to know when will the results be released. And also in the image I attached it I think shows five different scores for each questions you asked through curl. Is that the mark for each questions and total mark should be considered?

also want to know if we need to do any extra projects for the bonus marks.

thank you  
Here's a description of the image:
The image shows a computer screen displaying a terminal output. The text includes file paths, processing questions, scores, and HTTP status codes. The screen has various tabs like "DEBUG CONSOLE," "TERMINAL," "PORTS," "QUERY RESULTS (PREVIEW)," and "COMMENTS." The screen also has a timestamp, "06/04/2025 22:40", and a phone name "REDMI NOTE 12".
image text:
DEBUG CONSOLE TERMINAL PORTS QUERY RESULTS (PREVIEW) COMMENTS
data science tool//GA2//third.py (score: 8.30)
stion with file: E://data science tool//GA2//third.py
for: E://data science tool//GA2//third.py
n query: https://[USER].github.io
-43.17:0 "POST /ask HTTP/1.1" 200 OK
I
48,875 - tds\_app - INFO - Processing question: LexiSolve Inc. is a startup that delivers a conv
//data science tool//GA3//second.py (score: 12.90)
estion with file: E://data science tool//GA3//second.py
on for: E://data science tool//GA3//second.py
3.43.17:0 - "POST /ask HTTP/1.1" 200 OK
:48,907 - tds\_app - INFO Processing question: There is a tickets table in a SQLite database that
E://data science tool//GA1//eighteenth.py (score: 5.90)
question with file: E://data science tool//GA1//eighteenth.py
ion for: E://data science tool//GA1//eighteenth.py
58.43.17:0 - "POST /ask HTTP/1.1" 200 OK
41:49,754 - tds\_app INFO Processing question: Search using the Hacker News RSS API for the lates.
E://data science tool//GA4//sixth.py (score: 7.70)
- question with file: E://data science tool//GA4//sixth.py
ation for: E://data science tool//GA4//sixth.py
158.43.17:0 - "POST /ask HTTP/1.1" 200 OK
:41:55,269 - tds\_app INFO Processing question: As a data analyst at DataSure Technologies, you ha...
: E://data science tool//GA5//seventh.py (score: 14.50)
ng question with file: E://data science tool//GA5//seventh.py
lution for: E://data science tool//GA5//seventh.py
file in query: C:\Users\hsent\AppData\Local\Temp\unleash-repo-schema-v1-codeium-language-server.json
03.158.43.17:0 "POST /ask HTTP/1.1" 200 OK
nect REDMI NOTE 12
06/04/2025 22:40
PC

---

i am running via ngrok , and have recieved no pings yet please check

---

This Makes sense. Thanks.

---

please send complete screenshot ..

---

[@Saransh\_Saini](/u/saransh_saini) and [@carlton](/u/carlton) sir ..

Please check my link sir and please use http instead of https , I have submitted the link correctly …Kindly co-operate..

---

Postman can’t be used for automation. Had to write a script for the entire process.

---

[@Saransh\_Saini](/u/saransh_saini) I see a lot of 308’s as status codes in the logs I can see on render. Could you let me know if testing of my project was successful? Or if I did something wrong? My roll number is 21f2001573.

(A hint on my score would be welcome. ^\_^)

---

can u please check 23f3001787 as i havent recieved any hits on my ngrok logs

---

Thanks lol maybe i wont fail XD. But really thanks

---

Lol that question was only right for you XD

---

[@Saransh\_Saini](/u/saransh_saini)  
Sir can you please check 24f2000940?

---

[@Saransh\_Saini](/u/saransh_saini) could you please give indication of how long we should keep the server running? Is it ok to shut those down now or will more evaluations be conducted?

---

You have been evaluated.

---

Your app crashed during the initial evaluation. But the re-run was successful.

---

[@Jivraj](/u/jivraj) sir could you please check for 24f2003130… Today’s morning there was a glitch in my vercel…but I think since it was after evaluation it shouldn’t have impacted that…could you please verify it once

---

[@Saransh\_Saini](/u/saransh_saini) a gentle reminder.

---

You have been successfully evaluated

---

thank you , so I can shut my ngrok session now right

---

Keep it running for the next hour, have to generate your report/

---

[@Saransh\_Saini](/u/saransh_saini)  
Hello sir, can you please say when can we expect results to be published? .

Also we would like to know still how much time or days should our server be running?

Thankyou in advance

---

can you share your email id

---

will I know if its done generating ?

---

[@saransh\_saini](/u/saransh_saini) [@carlton](/u/carlton) Can we kindly expect the result for Project 2 today?

---

No, but we’ll release the first batch soon.

---

Hello [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) Could you please share an update on the expected results for P2? Also, could you confirm whether my evaluation has been completed?  
Additionally, when would it be safe to stop the VM, as it is consuming a significant amount of credits?  
Looking forward to your response.  
Thanks and Regards.

---

[@Saransh\_Saini](/u/saransh_saini)  
is my evaluated yet? lemme know due to credit on azure need to check them also.

---

Hello,

I wanted to provide an update regarding the issue I faced while I was in Jammu. During my stay, my laptop was on, but I encountered an error that caused my endpoint to crash. It seemed that Cloudflared mentioned needing an update, which I believe contributed to the problem.

Now that I’m back in Delhi, I’m connected to the internet, and I’m happy to report that my endpoint is working again.

see this image I have designed my endpoint to monitor with discord webhook  
image description: The image shows a dark-themed interface with a list of requests and queries, a search option for IMDb, and an alert indicating that the API is down.
image text:
\* Total requests: 39
\* IP addresses:
\* 43.230.106.157: 39 requests
\* Recent queries:
\* InfoCore Solutions is a technology consulting firm that maintains an extensive internal knowledge ba...
\* Develop a FastAPI application that:
Exposes a GET endpoint /execute?q=... where the query parameter...
\* Prompt to Yes
\* ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages...
\* Source: Utilize IMDb's advanced web search at https://www.imdb.com/search/title/ to access movie dat...
IMDb
Advanced search
IMDb
ALERT: API Status - 2025-04-07 13:01:32
The API at app.algsoch.tech is currently DOWN or experiencing issues.
API is DOWN
Status: DOWN
Last checked: 2025-04-07 13:01:32

---

Its done [@parthivn28](/u/parthivn28)

---

thank you for the swift response

---

Hey [@Saransh\_Saini](/u/saransh_saini) , can you please confirm if my report was created or not so that I can turn off the vm on azure if it has been done already.

Thank you again!

---

Hi [@Saransh\_Saini](/u/saransh_saini)  
Hope you’re doing well.  
If the evaluation process has been completed, kindly let us know so that we can stop the Azure Web App service.  
My roll number is: **21f3001076**.

Thank you!  
Best regards,  
Lakshay

---

[@Saransh\_Saini](/u/saransh_saini)  
Hello sir, my mail id is 23f3000975@ds.study.iitm.ac.in

If possible I would like to know my mark.

Thank you

---

[@Saransh\_Saini](/u/saransh_saini)  
Could you let me know if my evaluation is complete? Would like to shut down my vm.

---

Yes, [@21f2000709](/u/21f2000709) Your entire evaluation has been completed, along with your report generation. You may shutdown your VM.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/harish.s/48/67995_2.png) HARISH.S:

> 23f3000975

[@Saransh\_Saini](/u/saransh_saini)  
Sir, is my evaluation and project report generation completed.? can i also close the server?  
my roll no.23f3000975

---

[@Saransh\_Saini](/u/saransh_saini)  
Sir, I saw from the logs on Cloud Run that my project was probably evaluated on 5th April at around 11:51 PM and all the requests made during that time resulted in 3 response status codes: 302, 307 and 405 by no fault of my app, but rather errors in the request itself. I mentioned the exactly correct URL of my app in the form but the evaluation logs show three different types of URL to which request was made. As I mentioned in the form, my url is of the format “https://…/api/” and allows only POST requests.

1. The app was supposed to allow POST requests and I allowed only POST requests, so GET requests even to correct url resulted in 405 response
2. When POST requests were actually made, two wrong urls were used for all the POST requests  
   a. http://…/api/ → resulted in 302 response  
   b. https://…/api → resulted in a 307  
   whereas the url I gave was of the format “https://…/api/”

The logs from Cloud Run  
image description: The image displays a log of network requests, likely from a web application. Each line represents a request with details like timestamp, request type (POST, GET), HTTP status code, response time, and the URL accessed. There are a number of "405 Method Not Allowed" errors, indicating that the server doesn't support the requested method for certain API endpoints. Some requests are being redirected (302 and 307 status codes). The URLs point to a domain like tdsproject2shiva, a possible application or service name.
image text:
2025-04-05 23:51:12.872 INFO: 169.254.169.126:49510 - "POST /api HTTP/1.1" 307 Temporary Redirect
2025-04-05 23:51:12.872 INFO: 169.254.169.126:63834 - "POST /api HTTP/1.1" 307 Temporary Redirect
i 2025-04-05 23:51:12.930 POST 302 0 ms python-reque... http://tdsproject2shiva-962709320549.asia-south1.run.app/api/
i 2025-04-05 23:51:12.932 POST 302 0 ms python-reque... http://tdsproject2shiva-962709320549.asia-south1.run.app/api/
i 2025-04-05 23:51:12.944 POST 302 0 ms python-reque... http://tdsproject2shiva-962709320549.asia-south1.run.app/api/
! 2025-04-05 23:51:12.991 GET 405 140 B 1 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/
2025-04-05 23:51:12.993 INFO: 169.254.169.126:49512 - "GET /api/ HTTP/1.1" 405 Method Not Allowed
! 2025-04-05 23:51:12.997 GET 405 140 B 2 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/
2025-04-05 23:51:12.999 INFO: 169.254.169.126:55644 - "GET /api/ HTTP/1.1" 405 Method Not Allowed
! 2025-04-05 23:51:13.025 GET 405 140 B 1 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/
2025-04-05 23:51:13.027 INFO: 169.254.169.126:49514 - "GET /api/ HTTP/1.1" 405 Method Not Allowed
i 2025-04-05 23:51:13.493 POST 307 140 B 2 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api
2025-04-05 23:51:13.498 INFO: 169.254.169.126:55646 - "POST /api HTTP/1.1" 307 Temporary Redirect
i 2025-04-05 23:51:14.109 POST 307 140 B 2 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api
2025-04-05 23:51:14.112 INFO: 169.254.169.126:55652 - "POST /api HTTP/1.1" 307 Temporary Redirect
i 2025-04-05 23:51:14.209 POST 302 0 ms python-reque... http://tdsproject2shiva-962709320549.asia-south1.run.app/api/
! 2025-04-05 23:51:14.246 GET 405 140 B 1 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/
2025-04-05 23:51:14.248 INFO: 169.254.169.126:19550 - "GET /api/ HTTP/1.1" 405 Method Not Allowed
i 2025-04-05 23:51:14.450 POST 302 0 ms python-reque... http://tdsproject2shiva-962709320549.asia-south1.run.app/api/
! 2025-04-05 23:51:14.497 GET 405 140 B 1 ms python-reque... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/
2025-04-05 23:51:14.500 INFO: 169.254.169.126:49516 - "GET /api/ HTTP/1.1" 405 Method Not Allowed
i 2025-04-06 00:14:41.329 POST 200 156 B 509 ms python-httpx... https://tdsproject2shiva-962709320549.asia-south1.run.app/api/

As you can see from the above logs, all POST requests made to my app have the wrong url, some have only http and some end with “/api” instead of “/api/”, both of which do not match with the correct url I gave in the Google Form (screenshot attached below).

image description: The image displays a form titled "TDS Project 2 - Jan 2025". The form asks for a GitHub repository link and an API endpoint link. The user is instructed to log in with their "iitm.ac.in" or work email ID. It mentions that only one response is allowed and it is possible to correct the answer.
image text: TDS Project 2 - Jan 2025
Please log in with your iitm.ac.in or your work email ID.
You can submit only one response.
You can correct your response after you submit.
Your email (22f3000819@ds.study.iitm.ac.in) was recorded when you submitted this form.
What is the link to your GitHub repository which has the code for Project 2? \*
It should look like https://github.com/user-name/repository-name
https://github.com/RichPerspective007/tds\_p2
What is the link to your API endpoint? \*
Make sure we can send a POST request to this exact URL
https://tdsproject2shiva-962709320549.asia-south1.run.app/api/

I request you to re-evaluate my project 2 with the correct url exactly as I had submitted in the Google Form.

Thank you.  
Regards,  
Shivaditya

---

[@Saransh\_Saini](/u/saransh_saini)

One more thing—could you please clarify whether the evaluation process includes both types of responses mentioned in post number 202?

---

You have been evaluated.

---

You have been evaluated, successfully.

---

[@Saransh\_Saini](/u/saransh_saini) Have I been evaluated? My roll number is 21f2001573.

---

[@Saransh\_Saini](/u/saransh_saini) Is my project evaluation done yet? my Roll no.: 24f1002555

---

[@Saransh\_Saini](/u/saransh_saini)

Hi sir, when will be project 2 results released for all?

Thanks,  
Sujay D

---

My IITM student dashboard on the portal shows absent for course project (COURSE PROJET - Absent). Is this referring to project 1 or 2? Coz i missed Project 1 but submitted Project 2 successfully. Also the logs show that the evaluation was performed on the submitted enpoint. So should I be concerned about the dashboard showing ‘Absent’ or will it be updated in a few days?

---

Hello [@Saransh\_Saini](/u/saransh_saini) can you please confirm if my report was created or not so that I can turn off the vm on azure if it has been done already.

---

[@Saransh\_Saini](/u/saransh_saini) when can expect result today or tomorrow or later?

---

Probably in 2 days time assuming no problems or other unforseen errors occur.

---

[@Carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini), it would be helpful if you could specify a date — a clear deadline

---

We cant specify a clear deadline. If we could we would. At the present time there are roughly 100+ evals left in the pipeline. And we retry them to give students the best chance of getting a score. Sometimes we accomodate some unusual situations that we have been made aware of but all of those interrupt our workflows and so it takes time. Which makes this process a little unpredictable.

This is the first term where we have had students deploy solutions that require significant compute resources on our end to evaluate. So there was always going to be hickups. But i think that we have delivered an equally enriching learning experience as a result which is enough to land you an actual job. (Might not be so enriching on your CGPA admittedly, but thats a small price to pay for invaluable skills you hopefully have gained)

---

[@carlton](/u/carlton) Could you clarify if some kind of a normalisation will be done this time as well? Or if some bonus marks will be given? Last time, it didn’t help as much because the highest marks were 16.

---

Normalisation is only helpful when no one scores the top marks.

---

It will be similar in case the top cumulative score after the ET is, say, 90… [@carlton](/u/carlton)

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) Please can you tell me whether my evaluation is done or not. For roll no: 22f2000946

If yes, I will stop my VM. I am running low on credits.

---

We will complete evaluation in two days. We will also send out a mail today for those whose evaluation has been completed

---

sir i am unable to work with other things on my laptop  
image description: The image shows a web browser error message on a white background, with the text "Aw, Snap!" above a message describing the problem and the "Learn more" link.
image text: Aw, Snap!
Something went wrong while displaying this webpage.
Error code: Out of Memory
Learn more
  
because laptop giving error because my system ran out of memory and because api working continuously more than 1 week

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
This is a gentle reminder to kindly send the confirmation email indicating for whom the evaluation of Project 2 has been completed.

Additionally, I would like to confirm whether we can shut down our Azure VM after this, or if we should keep it running in case there is an additional evaluation. In one of the sessions, you had mentioned the possibility of offering alternate questions as a second chance for students, evaluated at half the original marking scheme (i.e., 2 marks per question).

---

image description: The image shows a user interface with log entries and function invocation details. On the left, there's a section displaying logs with timestamps and descriptions. The logs indicate actions such as sending an email and triggering a workflow. The logs section shows "3 Total". On the right, it provides details about a "Function Invocation," including route, location, runtime (Python 3.12), execution duration, and memory usage. The function resulted in a "Gateway Timeout 504" error. Deployment information includes deployment ID and environment.
image text: APR 09 00:11:06.94 POST 504 tds-ga-proj2.ve... f /api/ 3 X Failed to tr APR 09 00:11:00.79 POST 307 tds-ga-proj2.ve... f /api 127.0.0.1 - [08 Firewall Allowed f Function Invocation Gateway Timeout 504 Route /main.py Location Washington, D.C., USA (iad1) Runtime Python 3.12 Execution Duration / Maximum 10s / 10s Memory Used / Maximum 214 MB / 1024 MB Response finished Deployment Information Deployment ID dpl\_EFXAUNYSadoksLSimpbQCo5jo... Environment production Logs 3 Total f Vercel Function 00:11:07.064 Email ID 23f1000598@ds.study.iitm.ac.in 00:11:07.112 Email updated in index.html 00:11:07.149 X Failed to trigger workflow: 401 - {"message": "Bad credentials", "docume ntation\_url":"https://docs.github.com/rest", "status":"401"} No more logs to show within selected timeline
  
Hello [@Saransh\_Saini](/u/saransh_saini) , [@Jivraj](/u/jivraj)  
Sir When i test it locally , my LLM is working fine , even running the app , it gave result in 2 sec ,  
I dont know what happened in the logs , it was showing some runtime error ,  
As i am using free plan of vercel , so it allow for 10 sec only ,  
I think any heavy file being run , so it just take some more time , more than 10 sec , but inbuild feature of free plan allow to run only 10 sec … and thats why this happened , i guess

does it means , my LLM failed ??  
Can you please try some other question , it will work , or even for heavy question it work ,  
You can check its working from interface too  
Please check once !!

---

We will be sending out emails to both sets. Ones who have to keep it on and ones who can shut it down. If you have not received a shutdown notice, assume that you have to keep it on. I apologise for the late reply, we ran into some unforeseen problems, hence the delay.

Thank you for your patience,  
Kind regards

---

[@carlton](/u/carlton), [@Jivraj](/u/jivraj), [@Saransh\_Saini](/u/saransh_saini)  
Respected Sir,  
I received an email stating we have to turn on URL endpoint again. I am using free version of NGROK if I want to re-start my application then my NGROK URL will change and the forms are closed. What Should I do ? this is urgent.

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) sir today I received this email  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a text-based announcement. It is addressed to "Dear Learner" and contains several paragraphs. The main points are: a request not to ignore the announcement, checks being done on server endpoints for "TDS Project 2," a request to turn something back on, an apology for inconvenience, and a promise of further email updates. It also mentions awareness of users using credits on platforms like Azure. The text is written in a formal tone and seems to be an official communication.
\*\*image text:\*\*
Dear Learner,
Please do not ignore this important announcement. We are still doing some checks on the server endpoints for your TDS Project 2.
If you have turned it off because you were told that evaluations were complete, please turn them back on.
We apologise for the inconvenience caused. We aim to complete the evaluations as soon as possible and are cognizant that some of you are using up credits on azure and other platforms to keep them up and running.
We will inform you in subsequent emails when your evaluation is complete so that you do not have to keep them up and running longer than necessary.
-
Kind regards
  
I have did not turned it off it is just that the first request take time of 50 to 60 sec as you can see in the image.  
image description: A dark mode screenshot of a web application interface, likely for API testing or development. The interface is divided into several sections, including request settings, query parameters, headers, body, and test results. The "POST" method is selected. The body section is displaying a JSON response with the key "answer" and the value "140". The status of the API call is displayed at the bottom with "200 OK" and other data.
image text: Untitled-1 Untitled Request https://tds-pro... POST Params Authorization Headers (9) Body Pre-request Script Tests Settings Query Params Key Value Key Value Body Cookies Headers (12) Test Results Pretty Raw Preview JSON 1 2 "answer": "140" 3 Save No Environment Send Code Cookie Status: 200 OK Time: 53.13 s Size: 361 B  
and it also take same time in linux  
image description: The image shows a terminal output with a command being executed. It involves a `curl` command to make a POST request to an API with a multipart/form-data content type. The command includes a formula for Google Sheets. The output shows the response from the API, including the answer "140".
image text: sahil@DESKTOP-N2T75TO:~$ curl -X POST "/api/" -H "Content-Type: multipart/form-data" -F "question=Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel) =SUM(ARRAY\_CONSTRAIN(SEQUENCE (100, 100, 5, 2), 1, 10)) What is the result?"
{"answer":"140"}sahil@DESKTOP-N2T75TO:~$
sahil@DESKTOP-N2T75TO:~$
  
**Please allow some time for my server hosted on Render to initialize, as it may take a moment to become fully active.**  
Thank you for your patience and understanding.

---

Just reply to the email that I have sent to you regarding your query. We will make exceptions for students facing this issue of having a changed end point due to the way ngrok works.

Kind regards

---

## Humble Request to Update API Request Link

Dear Team,

I hope this message finds you well. I’m reaching out to kindly ask if it would be possible to update my API request link for project 2 in TDS. I realized that I mistakenly used the wrong endpoint in my earlier request.

**Previous API Request Link:**

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/a/aae809b0bbff330e7cec1d2f6ae9eb8551d928c2.png)
[project2llm-production.up.railway.app](https://project2llm-production.up.railway.app/docs)

### [IITM Assignment API - Swagger UI](https://project2llm-production.up.railway.app/docs)

**Correct API Request Link:**  
<https://project2llm-production.up.railway.app/api/>  
<https://project2llm-production.up.railway.app/api/>

Would it be possible for you to allow me to make this change, or kindly update the link on my behalf? I sincerely apologize for the confusion, and I’d be truly grateful for your support and understanding.

Thank you so much for your time and consideration.

Warm regards,  
Pratyush Pulak Nishhank

---

Thank you for considering it also one question sir, how long do I have to keep it running ?

---

But Sir please give some bonus , As in earlier terms , everyone got S grade in TDS , without doing anything , and from this term the difficulty level increased rapidly , just like e^x  
Although I know that our LLM doesnt worked fully(100%) , but atleast they worked 50-60%  
We have learned so many things and try to implement in it too,…

Atleast give some bonus for our hardwork , and participating in both LLM project , so even we dont get S grade , but will get B , A , grade … and our CGPA doesn’t decrease much  
because projects hold the major chunk in grading

[@carlton](/u/carlton)

---

Agree with this sentiment.

Hope there are bonus points for participation in discourse as well.

---

[@carlton](/u/carlton)  
i submitted incorrect api request link

my correct api link:  
<http://127.0.0.1:8000/api/post_ask_question>

is it possible to change some how…

---

suppose i have resolved the hosting issue that the link i provided had now , will u still evaluate as i fixed the issue in response to the email i received on 8th april?

---

Sir, [@Jivraj](/u/jivraj) can I know how long do I need to keep the server running ?  
Roll No. 22f200559

---

It seems you have provided a local address endpoint, which means it will only work on your computer. If I run it on my computer, it will redirect to my port 8000 if it is running.

---

till your endpoint has evaluated

---

[@carlton](/u/carlton),[@Saransh\_Saini](/u/saransh_saini)  
sir my roll number is 23f2004462

Due to an unexpected power outage, my PC shut down abruptly, causing my local server and ngrok tunnel to terminate. When the system rebooted, I restarted the server and ngrok, which generated a new API endpoint as ngrok URLs are temporary and change with every session. The previous endpoint is no longer accessible, and the new one now serves as the API endpoint. I understand the need for a consistent URL and will explore solutions like reserving a domain through ngrok’s paid plan to prevent such issues in the future. Apologies for any inconvenience caused, and thank you for understanding.

New project 2 url:- <https://96c8-2401-4900-6290-6a14-b433-2faa-a056-a6e5.ngrok-free.app/api/>

---

[@carlton](/u/carlton) ,[@Saransh\_Saini](/u/saransh_saini)  
same goes for me sir my pc also shut down  
sir my roll number is 23f2005141  
project 2 url <https://b2a4-2401-4900-6290-6a14-b433-2faa-a056-a6e5.ngrok-free.app/api/>

---

my project is running and working in vscode but when checked in git its not like  
post—401 unauthorized  
i tried making changes today but same issue…  
i think its the token but i tried pasting my token in postman…none worked  
i used api token, proxy token and even github barrier token…that didnt work either  
can anyon explain why

when i ran it local yep its giving me answers

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) Respected sir, by mistake I have submitted the endpoint as : <https://tds-project-2-peach.vercel.app/> while the corrected api which is deployed on vercel for direct requests is : <https://tds-project-2-peach.vercel.app/api/>  
The link provided is also working one but this link has the frontend part not the url endpoint.  
kindly evaluate me on the basis of the updated link : <https://tds-project-2-peach.vercel.app/api/>

Reg. No - 23f1001995

---

I think my endpoint has been evaluated, given how POST requests stopped after 3pm. Do I still have to keep it on perhaps through overnight, my laptop now has started to heat up. [@Jivraj](/u/jivraj) sir any updates whether my evaluation is completed or not ?.

---

I kindly request, if you could please consider reevaluating my assignment. This small error was not reflective of the overall functionality, and I’m worried that the resulting grade might significantly impact my performance and cause me failing in the course.

---

Here's a description of the image:
The image is a screenshot of an email. The subject of the email is "[TDS Jan 25] Project 2 Announcement". The sender is "22t1 se2002". The body of the email informs the recipient that their evaluations on Project 2 have been completed and they may switch off their server.
image text:
[TDS Jan 25] Project 2 Announcement Inbox x
22t1 se2002
S
to bcc: me
2:28 AM (18 hours ago)
:
Dear Learner,
We have successfully completed your evaluations on Project 2 endpoints. You may switch off your server now. You will receive a score for your Project 2 as soon as all other
evaluations are completed.
Thanks
Kind regards,
TDS Team
  
I have received this message do this message suggest that my evaluation is successfully completed coz I forgot to add /api at the end of my vercel url . Or is it like the submission had ran but ultimately produced my score 0. If this is the case I request you to reevaluate my submission.  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

Respected Course Team,

Harsh this side from NIT Allahabad, I am writing to inform you that I received a notification  
Here's a description of the image:
The image is a screenshot of an email. The subject line reads "[TDS Jan 25] Important announcement regarding Project 2". The email is from "22t1 se2002 <se2002@study.iitm.ac.in>" to "me". The email content is an announcement to learners about TDS Project 2, mentioning server checks, evaluation completion, and platform credits. There are options to reply and forward the email and unsubscribe.
image text:
[TDS Jan 25] Important announcement regarding Project 2
22t1 se2002 <se2002@study.iitm.ac.in>
to me ▾
Dear Learner,
Please do not ignore this important announcement. We are still doing some checks on the server endpoints for your TDS Project 2.
If you have turned it off because you were told that evaluations were complete, please turn them back on.
2:26 AM (20 hours ago)☆
We apologise for the inconvenience caused. We aim to complete the evaluations as soon as possible and are cognizant that some of you are using up credits on azure and other
platforms to keep them up and running.
We will inform you in subsequent emails when your evaluation is complete so that you do not have to keep them up and running longer than necessary.
Kind regards,
TDS Team
Note: Do NOT reply to this email. It is only meant for official announcements and messages. If you need any further assistance please contact the course team via Discourse.
Unsubscribe
← Reply Forward
  
regarding an issue with my submission.

I believe the issue may have occurred because I had mistakenly provided an incorrect API endpoint in my earlier submission. However, my server is still actively running on Vercel  
<https://tds-project-2-peach.vercel.app>  
and the correct API endpoint is:

correct api : <https://tds-project-2-peach.vercel.app/api/>

Everything else in the project is functioning as expected. I kindly request you to re-evaluate my submission using the correct endpoint as i am currently in my 3rd year of BTech Chemical engineering at NIT Allahabad and my placement session is coming so i don’t want to get failed in this course due to such a small mistake.

Thank you for your understanding and support.

---

Hello sir  
can you check and say if my server has been evaluated or not ?  
My roll no : 23f3003871

My endpoint is working smoothly, I am showing it to you in this photo.  
Here's a brief description of the image:
The image shows a computer screen with code, possibly in a Jupyter Notebook environment. The code appears to be related to data processing, likely involving CSV and text files with different encodings.
image text:
```
C
colab.research.google.com/drive/1lhxaakHW1Kk-s8tB1XsQurYhbP41aEJB#scrollTo=ekqk-hqAAJIN
nnect to the reCAPTCHA service. Please check your internet connection and reload to get a reCAPTCHA challenge.
Untitled79.ipynb ✩
File Edit View Insert Runtime Tools Help
ands + Code + Text
url = "https://tds-project-2-ruby.vercel.app/api/"
files = [
'file': open(r'q-unicode-data.zip', 'rb')
data = {
'question': """Download and process the files in q-unicode-data.zip which contains three files with different encodings:
data1.csv: CSV file encoded in CP-1252
data2.csv: CSV file encoded in UTF-8
data3.txt: Tab-separated file encoded in UTF-16
Each file has 2 columns: symbol and value. Sum up all the values where the symbol matches < OR Š OR > across all three files.
What is the sum of all values associated with these symbols?"""
}
response = requests.post(url, files=files, data=data)
print(response.status\_code)
print(response.text)
200
{"answer":39961}
Type here to search
```

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
urgent !!  
hello sir my roll no.23f3000975  
My laptop has been on for nearly twelve days. Due to some reasons my laptop restarted automatically and terminated the ngrok server. So i restarted my ngrok server and here i attach its url along with its endpoint “ask”.

<https://e95b-2405-201-e04b-d085-9cf5-4f92-fe5a-309e.ngrok-free.app/ask>

kindly reply soon SIr…

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) sir, please reply

---

[@Saransh\_Saini](/u/saransh_saini)  
Hello sir, could you please confirm whether I have been evaluated or not?  
Roll\_No.: 23F3004186  
Here's a description of the image:
The image is a screenshot of an email. The subject of the email is "TDS P2 Endpoint." It is from Vishnu Kumar Jha with the email address <23f3004186@ds.study.iitm.ac.in>. The email is addressed to "Dear Saransh," and it contains a URL for a P2 API endpoint. The email also includes the sender's roll number (23F3004186) and ends with a thank you and the sender's name. There's also an image of a car in the top left corner.
image text: TDS P2 Endpoint
23F3004186 VISHNU KUMAR JHA <23f3004186@ds.study.iitm.ac.in>
to 22f1001123
Dear Saransh,
I hope this message finds you well.
Please find below the complete public endpoint for my P2 API:
https://vishnu-dns.centralindia.cloudapp.azure.com/api
Please let me know if there are any further issues.
Roll No: 23F3004186
Thank you,
Vishnu Kumar Jha

---

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)  
sir,  
I kept my laptop on overnight, but in the morning I see my vs-code application and ngrok server along with google chrome was closed on it’s own. I am confused, do I have to run again ? or my enpoint has been evaluated.

---

i also got this same problem.

---

Do all of us have to give the latest project link or only those whose links have actually changed. [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton) [@Jivraj](/u/jivraj).

Basically should we resubmit the link using the form sent today if our link has not changed?

PS: Maybe send a mail to everyone to update the access of their GA7 links to viewer for everyone at IIT Madras.

---

Just submit whatever is the latest working link. You do not have to submit a new form if you have received an email that said your evaluation was completed.

---

We already sent an email asking people to update their ga7 permissions

---

[@Saransh\_Saini](/u/saransh_saini)  
Could you let me know if my evaluation is complete?

---

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) [@jkmadathil](/u/jkmadathil)

Dear Sirs,

Most of us have hosted our projects in Azure and this is costing us real money .. We have just gotten to a stage where if you could just please let us know if our endpoints have been evaluated and there is some score we will happily take it down.  
Kindly bear in mind the there is a financial component ( some of us have free accounts ) involved here and I urge and request you to kindly expedite the evaluation process so that we decrease the financial burden placed upon us by this exercise…

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Sir, please confirm me whether I have been evaluated or not. Because my azure balance is reducing day by day.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
I just got the mail stating that my evaluation is complete and I can turn off my server.  
However the Cloud Run logs show that all POST requests were made to the wrong end point.

The exact url I gave ends with “/api/” but every POST request was either made to “/api” which resulted in a 307 response or with “http” instead of “https” which resulted in a 302 response. Only the get requests were made to the correct endpoint but since the app was supposed to allow POST requests only, making GET requests just resulted in 405.  
Here's a brief description of the image:
The image is a screenshot of a Google Cloud Logs page for a project named "tdsproject2shiva". It displays a log of various events, including HTTP requests, server processes, and application startup details. The logs are filtered, with a message indicating "No newer entries found matching current filter.".
image text:
```text
12:16
Vo) 5G
LTE1
LTE2
Vo)) 82%
e.cloud.google.com +
19
Google Cloud
WorkshopProj
Search (/) for resources, docs, products, a... Q Search
Cloud Run
← Service details
Set up Continuous Deployment
tdsproject2shiva
Region: asia-south1
URL: https://tdsproject2shiva-962709320549.asia-south1.run.app
Metrics
SLOS Logs
Revisions Triggers
Networking
Security YAML
Learn
①
Sca
Severity
Logs Default
Filter Search all fields and values
Severity Timestamp
Summary
>i
2025-04-08 01:17:36.856 IST
POST 200 171 B 32 ms python-httpx/0.28.1
https://tdsproject2shiva-962709320549.asia-south1.r...
> \*
2025-04-08 01:17:36.894 IST
processing question
> \*
2025-04-08 01:17:36.894 IST
trying to load
> \*
2025-04-08 01:17:36.894 IST
loaded embeddings
> \*
2025-04-08 01:17:36.894 IST
INFO: 169.254.169.126:49552 "POST /api/ HTTP/1.1" 200 OK
>i
2025-04-08 01:20:49.720 IST
POST 307 140 B 2 ms python-httpx/0.28.1
https://tdsproject2shiva-962709320549.asia-south1.ru....
>
\*
2025-04-08 01:20:49.728 IST
INFO: 169.254.169.126:45462 "POST /api HTTP/1.1" 307 Temporary Redirect
>
2025-04-09 16:08:07.599 IST
INFO: Started server process [2]
>
2025-04-09 16:08:07.599 IST
INFO: Waiting for application startup.
>
2025-04-09 16:08:07.599 IST
INFO: Application startup complete.
> \*
2025-04-09 16:08:07.600 IST
INFO: Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
>i
2025-04-09 16:08:07.600 IST
Default STARTUP TCP probe succeeded after 1 attempt for container "tdsproject2shiva-1" on port 80....
>i
2025-04-11 01:31:17.558 IST
POST 307 140 B 2 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1.....
!<
2025-04-11 01:31:17.558 IST
POST 307 140 B 1 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1....
>i
2025-04-11 01:31:17.559 IST
POST 307 140 B 1 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1....
> \*
2025-04-11 01:31:17.565 IST
Some imports
> \*
2025-04-11 01:31:17.565 IST
all imports
> \*
2025-04-11 01:31:17.565 IST
app created
>
2025-04-11 01:31:17.565 IST
cors added
>
2025-04-11 01:31:17.565 IST
>
\*
2025-04-11 01:31:17.565 IST
INFO: 169.254.169.126:10718 "POST /api HTTP/1.1" 307 Temporary Redirect
INFO: 169.254.169.126:6804 "POST /api HTTP/1.1" 307 Temporary Redirect
>
\*
2025-04-11 01:31:17.566 IST
>i
2025-04-11 01:31:17.641 IST
INFO: 169.254.169.126:10732 "POST /api HTTP/1.1" 307 Temporary Redirect
POST 302 0 B0 ms python-requests/2.32.3
http://tdsproject2shiva-962709320549.asia-south1.ru...
> 2025-04-11 01:31:17.642 IST
POST 302 0 B0 ms python-requests/2.32.3
http://tdsproject2shiva-962709320549.asia-south1.ru....
>i
2025-04-11 01:31:17.642 IST
POST 302 0 B0 ms python-requests/2.32.3
>!
>!
2025-04-11 01:31:17.700 IST GET 405 140 B 2 ms python-requests/2.32.3
2025-04-11 01:31:17.701 IST GET 405 140 B 1 ms python-requests/2.32.3
http://tdsproject2shiva-962709320549.asia-south1.ru....
https://tdsproject2shiva-962709320549.asia-south1...
https://tdsproject2shiva-962709320549.asia-south1...
> \*
2025-04-11 01:31:17.703 IST
INFO: 169.254.169.126:30602
"GET /api/ HTTP/1.1" 405 Method Not Allowed
>
2025-04-11 01:31:17.703 IST
> ! 2025-04-11 01:31:17.725 IST
INFO: 169.254.169.126:6816 "GET /api/ HTTP/1.1" 405 Method Not Allowed
GET 405 140 B 1 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1...
> \*
2025-04-11 01:31:17.727 IST
INFO: 169.254.169.126:6828 "GET /api/ HTTP/1.1" 405 Method Not Allowed
>i
2025-04-11 01:31:17.950 IST
POST 307 140 B 2 ms python-requests/2.32.3 https://tdsproject2shiva-962709320549.asia-south1.....
> \*
2025-04-11 01:31:17.955 IST
INFO: 169.254.169.126:6844 "POST /api HTTP/1.1" 307 Temporary Redirect
>i
2025-04-11 01:31:18.291 IST
POST 302 0 B0 ms python-requests/2.32.3
http://tdsproject2shiva-962709320549.asia-south1.ru...
>
2025-04-11 01:31:18.333 IST
GET 405 140 B 1 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1...
>
2025-04-11 01:31:18.335 IST
INFO: 169.254.169.126:6856
"GET /api/ HTTP/1.1" 405 Method Not Allowed
>i
2025-04-11 01:31:18.406 IST
POST 307 140 B 1 ms python-requests/2.32.3 https://tdsproject2shiva-962709320549.asia-south1....
> \*
2025-04-11 01:31:18.409 IST
INFO: 169.254.169.126:10738 "POST /api HTTP/1.1" 307 Temporary Redirect
>i
2025-04-11 01:31:18.454 IST
POST 302 0 B0 ms python-requests/2.32.3
http://tdsproject2shiva-962709320549.asia-south1.ru....
> ! 2025-04-11 01:31:18.491 IST
GET 405 140 B 1 ms python-requests/2.32.3
https://tdsproject2shiva-962709320549.asia-south1...
> \*
2025-04-11 01:31:18.494 IST INFO: 169.254.169.126:6868 "GET /api/ HTTP/1.1" 405 Method Not Allowed
No newer entries found matching current filter.
<
```

I request you to use the exact url I gave in the gform and make POST requests to it to re-evaluate me. I gave the exact url as asked in the form.  
image description: The image shows an email with a black background. The email content includes a link to a GitHub repository and a question about an API endpoint. There are also options to reply, reply all, or forward the email. The status bar at the top shows the time, network, and battery information.
image text:
12:23
https://github.com/
RichPerspective007/tds\_p2
What is the link to your API
endpoint? \*
Make sure we can send a POST
request to this exact URL
https://tdsproject2shiva-
962709320549.asia-south1.run.
app/api/
Create your own Google Form
Does this form look suspicious? Report
Reply
Reply all
Forward
No add-ons available for this email
99+
8

Thanks  
Regards,  
Shivaditya

---

[@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)  
Hello sir,  
I apologize for bothering you again.  
About 30 minutes ago, I received an email stating that project 2 has been evaluated. However, when I checked my IP stats, I found there is no special API access. You can verify this. I want to understand whether this is just a wrong email I received or if there is an issue with your system’s evaluation. Please clarify this doubt, as I am unable to focus on my final term exam.  
i closed my local machine too I spent one month on this project please consider my problem

image description: The image shows a command-line output from a Python script. The script seems to be analyzing network traffic. The output displays 5 unique IP addresses and how many times they accessed the "/api/" endpoint, along with a total count and the number of unique IPs accessing the endpoint.
image text:
```
PS E:\data science tool\main\grok> python uniu.py
Found 5 unique IP addresses:
IP: 43.230.106.157
Accessed endpoints: /api/
API endpoint access count: 93
IP: 52.234.41.123
Accessed endpoints: /api/
API endpoint access count: 48
IP: 20.42.17.59
Accessed endpoints: /api/
API endpoint access count: 39
IP: 20.57.44.194
Accessed endpoints: /api/
API endpoint access count: 43
IP: 172.183.175.198
Accessed endpoints: /api/
API endpoint access count: 39
Total /api/ endpoint calls: 262
IPs accessing /api/ endpoint: 5
```

---

I checked my Vercel logs and saw that the requests were sent to the /api endpoint instead of the /api/ endpoint that I specifically gave in the google forms.

To confirm this I also sent a request to /api and /api/ enpoints and the /api gave a 404 error while /api/ gave a 200 message.

Please look into this  
[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

I have mistakenly filled `tds-project2-final-omega.vercel.app` instead of `https://tds-project2-final-omega.vercel.app/api/` in gform, i humbly request you to pls accept this .  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
i have filled gform with 23f1002838@ds.study.iitm.ac.in  
i have filled gform for end point edit i hope this will work

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000237/48/66999_2.png) 23f2000237:

> I checked my Vercel logs and saw that the requests were sent to the /api endpoint i

where did you check it?

Also, on <https://www.vercel-status.com/> this is showing  
**Update** - npm have released a status page incident, and users can monitor further updates here: [https://status.npmjs.org](https://status.npmjs.org/)  
Apr 11, 2025 - 03:02 UTC

**Monitoring** - We have observed authentication issues to private registries using npm access tokens. Affected users may see 4xx errors when installing private packages. Manually regenerating tokens appears to resolve this issue. At this time, there is no official statement from npm or GitHub regarding the root cause.  
Apr 11, 2025 - 02:37 UTC

---

Yes I also got the same email, but when I checked my vercel dashboard I found no such api access. Kindly verify this [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

Will we receive scores by today?

---

Today I got my TDS Project-2 Score and it is showing as absent although I submitted my TDS project 2 , also deployed the app successfully and also filled the g-form

Here’s my deployed application on-render link with the attached screenshot of my TDS Dashboard:  
image description : The image shows the course marks of a student for the course "Tools in Data Science". The details of the marks for Assignments, Programming Quiz, and Course Projects are provided. The student is "Allowed to take End Term Exam".
image text: Tools in Data Science
NEW COURSE
Week 1 Assignment - 92.50
Week 2 Assignment - 90.00
Week 3 Assignment - 0.00
Week 4 Assignment - 100.00
Week 5 Assignment - 100.00
Week 6 Assignment - Absent
PROGRAMMING QUIZ 1 - 90.00
COURSE PROJECT - 5.00
Course Project Score 2 - Absent
Allowed to take End Term Exam?
Yes
Go to Course page >

aap link : <https://tds-project2-21f3000591.onrender.com>

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Dear Sir,  
In my course dashboard, it shows project 2 status as absent, but i have already submitted the repo and api points well before deadline in the given forum. Still my vercel server is running and api is resolving as expected. Please look into this matter, because I already had issue in my project 1 and lost marks in that. Expecting a positive response from your end.

ID: 21f2000304

---

[@carlton](/u/carlton) [@jivraj](/u/jivraj) [@saransh\_Saini](/u/saransh_saini)  
hello sir, in my portal the project 2 score is showing absent even after submitting tds project 2 successfully in google form and keeping the server running all the time, please can you recheck it again, deployment link:<https://tds-p2-gun1.onrender.com>

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
Hello Sir, my project 2 score is showing as 0. I had got email saying please update endpoint because earlier endpoint was having problems. I had sent <https://c7f6-150-107-43-5.ngrok-free.app/api/> as updated endpoint in google form on April 10th. Same day I had got around 9 requests on that endpoint around 4:56 PM. They were 200 OK requests on /api/ and 4 requests were 307 redirect on /api. I presume they were from TDS team. Next day got email to shut off endpoint. I had tested endpoint locally and on ngrok. Both were fine. Was the updated endpoint in the google form evaluated? Was there some problem with the updated endpoint?

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

Please look into this, my portal is showing zero marks

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
My portal is showing 0 even no github repo is made so are evalaution even done???  
Pls tell

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
On my portal it’s showing that Course Project Score 2 - Absent  
but I submitted and fill the form also deployed the app successfully.

---

Namaste Sir. The projects have been quite challenging, and I have applied my knowledge to the best of my ability. I’ve submitted the project but it’s showing 0 in the portal. Bonus marks for creating APIs and so in the projects would be greatly appreciated. I am planning to start my degree in the upcoming term, and this is the last subject I am completing at this level. So, I kindly request your assistance, sir.

---

Hello Sir,  
For me as well Project 2 scores are showing 0.I have spent alot of time and effort in this project. Please look into it.

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) sir ,  
I am writing to kindly request a re-evaluation of my Project 2 submission. As I had previously mentioned, the Render deployment link I submitted may take approximately **50 to 60 seconds** to activate upon the first load. This behavior is typical of free-tier deployments on Render, and I assure you that the application functions correctly in both **Podman** and **Linux** environments.

Upon reviewing my Render logs, I could not find any indication that the project was accessed or evaluated during the expected activation time. To ensure smooth accessibility, I have also deployed the same GitHub repository on **Railway** and submitted that link as well.

If possible, I kindly request either of the following:

1. Re-evaluation using the **Railway link** I provided, or
2. Re-evaluation using the **Render link**, with allowance for the 50–60 second activation time.

Your consideration and understanding in this matter would be greatly appreciated. Please let me know if any further clarification or information is needed.

Thank you for your support and guidance.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) I knew that this affected my project 2 score and that’s why I made that post(the one to which I’m replying in this message). Please look into this. My api is working and still on and will be on till 18th April when my credits will run out. Please re-evaluate my project 2 with the exact url I gave in the form. My project 2 was evaluated on the wrong url and this led to a zero in the project 2 score.

---

Hi sir [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

I need your immediate attention regarding my project-2, as I received zero marks, but my server is running completely fine. Below are the key points that I need you to look into:

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Server is running and reachable. and Giving Correct Answers**  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **GET and POST requests tested via Postman and VS Code**, both return **200 OK**.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Tested on my laptop and by 10+ other people** – all received correct results.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **No issues seen in logs or deployment** – everything was set up properly.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Others in my group got full marks** – we worked on the same project.

![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **I have no idea what went wrong during the evaluation.**  
![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **I’ve spent weeks working on this project**, including sleepless nights.  
![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **This is my last term** – if I fail, I will have to repeat the entire diploma.

Please recheck my project thoroughly. Here are the important links for you to verify:

* **API Documentation:** [FastAPI - Swagger UI](http://shashitdsproject2.centralindia.cloudapp.azure.com/docs)
* **API Endpoint:** <http://shashitdsproject2.centralindia.cloudapp.azure.com/api>

I truly believe that my server is functioning as expected, and I just need a re-evaluation to confirm that.

I’ve put in a lot of effort into this, and I sincerely request that you review it again.

as you can see my vm is working fine here  
image description: The image is a screenshot of a serial console within the Microsoft Azure portal, displaying output from a virtual machine named "shashitdsproject2". The console shows commands executed in a terminal, along with their responses, including attempts to manage a service called "uvicorn." The visible commands relate to starting, enabling, and restarting services, which are related to nginx and uvicorn. There's also a python script.
image text:
async def process\_request(
question: str = Form(...),
file: Optional [UploadFile] = File(None)
):
try:
#data = question
#print (data)
shashi@shashitdsproject2:~/GASolver$ sudo systemctl restart nginx
shashi@shashitdsproject2:~/GASolver$ ^[[200~sudo systemctl restart~
sudo: command not found
shashi@shashitdsproject2:~/GASolver$ sudo systemctl daemon-reload && sudo systemctl start uvicorn && sudo systemctl enable uvicorn && sudo sy
stemctl status uvicornt2:~/GASolver$ sudo systemctl daemon-reload && sudo systemctl start uvicorn && sudo systemctl enable uvicorn && sudo sy
• uvicorn.service - Uvicorn FastAPI Server
Loaded: loaded (/etc/systemd/system/uvicorn.service; enabled; preset: enab
Active: active (running) since Mon 2025-04-14 09:35:04 UTC; 33s ago
Main PID: 1782 (python)
Tasks: 2 (limit: 9444)
Memory: 318.1M (peak: 320.1M)
CPU: 4.123s
CGroup: /system.slice/uvicorn.service
/home/shashi/GASolver/.envpr2/bin/python -m uvicorn main:ap>
Apr 14 09:35:04 shashitdsproject2 systemd[1]: Started uvicorn.service - Uvicorn
Apr 14 09:35:05 shashitdsproject2 python[1782]: /home/shashi/GASolver/.envpr2/1
Apr 14 09:35:05 shashitdsproject2 python[1782]: warnings.warn('Using slow purs
Apr 14 09:35:05 shashitdsproject2 python[1782]: /home/shashi/GASolver/.envpr2/1
Apr 14 09:35:05 shashitdsproject2 python[1782]: warn("Couldn't find ffmpeg or
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Started server proces
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Waiting for applicati
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Application startup c
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Uvicorn running on ht
shashi@shashitdsproject2:~/GASolver$

its running as you can see here  
image description: The image is a webpage displaying the results of an API request. It's divided into sections for "Responses," "Curl," "Request URL," and "Server response." The main content is a POST request to the API endpoint with headers and parameters. The server's response includes a status code of 200 and a response body with the answer "5082."
image text:
My Dashb
Graded As
Ex TDS 2025
A shashitds
FastAPI
FINAL-TD
Azure for
A shashitds
Azure VM
Meet
+
shashitdsproject2.centralindia.cloudapp.azure.com/docs#/default/process\_request\_api\_post
☆
Responses
Curl
Execute
curl -X 'POST'
'https://shashitdsproject2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=What is the number of successful GET requests for pages under /malayalammp3/ from 15:00 until before 22:00 on Saturdays?' \
-F 'file=@s-anand.net-May-2024.gz;type=application/x-gzip'
Request URL
https://shashitdsproject2.centralindia.cloudapp.azure.com/api
Server response
Code
Details
200
Response body
{
"answer": 5082
}
Response headers
access-control-allow-credentials: true
access-control-allow-origin: \*
connection: keep-alive
content-length: 15
content-type: application/json
date: Mon, 14 Apr 2025 09:39:00 GMT
server: nginx/1.24.0 (Ubuntu)
Responses
Code
Description
Clear
宝 Download
Links

POST request through postman vscode  
Here's a description of the image:
The image is a screenshot of a Postman window, likely displaying an API request and response. The interface shows several sections like:
\* \*\*Top Bar:\*\* Includes file operations, a search bar, and control icons.
\* \*\*Sidebar:\*\* Has sections for workspace management and collection organization.
\* \*\*Request Panel:\*\* Displays the details of an API request (method, URL, parameters, headers, body, etc.).
\* \*\*Response Panel:\*\* Shows the API response, in this case, the "Body" section is open, with options for viewing in "Pretty," "Raw," "Preview," and "HTML" formats.
\* \*\*Footer:\*\* Displays the HTTP status, time, and size of the response.
The focus seems to be on the "Body" section of the response, which is currently displaying an HTML view. The HTML code shows a section containing a div with an ID "swagger-ui" and script tags that point to a swagger-ui-bundle.js file. It also shows some Javascript code using SwaggerUIBundle.
image text:
```html
9
10
<body>
11
<div id="swagger-ui">
12
</div>
13
<script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
14
<!-- SwaggerUIBundle` is now available on the page -->
15
<script>
16
const ui = SwaggerUIBundle({
17
url: '/openapi.json',
18
"dom\_id": "#swagger-ui",
19
"layout": "BaseLayout",
```

GET request through postman vscode  
Here's a brief description of the image:
The image is a screenshot of a Postman interface. The interface shows a GET request to "http://localhost:8000/api". The bottom section displays the HTML response, including a script related to SwaggerUI.
image text:
File Edit Selection View Go
POSTMAN
← →
HTTP http://localhos... • X
{...}
My Workspace
+
HTTP
New HTTP Request
D
GET
http://localhost:8000/api
Search
08
shashitdsproject2.centralindia.cloudapp.azure.com/docs
Params
Authorization
Headers (9) Body Pre-request Script Tests Settings
+
Filter
Query Params
New Collection
Key
empty
Key
Add a request to start
Body
Cookies Headers (6) Test Results
Pretty
Raw
Preview
HTML
Value
Value
Π
X
Save
No Environment
Status: 200 OK Time: 247 ms Size: 1.11 KB
9
10
<body>
11
12
13
14
15
16
17
<div id="swagger-ui">
</div>
<script
src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
<!-- SwaggerUIBundle is now available on the page -->
<script>
const ui = SwaggerUIBundle({
url: '/openapi.json',
18
"dom\_id": "#swagger-ui",
19
"layout": "BaseLayout",
X0A0
Send
Code Cookies
Windsurf: {...}

my server running on my friends on my friends laptop  
Here's a brief description of the image:
The image is a screenshot of a webpage displaying API request and response details. It includes a request URL, server response with code 200, response body containing a GitHub URL, and response headers. The webpage is likely related to processing API requests.
image text:
```
cURL -A POST
'https://shashitdsproject2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/'
Request URL
https://shashitdsproject2.centralindia.cloudapp.azure.com/api
Server response
Code Details
200 Response body
{
"answer": "https://shashikumarkohir.github.io/my-portfolio/"
}
Response headers
access-control-allow-credentials: true
access-control-allow-origin: https://shashitdsproject2.centralindia.cloudapp.azure.com
connection: keep-alive
content-length: 61
content-type: application/json
date: Mon, 14 Apr 2025 09:39:00 GMT
server: nginx/1.24.0 (Ubuntu)
vary: Origin
Responses
Code Description
```

Thanks,  
Shashi

---

**Sir** Please **don’t ignore this** —this is my **last term** and if I fail, I will have to restart the entire diploma. **I kindly request you to reconsider my project evaluation.**  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Saransh\_Saini](/u/saransh_saini)

---

MY Project 2 status is currently marked as Absent in the course dashboard. However, I would like to clarify that I submitted the repository and API endpoints well before the deadline through the designated forum.

Additionally, my Vercel server is still active, and the API is functioning correctly, as can be verified here:  
![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:") [API Form Submission](https://tdsproject2.vercel.app/api/)

I kindly request you to review my submission  
Here's a description of the image:
The image shows a browser window with a web page. In the center, there is a white card-like form titled "Submit Your Question". The form includes a "Question:" text area, an "Upload ZIP File (optional):" section with a "Choose File" button and a "No file chosen" text, and a "Submit" button. The URL in the browser's address bar is "tdsproject2.vercel.app/api/".
image text: Submit Your Question
Question:
Upload ZIP File (optional):
Choose File No file chosen
Submit

---

Project 2 marks are showing 0 for me, when I checked logs no requests were made to my endpoint. Could you please check into this, and update as soon as possible?  
Getting marks in this project would help me to pass this sub. Also, please check if evaluation has been done for my endpoint or not.

Thank you

---

2 to 3 days can be given to fix issues please, help us students complete this subject successfully ![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14 ":smiling_face_with_tear:") Please consider this sir

---

Sir, I too had provided render API and my logs do not show that it was accessed during the evaluation period. I had submitted the link in the form which was provided to update the link as i had not received any mail that my project had been evaluated before that.  
Due to this, my score stands 0 as of now.  
Sir, can you please look into this. Thank you

---

21f3002753@ds.study.iitm.ac.in  
Anyone know this email id  
i have sent request to access but he or she did not response today is deadline for GA7

---

Sir what if they don’t provide access i have sent manual email and through request but no response get received although i have completed 1 from 3 and 3 from 5

---

Bruh why are u posting ga7 in project 2 post?

---

is anything wrong and GA7 tagline not created and in this group people quickly response so i use this

---

Hi Sir, [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) Please check my project, It’s all working, why is it showing me 0 on dashboard? project2,… rollnumber 23f2001390 and mail is 23f2001390@ds.study.iitm.ac.in

---

same for me its showing 0 for me

---

Same here, marked absent despite having submitted the Google form.

---

my score also showing zero..kindly look this sir

---

MY Project 2 status is currently marked as Absent in the course dashboard. However, I would like to clarify that I submitted the repository and API endpoints well before the deadline through the designated forum.

Additionally, my Vercel server is still active, and the API is functioning correctly, as can be verified here:  
![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:")<https://project2-three-plum.vercel.app/api/>

I kindly request you to review my submission

---

## Request for Re-evaluation

I have completed the entire project and ensured that my model is working correctly. Despite this, I have received **zero marks**, which seems to be an error.

API LINK:<https://project2llm-production.up.railway.app/api/>  
<https://project2llm-production.up.railway.app/api/>

I kindly request a re-evaluation of my submission. Please verify the working model and the completion of all project requirements.

Thank you.  
[@carlton](/u/carlton) [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj)

---

project url: <https://tdsproject2-eight.vercel.app/>

---

Dear Sir,

In my course dashboard, Project 2 score is shown as zero. However, I had submitted the repository and API endpoints (<http://35.192.157.22.80>) through the Google Form. I had received a mail to make edit in API end point if changed. I had edited my api end point by adding /api/ and it was <http://35.192.157.22/api/>. My server was running fine. I have worked hard to do this project and now receiving a score of zero. Kindly look into it.

---

Sir I have also recieved 0 marks, but I checked now also using python requests library and my server is working fine . But I see a lot of GET requets instead of POST in my logs file which was for the past couple of days requests, which is very unlikely . Please check my link again , its still active . App link - <http://16.16.189.187:8000/tdsp2>

My test file-  
Here's a description of the image:
The image shows a code editor with Python code and the output of the code. The code is designed to interact with a FastAPI server. The code defines a URL, form data including a question about sales, and uses the `requests` library to send a POST request. The output in the terminal shows a status code of 200, indicating success, and the JSON response containing the SQL query that was executed.
image text:
```
1
import requests
2
3
# Replace with your actual FastAPI server URL
4
url = "http://16.16.189.187:8000/tdsp2"
5
6
# Define form data
7
data = {
8
"question": r"""What is the total sales of all the items in the "Gold" ticket type? Write SQL to ca
9
}
10
11
12
files={"file": ("q-fastapi.csv", open("C:/Users/suneh/Downloads/q-fastapi.csv", "rb"), "text/plain")}
# Send the POST request
response = requests.post(url, data=data) #files=files
13
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
> powershell
PS C:\Users\suneh\lab5> python burima.py
Status Code: 200
Response JSON: {"answer": "SELECT SUM(units \* price) AS total\_sales FROM tickets WHERE LOWER (TRIM(type)) = 'gold';"}
PS C:\Users\suneh\lab5>
```

My server log file -  
image description: The image shows a black background with white text arranged in lines. The text appears to be log entries, with each line starting with "INFO" or "WARNING" followed by details such as IP addresses, port numbers, and HTTP request information. Many of the lines indicate "404 Not Found" errors or "Invalid HTTP request received".
image text:
```
INFO: 103.158.43.17:17624 - "POST /tdsp2 HTTP/1.1" 200 OK
INFO: 3.138.153.199:41458 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 3.138.153.199:42404 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 147.185.132.39:64970 - "GET / HTTP/1.1" 404 Not Found
INFO: 5.79.219.172:42842 - "GET / HTTP/1.1" 404 Not Found
INFO: 109.117.240.53:57966 - "GET / HTTP/1.0" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 198.235.24.68:57798 - "GET / HTTP/1.1" 404 Not Found
INFO: 167.94.138.61:60428 - "GET / HTTP/1.1" 404 Not Found
INFO: 167.94.138.61:60492 - "PRI %2A HTTP/2.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 167.94.138.61:35668 - "GET /favicon.ico HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 45.43.33.210:38675 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
```

My app request handeling -  
![Screenshot 2025-04-14 224629](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/c/1/c1e0c6274b4c8ceb28601204a035ac988a58548d_2_690x53.png)

please kindly look into the matter sir  
[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

I noticed that my Project 2 status is currently marked as “Absent” in the course dashboard. However, I would like to clarify that I \*\*submitted the GitHub repository and Vercel API link well before the deadline  
via the designated forum.

Additionally, my **Vercel server is still active**, and the API is functioning correctly, which can be verified here:  
![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:") [API Form Submission](https://tdsproject2.vercel.app/api/)

I also have a **response copy from the forum confirming my submission**, including both the GitHub and Vercel links, as proof. I kindly request you to review this and take the necessary steps to update my project status.  
Here's a brief description of the image:
The image shows a Google Form. There are two questions asking for links. The first asks for a GitHub repository link, and the second asks for an API endpoint link. There are also links to create a Google Form and to report if the current form looks suspicious.
image text:
What is the link to your GitHub repository which has the code for Project 2? \*
It should look like https://github.com/user-name/repository-name
https://github.com/itskaiffazal/tdsproject2
What is the link to your API endpoint? \*
Make sure we can send a POST request to this exact URL
https://tdsproject2.vercel.app/api/
Create your own Google Form
Does this form look suspicious? Report
  
Here's a description of the image:
The image shows a webpage interface. The webpage is asking the user to submit a question. There is a text box for the question. There is also an option to upload a ZIP file.
image text:
Submit Your Question
Question:
Upload ZIP File (optional):
Choose File No file chosen
Submit

---

I Got 0 in Project 2 but my server was perfectly working and giving accurate responses .

---

Request a re-evaluation of my **Project 2** score. Despite submitting the project as per the given deadlines, my portal currently shows a score of **0**.

I have cross-checked my submissions and believe there may have been an error in evaluation or in updating the marks.

---

For my project, it is showing absent, Can you please check it, as the project is working?

---

[@Saransh Saini](mailto:22f1001123@ds.study.iitm.ac.in) [@JIVRAJ SINGH SHEKHAWAT](mailto:22f3002542@ds.study.iitm.ac.in) Please coordinate and check the issues raised. Thanks & Regards

---

For TDS project 2, it is showing 0 in course dashboard, but when I tested the URL it is working fine. Is there any log similar to project1 to check what gone wrong? Could you please check on this sir? [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

Dear Sir, [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I need your immediate attention regarding my **project-2 , as I received zero marks,** but **my server is running completely fine**. Below are the key points that I need you to look into:

Server is running and reachable. and Giving The Correct Answers

GET and POST requests tested via Postman and VS Code, both return 200 OK.

Tested on my laptop and by 10+ other people – all received correct results.

No issues seen in logs or deployment – everything was set up properly.

Others in my group got full marks – we worked on the same project.

I have no idea what went wrong during the evaluation.

I’ve spent weeks working on this project, including sleepless nights.  
Cant have least scores despite all the efforts.

Please recheck my project thoroughly. Here are the important links for you to verify:  
**API Documentation: [FastAPI - Swagger UI](https://bhavanaproj2.centralindia.cloudapp.azure.com/docs)**

**I truly believe that my server is functioning as expected, and I just need a re-evaluation to confirm that.  
I’ve put in a lot of effort into this, and I sincerely request that you review it again.  
Please don’t ignore this.  
Thanks,  
**Bhavana G V  
23f3004066  
Email: [23f3004066@ds.study.iitm.ac.in](mailto:23f3004066@ds.study.iitm.ac.in)**

Here im attaching All the proofs of my server which is running  
above is my server running perfectly fine  
below is the execution and getting right answers screenshots  
Here's a description of the image:
The image is a screenshot of a webpage displaying API response information. It is divided into several sections: "Responses", "Curl", "Request URL", "Server response". The "Curl" section shows the curl command used to make a POST request to an API endpoint, including headers and the data being sent. The "Request URL" displays the API endpoint URL. The "Server response" section includes the HTTP status code (200) and the response body, which contains weather data for several dates.
image text:
```
← bhavanaproj2.centralindia.cloudapp.azure.com/docs#/default/process\_request\_api\_post
Execute Clear
Responses
Curl
curl -X 'POST' \
'https://bhavanaproj2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=Your Task As part of this initiative, you are tasked with developing a system that automates the following: API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather for
Request URL
https://bhavanaproj2.centralindia.cloudapp.azure.com/api
Server response
Code Details
200
Response body
{
"answer": {
"2025-04-15": "Sunny and light winds",
"2025-04-16": "Thundery showers and light winds",
"2025-04-17": "Thundery showers and a gentle breeze",
"2025-04-18": "Sunny intervals and a gentle breeze"
"2025-04-19": "Thundery showers and a gentle breeze",
"2025-04-20": "Thundery showers and a gentle breeze",
"2025-04-21": "Thundery showers and a gentle breeze",
"2025-04-22": "Sunny intervals and a gentle breeze"
"2025-04-23": "Thundery showers and a gentle breeze",
"2025-04-24": "Thundery showers and a gentle breeze",
"2025-04-25": "Thundery showers and a gentle breeze",
"2025-04-26": "Thundery showers and a gentle breeze",
"2025-04-27": "Thundery showers and a gentle breeze",
"2025-04-28": "Thundery showers and a gentle breeze"
}
}
Response headers
Download
```

**Please consider this message , dont ignore** (I dont want to score less despite all the effort. )**

---

[@Saransh\_Saini](/u/saransh_saini) [@s.anand](/u/s.anand)  
please dont ignore this  
i have got right solutions as you can see, so please consider for rechecking.  
image description: The image shows a webpage with sections for question input, file upload, and a response area. The question section allows the user to input a string, with an example formula provided. There is a file upload section that allows the user to upload a file. After executing, the 'Responses' section displays the Curl command, Request URL, and the server's response, including the code and details. The download button is present at the bottom of the response body.
image text: question \* required
string
Let's make sure you can write formulas in Google Sheets. Ty
file
Choose File No file chosen
string | (string |
null) ($binary)
Send empty value
Execute
Clear
Responses
Curl
curl -X 'POST' \
'https://bhavanaproj2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=Let'\''s make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won'\''t work in Excel) =SUM(ARRAY\_CONSTRAIN(SEQUENCE(100, 100, 9, 11), 1, 10)) What is th
Request URL
https://bhavanaproj2.centralindia.cloudapp.azure.com/api
Server response
Code Details
200
Response body
{
"answer": 585
}
Download

---

Yes sir please check the issue as many people are facing the same problem.  
[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)

---

Request a re-evaluation of my **Project 2** score. Despite submitting the project as per the given deadlines, my portal currently shows a score of **0**.

I have cross-checked my submissions and believe there may have been an error in evaluation or in updating the marks

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

My marks are also showing as zero.

My suggestion is to provide students with the logs of your evaluation script, so we know if it is that server was not reachable, the answer is incorrect, or the response format was incorrect..etc

Request you to let us know if there is going to be re-evaluation so we can get the Azure instance running again

---

Hi everyone, I believe this issue has already been raised, even I got a 0 for my project 2. Is this an error on the backend?

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
EDIT: Update on previous post.

Attached image of requests made on my endpoint by I presume the TDS team at 4:53 PM on 10th April:  
Here's a description of the image:
\*\*Overall:\*\* The image captures a close-up of a laptop screen displaying a terminal interface, along with the keyboard of the laptop. The screen shows network request details.
\*\*Screen Details:\*\* The screen displays text in a terminal-like format, which suggests network monitoring or development activity. Some of the information includes:
\* Status information (online)
\* Network details: URLs and timing information
\* Request details
\* HTTP status codes like 307 (Temporary Redirect) and 200 (OK)
\*\*Laptop:\*\* The lower part of the image features the laptop's keyboard, which shows the keys F3 through F8 and part of the number row. The bottom row contains the usual modifier keys. The background is the default desktop wallpaper.
image text:
Status
online
Gaurav Ghodge (Plan: Free)
3.22.0
India (in)
24ms
http://127.0.0.1:4040
https://c7f6-150-107-43-5.ngrok-free.app ->
ttl
7
opn rt1 rt5 p50 p90
0 0.01 0.01 8.76 10.3
Requests
53:08.409 IST POST /api
53:08.475 IST POST /api/
53:07.786 IST POST /api
53:07.786 IST POST /api
:53:07.786 IST POST /api
:53:07.896 IST POST /api/
5:53:07.886 IST POST /api/
307 Temporary Redirect
200 OK
307 Temporary Redirect
307 Temporary Redirect
307 Temporary Redirect
200 OK
200 OK
307 Temporary Redirect
6:53:07.786 IST POST /api
6:53:07.886 IST POST /api/
13:37:23.955 IST POST /api/
200 OK
200 OK
A
qb
A
80
Q
오
DD
F3
F4
F5
F6
F7
F
#
$
%
A
&
\*
4
5
6
7
8

Ran curl request multiple times LOCALLY on endpoint after score got published to check:  
Here's a description of the image:
The image is a screenshot of a coding environment, likely VS Code, displaying code and terminal output.
Key elements:
\* \*\*Code Editor:\*\* The main panel shows Python code. The code is related to a FastAPI application, including import statements, CORS middleware setup, and an API endpoint for processing questions.
\* \*\*File Explorer:\*\* On the left, a file explorer shows the project structure, with files like `main.py`, `file\_handler.py`, `functions.py`, and others.
\* \*\*Terminal:\*\* A terminal at the bottom shows a `curl` command being executed to test the API, along with the expected output: `"answer":"1121"`.
\* \*\*Status Bar:\*\* The status bar at the bottom shows information such as the line and column numbers, spaces, encoding, and the Python version.
image text:
```
EXPLORER
✓ TDS-PROJECT-2.2
app
>\_pycache\_
✓ utils
>\_pycache\_
file\_handler.py
functions.py
openai\_client.py
main.py
> tds-project-2
> tests
.env
{} Answers.json
LICENSE
README.md
requirements.txt
server.py
main.py
X
app > main.py > ...
1 from fastapi import FastAPI, File, UploadFile, Form, HTTPException
2 from fastapi.middleware.cors import CORSMiddleware
3 import os
4 from typing import Optional
5 from app.utils.openai\_client import get\_openai\_response
6 from app.utils.file\_handler import save\_upload\_file\_temporarily
7
8 # Import the functions you want to test directly
9 from app.utils.functions import \*
10
11 app = FastAPI(title="IITM Assignment API")
12
13 # Add CORS middleware
14 app.add\_middleware(
15 CORSMiddleware,
16 allow\_origins=["\*"],
17 allow\_credentials=True,
18 allow\_methods=["\*"],
19 allow\_headers=["\*"],
20 )
21
22
23 @app.post("/api/")
24 async def process\_question(
25 question: str = Form(...), file: Optional[UploadFile] = File(None)
26 ):
27 try:
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
gauravghodge@Gauravs-MacBook-Air TDS-PROJECT-2.2 % curl -X POST "http://localhost:8000/api/" -H "Content-Type: multipart/form-data" -F que
stion="How many Wednesdays are there in the date range 1986-08-06 to 2008-01-29?"
{"answer":"1121"}
gauravghodge@Gauravs-MacBook-Air TDS-PROJECT-2.2 %
> OUTLINE
> TIMELINE
X
Python
zsh
Ln 1, Col 1 Spaces: 4 UTF-8 LF {} Python 3.13.2
Go Live
```

Ran curl request multiple times ON NGROK on endpoint after score got published to check:  
image description: The image displays a computer screen with multiple windows and text. On the left side is a file explorer showing a project structure. The center shows a code editor with Python code, and at the top is the file named `main.py`. A terminal window is also open and displays commands, including `curl` commands related to an API.
image text:
```
EXPLORER
✓ TDS-PROJECT-2.2
app
>\_pycache\_
✓ utils
>\_pycache\_
file\_handler.py
functions.py
openai\_client.py
main.py
> tds-project-2
> tests
.env
{} Answers.json
LICENSE
README.md
requirements.txt
server.py
> OUTLINE
> TIMELINE
main.py
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from typing import Optional
from app.utils.openai\_client import get\_openai\_response
from app.utils.file\_handler import save\_upload\_file\_temporarily
gauravghodge - ngrok http 8000-80x24
gauravghodge --zsh - 119x33
Last login: Tue Apr 15 19:01:31 on ttys013
[gauravghodge@Gauravs-MacBook-Air ~] % curl -X POST "https://4fd9-150-107-43-113.ngrok-free.app/api/" -H "Content-Type: m
ultipart/form-data" -F question="How many Wednesdays are there in the date range 1986-08-06 to 2008-01-29?"
{"answer":"1121"}
```

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) Sir, i got 0 in project 2 also, please check, there might be some error from your side

---

Hi Sir,

Even I got zero in project 2. My server was running fine and both get and post requests were going through. I stopped the server after I got a confirmation mail that the evaluation were completed. Please check.

---

Dear TAs please help - even I got 0 in project 2 even though I have submitted the right links with all prerequisites & working server. If you can share some evaluation logs or errors that would be very helpful to know where I went wrong possibly.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
I received 20 in project 2 which I think is not correct. I also tested my api with questions with different parameters to make sure it is giving correct responses. You are requested to kindly recheck and share the evaluation logs.

---

Hi sir [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand)

I need your immediate attention regarding my project-2, as I received zero marks, but my server is running completely fine. Below are the key points that I need you to look into:

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Server is running and reachable.**  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **GET and POST requests tested via Postman and VS Code**, both return **200 OK**.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Tested on my laptop and by 10+ other people** – all received correct results.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **No issues seen in logs or deployment** – everything was set up properly.  
![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") **Others in my group got full marks** – we worked on the same project.

![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **I have no idea what went wrong during the evaluation.**  
![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **I’ve spent weeks working on this project**, including sleepless nights.  
![:red_exclamation_mark:](https://emoji.discourse-cdn.com/google/red_exclamation_mark.png?v=14 ":red_exclamation_mark:") **This is my last term** – if I fail, I will have to repeat the entire diploma.

Please recheck my project thoroughly. Here are the important links for you to verify:

* **API Documentation:** [FastAPI - Swagger UI](http://shashitdsproject2.centralindia.cloudapp.azure.com/docs)
* **API Endpoint:** <http://shashitdsproject2.centralindia.cloudapp.azure.com/api>

I truly believe that my server is functioning as expected, and I just need a re-evaluation to confirm that.

I’ve put in a lot of effort into this, and I sincerely request that you review it again.

as you can see my vm is working fine here  
image description: The image shows a terminal window within the Azure portal, displaying the serial console of a virtual machine named "shashitdsproject2". The terminal output includes commands related to starting and enabling a service, along with status updates and log messages. The active service is "uvicorn.service".
image text:
```python
async def process\_request(
question: str = Form(...),
file: Optional[UploadFile] = File(None)
):
try:
# data = question
# print(data)
shashi@shashitdsproject2:~/GASolver$ sudo systemctl restart nginx
shashi@shashitdsproject2:~/GASolver$ ^[[200~sudo systemctl restart~
sudo: command not found
shashi@shashitdsproject2:~/GASolver$ sudo systemctl daemon-reload && sudo systemctl start uvicorn && sudo systemctl enable uvicorn && sudo sy
stemctl status uvicornt2:~/GASolver$ sudo systemctl daemon-reload && sudo systemctl start uvicorn && sudo systemctl enable uvicorn && sudo sy
● uvicorn.service - Uvicorn FastAPI Server
Loaded: loaded (/etc/systemd/system/uvicorn.service; enabled; preset: enabled)
Active: active (running) since Mon 2025-04-14 09:35:04 UTC; 33s ago
Main PID: 1782 (python)
Tasks: 2 (limit: 9444)
Memory: 318.1M (peak: 320.1M)
CPU: 4.123s
CGroup: /system.slice/uvicorn.service
/home/shashi/GASolver/.envpr2/bin/python -m uvicorn main:ap>
Apr 14 09:35:04 shashitdsproject2 systemd[1]: Started uvicorn.service - Uvicorn...
Apr 14 09:35:05 shashitdsproject2 python[1782]: /home/shashi/GASolver/.envpr2/1...
Apr 14 09:35:05 shashitdsproject2 python[1782]: warnings.warn("Using slow purs...
Apr 14 09:35:05 shashitdsproject2 python[1782]: /home/shashi/GASolver/.envpr2/1...
Apr 14 09:35:05 shashitdsproject2 python[1782]: warn("Couldn't find ffmpeg or...
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Started server proces...
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Waiting for applicati...
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Application startup c...
Apr 14 09:35:08 shashitdsproject2 python[1782]: INFO: Uvicorn running on ht...
shashi@shashitdsproject2:~/GASolver$
```

its running as you can see here  
image description: The image is a screenshot of a webpage displaying API response details. The page is related to "shashitdsproject2.centralindia.cloudapp.azure.com". The interface has sections for "Curl", "Request URL", "Server response", and "Responses". The "Server response" section shows a "Code" of 200 and a "Response body" containing a JSON object with "answer": 5082. The image also includes "Response headers" with details like content-type and date.
image text:
Responses
Curl
Execute
curl -X 'POST' \
'https://shashitdsproject2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=What is the number of successful GET requests for pages under /malayalammp3/ from 15:00 until before 22:00 on Saturdays?' \
-F 'file=@s-anand.net-May-2024.gz;type=application/x-gzip'
Request URL
https://shashitdsproject2.centralindia.cloudapp.azure.com/api
Server response
Code Details
200
Response body
{
"answer": 5082
}
Response headers
access-control-allow-credentials: true
access-control-allow-origin: \*
connection: keep-alive
content-length: 15
content-type: application/json
date: Mon, 14 Apr 2025 09:39:00 GMT
server: nginx/1.24.0 (Ubuntu)
Responses
Code
Description
Clear
Download
Links

POST request through postman vscode  
Here's a brief description of the image:
The image shows a dark-themed user interface, likely a Postman application, displaying the results of a POST request. The request is directed to "http://localhost:8000/api" and the body of the response is displayed as HTML. There is an HTML body which contains a div with "swagger-ui" id and a script tag to include a swagger-ui-bundle.js file.
image text:
```
☑ File Edit Selection View Go
...
POSTMAN
HIIP http://localhos... • X
My Workspace
☑
HTTP
http://localhost:8000/api
New HTTP Request
POST
...
Search
...
shashitdsproject2.centralindia.cloudapp.azure.com/docs
Params
Authorization
Headers (9)
Body
Pre-request Script
Tests
Settings
New Collection
empty
Add a request to start
Query Params
Key
Key
Body
Cookies
Headers (6) Test Results
Pretty Raw Preview
HTML
9
10
<body>
11
12
</div>
13
14
15
16
17
18
19
0A0
Value
Value
...
<div id="swagger-ui">
<script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
<!-- SwaggerUIBundle` is now available on the page -->
<script>
const ui = SwaggerUIBundle({
url: '/openapi.json',
"dom\_id": "#swagger-ui",
"layout": "BaseLayout",
...
```

GET request through postman vscode  
Here's a description of the image:
The image shows a Postman interface displaying the results of a GET request to an API endpoint. The request is directed to "http://localhost:8000/api". The response body is displayed in HTML format. The response includes HTML code that sets up a Swagger UI. The status code is "200 OK" with a time of 247ms and a size of 1.11 KB.
image text:
```
File Edit Selection View Go
POSTMAN
← →
HIIP http://localhos... • X
{...}
My Workspace
+
HTTP
New HTTP Request
D
GET
http://localhost:8000/api
Search
08
shashitdsproject2.centralindia.cloudapp.azure.com/docs
Params
Authorization
Headers (9) Body Pre-request Script Tests Settings
+
Filter
Query Params
New Collection
Key
empty
Key
Add a request to start
Body
Cookies Headers (6) Test Results
Pretty
Raw
Preview
HTML
Value
Value
Π
X
Save
No Environment
Status: 200 OK Time: 247 ms Size: 1.11 KB
9
10
<body>
11
12
13
14
15
16
17
<div id="swagger-ui">
</div>
<script
src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
<!-- SwaggerUIBundle is now available on the page -->
<script>
const ui = SwaggerUIBundle({
url: '/openapi.json',
18
"dom\_id": "#swagger-ui",
19
"layout": "BaseLayout",
X0A0
Send
Code Cookies
Windsurf: {...}
```

my server running on my friends on my friends laptop  
Here's a description of the image:
\*\*Overall:\*\* The image appears to be a screenshot of a web page displaying information related to API requests and responses. It shows a curl command, request URLs, server responses, and response headers.
\*\*Key elements:\*\*
\* \*\*Curl Command:\*\* The image shows a curl command with various options.
\* \*\*Request URL:\*\* The request URL is mentioned.
\* \*\*Server Response:\*\* The image shows server response details, including the code (200), response body, and response headers.
\* \*\*Response Body:\*\* The response body contains a JSON with the answer.
\* \*\*Response Headers:\*\* The response headers provide information like access-control, content-length, content-type, and server information.
\* \*\*"Download" button:\*\* A button with the label "Download" is present.
\*\*Text:\*\*
```
curl - POST
'https://shashitdsproject2.centralindia.cloudapp.azure.com/api' \
-H 'accept: application/json' \
-H 'Content-Type: multipart/form-data' \
-F 'question=What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/'
Request URL
https://shashitdsproject2.centralindia.cloudapp.azure.com/api
Server response
Code Details
200 Response body
{
"answer": "https://shashikumarkohir.github.io/my-portfolio/"
}
Response headers
access-control-allow-credentials: true
access-control-allow-origin: https://shashitdsproject2.centralindia.cloudapp.azure.com
connection: keep-alive
content-length: 61
content-type: application/json
date: Mon, 14 Apr 2025 09:39:00 GMT
server: nginx/1.24.0 (Ubuntu)
vary: Origin
Responses
Code Description
```

Thanks,  
Shashi

---

[@Saransh Saini](mailto:22f1001123@ds.study.iitm.ac.in) [@JIVRAJ SINGH SHEKHAWAT](mailto:22f3002542@ds.study.iitm.ac.in)

Can you coordinate and check this submission? Thanks.

---

Hi [@carlton](/u/carlton)  
[@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
Sir the same issue occurred on my end as well. My endpoint is returning the correct output, as demonstrated by [@SK76](/u/sk76) . However, it has still been marked as 0.  
Could you please check whether the evaluation is still in progress or has been finalized? I would appreciate any update on the status.  
(54/57 questions working, tested with different values and parameters)  
Roll num : 21f3001076  
Thank you.  
Lakshay

---

[@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) Could you reveal what tests were done for our second projects? So that we can test for ourselves. I have been give a zero.

Roll number: 21f2001573

[@carlton](/u/carlton)

---

Even i am facing the same issue and from the same group . The other members of the same group have scored well but not able to figure out why we have scored 0. Please look into it asap and update the marks. Dont wanna lose all the efforts in one mistake so please look into it.  
Below are my links . I have sent mail also.

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/a/aae809b0bbff330e7cec1d2f6ae9eb8551d928c2.png)
[bhavanaproj2.centralindia.cloudapp.azure.com](https://bhavanaproj2.centralindia.cloudapp.azure.com/docs)

### [FastAPI - Swagger UI](https://bhavanaproj2.centralindia.cloudapp.azure.com/docs)

<https://bhavanaproj2.centralindia.cloudapp.azure.com/api>  
Name : Bhavana G V  
23f3004066  
email: 23f3004066@ds.study.iitm.ac.in

---

Please dont ignore this message Sir [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Sir, just checking if there’s any update. My Azure portal is still running, but the credits are almost used up.

---

We are sending an email out for all those that have raised an issue within the next few hours. The content of the email will be to keep your server up in the window that we prescribe. That window will be mentioned in the email. You do not need to keep the vm running at the moment. Just check the email when it comes.

---

Continuing the discussion from [TDS Project 2 Score is 0](https://discourse.onlinedegree.iitm.ac.in/t/tds-project-2-score-is-0/172633/11):

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

Sir, We respect you and there might be a mistake on your side. But kindly solve all our discrepancies as soon as possible.

Regards,  
Sengathirsoorian E T

(Friends, if you have any queries, append in this post)

---

It is showing absent in my dashboard even though i submitted the project

---

It is showing absent in mine as well

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) I am making this post because I didn’t get reply to my [post on the same matter.](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/477)

Please check it out. My app can remain deployed only till April 18th. In the Cloud Run logs, I do see some multiple POST requests made today with 200 response but I’m not sure whether it was the TDS team doing a re-evaluation or someone else.

Also, are there any updates on [this bug in project 1 in datagen.](https://discourse.onlinedegree.iitm.ac.in/t/tds-official-project1-discrepencies/171141/451)

Thanks.  
Regards,  
Shivaditya

---

Hello,

I recieved my Project 2 Scores and I have recieved 20/100. Two of us had shared the code and the other person has recieved higher marks. Whats the reason for this discrepancy? Kindly shed some light on this situation and please share any evaluation logs from your end. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Thanks and Regards

---

[@Saransh Saini](mailto:22f1001123@ds.study.iitm.ac.in) [@JIVRAJ SINGH SHEKHAWAT](mailto:22f3002542@ds.study.iitm.ac.in) please coordinate and check this submission. Thanks & Regards

---

1 carlton sir i had submitted project 2 and rechecked it multiple time but it is showing absent in project 2 please look into this matter

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) I also received 20 in project 2 which I think is not correct. I also tested my api with questions with different parameters to make sure it is giving correct responses with questions with variable parameters. You are requested to kindly recheck and share the evaluation logs.

---

Hello,  
I had filled up and submitted the TDS project 2 and I have double check it for working,  
My Project Score is showing 0 I believe there’s a mistake.  
Please help me out

---

same happened with me

---

It shows ‘Absent’ for me despite submitting the google form.

---

same with me!! everything was working fine.

---

same for me! please check

---

Same for me! please check

---

[@JIVRAJ SINGH SHEKHAWAT](mailto:22f3002542@ds.study.iitm.ac.in) [@Saransh Saini](mailto:22f1001123@ds.study.iitm.ac.in) Please coordinate and check the issues raised. Thanks & Regards

---

same happened for me ! please check

---

Same for me! Please check [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

It is showing absent for me as well. Kindly check. Thank you.

---

Sir, Same here, you can access it via this link [Assignment solver](https://phoenix-1743854088883.staticrun.app/)

I kindly request you to check immediately by this link as I also have made it as an web app for your ease.

(my friends: please don’t use the link, as the api token request will be over)

Please look after it, already I was marked as absent for project -1 and now for this project -2 as 0. I don’t know why?..I don’t know whether I could be able to pass this course even with lots of efforts..

---

sir, my project 2 score is also showing as 0. Please recheck. As many of us are facing the same issue i kindly request to confirm please. Failing in this subject due this will affect us badly.

---

I am also seeing a score of 0. This is after the course TA’s said that I had scored well on the project without revealing my score. But I am pretty sure they won’t classify 0/100 as a good score.

---

Sir,  
I have submitted the working url but forgot to add /api in the end. Please consider my request and evaluate this below link. This below link is same as the submitted link just with /api.  
image description: The image is a screenshot of a Google Form, possibly filled out on a mobile device. It asks for specific information, likely related to a project submission.
image text: work email ID.
You can submit only one response.
You can correct your response after you
submit.
Your email (24f2006749@ds.study.iitm.ac.in) was recorded when you submitted this
form.
What is the link to your GitHub
repository which has the code for
Project 2? \*
It should look like https://github.com/user-
name/repository-name
https://github.com/Sakshi6749/PROJECT-
2
What is the link to your API endpoint?
\*
Make sure we can send a POST request to this
exact URL
saakshi-llama.centralindia.
cloudapp.azure.com
Create your own Google Form
Does this form look suspicious? Report

<https://saakshi-llama.centralindia.cloudapp.azure.com/api>

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)

---

hello sir when you share evaluation file we need to check

---

Sir, its showing me 0 as well.

---

2 days back I got my TDS Project-2 Score and it is showing as absent although I submitted my TDS project 2 , also deployed the app successfully and also filled the g-form

Here’s my deployed application on-render link with the attached screenshot of my TDS Dashboard:

Project : <https://tds-project2-21f3000591.onrender.com/>

Here's a description of the image:
The image is a webpage showing the details of a course. It appears to be an online learning platform.
image text: Tools in Data Science
NEW COURSE
Week 1 Assignment - 92.50
Week 2 Assignment - 90.00
Week 3 Assignment - 0.00
Week 4 Assignment - 100.00
Week 5 Assignment - 100.00
Week 6 Assignment - Absent
Week 7 Assignment - Absent
Average Assignment for final Scoring - 96.00
PROGRAMMING QUIZ 1 - 90.00
COURSE PROJECT - 5.00
Course Project Score 2 - Absent
Allowed to take End Term Exam?
Yes
Go to Course page >

---

It does show absent for me too IN Project two even though i have submitted the form hosted the site made the repo and done litearlly everything  
Anyways i have scored 0 in proj 1 bcz of docker not working or something and with this there is no chance i get better than an E if in case i pass

---

Shows Absent for me as well please check

---

Sir this is same happening with me please look into this ![:disappointed_face:](https://emoji.discourse-cdn.com/google/disappointed_face.png?v=14 ":disappointed_face:")

---

Though I have done alll the required stuffs for the project 2, It is showing absent for me two.  
Kindly look into the case sir..

---

Respected sir  
My projects scores also shows 0 like others , i deleted my vm when the email specifies that evaluation is complete comes , in this email it is also mention that your scores and evaluation log will also send by email , no email like this come , please look in to this matter as earliest.

---

even my score is zero even if my project runs fine

---

Hello sir [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

Could you please check my project 2 evaluation. it is showing 0 but when I tested it worked fine. My api is still running

---

sir my score is showing zero even if i have submitted the project correctly.please re-evaluate my project <https://roe-i6ghzat4g-manu-cs-projects.vercel.app/>

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)  
I got a mail saying project 2 endpoints will be tested again.  
It also says that those updated endpoints which were submitted in the google form will be tested. Since i had submitted ngrok endpoint, wont it be invalid now?  
And if i start ngrok server wont it give me new endpoint?

---

Although I have completed all the required tasks for Project 2, it is still showing me as absent. I kindly request you to look into this issue, sir.  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton) .

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
hello sir, what will happen if new score is lesser than the old one? will you consider whichever score is greater or new one sir? Kindly reply sir. and considering the best score in these 2 evaluations is better i think sir. Kindly consider this sir.

Thank you  
Harish

---

Could someone clarify whether the endpoint should include /api when being evaluated? I submitted it without /api and I’m wondering if it will be automatically appended or if we must include it explicitly. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

there is no automatic appending.  
We will test **exactly** what we sent in the email (if you got an email) which is **exactly** what you submitted .

---

we will consider the greater of the two

---

need to include the /api in the end. without that your mark will be 0 , since it cannot be evaluated without an end point

---

You were not present in the form Anand gave us. It most likely because you submitted after the deadline (or made edits after the deadline, if the form he shared allowed edits).

---

sir i am using ngrok. Shall i edit the old url in the form with the new one ? will you consider the new url in the form?

---

If u restart ngrok it changes endpoint every time. Your old endpoint is non existent as far as i know.

---

yeah thats why asking.

---

Is the marks shown on dashboard out of 20 or 100? coz i can clearly see in the logs that my api has answered all questions correctly, and my dashboard shows score of 20 for project 2.

---

I also want to know the same thing. Our old ngrok endpoint is useless at this point.

---

marks are always out of 100 on dashboard

---

[@carlton](/u/carlton)  
sir i am using ngrok. Shall i edit the old url in the form with the new one ? will you consider the new url in the form?

---

I’m writing to clarify the status of my Project 2, which is currently marked as “Absent”. I would like to respectfully state that I **submitted the form before the deadline** — specifically on 31st March 2025 at 22:11 , and I have the response copy as proof.

I would also like to emphasize that:

No edits were made to the form after submission.  
I did not make any changes to the project or submission after the deadline.  
My Vercel API is still active and functioning as expected.

Here are the submitted links:

![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:") GitHub Repo: [GitHub - itskaiffazal/tdsproject2: Tools in data science Project 2 - TDS Solver](https://github.com/itskaiffazal/tdsproject2)  
![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:") API Endpoint: <https://tdsproject2.vercel.app/api/>

I kindly request you to review my submission and take the necessary steps to update the status.  
image description: The image is a Gmail email confirmation for a Google Form. The subject of the email is "TDS Project 2 - Jan 2025". The email confirms the filling out of the form and offers an "Edit response" button.
image text: M Gmail
TDS Project 2 - Jan 2025
1 message
Google Forms <forms-receipts-noreply@google.com>
To: kaiffazal001@gmail.com
Google Forms
Thanks for filling in TDS Project 2 - Jan 2025
Here's what was received.
Edit response
Kaif Fazal <kaiffazal001@gmail.com>
31 March 2025 at 22:11
  
image description: The image is a screenshot of a Google Form with two questions and their corresponding answers related to Project 2. The first question asks for a link to the GitHub repository containing the code, with a sample URL provided, and the answer given is a URL. The second question requests the link to the API endpoint, along with a note about the POST request, and provides a specific URL as the answer. The form also contains links to "Create your own Google Form" and "Does this form look suspicious? Report".
image text: What is the link to your GitHub repository which has the code for Project 2? \*
It should look like https://github.com/user-name/repository-name
https://github.com/itskaiffazal/tdsproject2
What is the link to your API endpoint? \*
Make sure we can send a POST request to this exact URL
https://tdsproject2.vercel.app/api/
Create your own Google Form
Does this form look suspicious? Report
  
Here's a description of the image:
The image shows a webpage with a form for submitting a question. The form includes fields for entering a question, uploading a ZIP file, and a submit button.
image text:
<
tdsproject2.vercel.app/api/
Submit Your Question
Question:
Upload ZIP File (optional):
Choose File No file chosen
Submit

---

You used your personal email address while filling the form. It is impossible for us to track who is submitting a form if you do not use your official email id. Unfortunately we cannot evaluate your submission.

---

[@carlton](/u/carlton) , [@Jivraj](/u/jivraj) , [@Saransh\_Saini](/u/saransh_saini)  
Sir,  
Earlier I received an email stating I need to turn on my server **again** , but I am afraid that I will not be able to do so as I have already travelling and will be travelling till 18th. I am sure you will understand my situation and therefore requesting to please help/suggest on way forward. Thanking in advance for your valuable help and support.  
Kind Regards,  
Anushka Kumar (22f2000559)

---

Sir i have not received any email regarding this please look into my url

[project2final-beta.vercel.app](https://project2final-beta.vercel.app/)

### [TDS Solver](https://project2final-beta.vercel.app/)

Sorry to keep bothering you again and again but it is very important for me that my project 2 scores are up to the mark to pass kn the end term

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
sir i am sorry that i keep resending this same message but please clarify this alone sir.  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of an email. It is a message to a learner, informing them about a re-run of P2 Evaluations due to a low score. The email requests the learner to turn on their server endpoint from 11:00 pm to 2:00 am. It also specifies that the endpoint will be tested based on the official forms submitted and the provided link.
\*\*image text:\*\*
22t1 se2002
to me
Dear Learner,
We have decided to re-run P2 Evaluations on your endpoint server because of your low score.
We kindly request you to turn on your server endpoint from 11:00 pm to 02:00 am TONIGHT. After that you may turn off your server. You do not need to turn it on before 11:00
pm. We will start evaluations at 11:00pm and it will end at 2:00 am.
We will be testing the endpoint that you have submitted in the official forms only.
Please note that we will NOT test endpoints that you submitted in discourse or via email.
If you sent an updated endpoint in the latest form which we had sent, we will test that endpoint, otherwise we will use your previous endpoint. The endpoint we are testing is shown
below (no other endpoint will be tested):
https://e95b-2405-201-e04b-d085-9cf5-4f92-fe5a-309e.ngrok-free.app/ask

the mail i got mentions that no other endpoint will be tested and it is showing the old ngrok link. now if i edit the form and change the url will you consider the new one? please clarify sir…

---

image description: The image shows a screenshot of a form, possibly a Google Form. The form asks two questions about a project.
image text: What is the link to your GitHub repository which has the code for Project 2? \* It should look like https://github.com/user-name/repository-name https://github.com/kartikayy1/ project2final What is the link to your API endpoint? \* Make sure we can send a POST request to this exact URL https://project2final-beta.vercel.app/ Create your own Google Form Does this form look suspicious? Report Reply 99+

---

we are discussing it with operations. as soon as we know we will inform you.

---

I sincerely apologize for not using my official email address — it was an honest oversight and not an attempt to bypass any rules. I’d be truly grateful if you could kindly consider evaluating my project based on the valid, timely submission and the active working links provided.

This situation is quite distressing for me, as it could result in a significant setback, potentially requiring me to repeat the entire course. I fully acknowledge that the mistake was mine — a small yet critical one — and I sincerely request that if there is even a slight possibility of evaluation, please consider it.

Please let me know if there is anything I can do to assist with verification. Your understanding and support would genuinely mean a lot.

Thank you for your time and consideration.

---

Respected Carlton Sir,  
I thought in gform we need to submit the deployment url:

[tdsproject2-eight.vercel.app](https://tdsproject2-eight.vercel.app/)

### [TDS Solver](https://tdsproject2-eight.vercel.app/)

but for the API testing we need to add /api/ to the url:

<https://tdsproject2-eight.vercel.app/api/>

Please do my evaluation on this link, its the same just we need to go to /api/ in the URL

---

Sir i also did the same mistake and am truly sorry for what i did but it is my dearest request if you can look into this matter as it is very essential that the project is evaluated.  
I am once again very sorry for the mistake

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

Dear Sirs,

I apologize for the inconvenience caused by reaching out again. I came to know that many students have received an email stating that the re-evaluation for Project 2 will be conducted today between 11 PM and 2 AM. However, I have not received any such communication on my end.

I would like to bring to your attention that I actively helped several peers deploy their servers on Vercel and resolve various issues, and many of them received marks as high as 80. Unfortunately, my own record still shows as “Absent,” despite the fact that I submitted the Google Form well before the deadline and my server has been live and running for over two weeks.

For your verification, I am attaching screenshots of my GitHub repository and the Vercel deployment dashboard, which clearly show the deployment.

I sincerely request you to kindly consider this issue. This situation has caused significant mental stress, especially as I had already faced a grading issue in Project 1. The anxiety and uncertainty around my Project 2 score have negatively affected my focus during the end-term exam and viva for other projects as well. Receiving a zero in this project would only further impact my overall performance and morale, despite the genuine effort I have put in.

I genuinely hope for a positive response and a fair re-evaluation.

Thank you very much for your time and understanding.

api link : <https://tds-proj2f.vercel.app/>

image description: A screenshot of a GitHub repository overview. The repository is named "tds\_proj2f" and is public. It displays the main branch, with 1 branch and 0 tags. The latest commit is labeled "21f2000304 final commit" and shows a green checkmark. A list of files and folders is visible: .env, .gitignore, GA1.html, LICENSE, README.md, download.png, ga1.py, ga2.py, ga2\_6.py, and ga2\_9.py, each with a "final commit" label and the time elapsed as "2 weeks ago".
image text: tds\_proj2f Public Unpin Unwatch 1 main 1 Branch 0 Tags Go to file t Add file <> Code 21f2000304 final commit 2e818b2 2 weeks ago 1 Commit .env final commit 2 weeks ago .gitignore final commit 2 weeks ago GA1.html final commit 2 weeks ago LICENSE final commit 2 weeks ago README.md final commit 2 weeks ago download.png final commit 2 weeks ago ga1.py final commit 2 weeks ago ga2.py final commit 2 weeks ago ga2\_6.py final commit 2 weeks ago ga2\_9.py final commit 2 weeks ago

---

Respected Sir,

I thought we need to submit the deployment url in gform

[tdsproject2-eight.vercel.app](https://tdsproject2-eight.vercel.app/)

### [TDS Solver](https://tdsproject2-eight.vercel.app/)

but for the API testing we need to add /api/ to the url:

<https://tdsproject2-eight.vercel.app/api/>

Please do my evaluation on this link, its the same just we need to go to /api/ in the URL

thank you

---

[@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Respected Sir,  
Sir I made a mistake while submitting the GFORM in hurry, I submitted the deployment URL instead of API URL:  
currently for re-evaluation my URL that I received on my mail id is:

`https://tdsproject2-eight.vercel.app/`

but for API testing we need to add /api/ to the URL so final URL is:

`https://tdsproject2-eight.vercel.app/api/`

I’m sorry for this mistake sir, please accept this small change, we just need to add /api/ to the URL

Thank you

actually 2 of my friend had submitted similar url with no /api/ but he got 80 marks and I also submitted without /api/ url but I got 0 so for re evaluation sir please add /api/ to the original URL as mentioned Above Please Sir

Thank you  
23f2001390@ds.study.iitm.ac.in

---

[@carlton](/u/carlton) I appreciate your response. I didn’t include “/api” at the end. Could you confirm if I’m allowed to update the form now before tonight’s evaluation? Thanks in advance.

---

I would like to clarify that I had submitted the form before the deadline. However, I believe I might have submitted it once again after the deadline, just to ensure that my project was submitted correctly.  
Please find attached the screenshot of my submission made before the deadline. Also, I haven’t received any response sheet for the form submitted after the deadline.

Thank you!  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

image description: The image is a screenshot of an email from Google Forms. The email's subject is "TDS Project 2 - Jan 2025" and is marked as "Inbox". The sender is "Google Forms" and the date is "31 Mar". The email is addressed to "24ds1000119@ds.study.iitm.ac.in". The email also states that the message is "Standard encryption (TLS)" and provides a link to "See security details". The email body includes a message thanking the recipient for filling out "TDS Project 2 - Jan 2025" and offers an "Edit response" button. At the bottom of the screen, there are icons for mail, chat, and video calls with notification badges.
image text: TDS Project 2 - Jan 2025 Inbox
Google Forms 31 Mar
G to me
From Google Forms • forms-receipts
-noreply@google.com
To 24ds1000119@ds.study.iitm.ac.in
Date 31 Mar 2025, 11:47 pm
Standard encryption (TLS).
See security details
Google Forms
Thanks for filling out TDS
Project 2 - Jan 2025
Here's what was received.
Edit response

---

hello sir,  
the link have submitted has a UI interface for solving the question which looks somewhat like this  
image description: The image is a form or interface with a blue and purple gradient theme. At the top it says "TDS GA Solver". Below this, there is a text input field labeled "Ask a GA Question". Underneath, there is a section to upload a file labeled "Upload File (Optional)". There is a button labeled "Submit". Finally, there is a section for a "Response".
image text: TDS GA Solver
Ask a GA Question:
Type your question here...
Upload File (Optional):
Choose File No file chosen
Submit
Response:

in order to access the endpoint we just need to add “/api” on the end however in the form I have submitted the link without the end line.  
Please Consider,  
Thanks & Regards,

---

So anyone with an ngrok endpoint can send their new ngrok to us, but obviously you will need to start the server up much sooner than 11 in that case. An email will be sent to you specifically. DO NOT give us the endpoint on discourse. Reply to the email we will send specifically for you.

---

Hello,

For my results, it is marked as absent. Can you please confirm what has gone wrong as I am really confident I have submitted Gform on deadline day around 3-5pm. Thank you

[@carlton](/u/carlton)

---

I’m not able to restart my Virtual Machine as my Azure subscription has expired and my account is disabled.

Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of an email from Microsoft Azure. The email informs the recipient that their free credit has expired and they need to upgrade to a pay-as-you-go subscription to continue using Azure services. The email provides details about the benefits of upgrading. The email is marked as sent on Tue 4/15/2025 3:39 AM.
\*\*Image Text:\*\*
Microsoft Azure<azure-noreply@microsoft.com>
To: You
Tue 4/15/2025 3:39 AM
Microsoft Azure
Upgrade now to keep building in Azure
Your free credit has expired, so we've disabled your subscription and services. It's
an easy fix-just upgrade to a pay-as-you-go subscription to keep using all your
configured services and data in place. You get:
• 12 months of popular products for free.
• More than 25 products that are always free.
For everything else, only pay for what you use each month. It's easy to cancel, any
time.
Sign up for a new subscription >
We'll keep your subscription data before permanently deleting it on April 14, 2025.
Please log in and save any important data before then. Resume using your

Please suggest the way forward.

---

Since we will be evaluating between 11 to am you can run application on local machine and provide us with the ngrok url by 10:30 pm.

Send us the correct endpoint test it before sending us.

---

[@Jivraj](/u/jivraj)  
I should send ngrok endpoint replying to the same email u sent me right?  
No extra google form will be there right?

---

Yes to the same Mail

---

[@Jivraj](/u/jivraj)  
Dear Sir,

I’m sorry to bother you again, but I’m in a desperate situation and have no other option but to reach out through this channel.

As I mentioned in my previous message, my score has been marked as “absent,” even though I submitted my project well before the deadline. Additionally, I have not received any communication regarding a re-evaluation.

I kindly request you to look into this matter and provide a response at the earliest.

---

\***Request to Use Public DNS for Course Tool API Deployment or Use Alternate Endpoint**

Dear [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

I hope you’re doing well!

I’m currently running my server and trying to access the API hosted at:

```
https://sss-production-7a97.up.railway.app/api/

```

However, I’m encountering the following error:

```
curl: (6) Could not resolve host: sss-production-7a97.up.railway.app

```

After some investigation, I found that the issue is related to DNS resolution. The API becomes accessible when using **public DNS services** like **Google (8.8.8.8)** or **Cloudflare (1.1.1.1)**. This suggests that the current deployment environment may be using a restricted or unreliable DNS resolver, which causes access issues on some networks (e.g., Jio).

---

### :hammer_and_wrench: Suggested Fix:

To ensure reliable access for all students, could you please consider updating the deployment or testing environment to use a **public DNS** provider?

Recommended options:

* **Google DNS**: `8.8.8.8`, `8.8.4.4`
* **Cloudflare DNS**: `1.1.1.1`, `1.0.0.1`

This can typically be configured via Docker settings or the environment’s networking configuration.

---

### :repeat_button: Alternate Option:

If the DNS change isn’t possible at the moment, I kindly request that you evaluate my project using the **previously deployed endpoint** instead:

```
https://tds-project-2-pnlm.onrender.com/api/

```

Please note that this endpoint may take **50 to 60 seconds** to respond, as it’s hosted on a platform with a cold start delay — but it is fully functional and provides the correct outputs.

Both endpoints are currently active and return identical results.

---

Thank you so much for your time and support — I truly appreciate the effort you’re putting into helping us succeed in this course!

Best regards,  
**Sahil Raj**

---

Will it be possible for the evaluation of vercel link as well i have veen marked absent due to the email issues prevailing please look into this matter

---

Sir, my endpoint is deployed on render too. Hence it may take upto two minutes for the server to respond.  
Thankyou!

---

Thanks. These re evals are running on the gcloud vm so it should not be an issue, but we will check anyway. Its a good tip.

---

what should i do , i deleted my vm after the email that your evaluation completed , it is said in email that evaluation log and score will be sent but nothing come , it seems my updated api endpoint is not evaluated , score comes from previous endpoint , please what to do now ? again i am saying i deleted my vm [@s.anand](/u/s.anand) [@carlton](/u/carlton)

---

Dear [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

In the google form which we submitted I had pasted the API endpoint as the one which I got in the vercel dashboard i.e. <https://tds-project2-rho.vercel.app/>  
whereas the correct api for giving post requests has **/api** added to the above which i forgot to add. i.e\*\*.[https://tds-project2-rho.vercel.app/api/\*\*](https://tds-project2-rho.vercel.app/api/**)  
I have checked again and the post requests are working.  
I know that I made a mistake in the form and regret the same. If possible, please evaluate my project 2 with the above endpoint

---

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

These are my new endpoints: <https://gasolver-hgayefe7b0avhpc6.southindia-01.azurewebsites.net/api/> I have replied to the email regarding the re-evaluation message that was sent to me. Since I deleted the Azure Web Service Plan after receiving instructions from the TDS team to stop the service, I now need to host it again .Please let me know the next steps.

---

Greetings, [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

I hope this message finds you well.

I am writing to kindly request the addition of an API to the link I previously submitted for Project 2. I realized that including this API is essential for the complete functionality and demonstration of the project.

please use this api url -: <https://rahulbot-a369.onrender.com/api/>  
instead of this - <https://rahulbot-a369.onrender.com/>

Thank you for your time and support. Looking forward to your response.

Best regards,  
Rahul Pathak  
23f2000798@ds.study.iitm.ac.in

---

[@Pritul\_raut](/u/pritul_raut) , [@22f3001416](/u/22f3001416)

Start server locally and send us your ngrok url’s.

---

[@rahul\_pathak12](/u/rahul_pathak12) [@JerinJohn01](/u/jerinjohn01)

Please fill the form below we will only pick your endpoints from there, we won’t be picking from discourse posts.

[accounts.google.com](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfJQb2SmT-UKRM6Uc8lZ0Z3-hcgsv1Hn3M31dPqIFE48JXoVQ%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfJQb2SmT-UKRM6Uc8lZ0Z3-hcgsv1Hn3M31dPqIFE48JXoVQ%2Fviewform&ifkv=AXH0vVvOfa6rJTIw-NVj1wEvYsFmjKCtcgg1nN0BTd1vvajBbRTzOG5xg8FlZFBbhOS3XSlJ3DjRww&ltmpl=forms&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1911273912%3A1744825710700248)

### [Google Forms: Sign-in](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfJQb2SmT-UKRM6Uc8lZ0Z3-hcgsv1Hn3M31dPqIFE48JXoVQ%2Fviewform&followup=https%3A%2F%2Fdocs.google.com%2Fforms%2Fd%2Fe%2F1FAIpQLSfJQb2SmT-UKRM6Uc8lZ0Z3-hcgsv1Hn3M31dPqIFE48JXoVQ%2Fviewform&ifkv=AXH0vVvOfa6rJTIw-NVj1wEvYsFmjKCtcgg1nN0BTd1vvajBbRTzOG5xg8FlZFBbhOS3XSlJ3DjRww&ltmpl=forms&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1911273912%3A1744825710700248)

Access Google Forms with a personal Google account or Google Workspace account (for business use).

---

Hi @all

Please use the form that is sent. We will consider it if you send it as soon as possible. Please note that this is still at our discretion. We will try to consider everyones endpoint who submit on this form only.

<https://forms.gle/m2pzirzGvphPB5zq8>

---

Hi Jivraj,

I would like to draw attention to a specific question regarding the process of creating an HTML file and publishing it to GitHub. I notice that I am not providing a preloaded answer when this question arises. Instead, it creates a new repository and an HTML file, then deploys it on GitHub. Initially, it presents a URL, but I understand that your server checks to verify whether the URL contains valid HTML. This verification process takes time, which can lead to an incorrect response when checking the URL right after deployment.

At that moment, the URL might not display the HTML content or be verified by your server, even though eventually, the deployment is successful and the URL is correct. Please keep in mind that publishing to GitHub requires some time; it’s not feasible to expedite this process drastically, to my knowledge.

I checked and noted that this question has been asked recently.

Additionally, I believe the image may show your server’s IP address.

Thank you!  
image description: The image is a screenshot of a Windows PowerShell terminal. The text displayed shows a log or output from a data science tool, likely related to API requests. The text includes file paths, IP addresses, and status codes (200 OK). The focus of the text appears to be debugging or logging API calls.
image text:
ng question with file: E://data science tool//GA1//eighteenth.py
lution for: E://data science tool//GA1//eighteenth.py
3.158.43.22:0 - "POST /api/ HTTP/1.1" 200 OK
3:02:08,019 - tds\_app - INFO - Logged IP 103.158.43.22 accessing /api/
in: openai
3:02:08,102 - tds\_app - INFO - Logged IP 103.158.43.22 accessing /api/
: GitHub Pages query → GA2/third.py
in: github
E://data science tool//GA3//second.py (score: 0.41, confidence: 40%)
ng question with file: E://data science tool//GA3//second.py
lution for: E://data science tool//GA3//second.py
E://data science tool//GA2//third.py (score: 0.50, confidence: 50%)
ng question with file: E://data science tool//GA2//third.py
lution for: E://data science tool//GA2//third.py
3.158.43.22:0 - "POST /api/ HTTP/1.1" 200 OK
3:02:08,845 - tds\_app - INFO - Logged IP 103.158.43.22 accessing /api/
in: excel
E://data science tool//GA4//sixth.py (score: ua

---

How long you want us to keep timeout of request is, right now we have 60 seconds of timeout.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I have received 5 “200 OK” POST requests on my ngrok endpoint(which i had sent replying to [@Jivraj](/u/jivraj) email before 10:30 PM) between 11:02 PM to 11:05 PM.  
Do i need to update my previous gform? Or is everything done from my end?  
Im keeping server on till tomorrow morning.

---

[@carlton](/u/carlton) yes sir same doubt as [@GaURaVinDeX](/u/gauravindex) . i also got 5 200 ok requests in my terinal. i sent the url to the mail i got before. do i need to update this gform again? or Or is everything done from my end?  
I m keeping server on till tomorrow morning.

---

If you filled the gform that is sufficient.

---

sir i replied for the mail i recieved for new ngrok link. so now you are asking to fill this gform sir?

---

If you filled the gform before its fine. Its for all those that had accidently gave us wrong ones.

---

Sir, I replied to the email received by me from [@jivraj](/u/jivraj) as it was instructed. Should i fill gform now also?

---

Email to jivraj for ngrok was fine. Since he emailed you directly for the ngrok folks

---

Ok. Because our gform of 10th April has old ngrok endpoint which isnt valid now. Only the one which we have emailed to [@Jivraj](/u/jivraj) before 10:30 PM is current active. So i conclude our emailed ngrok endpoints of today to [@Jivraj](/u/jivraj) are enough.

---

Yes todays ngrok you sent to jivraj is fine. Because old ones are invalid

---

[@carlton](/u/carlton) Please recheck my project 2 also as I got 0 on dashboard. I and my two friends made this together but he got 80 and I got 0, how is this possible?

---

Sir, submitted the gform and also replied to the mail that I received about re-evaluation

---

sir , I got 39 with project 2 score as 0. Will fail by 1 mark if my project 2 is 0. haha…

---

You did not provide the right endpoint. Did you fill the form with the right endpoint.

---

deploying time the html page on GitHub page that is not in my hand

---

[algsoch.github.io](https://algsoch.github.io/portfolio-1744825944/)

### [Professional Portfolio | 24f2006438](https://algsoch.github.io/portfolio-1744825944/)

you can clearly see there is html page publish  
i think that time my api gave answer with this url

---

Do you have proof that you have submitted before deadline? Because the gfrom shows the timestamp of being after deadline

---

Sir, I had submitted the project on 31st March at 11:30 PM itself. However, I made a change to the Vercel endpoint and updated it on 1st April. I can provide a screenshot of the Vercel deployment as proof. Unfortunately, I didn’t keep a copy of the Google Form submission. But to be honest, I shared the deployed project with some of my friends on 1st and 2nd April, after my edit, and they submitted it through the form after me. They received marks, but I haven’t received the same.

---

Hi [@afsalshah](/u/afsalshah)

You submitted google form with wrong email address.  
This was the email address you used for filling form.

quizapp.mad2@gmail.com

---

Sorry, Sir. I just realized the reason why my submission was not considered — I had used the email ID I created specifically for my MAD2 project. It was a genuine mistake on my part. However, I noticed in a previous thread that another student who submitted using a different email ID was given a chance to update it. I kindly request you to consider giving me the same opportunity as well.  
I have given my endpoint to the gform circulated in this thread.

---

We didn’t account for such cases. The purpose of that form was to reevaluate only those who submitted using their IITM email but had provided the wrong endpoint.

Anyone who didn’t use their IITM email during submission—even if they later filled out the form—was filtered out and not considered for reevaluation.

---

I understand your point, Sir. It was a mistake on my part, but if possible, I kindly request you to consider my submission given the circumstances.

---

can you send this email which is there in screenshot to me(22f3002542@ds.study.iitm.ac.in) ?

If that proof you can give we will consider reevaluating.

---

Hi [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini) I believe it is a bit late now, but my Programming Quiz score is being displayed as Absent, I remember very well that I got a 4 out of 10, but it has been displaying Absent for a very long time now. This the ROE exam I am talking about here. Kindly fix this issue too.  
![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/4/a/4a37ffc853ba3bd69c6c09d59edfaff926abc7b4.png)

---

Hi Team,

Yesterday, I received a mail stating that our **Project 2** would be **reevaluated between 11 PM and 2 AM tonight**, and that the following endpoint would be used to test the API:

![:link:](https://emoji.discourse-cdn.com/google/link.png?v=14 ":link:") <https://project2llm-production.up.railway.app/api/>

However, I have not seen any logs in Railway during that timeframe, and my score on the dashboard is still showing as **0**.

Could you please confirm if my URL was actually reevaluated?

Thank you!  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@s.anand](/u/s.anand) [@Saransh\_Saini](/u/saransh_saini)

---

Dear Sir

Yesterday I received the mail to start my server from 11 pm to 2 am, but I am very sorry that I did not read the mail on time and hence could not start the server on time. I request you kindly to give a second chance for re evaluation. I have done the project and it would not be fair if it is not evaluated.

Thank you

---

Hi Team,

Please confirm if the evaluations were carried out last night as I don’t see any logs on my api. I had shared my updated ngrok link on email as well as the form shared yesterday.

Thank You!

---

yes i have filled that but i have tested my API many times before and after gform

---

I am really sorry sir for bothering you again and again but i kindly request you to look into this matter i had submitted my gform link but i am marked absent the link for my git repository is [GitHub - kartikayy1/project2final](https://github.com/kartikayy1/project2final)

And my vercel link is

[project2final-beta.vercel.app](https://project2final-beta.vercel.app/)

### [TDS Solver](https://project2final-beta.vercel.app/)

It is my humble request if you can evaluate the project and update my marks

---

I am really sorry sir for bothering you again and again but i kindly request you to look into this matter i had submitted my gform link but i am marked absent the link for my git repository is [GitHub - kartikayy1/project2final](https://github.com/kartikayy1/project2final)

And my vercel link is

[project2final-beta.vercel.app](https://project2final-beta.vercel.app/)

### [TDS Solver](https://project2final-beta.vercel.app/)

---

sir i didn’t get any mail regarding evaluation of project 2 yet , though i submitted it before the deadline

---

Sir, have the scores been updated after the re-evaluation? Will we receive logs for the evaluation?

---

You filled form after 11 pm, and we pulled out all the responses before 11 Pm.

---

yes logs will be sentout

---

And sir have the results been updated on Dashboard? Asking because the score’s still 0 on the dashboard.

---

**Subject:** Clarification Regarding Project 2 Reevaluation

Hi Team,

I received an email yesterday stating that our Project 2 would be reevaluated between 11 PM and 2 AM tonight.  
However, I haven’t seen any deployment logs on Railway during that timeframe, and my score on the dashboard is still showing as 0.

My url is working perfectly still there is no logs in the railway.

Could you please confirm whether my Project 2 was actually reevaluated?

Thank you!

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

Can you send us proof that you have submitted the form, I looked at the submissions and could not find your email there.

---

Your submission was reevaluated, I confirm that in timeframe of 11PM to 2 AM

---

No They will be updated by today.

---

I had replied to the email before 11pm with the updated URL as suggested by you in the earlier thread before the form was released.

I submitted the form as soon as I saw the message on discourse which was after 11pm.

---

You used this email address for submitting form

kingshubh011@gmail.com

Which is not IITM email address, how would we know whom it belongs to?

---

can you show us what you submitted? Was it a valid url ?

---

Oh no , i didn’t noticed because the deadline was about to end. But nothing can be done now? My project is working fine and the score i got in project 1 are also not good so I need the marks to improve my score

---

Sir! Is it possible that the railway won’t show any of the logs even if the api url is tested?

---

I don’t know answer to that question, have never used railway, you need to figure out yourself

---

Sir here is a screenshot of my google form that i submitted

---

Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of a mobile device screen, likely a form or a message exchange, with a dark theme. It contains text fields asking for links to a GitHub repository and an API endpoint.
\*\*Image Text:\*\*
\* What is the link to your GitHub repository which has the code for Project 2? \\*
\* It should look like https://github.com/user-name/repository-name
\* https://github.com/kartikayy1/project2final
\* What is the link to your API endpoint? \\*
\* Make sure we can send a POST request to this exact URL
\* https://project2final-beta.vercel.app/
\* Create your own Google Form
\* Does this form look suspicious? Report
\* Reply

---

I am really sorry sir i cant apologise enough but by mistake i used my personal email address instead of the iitm emial snd i deeply apologize for the inconveniences but i request you to kindly consider this project as it is very essential for me to pass this course  
I will make sure that such silly mistake does not happen in the future but i request you to please Consider this time.  
The email used would be [kartikaytaunk@gmail.com](mailto:kartikaytaunk@gmail.com)

---

[@Jivraj](/u/jivraj)  
Since html page take time to host and github link comes in output early … how will u guys will evaluate that question since after since website take extra 5-8 second to get live but the github url in output comes before that

---

image description: The image is a screenshot of a form in a dark mode interface. The form's content is related to updating URL endpoints. It includes a message explaining the purpose of the form and instructions to provide updated endpoints.
image text:
1:16 PM | 0.1KB/s
To streamline the process of URL endpoints
changes and accommodate your
grievances we have created this form for
you to be able to update your endpoints.
Your email (23f1002643@ds.study.iitm.ac.
in) was recorded when you submitted this
form.
Please provide your updated
endpoint.
If the endpoint changes, please edit
this form that you have already
submitted so that we can have the
latest endpoint. Do not submit
multiple forms.
\*
tds-ga-llm.vercel.app/api
Create your own Google Form
Does this form look suspicious? Report

---

Yes, the new page took about 5–10 seconds to go live after the GitHub repository was created when we used Gmail as a parameter.  
If the Gmail is fixed, we can hardcode it in advance.  
In our case, Gmail is a parameter, so the function should remain dynamic and it would take 5-10 second to go live after we received answer.

---

We are not evaluating any wrong submissions.

---

sir my project 2 is also showing 0 but it was working. pls check if it was not working at least give some marks for the effort that w have put. I also accept that we have learnt a lot in this course and marks doesnot matter. but after putting a lot of effort day and night getting a zero, gives a drastic discouragement to even look at the laptop. pls consider if possible.

---

I have completed and submitted the assigned project 2, and I have verified that it is working correctly as per the given instructions.

However, I noticed that the score awarded to me for the project is 0. I believe this may be an error, as my project meets the required criteria and functions as expected.

I kindly request you to review my submission and let me know if there was any issue during evaluation or submission that may have led to this result.

I have deployed the project on vercel as instructed.  
I have uploaded all the links in google form and submitted it.

To support this, I am attaching a screenshot of the PowerShell window that shows an example of my application running successfully for one of the questions.  
Here's a description of the image:
The image displays a command-line interface showing a series of commands and responses, likely related to a web API. The context involves using PowerShell to send a POST request to a specific URL. The response includes HTTP status, cache information, content details, and a JSON payload containing the "answer": 465 and "status": "success".
image text:
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows
PS C:\Users\anshu> http -f POST "https://tds-solver-lyart.vercel.app/api/" question="
>> Let's make sure you can write formulas in Google Sheets. Type this formula into Google Sheets. (It won't work in Excel)
>> =SUM(ARRAY\_CONSTRAIN(SEQUENCE(100, 100, 15, 7), 1, 10))
>> What is the result?"
HTTP/1.1 200 OK
Cache-Control: public, max-age=0, must-revalidate
Content-Length: 33
Content-Type: application/json
Date: Thu, 17 Apr 2025 04:23:01 GMT
Server: Vercel
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
X-Vercel-Cache: MISS
X-Vercel-Id: bom1::iad1::frgp2-1744863774071-f23dd132a3bb
{
"answer": 465,
"status": "success"
}

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) I appreciate the team incorporating my updated response at the endpoint with the “/api” path and re-evaluating accordingly, as well as sharing the results via email.

To my surprise, when I invoke the same endpoint that was evaluated — using the correct multipart/form-data payload with both question and file fields — I consistently receive a 200 OK response with the expected output.

Moreover, if I omit either field from the form-data, the server returns the exact validation error mentioned in the re-evaluation report, which makes sense. Based on this behavior and the details in the shared report, I’d like to confirm: during the re-evaluation, was the request payload indeed sent with both question and file fields included in the form-data?

For reference, I’ve attached a screenshot demonstrating the response.

image description: The image is a block of text on a black background. The text appears to be a list of API calls and their results. The calls all point to fileqa-app.vercel.app/api/. The tests are each marked as "FAILED" with the error: "HTTP 400: {\"error\":\"Missing question or file\"}".
image text:
```
[
{
"api": "https://fileqa-app.vercel.app/api/",
"test\_code": "GA1\_q18",
"status": "FAILED",
"error": "HTTP 400: {\"error\":\"Missing question or file\"}"
},
{
"api": "https://fileqa-app.vercel.app/api/",
"test\_code": "GA4\_q6",
"status": "FAILED",
"error": "HTTP 400: {\"error\":\"Missing question or file\"}"
},
{
"api": "https://fileqa-app.vercel.app/api/",
"test\_code": "GA2\_q3",
"status": "FAILED",
"error": "HTTP 400: {\"error\":\"Missing question or file\"}"
},
{
"api": "https://fileqa-app.vercel.app/api/",
"test\_code": "GA3\_q2",
"status": "FAILED",
"error": "HTTP 400: {\"error\":\"Missing question or file\"}"
},
{
"api": "https://fileqa-app.vercel.app/api/",
"test\_code": "GA5\_q7",
"status": "FAILED",
"error": "HTTP 400: {\"error\":\"Missing question or file\"}"
}
```  
Here's a description of the image:
The image is a screenshot of a POST request being sent via an API testing tool. The request is being sent to `https://fileqa-app.vercel.app/api/`. The "Body" section is active and uses "form-data". The "question" key is unchecked, but the "file" key is checked, with a file named `abcd.zip` is attached. An arrow points to the "Sending request without Question" text above the "Value" section. A "400 Bad Request" status is displayed after sending. The JSON response displays `{"error": "Missing question or file"}`. An arrow points to the "Response same as evaluvation" text below the response.
image text:
```
HTTP https://fileqa-app.vercel.app/api/
POST
https://fileqa-app.vercel.app/api/
Params Authorization Headers (9) Body Scripts Settings
none form-data
Key
question
file
Key
x-www-form-urlencoded
Body Cookies Headers (10) Test Results
raw binary GraphQL
Sending request without Question
Text
What is the value in the "answer" column of the ...
File
▲ abcd.zip
Text
Value
Description
Save
Share
Send
Cookies
...
Bulk Edit
400 Bad Request 1.92 s 433 B ...
{} JSON Preview Visualize
1
{
2
"error": "Missing question or file"
Response same as evaluvation
3
}
```  
Here's a description of the image:
The image is a screenshot of a web application or API testing tool, likely Postman, demonstrating a POST request.
Key elements and their descriptions:
\* \*\*URL:\*\* The target URL is `https://fileqa-app.vercel.app/api/`.
\* \*\*Request Method:\*\* POST.
\* \*\*Body:\*\* The request body is configured as `form-data`. The 'question' field is selected, while the 'file' field is not. The 'file' field has abcd.zip.
\* \*\*Response:\*\* The response to this request shows a JSON with an "error": "Missing question or file", and a 400 Bad Request status.
image text:
HTTP https://fileqa-app.vercel.app/api/
POST https://fileqa-app.vercel.app/api/
Params Authorization Headers (9) Body Scripts Settings
none form-data x-www-form-urlencoded raw binary GraphQL
Key Value Description Bulk Edit
question Text What is the value in the "answer" column of the ...
file File ▲ abcd.zip
Key Text Value Description
Body Cookies Headers (10) Test Results
{} JSON Preview Visualize
1 {
2 "error": "Missing question or file"
3 }
Sending req without file
response same as evaluvation report
Save Share
Send
Cookies
400 Bad Request • 774 ms • 433 B.
  
image description: The image is a screenshot of a tool used for API testing, likely Postman. It shows a POST request being sent to an API endpoint with "form-data" selected in the body. The body contains two key-value pairs: "question" with a text value and "file" with a file value. An arrow points to the "200 OK" status, indicating a successful response. Another arrow indicates the expected JSON response, which includes the key "answer" with the value "1234567890".
image text: POST https://fileqa-app.vercel.app/api/
Expected res code
Sent req with file/question both
Expected response
"answer": "1234567890"

---

image description: The image shows a text-based representation of JSON data, likely related to API testing or error reporting. It displays an array containing two objects. Each object describes a test case, specifying the API endpoint, a test code, a status ("FAILED"), and an error message. The error message consistently indicates an "HTTP 405" error, meaning the method is not allowed for the requested URL.
image text:
```json
[
{
"api": "https://tds-solver-bml0qi7k5-adityas-projects-07f86c8b.vercel.app/",
"test\_code": "GA1\_q18",
"status": "FAILED",
"error": "HTTP 405: <!doctype html>\n<html lang=en>\n<title>405 Method Not Allowed</title>\n<h1>Method Not
Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n"
},
{
"api": "https://tds-solver-bml0qi7k5-adityas-projects-07f86c8b.vercel.app/",
"test\_code": "GA4\_q6",
"status": "FAILED",
"error": "HTTP 405: <!doctype html>\n<html lang=en>\n<title>405 Method Not Allowed</title>\n<h1>Method Not
Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n"
},
```

> I would like to highlight an issue regarding the evaluation of the TDS Solver Project 2.

> As per the official project instructions, our API was clearly required to handle **POST** requests at /api/ with multipart/form-data.

> Nowhere in the documentation was it mentioned that the API should handle **GET** requests.

> However, during evaluation, GET requests seem to be made to the endpoint, leading to **405 Method Not Allowed** errors.

> These errors are expected behavior for an API that is properly built to accept only POST, exactly as per the project guidelines.

> Therefore, I request that the evaluation team **only test using POST requests** as originally instructed.

> Penalizing students because of unnecessary GET requests would be **unfair and incorrect** based on the project requirements.

> Please ensure that evaluation happens strictly according to the provided instructions.

---

For further more clarification to prove my endpoint is working as expected.

image description: The image is a screenshot of a Postman request and response. The user has changed the zip file to one that doesn't have a CSV file. The request is made to "https://fileqa-app.vercel.app/api/". The response received is "400 Bad Request" with the error message "No CSV file found in zip.".
image text:
https://fileqa-app.vercel.app/api/
POST
https://fileqa-app.vercel.app/api/
Params Authorization Headers (9) Body Scripts Settings
none form-data
x-www-form-urlencoded
raw
binary GraphQL
Key
Value
Description Changed the zip file
question
Text
What is the value in the "answer" column of the ...
which doesnt having
file
File
A q-move-rename-files.zip
any CSV.
Key
Text
Value
Description
Body Cookies Headers (10) Test Results
400 Bad Request 846 ms 434 B ...
{} JSON
Preview
Visualize
1
{
2
"error": "No CSV file found in zip."
Got the expected error response :)
3
}

Here's a description of the image:
The image is a screenshot of a web application interface, likely for making API requests.
Key elements:
\* \*\*URL:\*\* The URL `https://fileqa-app.vercel.app/api/` is visible in the address bar and used for a `POST` request.
\* \*\*Request Body:\*\* The "Body" section is highlighted. It includes two fields: `question` (type: Text) and `file` (type: File) with the value `abcd.zip`.
\* \*\*Response:\*\* The bottom section displays a JSON response with a key `"answer"` and a value of `"3812934199"`. The result is "200 OK".
\* \*\*Annotations:\*\* There are red arrows with text: "Updated the zip with new csv file with diff value" and "Got expected answer.".
image text:
HTTP https://fileqa-app.vercel.app/api/
POST https://fileqa-app.vercel.app/api/
Params Authorization Headers (9) Body • Scripts Settings
none form-data x-www-form-urlencoded raw binary GraphQL
Key Value Description ... Bulk Edit
question Text What is the value in the "answer" column of the ...
file File ▲ abcd.zip
Key Text Value Description
Updated the zip with new csv file
with diff value 200 OK • 1.16 s 410 B. ...
Body Cookies Headers (10) Test Results
{} JSON Preview Visualize
1 {
2 "answer": "3812934199"
3 }
Got expected answer.

image description: The image shows a screenshot of an API testing tool, likely Postman or a similar tool. It displays a POST request to a specific API endpoint. The request body is set to "form-data," and the screenshot focuses on the input fields. Two fields are visible: "question" with a text input and "file" with a file upload option, displaying "def.zip". Below, the response to the request in JSON format is visible. The response indicates an error: "Answer column not found or empty." The image is annotated with arrows and text, pointing to the file upload and the error message, indicating the expected outcome of the test.
image text: POST https://fileqa-app.vercel.app/api/ Params Authorization Headers (9) Body⚫ Scripts Settings none form-data x-www-form-urlencoded raw binary GraphQL Save Share Send Cookies Key Value Description ... Bulk Edit question Text What is the value in the "answer" column of the ... file File A def.zip Text Value Zip with new csv without any values. just having column names Body Cookies Headers (10) Test Results ① {} JSON Preview Visualize 1 { 2 "error": "Answer column not found or empty." 3 } Expected error answer :)

If there are any additional scenarios you’d like me to test, feel free to let me know, I’d be happy to help validate that the endpoint is functioning as expected. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

image description: The image displays a block of code formatted as a JSON object. The code includes information about an API, a test code, a status indicating an error, and an error message related to a SQL syntax error.
image text: ```
{
"api": "https://roe-i6ghzat4g-manu-cs-projects.vercel.app/api/",
"test\_code": "GA1\_q18",
"status": "ERROR",
"error": "near \"```sql\nSELECT SUM(price\* units) AS total\_sales\nFROM tickets\nWHERE LOWER (type) = 'gold';\n```\": syntax error"
}
```  
the answer is correct expect for extra spaces it was told that those spaces are neglectable still it showed as error plz consider this [@carlton](/u/carlton)

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
this was one of the question it asked on api  
‘’‘{  
“api”: “<https://app.algsoch.tech/api/>”,  
“test\_code”: “GA2\_q3”,  
“status”: “FAILED”,  
“actual”: “ tag not found”,  
“expected”: “24f2006438@ds.study.iitm.ac.in”  
},’‘’  
Now I am demonstrating that my HTML page includes an email tag. You can see it here.  
image description: The image has a blue background with white text in it. At the top is the text "Get In Touch" with the phrase "Feel free to reach out for collaborations or just a friendly chat!" below. Below this, is the email address "24f2006438@ds.study.iitm.ac.in". At the bottom are 3 icons for GitHub, LinkedIn and Twitter.
image text: Get In Touch
Feel free to reach out for collaborations or just a friendly chat!
Email: 24f2006438@ds.study.iitm.ac.in
in

and  
{  
“api”: “<https://app.algsoch.tech/api/>”,  
“test\_code”: “GA4\_q6”,  
“status”: “FAILED”,  
“actual”: “[GitHub - sminez/ad: an adaptable text editor](https://github.com/sminez/ad)”,  
“expected”: “[The 2FA app that tells you when you get `314159`](https://blog.jacobstechtavern.com/p/building-a-2fa-app-that-detects-patterns)”  
}  
I am unsure of the exact question, but it seems that the question can be modified with search terms and points. For example, in the account, it was stated as [‘text editor’, at least 77 points’]. If this were the parameter, then my answer would be correct, and I have proof.  
image description: The image shows a Hacker News search result page. There are two "Ad" listings for "An Adaptable Text Editor", both with the URL "https://github.com/sminez/ad".
image text: H
Search Hacker News
Search Stories by Popularity for All time
Ad: An Adaptable Text Editor (https://github.com/sminez/ad)
142 points | xelxebar | 4 months ago | 61 comments
Ad: An Adaptable Text Editor (https://github.com/sminez/ad)
5 points | todsacerdoti | 8 months ago | 1 comments

and this  
{  
“api”: “<https://app.algsoch.tech/api/>”,  
“test\_code”: “GA3\_q2”,  
“status”: “FAILED”,  
“actual”: 125,  
“expected”: “Range: 55 to 65”  
}  
I’m not sure what the exact question was, but it was correct for me again. I have another question or doubt.

---

Case 3: JSON Key Count – XF Parameter (GA5\_q7)

{

“api”: “<https://app.algsoch.tech/api/>”,

“test\_code”: “GA5\_q7”,

“status”: “ERROR”,

“error”: “invalid literal for int() with base 10: ‘Error: Invalid JSON in the file. Expecting value: line 1 column 1 (char 0)’”

}

#### :memo: What Was Expected:

The question required developing a script that:

* Parses a large, deeply nested JSON log file, and
* Counts how many times a specific key — represented by XF — appears in the JSON structure.

It was explicitly stated that:

* Only key matches for XF are to be counted, not values.
* The file to be used was:  
  E:\data science tool\GA5\q-extract-nested-json-keys.json

#### :white_check_mark: What I Did:

I used the correct approach, parsing the nested JSON file and counting how many times the key XF appeared throughout the structure.

Here’s the actual response I got using this cURL command:

curl -X POST <https://app.algsoch.tech/api/> \

-H “accept: application/json” \

-F “question=…How many times does XF appear as a key?” \

-F “file=@E:\data science tool\GA5\q-extract-nested-json-keys.json”

API Output:{“answer”:“14602”}

This indicates that my logic worked correctly and the key XF appeared 14,602 times, exactly as intended.

#### :warning: What Went Wrong on API Side:

The API returned a parsing error, indicating:

“invalid literal for int() with base 10: ‘Error: Invalid JSON in the file…’”

However:

* My file was valid JSON, properly parsed.
* The actual issue seems to be on the API’s side — possibly mishandling the file read or decoding before passing it to the evaluator.
* It may have expected an integer but received a string-wrapped error or non-integer data, causing it to crash.

#### :light_bulb: Insight:

If the original question was about counting the key XF, my solution was 100% correct.

However, if the question dynamically changed the key name or added extra criteria (e.g., only count if value == true, or only under a certain section), then the result might differ. But from the default XF-focused question, my logic and result match perfectly.

---

image description: The image shows a JSON object with "api", "test\\_code", "status" and "error" keys. The error shows a SQL syntax error.
image text:
```json
[
{
"api": "https://roe-i6ghzat4g-manu-cs-projects.vercel.app/api/",
"test\_code": "GA1\_q18",
"status": "ERROR",
"error": "near \"```sql\nSELECT SUM(price \* units) AS total\_sales\nFROM tickets\nWHERE LOWER(type) = 'gold';\n```\": syntax error"
},
```

in this question even though the answer is correct except those extra spaces it has been showing error plz check into this [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

## Issue with Marks Not Updated on Dashboard

Dear Team,

I would like to bring to your attention that although I have successfully passed **at least one out of the five questions**, the marks have **not yet been updated** in my dashboard.

Kindly look into this issue and update my Project 2 marks accordingly.

Thank you for your assistance!  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

[@23f2002286](/u/23f2002286) and everyone else,

At the end of the term operations has a lot of updates to push. We have sent the marks to them, but they have not yet pushed it to the dashboard. As soon as they push it, they will inform us and we will then send out a discrepancy form to all of you if you find any issues.

Thanks and Kind regards

---

I had completed project 2 but because of a mistake i filled the form with my personal mail id fue to which the project eas not evaluated i fully consider this to be my fault and assure that something like this will not happen in the future .

If my evaluation of project 2 is not done then i will fail the tds course and will have to repeat this course which will cause a financial strain on me

I know that it is difficult for you to consider this request but it is my humblest request if you can just look through the project i tried to complete the project with the best of my abilities

It will be really helpful if you can access the project  
My git repository link is - GitHub - kartikayy1/project2final

My vercel link is - <https://project2final-beta.vercel.app/>

---

initially I have received a score of 80 for project 2 but today im seeing on my dashboard it is showing 0. I request you to please check the discrepancy. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

my roll no is 23f1002558

---

My project 2 score is showing absent, roll num is 23f1000561.

---

Good Afternoon Sir.  
This is regarding project 1 and project 2.

**Project-1 Evaluation**  
Sir, For the project 1, I have written the code, uploaded in GitHub and the dockerfile image is created and uploaded successfully.  
Sir, I already contacted regarding Project - 1, you said to check it by replicating the test environment. I did till running the dockerfile but I needed evaluate.py sir, which I didn’t get it. I got only 5 marks sir. Can you please check my code once sir and verify it as I have written the code and the dockerfile is running successfully.

**Project-2 Evaluation**  
Regarding project 2 also, I have uploaded my code in GitHub and deployed my app in Vercel. But, I got 0 sir. Can you check my code once again and verify it? According to the guidance given, I deployed my app through Vercel. The app got deployed but I am getting 404 Error, even after trying any troubleshooting method. Maybe, Vercel is in development stage.

Sir, but I wrote the code and deployed, but I got 0 marks only. Please check it and guide me to get it corrected. Sir, due to the projects I got poor marks on TDS. Please, I request you to re-evaluate and give me correct marks.

In anticipation of quick response  
Thank You

---

Hi everyone,

I know that some of you might be feeling anxious about your scores etc. We are currently in the process of validating your scores on all the projects, roe, assignments, exam and bonus, so we will not be able to respond quickly to each individual post here for the time being.

Once we validate, you will receive an email with your official scores that we will be pushing to Operations in a single update. Along with that email you will receive a discrepancy form where you can raise your issues. This will give us a consolidated view of problems and fix them.

Kindly wait for the email to come to you. It will be sent sometime this afternoon.

Kind regards,

TDS Team

---

Here's a description of the image:
The image is a screenshot of a Gmail window displaying an email. The email is about "TDS Project 2 Endpoints". The email's content includes a message to learners regarding changes to the project's endpoints and a form to update the endpoints. The email is from a sender associated with "IIT Madras".
image text:
My Dashboard - IIT MX Project 2 :: IITM Onlin X Project 2 - TDS Solver × Project 2 X TDS Project 2 - Jan 20 X MTDS Project 2 Endpoi X
Gmail
Q project 2
99+
Compose
Mail
Inbox
4,645
Chat
☆Starred
Snoozed
► Sent
Π
Edit response
TDS Project 2 Endpoints
Dear Learner,
☆
O
IIT Madras
A
X
5 of many
Due to some major operational changes in the backend, we have had some unforeseen delays in conducting the evaluations of Project 2 Endpoints. As a result, some of you, have had to restart your servers or enact some other changes to your servers in order to keep the endpoints alive. This may have resulted in your URLs changing.
+
Drafts
► Categories
More
To streamline the process of URL endpoints changes and accommodate your grievances we have created this form for you to be able to update your endpoints.
Labels
+
proctor
Your email address (23f1002942@ds.study.iitm.ac.in) was recorded when you submitted this form.
Type here to search
Please provide your updated endpoint.
If the endpoint changes, please edit this form that you have already submitted so that we can have the latest endpoint. Do not submit multiple forms.
^) ENG
14:34
18-04-2025

Dear Team,

this is proof that I have successfully submitted the form and the api is still working, why am i still marked as absent? Please respond my email is 23f1002942@ds.study.iitm.ac.in

---

Sir I have been marked Absent for the ROE exam, I was very much present and got a 4 out of 10, can you please check?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
Why am my I getting `GET` request to my api endpoint? It must be IITM’s http request because I have not shared it with anyone.

image description: The image shows a log of HTTP requests, with each line indicating an IP address, a timestamp, a request method (GET, PRI), the requested URL, and a status code (404 Not Found). Many of the requests resulted in a "404 Not Found" error, indicating that the requested resources were not found on the server. The image also contains "WARNING" lines indicating that invalid HTTP requests were received.
image text:
```
INFO: 123.160.223.72:54416 - "GET / HTTP/1.1" 404 Not Found
INFO: 198.235.24.156:61106 - "GET / HTTP/1.1" 404 Not Found
INFO: 137.184.237.203:49008 - "GET /squid-internal-mgr/cachemgr.cgi HTTP/1.1" 404 Not Found
INFO: 34.76.133.13:39380 - "GET / HTTP/1.1" 404 Not Found
INFO: 185.226.197.28:57285 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 44.220.185.78:44772 - "GET / HTTP/1.1" 404 Not Found
INFO: 196.251.71.213:41752 - "GET / HTTP/1.1" 404 Not Found
INFO: 147.185.132.19:60588 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 138.197.93.48:57332 - "GET / HTTP/1.1" 404 Not Found
INFO: 138.197.93.48:57340 - "GET /login HTTP/1.1" 404 Not Found
INFO: 147.185.132.240:63132 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 206.168.34.39:48972 - "GET / HTTP/1.1" 404 Not Found
INFO: 206.168.34.39:48984 - "PRI %2A HTTP/2.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 206.168.34.39:37652 - "GET /favicon.ico HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 205.210.31.25:63138 - "GET / HTTP/1.1" 404 Not Found
INFO: 182.52.66.178:57068 - "GET / HTTP/1.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 3.145.63.56:41312 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 64.62.156.156:8435 - "GET / HTTP/1.1" 404 Not Found
INFO: 64.62.156.157:49175 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO: 64.62.156.158:49711 - "GET http%3A//api.ipify.org/?format=json HTTP/1.1" 404 Not Found
INFO: 64.62.156.153:15905 - "CONNECT www.shadowserver.org%3A443 HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 199.45.155.111:37700 - "GET / HTTP/1.1" 404 Not Found
INFO: 199.45.155.111:45862 - "GET / HTTP/1.1" 404 Not Found
INFO: 199.45.155.111:45878 - "PRI %2A HTTP/2.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 199.45.155.111:43082 - "GET /favicon.ico HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 198.235.24.231:64768 - "GET / HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 64.227.97.195:58406 - "GET /squid-internal-mgr/cachemgr.cgi HTTP/1.1" 404 Not Found
INFO: 167.94.146.62:57102 - "GET / HTTP/1.1" 404 Not Found
INFO: 167.94.146.62:48726 - "GET / HTTP/1.1" 404 Not Found
INFO: 167.94.146.62:48728 - "PRI %2A HTTP/2.0" 404 Not Found
WARNING: Invalid HTTP request received.
INFO: 167.94.146.62:48730 - "GET /favicon.ico HTTP/1.1" 404 Not Found
WARNING: Invalid HTTP request received.
WARNING: Invalid HTTP request received.
INFO: 15.235.224.227:56193 - "GET / HTTP/1.1" 404 Not Found
```

It clearly written in the project 2 in TDS portal that api must accept `POST` request, not `GET`.

image description : The image shows a code snippet related to API endpoint interaction using curl commands, explaining how to make a POST request with optional file attachments. The text provides instructions on how to submit a request to an API endpoint, including a question and a file attachment, using the multipart/form-data format.
image text: Your application exposes an API endpoint. Let's assume that it is at https://your-app.vercel.app/api/ .
The endpoint must accept a POST request, e.g. POST https://your-app.vercel.app/api/ with the question as well as optional file attachments as multipart/form-data.
For example, here's how anyone can make a request:
```bash
curl -X POST "https://your-app.vercel.app/api/" \
-H "Content-Type: multipart/form-data" \
-F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is t
-F "file=@abcd.zip"
```

It is requested to kindly look into this matter and please clarify.

---

when we get log files for project 2

---

I had completed project 2 but because of a mistake i filled the form with my personal mail id fue to which the project eas not evaluated i fully consider this to be my fault and assure that something like this will not happen in the future .

If my evaluation of project 2 is not done then i will fail the tds course and will have to repeat this course which will cause a financial strain on me

I know that it is difficult for you to consider this request but it is my humblest request if you can just look through the project i tried to complete the project with the best of my abilities

It will be really helpful if you can access the project  
My git repository link is - GitHub - kartikayy1/project2final

My vercel link is - <https://project2final-beta.vercel.app/>

---

I am also receiving the odd GET requests, however, I don’t believe these are being sent by the evaluation teams. Our endpoints are open to internet and there are bots everywhere which will send these kind of random requests to scan for potential exploit/hacking targets.

---

Good Evening, I shreyansh Singh have been marked absent even though I submitted, 23f2002745

---

Maybe. Still clarification from [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) will be highly appreciated.

---

I too was getting these requests.

[@carlton](/u/carlton) sir mentioned this in one of the posts:

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[Project 2 - TDS Solver - Discussion Thread](https://discourse.onlinedegree.iitm.ac.in/t/project-2-tds-solver-discussion-thread/169029/367) [Tools in Data Science](/c/courses/tds-kb/34)

> They are malicious probes. A global cyber war is going on. So anything that can be compromised is being probed.

---

Just recieved this on my mail. Happy that everything worked out pretty well w/o the need for hardcoding. I’m guessing GA1-q18 bugged out because of escape sequences in the codeblock ![:joy:](https://emoji.discourse-cdn.com/google/joy.png?v=14 ":joy:") That’s LLMs for you!

Can’t expect 100% reliability, even at 0 temperature.

image description: The image displays a JSON file with a list of test results. The first test, "GA1\_q18", has an "ERROR" status and an error message indicating a syntax issue. The other tests ("GA2\_q3", "GA3\_q2", "GA4\_q6", "GA5\_q7") have a "PASSED" status.
image text:
```json
[
{
"test\_code": "GA1\_q18",
"status": "ERROR",
"error": "near \"`sql\\nSELECT SUM(units \* price) AS total\_sales\\nFROM tickets\\nWHERE LOWER(type) = 'gold';\\n```\": syntax error"
},
{
"test\_code": "GA2\_q3",
"status": "PASSED"
},
{
"test\_code": "GA3\_q2",
"status": "PASSED"
},
{
"test\_code": "GA4\_q6",
"status": "PASSED"
},
{
"test\_code": "GA5\_q7",
"status": "PASSED"
}
]
```

---

I have received the test result of Project 2 todat afternoon, it is showing GA 2 question 2 has failed but my answer is a hardcoded url (“<https://23f2004837.github.io/>”) from the code. This url is accessible and again tested of the GA platform for the same question and it is working as expected

Code:  
image description: The image displays the code of a Python script named "Q23.py" within a GitHub repository. The code includes import statements, a function definition ("execute"), and a dictionary named "cache" containing various email addresses and their corresponding URLs. There are also conditional statements to retrieve data based on an email parameter.
image text:
```
https://github.com/TDS-Hackers/GASolver/blob/main/GA2/Q23.py
TDS-Hackers / GASolver
Issues Pull requests Actions Projects 1 Wiki Security 2 Insights Sett
es
in
to file
GASolver / GA2/ Q23.py
+
23f2004837 Version 1
t
Code Blame 132 lines (105 loc) 4.37 KB
scode
1
A1
2
A2
3
4
Q21.py
5
Q210.py
6
7
Q22.py
8
9
Q23.py
10
Q24.py
11
12
Q25.py
13
Q26.py
14
15
Q27.py
16
import os, json
def execute(question: str, parameter):
#return gitPortfolio (parameter ["email"])
cache = {
}
"23f2004837@ds.study.iitm.ac.in": "https://23f2004837.github.io/'
"21f2000588@ds.study.iitm.ac.in": "https://digvijaysinhchudasamai
"24f2006749@ds.study.iitm.ac.in": "https://sakshi6749.github.io/po
"22f3002188@ds.study.iitm.ac.in": "https://22f3002188.github.io/pc
"22f2001590@ds.study.iitm.ac.in": "https://22f2001590.github.io/TD
if parameter ["email"] not in cache:
return {"Enter the value in url\_cache"}
return cache [parameter ["email"]]
```

url result:  
image description: The image shows a screenshot of a webpage. The title bar of the browser shows "https://23f2004837.github.io". Below, the email "23f2004837@ds.study.iitm.ac.in" is prominently displayed. Two more instances of the same email address are present below.
image text:
23f2004837@ds.study.iitm.ac.in
23f2004837@ds.study.iitm.ac.in
23f2004837@ds.study.iitm.ac.in

html elements:  
Here's a description of the image:
The image is a screenshot of a web browser's developer tools, specifically the "Elements" panel. It displays the HTML structure of a webpage.
Here's a breakdown of the elements:
\* \*\*HTML Structure:\*\* The HTML code is structured with the standard elements.
\* \*\*Specific Content:\*\* The code includes an `<h1>` tag with the text "23f2004837@ds.study.iitm.ac.in" and a `<p>` tag with an email link using the same email address.
image text:
```html
<html>
<head> </head>
<body>
<h1>23f2004837@ds.study.iitm.ac.in</h1>
" 23f2004837@ds.study.iitm.ac.in"
<p> == $0
<a href="mailto:23f2004837@ds.study.iitm.ac.in">23f2004837@ds.study.iitm.ac.in</a>
</p>
</body>
</html>
```

GA portal:  
image description: The image is a screenshot of a web browser's developer tools, focused on the "Sources" tab. The browser is displaying the code for "exam.js." Above, there is a prompt asking about the GitHub Pages URL. The provided URL is `https://23f2004837.github.io/`. The code highlighted in yellow is related to the URL, containing the URL within the code.
image text: What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/
https://23f2004837.github.io/
Checking...
If a recent change that's not reflected, add ?v=1, ?v=2 to the URL to bust the cache.
exam.js
y = await $(f) y = true, $ = async a=>{...}, f = "https://23f2004837.github.io/"
} catch (){
R = \_ R = "Incorrect. Try again."
}
else
$ === null ? f && (y = !0) : y = f === $.toString(); $ = async a=>{...}, f = "https://23f2004837.github.io/", y = true
return d[e] = y ? r[e].weight : 0,

image description: The image is a screenshot. The image shows a question about GitHub Pages URL. The answer is given and it is marked as "Correct".
image text: What is the GitHub Pages URL? It might look like: https://[USER].github.io/[REPO]/
https://23f2004837.github.io/
Correct

Please let me know what can I do get the evaluation logs.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@jkmadathil](/u/jkmadathil)

---

What’s the error in the log? It’s GA2 Question 3. I can see u haven’t wrapped your email address inside `<!--email_off-->` tag.

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
I have posted my Project 2 Discrepency here [Urgent Attn Needed: Project 2 Discrepency for GA2\_q3 and GA1\_q18](https://discourse.onlinedegree.iitm.ac.in/t/urgent-attn-needed-project-2-discrepency-for-ga2-q3-and-ga1-q18/173113):

---

[@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
I would like to bring to your attention that the project URL I submitted was accessible and working correctly in my browser, even without the “http” or “https” prefix. A friend of mine submitted a similar URL and received full marks. Furthermore, I have updated my URL using HTTPS via Google Forms, so I kindly request you to consider evaluating my project using the latest URL provided.

This is a humble request, as I am currently at risk of receiving a grade ‘E’, which will significantly impact my overall CGPA. As an alternative, I am also willing to retake the course in the next term and pay the fee again if needed.

In the P1, unfortunately scored zero due to a minor mistake and was not given an opportunity to correct it. I truly believe that in real-life scenarios, we are often given chances to rectify such errors, and I sincerely hope for the same consideration here.

---

[@s.anand](/u/s.anand)  
**Subject:** Request to Share My Student-Built TDS Assistant Platform

Dear Sir/Madam,

I hope you’re doing well.

I’m **Vicky Kumar**, a student from the Data Science and Applications program at **IIT Madras**. Over the last few months, I’ve built a personal project called **“Vicky App”** — a smart assistant platform specifically designed to help students in courses like **TDS,**.

The system is capable of:

* Accurately solving over **90% of assignment-style questions** using regex and phonetic matching
* Dynamically executing the right code logic based on the student’s input
* Processing uploaded files such as Excel, PDF, CSV, and JSON
* Delivering instant answers, completely independent of ChatGPT or any external LLM

You can test the platform here: <https://app.algsoch.tech>

---

### :light_bulb: What’s in it for students:

* They type their question, and the backend executes the correct solution automatically
* Especially helpful for GA preparation, understanding problem logic, and reducing repetitive workload
* I’ve made it **free for the first 3 questions**
* After that, students can access the full platform for just **₹199/month**, which helps me cover system maintenance and hosting costs

---

### :folded_hands: My Humble Request:

This is a tool I’ve built with immense effort and love for this course, and I genuinely believe it can benefit many students.

To sustain the platform — hosting, APIs, file management, and backend orchestration — I’ve introduced a small paid model after a free trial.

I would be extremely grateful if you could test it once and, if you find it helpful, consider sharing it with upcoming students or mentioning it in a Moodle announcement.

It’s built *by an IIT Madras student, for IIT Madras students* — with the sole goal of making their learning smoother, faster, and smarter.

Thank you so much for your time and support.

Warm regards,  
**Vicky Kumar**  
B.S. Data Science and Applications, IIT Madras  
![:e_mail:](https://emoji.discourse-cdn.com/google/e_mail.png?v=14 ":e_mail:") [npdimagine@gmail.com](mailto:npdimagine@gmail.com) | ![:mobile_phone:](https://emoji.discourse-cdn.com/google/mobile_phone.png?v=14 ":mobile_phone:") +91 8383848219  
![:globe_with_meridians:](https://emoji.discourse-cdn.com/google/globe_with_meridians.png?v=14 ":globe_with_meridians:") [Portfolio](https://sites.google.com/view/vicky-kumar/home) | [LinkedIn](https://www.linkedin.com/in/algsoch/)

It’s a tool built by a fellow IITM student, with deep respect for the academic rigor of this program — not to replace learning, but to accelerate it.

Please let me know if you’d like a walkthrough, or if any suggestions for improvements arise.

Warm regards,  
**Vicky Kumar**  
B.S. Data Science and Applications, IIT Madras  
[npdimagine@gmail.com](mailto:npdimagine@gmail.com) | +91 8383848219  
[LinkedIn](https://www.linkedin.com/in/algsoch/) | Portfolio

---

