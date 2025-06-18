# ga4-data-sourcing-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 4 - Data Sourcing](https://exam.sanand.workers.dev/tds-2025-01-ga4).

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

---

image description: The image shows a question and a JSON data block, as well as an error message. The question is "What is the JSON data?". Below the question, there is a data structure with fields: "id", "title", "year", and "rating". The error message indicates an expected value of 2.9, which is the same as the actual value.
image text: What is the JSON data?
"id": "tt7144296",
"title": "1. Kiss and Kill",
"year": 2017,
"rating": 2.9
},
Error: Expected: 2.9 Actual: 2.9
  
what is the error here?? sir [@Jivraj](/u/jivraj)

---

I have the Same doubt.

---

[@22f3001315](/u/22f3001315) [@21f3002277](/u/21f3002277) [@24ds2000024](/u/24ds2000024) – please try again after reloading the page. The new error message will be clearer, like this:

```
Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

```

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit: This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

[@23f2000237](/u/23f2000237) A good point. Yes, please include *all* titles. I’ve reworded the question accordingly. Thanks.

---

Q3. How to handle the error ? [@Jivraj](/u/jivraj)

TypeError: Cannot read properties of null (reading ‘0’)

```
http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}

```

error resolved

---

in my output which is correct  
there are two \n instead of one .

---

it should one(for newline), my code is working now

---

Dear Sir,  
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

Q4. How to handle the error ? [@Jivraj](/u/jivraj)

Error: At 2025-02-05: Values don’t match

---

There is no submit button is available in below screen. Is it fine to save the link url only. Please clarify (unless we click submit button the log of Graded Assignment 4 remains red)  
image description: The screenshot shows a webpage related to a graded assignment within an online course platform, likely for an IIT Madras course. The left side panel displays modules, with "Graded Assignment 4" highlighted under "Module 4: Data Sourcing". The main content displays the details of the assignment, including its due date, submission guidelines, and potential troubleshooting steps for access issues. The page also provides a link to access the assignment.
image text: Graded Assignment 4
Due date for this assignment: 2025-02-09, 23:59 IST.
You may submit any number of times before the due date. The final submission will be considered for grading.
If you have any difficulty accessing the graded assignment, please check the following causes:
Ad blockers need to be disabled/removed.
The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
Javascript is required for the site to work correctly.
Chrome Browser is the recommended software to access the contents.
Disable any browser extensions that may be interfere with the site from working correctly.
Overly aggressive anti-virus software may also cause similar access problems.
Corporate proxies and network policies may also cause access issues. Try and use your mobile internet or another network.
You must use your Student ID (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the graded assignment, otherwise your score will not be considered for evaluation.
Graded Assignment 4 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga4. Please attempt it.

---

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?  
(Assuming they have interacted in this thread)

---

Anyone scoring 10/10 on GA4 and replying with a *relevant* message on this thread will get 11/10 ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

For me I just made filter of rating between 2 and 7 in site and typed in console as per video. with that data got in console worked fine.  
copy the coding and save in place use it for data extract when finally submit

---

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name  
Here's a description of the image:
The image shows a search result page. On the left, there are search filters with "Title name" and a search bar filled with the text "Un matrimonio di troppo". The right side displays a graphic of a magnifying glass with an "X" through it, indicating "No results found". Below the graphic are the text "No results found" and "Please adjust your filters or start a new search".
image text: Search filters Expand all Title name Un matrimonio di troppo Title type X No results found Please adjust your filters or start a new search

---

how to get the BBC weather API key?

---

Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

[@JoelJeffrey](/u/joeljeffrey) It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---

you can go and login using your email id in this below mentioned link

<https://home.openweathermap.org/api_keys>

---

Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”

Can someone help me with this?  
Thanks

Edit: Resolved

---

Q8 I got the Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in. the .yml file contains the following  
" name: Daily Commit

on:  
schedule:  
- cron: ‘0 12 \* \* \*’ # Runs daily at 12:00 PM UTC  
workflow\_dispatch: # This allows manual trigger

jobs:  
commit:  
runs-on: ubuntu-latest

```
steps:
- name: Checkout repository
  uses: actions/checkout@v2

- name: Make a dummy change with email 23f2003853@ds.study.iitm.ac.in in the commit
  run: |
    echo "This is a daily commit" > daily_commit.txt
    git config --global user.email "23f2003853@ds.study.iitm.ac.in"
    git config --global user.name "23f2003853"
    git add daily_commit.txt
    git commit -m "Daily commit from 23f2003853@ds.study.iitm.ac.in"
    git push"

```

[@Jivraj](/u/jivraj) can help me to fix the issue

---

Have a step with your email id as its name. (Instead of checkout repository)  
Also make sure you give read and write permission so it commits without any error

---

name: Daily Commit

on:  
schedule:  
- cron: ‘0 0 \* \* \*’ # Runs once a day at midnight UTC  
workflow\_dispatch: # Allows manual triggering of the workflow

jobs:  
commit:  
runs-on: ubuntu-latest

```
steps:
- name: Checkout repository
  uses: actions/checkout@v3

- name: Make daily commit by 23f3000264@ds.study.iitm.ac.in
  run: |
    echo "Daily commit by 23f3000264@ds.study.iitm.ac.in" >> daily_commit.txt
    git add index.html
    git commit -m "Daily commit"
    git push
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

```

sir this is my code and im getting a error in this  
image description : The image is a screenshot of a terminal-like interface. It displays a prompt for entering a repository URL, a URL entered by a user, and an error message.
image text: Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/dakshagarwal76/daily-update
Error: No executed job step matches 23f3000264@ds.study.iitm.ac.in

---

dont remove the space after year- for example “year”: "2023- "

---

Please anyone help me in doing q1 , my doubt is when i open the website [Advanced search](http://www.imdb.com/search/title) , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

---

In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

---

```
Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
| ----- | ------- | ------- | --------- | ------- |
| 48    | 51      | 15      | 47        | 65      |
| 74    | 70      | 23      | 17        | 70      |
| 81    | 50      | 59      | 45        | 51      |
| 80    | 63      | 43      | 99        | 28      |
| 85    | 72      | 82      | 79        | 14      |
| 76    | 50      | 15      | 55        | 13      |
| 21    | 86      | 25      | 14        | 64      |
| 54    | 72      | 98      | 30        | 96      |
| 15    | 24      | 67      | 19        | 35      |
| 68    | 82      | 16      | 70        | 67      |
| 64    | 94      | 42      | 26        | 10      |
| 31    | 79      | 98      | 21        | 24      |
| 90    | 32      | 88      | 39        | 56      |
| 36    | 72      | 79      | 86        | 96      |
| 91    | 61      | 57      | 28        | 23      |
| 81    | 40      | 95      | 74        | 30      |
| 60    | 31      | 66      | 36        | 83      |
| 81    | 16      | 67      | 25        | 90      |
| 40    | 96      | 57      | 84        | 47      |
| 53    | 92      | 10      | 10        | 82      |
| 33    | 40      | 20      | 68        | 95      |
| 95    | 48      | 69      | 24        | 42      |
| 93    | 84      | 79      | 33        | 17      |
| 40    | 81      | 39      | 31        | 60      |
| 31    | 44      | 96      | 78        | 54      |
| 58    | 21      | 98      | 58        | 44      |
| 47    | 22      | 91      | 77        | 46      |
| 61    | 93      | 75      | 25        | 79      |
| 18    | 19      | 47      | 20        | 58      |
| 77    | 51      | 28      | 14        | 97      |

```

This is the piece of markdown that is being generated for the last question of ga4.Even after using the prettier of the mentioned version i am getting incorrect answer.  
Anyone like to help.  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting

> Incorrect. Try Again

errors

---

I think you have used the wrong document, because, this is the marks list for Q9

---

which tool you are using ?

---

HOW TO GET BBC API KEY  
image description: The image displays a programming task interface. It includes instructions for retrieving and processing weather data. There is a sample JSON output, and a prompt to provide the JSON weather forecast description for Tel Aviv with a code input box.
image text:
Due Sun, 9 Feb, 2025, 11:59 pm IST Score: 1/10 Check all Save
1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Tel Aviv. Send a GET request to the locator service to obtain the city's
locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
3. Data Transformation: Extract the issueDate and enhancedWeatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each
issueDate to its corresponding enhancedWeatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription.
The output would look like this:
{
"2025-01-01": "Sunny with scattered clouds"
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
What is the JSON weather forecast description for Tel Aviv?
SyntaxError: Unexpected end of JSON input

---

in the bbc question what should be starting and the ending date

---

you dont need the key you need that file used in 2 lecture videos just look for it.  
![:+1:](https://emoji.discourse-cdn.com/google/+1.png?v=12 ":+1:")

---

Please find below the screen shot showing the committed with step name my iitm email id  
image description: The image is a screenshot of a webpage displaying a workflow file in a GitHub repository. The file details are: a name, on a schedule (with cron timing), and workflow\_dispatch. There are also permissions set for contents write, jobs that run daily-commit on Ubuntu-latest, and steps including checking out actions and configuring Git.
image text:
Updated 23f2003853/workflow
← 23f2003853@ds.study.iitm.ac.in
23f2003853@ds.study.iitm.ac.in #13
Workflow file for this run
.github/workflows/daily-commit.yml at 81c2d99
1 name: 23f2003853@ds.study.iitm.ac.in
2
3 on:
4 schedule:
5 - cron: '0 10 \* \* \*' # Runs daily at 10:00 AM UTC
6 workflow\_dispatch: # Allows for manual triggering
7
8 permissions:
9 contents: write
10
11 jobs:
12 daily-commit:
13 runs-on: ubuntu-latest
14
15 steps:
16 - name: 23f2003853@ds.study.iitm.ac.in
17 uses: actions/checkout@v3
18 with:
19 persist-credentials: false
20
21 - name: Configure Git
  
But the answer says  
image description: The image is a screenshot of a webpage with white background. There's a green header at the top. The content includes a bulleted list of instructions, followed by a text input field for a repository URL. Below the input field is an error message. A blue "Check" button is present at the bottom left.
image text: Be located in .github/workflows/ directory
After creating the workflow:
• Trigger the workflow and wait for it to complete
• Ensure it appears as the most recent action in your repository
• Verify that it creates a commit during or within 5 minutes of the workflow run
Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/23f2003853/workflows
Error: No executed job step matches 2312003853@ds.study.iitm.ac.in
Check
  
Please help to fix the issue

---

Still the issue is there. Have posted screen shot.

---

what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

---

Please give the solution if you got any…have you been able to solve the bbc weather question?

---

[@s.anand](/u/s.anand) [@carlton](/u/carlton)  
In question 8 i got error  
“Enter your repository URL (format: <https://github.com/USER/REPO>):  
<https://github.com/Ansh205/github-actions>  
Error: No workflow runs found”  
But i have successfully commited  
image description: The image showcases a workflow interface displaying the status of several automated processes. The interface is dark-themed, and the main content includes a list of workflow runs. The top area contains a search bar and filters to refine the view. The workflow runs are listed with their names, status (indicated by check marks or red crosses), branch, and recent activity timestamps.
image text: All workflows, Showing runs from all workflows, 4 workflow runs, Daily Commit Workflow, Daily Commit Workflow #4: Manually run by Ansh205, main, 5 minutes ago, 19s, Daily Commit Workflow, Daily Commit Workflow #3: Manually run by Ansh205, main, 37 minutes ago, 14s, Daily Commit Workflow, Daily Commit Workflow #2: Manually run by Ansh205, main, 54 minutes ago, 11s, Daily Commit Workflow, Daily Commit Workflow #1: Manually run by Ansh205, main, 1 hour ago, 14s, Q Filter workflow runs, Event, Status, Branch, Actor

---

Just follow the links and notebooks given in the references.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
sir i have submitted my GA3 but its showing not submitted why?  
image description: The image is a screenshot of a web page, likely a learning platform or online exam interface. The top of the page displays a header with the course title "TDS 2025 Jan GA3 - Large Language Models." Below the title, there are instructions for the assessment, including points on how to check and save answers, and suggestions for troubleshooting. The page also shows the user's login information and a "Recent saves" section. The main content includes details about "Module 3: Large Language Models," with information on an assignment called "Graded Assignment 3," which is "Not Submitted." There are also columns for "Your Score," "Peer Average," and "Median Score," all currently displaying dashes.
image text: Ended at Wed, 5 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
TDS 2025 Jan GA3 - Large Language Models
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times.
3. Save regularly by pressing save. You can save multiple times. Your last saved submission will be evaluated.
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters.
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser.
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want.
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed.
Note: You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers.
Have questions? Join the discussion on Discourse
You are logged in as 23f1001348@ds.study.iitm.ac.in.
Logout
Recent saves
Reload from 2/4/2025, 4:04:47 PM. Score: 9.5
Module 3: Large Language Models
Assignment
Graded Assignment 3
Assessment (Due: 5 Feb 2025)
Not Submitted
Your Score Peer Average Median Score
---
---
---

---

[@s.anand](/u/s.anand) Sir no submit button is available. On the top of it say submission is required. Could you clarify us  
Here's a description of the image:
The image shows a webpage for "Graded Assignment 4" on the IIT Madras online degree platform. The webpage details the assignment's due date, submission guidelines, and troubleshooting advice, including disabling ad blockers, enabling cookies, using Javascript, and using the Chrome browser. It also specifies the need for the student's ID for the graded assignment and provides a link to access the assignment.
image text:
IIT Madras Jan 2025-TDS
Graded Assignment 4
Due date for this assignment: 2025-02-09, 23:59 IST.
You may submit any number of times before the due date. The final submission will be considered for grading.
If you have any difficulty accessing the graded assignment, please check the following causes:
Ad blockers need to be disabled/removed.
The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
Javascript is required for the site to work correctly.
Chrome Browser is the recommended software to access the contents.
Disable any browser extensions that may be interfere with the site from working correctly.
Overly aggressive anti-virus software may also cause similar access problems.
Corporate proxies and network policies may also cause access issues. Try and use your mobile internet or another network.
You must use your Student ID (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the graded assignment, otherwise your score will not be considered for evaluation.
Graded Assignment 4 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga4. Please attempt it.

---

what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

---

As per instruction we need to create a directory in that we should have .yml file. But I tried with there were two issues (1) Github has not allowed to run the file (as there was no menu is available to run manually) (I checked with Copolit AI it says it is not correct to have cron jobs in a directory, I am not sure) (2) when I submit the url to iitm I got the following error  
image description: The image is a screenshot containing instructions and a text input field with a GitHub repository URL. It appears to be related to setting up or configuring workflows.
image text: Be located in .github/workflows/ directory
After creating the workflow:
- Trigger the workflow and wait for it to complete
- Ensure it appears as the most recent action in your repository
- Verify that it creates a commit during or within 5 minutes of the workflow run
Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/23f2003853/workflows
YAMLParseError: Implicit keys need to be on a single line at line 1, column 1: <!DOCTYPE html>
  
I removed the directory and submitted the same url I got the following error  
Here's a description of the image:
The image shows a form for entering a repository URL. An input field is pre-populated with a URL, and an error message is displayed below it. A "Check" button is visible at the bottom.
image text:
Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/23f2003853/workflows
Error: No executed job step matches 23f2003853@ds.study.iitm.ac.in
Check
  
I do not know what to do next. Can TA help us

---

The submission is on the Actual assignment page like for all the previous GAs in TDS. This is the **ONLY** valid submission button for GA1, GA2, GA3, GA4, GA5.

Here's a description of the image:
The image is a screenshot of a webpage related to a TDS 2025 Jan GA exam. An arrow points to the "Save" button at the top. Below the title and instructions, the instructions detail saving answers and the allowed resources.
image text: exam.sanand.workers.dev/tds-2025-01-ga4
[Admin] Due Sun, 9 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
TDS 2025 Jan GA
Instructions
1. Learn what you need. Reading material is provided, but feel fr
2. Check answers regularly by pressing Check. It shows which
3. Save regularly by pressing Save. You can save multiple times
4. Reloading is OK. Your answers are saved in your browser (not
5. Browser may struggle. If you face loading issues, turn off sec
6. Use anything. You can use any resources you want. The Intern
7. It's hackable. It's possible to get the answer to some question

---

try with this

* name: Set up Git user (23f2003853@ds.study.iitm.ac.in)  
  run: |  
  git config --global user.name “GitHub Actions Bot”  
  git config --global user.email “23f2003853@ds.study.iitm.ac.in”

---

Thank you for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

---

In g4 which Question have that error you are getting

---

In the last two question of the ga,it is mentioned including both groups.so what is the meaning of this .  
image description: The image is a dark theme, instructional text. It is titled "Your Task" and provides instructions for data analysis. Key instructions include extracting data from a PDF, cleaning, filtering, and calculating results. The text is structured with bullet points and numbered steps, outlining the process. The main task is to calculate total biology marks based on specific criteria, with the final question at the bottom.
image text: Your Task
This file, q-extract-tables-from-pdf.pdf contains a table of student marks in Maths, Physics, English, Economics, and Biology.
Calculate the total Biology marks of students who scored 17 or more marks in Physics in groups 43-66 (including both groups).
1. Data Extraction:: Retrieve the PDF file containing the student marks table and use PDF parsing libraries (e.g., Tabula, Camelot, or PyPDF2) to accurately extract the table data
into a workable format (e.g., CSV, Excel, or a DataFrame).
2. Data Cleaning and Preparation: Convert marks to numerical data types to facilitate accurate calculations.
3. Data Filtering: Identify students who have scored marks between 17 and Physics in groups 43-66 (including both groups).
4. Calculation: Sum the marks of the filtered students to obtain the total marks for this specific cohort.
By automating the extraction and analysis of student marks, EduAnalytics empowers Greenwood High School to make informed decisions swiftly. This capability enables the school
to:
• Identify Performance Trends: Quickly spot areas where students excel or need additional support.
• Allocate Resources Effectively: Direct teaching resources and interventions to groups and subjects that require attention.
• Enhance Reporting Efficiency: Reduce the time and effort spent on manual data processing, allowing educators to focus more on teaching and student engagement.
• Support Data-Driven Strategies: Use accurate and timely data to shape educational strategies and improve overall student outcomes.
What is the total Biology marks of students who scored 17 or more marks in Physics in groups 43-66 (including both groups)?
  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

Hi Tushar,

If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.

kind regards

---

Question 4 "  
Sample output

{  
“25-02-04”: “Sunny intervals and light winds”,  
“25-02-05”: “Light rain and light winds”,

}  
Error: At root: Property name mismatch"

---

Hi, even i’m facing the same issue,  
image description: The image shows a GitHub Actions workflow for a "Daily Commit" job. It shows the status as "Success", the total duration as 18 seconds, and a sub-job "daily-commit" that took 7 seconds. The commit was manually triggered 16 hours ago.
image text: DigvijaysinhChudasamalITM / TDS\_GA\_4
Q Type to search
← Daily Commit
Daily Commit #10
Summary
Jobs
daily-commit
Run details
Usage
Workflow file
Manually triggered 16 hours ago
DigvijaysinhChudasamallTM - e9aef97 main
Status
Success
Total duration
18s
Artifacts
daily-commit.yml
on: workflow\_dispatch
daily-commit
7s
  
Here's a brief description of the image:
The image is a screenshot of a code editor, likely GitHub, displaying a YAML file named "daily-commit.yml". The file seems to define a workflow for automated daily commits, including details on scheduling, job configurations, and steps like checking out a repository, setting up Git, creating a commit message, and committing changes.
image text:
DigvijaysinhChudasamalITM / TDS\_GA\_4
Q Type to search
+
A
<> Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights Settings
t
1
2
3
on:
Files
TDS\_GA\_4/.github / workflows / daily-commit.yml
main
+ Q
DigvijaysinhChudasamallTM Update daily-commit.yml -- added pull repo code
Q Go to file
.github/workflows
daily-commit.yml
daily-commit.txt
Code Blame 38 lines (30 loc) 1.14 KB
Code 55% faster with GitHub Copilot
name: Daily Commit
4
schedule:
5
cron: "00\*\*
# Runs at 00:00 UTC every day
6
workflow\_dispatch: # Allow manual triggers
7
8
jobs:
9
daily-commit:
10
runs-on: ubuntu-latest
11
12
steps:
13
name: Checkout repository
14
uses: actions/checkout@v4
15
16
name: Set up Git configuration
17
run:
18
19
git config --local user.email "${{ github.actor }}@users.noreply.github.com"
git config --local user.name "GitHub Actions"
20
21
22
name: Create a file with a daily commit message
run: |
23
echo "This is an automated daily commit" >> daily-commit.txt
24
25
name: Commit changes
View Runs
e9aef97. 17 hours ago
History
Raw
  
image description : The image shows instructions on a dark background, including steps for a workflow and a prompt to enter a repository URL. An error message is displayed below the URL input field.
image text: After creating the workflow:
• Trigger the workflow and wait for it to complete
• Ensure it appears as the most recent action in your repository
• Verify that it creates a commit during or within 5 minutes of the workflow run
Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/DigvijaysinhChudasamalITM/TDS\_GA\_4
Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

[@Jivraj](/u/jivraj)  
[@Saransh\_Saini](/u/saransh_saini)  
[@carlton](/u/carlton)  
Can anyone please help to fix this issue and submit this correctly.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png) 21f3002277:

> Set up Git user (23f2003853@ds.study.iitm.ac.in)

Still the same error appears

---

Thanks for providing clarification Sir

---

I am also facing same issue can’t resolve.

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
In ques 4 Scrap the BBC Weather API,  
I scraped the locationId for my city (i.e Mumbai)

and post that also mapped each `issueDate` to its corresponding `enhancedWeatherDescription` .

The sample output mentioned was:  
The output would look like this:

```
{
  "2025-01-01": "Sunny with scattered clouds",
  "2025-01-02": "Partly cloudy with a chance of rain",
  "2025-01-03": "Overcast skies",
  // ... additional days
}

```

And My Output after scraping (And as explained by professor in Video 2 BBC weather was)

{  
“2025-02-05”: “A clear sky and light winds”,  
“2025-02-06”: “A clear sky and light winds”,  
“2025-02-07”: “A clear sky and light winds”,  
“2025-02-08”: “A clear sky and light winds”,  
“2025-02-09”: “A clear sky and light winds”,  
“2025-02-10”: “A clear sky and light winds”,  
“2025-02-11”: “A clear sky and light winds”,  
“2025-02-12”: “A clear sky and light winds”,  
“2025-02-13”: “A clear sky and light winds”,  
“2025-02-14”: “A clear sky and light winds”,  
“2025-02-15”: “A clear sky and light winds”,  
“2025-02-16”: “A clear sky and light winds”,  
“2025-02-17”: “A clear sky and light winds”,  
“2025-02-18”: “A clear sky and light winds”,  
“2025-02-19”: “A clear sky and light winds”  
}

But it’s giving Error::  
Error: At root: Different number of properties

Can you please help how to fix this issue.

---

Issue resolved for me after following below step  
After creating the workflow:

* Trigger the workflow and wait for it to complete
* Ensure it appears as the **most recent action** in your repository
* Verify that it creates a commit during or within 5 minutes of the workflow run

---

In place of “name: Setup up GIT config” change to “name: add commit {your\_email}”

---

use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format.

[@23f2004752](/u/23f2004752)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) could you please help me with this?

---

On running this colab with city = Mumbai,

I’m gettingh this error: Error: At root: Property name mismatch

---

it’s getting,

```
{
    "2025-02-06": "Sunny and a gentle breeze",
    "2025-02-07": "Sunny and a gentle breeze",
    "2025-02-08": "Sunny and a gentle breeze",
    "2025-02-09": "Sunny and a gentle breeze",
    "2025-02-10": "Sunny and a gentle breeze",
    "2025-02-11": "Sunny and a gentle breeze",
    "2025-02-12": "Sunny and a moderate breeze",
    "2025-02-13": "Sunny and a gentle breeze",
    "2025-02-14": "Sunny and a gentle breeze",
    "2025-02-15": "Sunny and a gentle breeze",
    "2025-02-16": "Sunny and a gentle breeze",
    "2025-02-17": "Sunny and a gentle breeze",
    "2025-02-18": "Sunny and a gentle breeze",
    "2025-02-19": "Sunny and a gentle breeze"

}

```

---

can tell me in your .yml which are all place did you use your iitm email id. Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

---

[@s.anand](/u/s.anand) [@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Is there any way to crack this , I tired multiple time no improvement.  
Also what does this " It is *very hard* to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison." mean.  
image description: The image is a dark mode screenshot of a document, with instructions to convert a PDF to Markdown format. There are also some provided sample text. The instructions are numbered, detailing the steps: convert the PDF to Markdown, format the Markdown with Prettier version 3.4.2, and submit the formatted Markdown. There is an "Impact" section describing the benefits of the project, including enhancing productivity and improving quality. Below the instructions, the screenshot displays a box for user input, with the sample text "Ater vulnero solio tabula.Auctus benigne coaegresco defetiscor delinquo. Talio balbus cultura vae. Sint deripio tener adfectus agnitio aro cruentus arbustum. Abstergo alii sollers" and shows "Incorrect. Try again.". The bottom of the image contains a statement about the difficulty of obtaining correct Markdown output from a PDF.
image text: q-pdf-to-markdown.pdf has the contents of a sample document.
1. Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible.
2. Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file.
3. Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission.
Impact
By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:
Enhances Productivity: Reduces the time and effort required to prepare documentation for clients.
Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism.
Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality.
Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems.
What is the markdown content of the PDF, formatted with prettier@3.4.2?
Ater vulnero solio tabula.
Auctus benigne coaegresco defetiscor delinquo.
Talio balbus cultura vae. Sint deripio tener adfectus agnitio aro cruentus arbustum. Abstergo alii sollers.
---
Incorrect. Try again.
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison.

---

Same problem please help me too if you get it right.

---

Yes followed all these steps, and still the error is being seen,

Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

---

Yes true,

Here’s the output:  
{  
“2025-02-05”: “Sunny and a gentle breeze”,  
“2025-02-06”: “Sunny and a gentle breeze”,  
“2025-02-07”: “Sunny and a gentle breeze”,  
“2025-02-08”: “Sunny and a gentle breeze”,  
“2025-02-09”: “Sunny and a gentle breeze”,  
“2025-02-10”: “Sunny and a gentle breeze”,  
“2025-02-11”: “Sunny and a moderate breeze”,  
“2025-02-12”: “Sunny and a gentle breeze”,  
“2025-02-13”: “Sunny and a gentle breeze”,  
“2025-02-14”: “Sunny and a gentle breeze”,  
“2025-02-15”: “Sunny and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny and a gentle breeze”,  
“2025-02-18”: “Sunny and a gentle breeze”  
}

But unfortunately this error persists,

Error: At root: Property name mismatch

---

Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

---

Yes true same happened with me.

---

re-check your answer again it may give an url. check the url

---

Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

---

No its giving such error:  
image description: The image is a dark gray screenshot of a webpage. The webpage is prompting the user to enter their repository URL in a specific format. The entered URL is highlighted with an error message indicating a failure to fetch data. The check button is present at the bottom.
image text: Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/DigvijaysinhChudasamalITM/TDS\_GA\_4
TypeError: Failed to fetch
Check

---

Here’s the action’s:  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a dark-themed user interface displaying workflow information. The left sidebar lists "Actions" and various management options. The main section showcases "All workflows" with a filter function and feedback prompt. There are two "Daily Commit" entries with details like time, branch, and actor information.
\*\*Image Text:\*\*
\* Actions
\* All workflows
\* Daily Commit
\* Management
\* Caches
\* Attestations
\* Runners
\* Usage metrics
\* Performance metrics
\* New workflow
\* All workflows
\* Showing runs from all workflows
\* Help us improve GitHub Actions
\* Tell us how to make GitHub Actions work better for you with three quick questions.
\* Give feedback
\* 15 workflow runs
\* Daily Commit
\* Daily Commit #15: Manually run by DigvijaysinhChudasamalITM
\* Daily Commit
\* Daily Commit #14: Manually run by DigvijaysinhChudasamalITM
\* main
\* main
\* Filter workflow runs
\* 13 minutes ago
\* 16s
\* 13 minutes ago
\* 17s

---

Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

---

What you meant by " Ensure the first item is schedule triggered confirmation"? You meant the latest one should be this right?

Here's a description of the image:
The image is a screenshot of the "Actions" section within a software development platform, likely GitHub. It displays a list of workflow runs, likely associated with continuous integration and continuous delivery (CI/CD) processes. The user interface is dark-themed.
Key elements:
\* \*\*Navigation Bar:\*\* Across the top, there's a navigation bar showing the user's profile, search bar, and other options.
\* \*\*Sidebar:\*\* On the left, there is a sidebar showing the navigation menu, with the "Actions" tab highlighted.
\* \*\*Main Content:\*\* The main area is divided into two main sections:
\* \*\*Workflow Information:\*\* A list of workflow runs with details like the workflow name, status, time elapsed, branch, and actor.
\* \*\*Buttons:\*\* "New workflow" and "Filter workflow runs" button.
\* \*\*Status:\*\* The image showcases workflow runs with different statuses, like completed (green checkmark) or failed (red X).
\* \*\*Help us improve GitHub Actions:\*\* A promotional note with a button to Give feedback.
image text: DigvijaysinhChudasamalITM / TDS\\_GA\\_4 Q Type to search <> Code Issues Pull requests Actions Projects Wiki Security Insights Settings Actions New workflow All workflows Showing runs from all workflows Q Filter workflow runs Help us improve GitHub Actions Tell us how to make GitHub Actions work better for you with three quick questions. Give feedback X 15 workflow runs Event Status Branch Actor All workflows Daily Commit Management Caches ✔ Attestations Runners Usage metrics Performance metrics Daily Commit Daily Commit #15: Manually run by DigvijaysinhChudasamallTM main 18 minutes ago 16s Daily Commit Daily Commit #14: Manually run by DigvijaysinhChudasamalITM main 18 minutes ago 17s ✔ Daily Commit Daily Commit #13: Manually run by DigvijaysinhChudasamalITM main 4 hours ago 10s ✔ Daily Commit Daily Commit #12: Manually run by DigvijaysinhChudasamalITM main 4 hours ago 11s Daily Commit Daily Commit #11: Scheduled main 10 hours ago 14s Daily Commit yesterday

---

check this type of screen  
image description: The image displays a section of a web page related to GitHub Actions workflow runs. A blue rectangular prompt is at the top, providing a "Give feedback" button to improve GitHub Actions. The main section shows a summary of "71 workflow runs". One run is detailed, displaying the email address "23f2003853@ds.study.iitm.ac.in" with a green checkmark, indicating a successful run. It also indicates that the run was on the "main" branch, and ran manually by "23f2003853" 23 minutes ago and took 19s to finish.
image text: Help us improve GitHub Actions
Tell us how to make GitHub Actions work better for you with three quick questions.
Give feedback
X
71 workflow runs
Event Status Branch Actor
23f2003853@ds.study.iitm.ac.in
23f2003853@ds.study.iitm.ac.in #23: Manually run by 23f2003853
main
23 minutes ago
19s

---

use name:email inside yml page

---

Yep done, thank you! ![:smiley:](https://emoji.discourse-cdn.com/google/smiley.png?v=12 ":smiley:")

---

```
Depopulo amoveo curo.
Concego creatinue ancilla vesper conicio cinimatico eribro.  
Custodia anica arbustum coniceto suma corporis aduno commenoro curiositas augero.  
Uredo thesis ancilla alter eun tener vomito praesentium templum.  
Magni deprimo celebre.

### Bellum pelor cornu vorax perspiciatis.

Labore elus umerus voluntarius.  
Vicissitudo cilíctum cicuta campana.  
Desino perspiciatis comodo.

### amarttudo tabesco crinis amissio

tui qui decumbo vobis  
audacia charismatubineus contigo  
aro eum talio elus  
coniuratio cubo ab vere  
validus tam patria deficio  
agnosco spectaculumcoerceo  
spectaculum vulpes valetudo  
minima cado suffragium  
asperiores thesaurus cometes  
vesica amplus cimentarius  
volum curiositas cornu

## Paupertrucido confido triduana ante sublime

# Consequatur comminor

Coadunatio delectus atqui placeat atque copia ventosus aer quae.  
Tatillo causa damatico validus torrena tivpinca.  
Adside nisi atavus aspiente.

[soius tam](https://tds.s-anand.net/#/markdown)

Ceno usilio desino velociter sit aut. Concedo accedo vac congregatio sperno venia sum sordeo animi tametsi. Accusamus suppellex turpis dedecor uliam vaco venusit:

- tu! amicitia ante suppellex studio
- utor debilito suasoria odio
- antea desino despecto magni

[coadunatio voco](https://tds.s-anand.net/#/markdown)

[incidunt aliquam](https://tds.s-anand.net/#/markdown)

Tametsitenuis conscendo.

- tempore vorner aestas commentoro
- absconditus coruscus

## Blanditiis tabula animi succedo

Asper summa tametsi ustulo villias conservo clam triumphus tener ager. Audax conforto adopto vesco arbustum deorsum terror impedit iure. Adsum atrox caries acc

Beatae ducimus aperio amarttudo caries

- cinis solvo unde unde arbustum
- canis civitas viro
- thorax pax demens
- arbustum suficco thorax testimonium ex.
- vinliter sumptus

Explicabo defico adfectus.

Comedo cattus justo tamdiu tumultus confido thesaurus coadunatio volutabrum. Succedo tabula audax copia vinculum.

**cogo audio suffragium**

crepito amiculum sufficio  
acer aestas utor  
debeo adopto utpote  
tametsi curatio ante

## Maxime vulgo depulso decipio atrox

## Career debeo

**conatus cui admoneo**

theatum pauper tego
pecco caeous vulgo
cursim desino arceo
balbus comminor et

```

In the question no. 10, I have tried numerous time to get it right markdown content but it was incorrect all the time.

I have tried these steps:

```
import pymupdf4llm
md_text = pymupdf4llm.to_markdown("/content/q-pdf-to-markdown.pdf")

import pathlib
pathlib.Path("output.md").write_bytes(md_text.encode())

```

Then i run this in bash

```
prettier --write output.md

```

And what i got frankly telling was far from this, I did some manual touchups, and this what i have now. This is the best version i could come up with. Saw the preview, it does matches with the pdf.

#Can someone please advise me a better approach?

---

hey, can you help me in doing this i can’t able to do this.

---

[@24ds3000090](/u/24ds3000090)

We will be changing this question. Even we found it hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards

---

[@JoelJeffrey](/u/joeljeffrey)

We will be changing this question. Even we found it pretty hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards

---

sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

---

<https://tds.s-anand.net/#/bbc-weather-api-with-python>

---

try manually inspecting the output of the api and compare it with your script output.  
Or else try refreshing the browser and check.

---

[@carlton](/u/carlton)  
Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

---

Please try city=“Mumbai” as a string literal.

---

Q4 BBC Weather

I don’t understand why I am getting

> Error: At root: Different number of properties

Is it because of different dates? Shall I match the dates?

[@carlton](/u/carlton) Please guide. Thank you.

image description: The image is a screenshot of a programming exercise, likely related to weather data processing. It presents a task involving the use of a weather API, with instructions to retrieve, extract, and transform weather data. It shows examples of how the output should look in JSON format and presents a question about the weather forecast for Osaka with an error message.
image text:
Your Task
As part of this initiative, you are tasked with developing a system that aut
1. API Integration and Data Retrieval: Use the BBC Weather API to fet
locationId. Include necessary query parameters such as API key, loca
2. Weather Data Extraction: Retrieve the weather forecast data using t
3. Data Transformation: Extract the issueDate and enhancedWeatherDes
issueDate to its corresponding enhancedWeatherDescription. Create a
The output would look like this:
{
"2025-01-01": "Sunny with scattered clouds",
"202-01-02": "Partly cloudy with a chance of rain",
"202-01-03": "Overcast skies",
// . additional days
}
What is the JSON weather forecast description for Osaka?
{
"2025-02-06": "A clear sky and light winds",
"2025-02-07": "Sunny intervals and a moderate breeze",
"2025-02-08": "Light rain showers and a gentle breeze",
"2025-02-09": "Sunny intervals and a gentle breeze",
"2025-02-10": "Sunny intervals and a gentle breeze",
Error: At root: Different number of properties
Check

---

## thema coruscus

* cupiditate celebrer
* argentum alius voro soluta
* sto decor capto suffoco acs tempus deludo deleo ventus odio

Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo  
territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum

| abeo | super | valetudo adhuc |
| --- | --- | --- |
| conatus | comptus | spiculum summisse |
| alienus | addo | demergo conturbo |
| uberrime | subseco | altus & ea |
| apto | cursus | infit & summa |

* tabula necessitatibus beneficium concido
* adhaero tepesco ars
* adnuo beatae
* cursim ahsens culpa animi aestivus

## Solium vulgus commodo claro curriculum valens

Aut ipsum spiritus tantillus vacuus adsum crebro animus pel paulatim. Tunc vallum  
torqueo aequus valens triduana illo. Uredo cursus fuga vir.

Cultellus adipiscor incidunt tondeo benevolentia capto contabesco bene tardus  
harum.

Bos subnecto beatae abeo vulnus terra verus balbus

* arguo via vallum usus aliquid
* tempus balbus videlicet acquiro

attonbitus tardus versus cuppedia  
derelinctuo curatio stalla solen  
comburo commodo caveo at  
deporto aliquid thymum  
confero sortitus ago  
triduana umquam acies

Beneficium doloremque aspernatur dolor dolorum despecto attonbitus unus alienus  
Capto optio dolores.  
Commodi sono denuo molestiae terebro  
Benigne anser vulgus brevis coaegresco vinum debeo.  
Cras aut ullam error terreo absque aro adstringo sublime thymum

## Triumphuslaudantium curto certus

Callide stabilis subito claudeo occaecati depono. Turba thymum bis deludo una.  
Sumo consuasor necessitatibus vix solitudo dolorum dolorem vinco inflammatio

* apparatus spero sulum desino ultra
* nauner necessitatibus bos calculus nlaceat
* animadverto defessus triumphus
* acquiro artificiose minima sortitus terminatio

Aegrus tot tot aetas. Clinís volva tamen sumptus. Solutio deludo suscipio deputo  
demens vero audeo annus alo accendo.

I am getting error: Incorrect. Try again.  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton) can you please explain the reason for this error

---

Hi Mishkat

Please refer to this post.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91) [Tools in Data Science](/c/courses/tds-kb/34)

> [@JoelJeffrey](/u/joeljeffrey)
> We will be changing this question. Even we found it pretty hard ![sweat_smile](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 "sweat_smile")
> Kind regards

Kind regards

---

[@s.anand](/u/s.anand) Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

---

Yep figured that, and after matching the data solved the error and got that question correct.  
Though thank you.

---

[@s.anand](/u/s.anand) Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

---

Yes we’ll were facing this issue.

[@carlton](/u/carlton) sir mentioned yesterday that they will change the question.

"We will be changing this question. Even we found it hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards"

So need to worry about that question for now.

---

OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

---

I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

---

On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.

(FYI, one person *did* solve it. A colleague, not someone from the IITM DS program.)

---

Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…

But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

same issue with me as well

---

Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols \* and + also) . Please inform me where I made mistake  
image description: The image displays the markdown content of a PDF formatted with prettier@3.4.2. There are four bullet points with phrases, and an error message "Missing lists".
image text: What is the markdown content of the PDF, formatted with prettier@3.4.2?
- cuppedia tamquam facilis confugo
- conservo depereo
- consectetur arx
- aeternus celebrer
Error: Missing lists

---

this is table. Check it  
image description: The image is a table with three columns and four rows. The first row contains three words: capitulus, deleniti, and pariatur. The subsequent rows contain words beneath each of the header words.
image text: capitulus deleniti pariatur voluptate barba bellum quaerat cedo cursus vestigium trans sortitus ait alioqui verumtamen

---

Q 10 - PDF to Markdown.

Why it is saying

> Incorrect. Try again?

Do I need to add CSS?

`Carbo ventosus tametsi patior. Recusandae ciminatio alienus nisi ventosus apud. Theatrum abutor aperio spargo vestrum virga placeat adulescens. Deripio alveus creator omnis tabula patria cupiditate in virga speculum. Acidu`s alienus vehemens vapulus.`

**earum clamo collum**  
curtus careo curatio  
tendo sunt culpo  
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco | solio | ademptio | terreo | bis |
| --- | --- | --- | --- | --- |
| tardus | carpo | allatus | depono | benevolentia |
| tunc | atavus | barba | urbs | considero |
| adulescensamplitudo |  | verbum | cultura | id |
| cenaculum | ipsum | sursum | conturbo | nemo |
| damno | arbitro | quibusdam | articulus | animadverto |

* ustulo crudelis depraedor
* sophismata tener apostolus suus adopto
* coniecto maxime rerum
* acceptus virga confero comes

cresco vomito

deputo ceno

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

valde vulgus

---

I checked many times. For me it says “Incorrect. Try again.”

---

Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

---

Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

---

I have added all those and pasted the markdown and it appears as [above](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/111).

```
`` Carbo ventosus tametsi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperio spargo vestrum virga placeat adulescens.
Deripio alveus creator omnis tabula patria cupiditate in virga speculum.
Acidu`s alienus vehemens vapulus. ``

**earum clamo collum**
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.

Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.

| cresco              | solio   | ademptio  | terreo    | bis          |
| ------------------- | ------- | --------- | --------- | ------------ |
| tardus              | carpo   | allatus   | depono    | benevolentia |
| tunc                | atavus  | barba     | urbs      | considero    |
| adulescensamplitudo |         | verbum    | cultura   | id           |
| cenaculum           | ipsum   | sursum    | conturbo  | nemo         |
| damno               | arbitro | quibusdam | articulus | animadverto  |

- ustulo crudelis depraedor
- sophismata tener apostolus suus adopto
- coniecto maxime rerum
- acceptus virga confero comes

[cresco vomito](;;;)

[deputo ceno](;;;)

# Cuppedia uberrime socius atque paens

# Sto theca testimonium aestus debitis

[valde vulgus](;;;)

```

Below is the screenshot of provided PDF. That font colour strains my eyes. Any particular reason for that PDF?

image description: A white background with black text in a serif font. The text appears to be Latin, formatted in a way that suggests it might be a draft or notes. Key elements include headings, words, and phrases.
image text: Carbo vencosus camessi patior.
Recusandae ciminatio alienus nisi ventosus apud.
Theatrum abutor aperto spargo vestrum virga placeat, adulescens
Doripio alveus creator omnis tabula patria cupiditata in virga speculum
Acidus aliamus vehemens vapulus.
iarum clamo collum
curtus careo curatio
tendo sunt culpo
Suus sit magni traho tempora.
Depraedor vae dedecor conturbo. Curia vigor vinco terebro alii tantum clam. Modi veniam alveus clementia sumo iusto adfero truculenter.
cresco solio ademptio terreo bis
tardus carpo allatus depono benevolentia
tunc atavus barba urbs considero
adulescensamplitudo verbum cultura id
cenaculum ipsum sursum conturbo nemo
damno arbitro quibusdam articulus animadverto
• ustulo crudelis depraedor
• sophismata tener apostolus suus adopto
• coniecto maxime rerum
• acceptus virga confero comes
cresco vomito
deputo ceno
Cuppedia uberrime socius atque paens
Sto theca testimonium aestus debitis
valde vulgus

---

I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.  
Any suggestion to move nearer to the actual solution.

---

You may try like this: cresco vomito

```
[cresco vomito](;;;)

```

---

Even I’m getting a similar error in Q2, it is expecting a foreign title whereas my search result gives only English titles.  
image description: The image shows JSON data with a title mismatch error. The error message indicates a problem with the title field within the JSON data. The "title" value is expected to be "13. Pídeme lo que quieras", but the actual value is "13. Ask Me What You Want".
image text: What is the JSON data?
```
{
"id": "tt8712204",
"title": "25. Batwoman",
"year": "2019-2022",
"rating": "3.6"
}
```
Error: At [12].title: Values don't match. Expected: "13. Pídeme lo que quieras". Actual: "13. Ask Me What You Want"
  
Please help.

---

I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.

Could be another reason too. TAs’ can feel free to pitch in.

---

A post was merged into an existing topic: [Tds: assignment is not submitting](/t/tds-assignment-is-not-submitting/166189/21)

---

your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

---

Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.  
Thank again.

---

Can we use hacking to get answers to some questions? Has anyone ever done it?

---

What format is required for the “missing links” here  
image description: The image is a document explaining the impact of a project related to automating PDF to Markdown conversion and also providing text in markdown format. The top of the document has a title "Impact" and some bulleted points explaining the benefits. Below is the markdown content with some words underlined in red. At the very end there is an error message saying "Missing links".
image text: Impact
By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion
and ensuring consistent formatting:
• Enhances Productivity: Reduces the time and effort required to prepare documentation for clients.
• Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism.
• Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality.
• Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems.
What is the markdown content of the PDF, formatted with prettier@3.4.2?
Audax teneo centum cilicium vigor venio.
Patria credo tonsor.
Defessus pax volup vomito creator video campana cedo vita votum.
Laudantium victoria aer via tepidus.
Adulescens corporis triumphus coruscus sordeo trans dolorum.
Error: Missing links
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic
things.

Here is my markdown

```
- statua demulceo amaritudo tametsi

- tam ante

- dens spiritus

- thema succurro sollers audio

Conforto conor tum deputo caecus cervus coepi aegrotatio totam xiphias. Repudiandae ducimus acerbitas ademptio . Delectatio tamquam suus.

Centum usitas tamen cedo auctus turpis video clibanus. Correptius beatus crepusculum decens succedo alias aperte decumbo trado. Talio universe deduco caute sui u

vester undique

- subito umbra

- caritas saepe

- taceo concido bos

Tenetur exercitationem numquam ultio tyrannus aeger vindico. Subvenio ambulo vacuus. Quidem quam tactus tracto aureus cupiditas.

thema astrum

# Spero uter

Harum cometes damnatio theologus virgo aperiam velut cursim.

**venustaspeccatus adsum**

acidus quisquam torrens

clam adeptio virga

Depulso claro consectetur concedo aveho bis pectus traho nobis. Cura adicio colligo corporis eligendi soluta ducimus carus. Allatus sapiente summa atqui deludo cur

```

Terebro vallum rem velociter currus suppellex.  
Viduo damno ustilo valetudo.  
Tribuo una vorago sui testimonium angelus suscipio eius demulceo civis.

```

Delectus coniecto repellendus amoveo amissio incidunt

```

Audax teneo centum cilicium vigor venio.  
Patria credo tonsor.  
Defessus pax volup vomito creator video campana cedo vita votum.  
Laudantium victoria aer via tepidus.  
Adulescens corporis triumphus coruscus sordeo trans dolorum.

```

- doloremque cum allatus aduro

- inventore thalassinus

- aperiam tergiversatio

- contigo alienus aranea cito cogo

Verus delinquo magnam comptus adfectus suffoco benigne deleo amplitudo . Cura deleniti theologus vestigium aranea denique vester doloribus . Venio cimentarius cr

depereo subvenio

---

```

---

In the pdf you see some blue color font for specific words write that word in format

```
[word](#)

```

---

1. There are only four texts which look like link texts in the pdf.  
   All four properly coded in link markdown syntax, in the preview, they appear as link texts same as in pdf.

Link text

Even after chaning all the 4 texts which appered in blue color in the pdf to link texts,  
below error is still observed.

Error: Missing links

Did anyone else face same issue ?

2. Also, no text in the pdf looks like a code block.  
   But, Missing Code error was seen and after changing one of the paragraph by using markdown code syntax that error is gone.

Appreciate any suggestions on the link error.

---

Replace actual text to expected text until you got correct

---

same kind of error is arising with me too.Any suggestion what is wrong with it??

---

the rating should be treated as string.  
Format is as “2.9” instead of number 2.9

---

Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

---

i am facing a similar issue

image description: A screenshot from a coding interface that shows the JSON weather forecast description for Shanghai, with an error message. The forecast details days from "2025-02-07" to "2025-02-11" with different weather conditions. The interface highlights an error: "Different number of properties". A blue button labeled "Check" is present at the bottom.
image text:
The output would look like this:
```
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
//... additional days
}
```
What is the JSON weather forecast description for Shanghai?
```
{
"2025-02-07": "A clear sky and a moderate breeze",
"2025-02-08": "Sunny and a moderate breeze",
"2025-02-09": "Sunny and a gentle breeze",
"2025-02-10": "Sunny and a gentle breeze",
"2025-02-11": "Sunny intervals and a moderate breeze",
Error: At root: Different number of properties
Check
```

---

Here's a description of the image:
The image is a screenshot of a webpage. The top of the page shows the exam information and a score of 10/10. The main content has a message about bonus marks for posting on a discussion forum, followed by the user's login information and recent saves of the exam.
image text: Due Sun, 9 Feb, 2025, 11:59 pm IST Score: 10 / 10 Check all Save
Have questions? Join the discussion on Discourse
Bonus marks for posting on Discourse
To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]\_with a relevant question or reply will get 1 bonus mark on this graded assignment.
You are logged in as 23f2005275@ds.study.iitm.ac.in.
Logout
Recent saves (most recent is your official score)
Reload from 07/02/2025, 23:51:21. Score: 10
Reload from 07/02/2025, 20:30:21. Score: 5
Reload from 07/02/2025, 18:17:58. Score: 3
  
succesfully completed GA4 with 10/10 Marks

---

sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

---

In Q2. getting , able to fix most of the errors but  
Here's a brief description of the image:
The image shows a webpage displaying movie titles, ratings, and other details. A console is open on the right side of the screen, showing JSON data related to the movie search results.
image text: "id": "tt9218128",
"title": "12. Gladiator II",
"year": "2024",
"rating": "6.6"
"id": "tt30057084",
"title": "13. Babygirl",
"year": "2024",
"rating": "6.1"
"id": "tt26748649",
"title": "14. High Potential",
"year": "2024-",
"rating": "7.6"
"id": "tt28607951",
"title": "15. Anora",
"year": "2024",
"rating": "7.8"
"id": "tt14858658",
"title": "16. Blink Twice",
"year": "2024",
"rating": "6.5"
"id": "tt21191806",
"title": "17. Back in Action",
"year": "2025",
"rating": "5.9"
"id": "tt10078772",
"title": "18. Flight Risk",
"year": "2025",
"rating": "5.5"
"id": "tt16030542",
"title": "19. The Recruit",
"year": "2022-",
"rating": "7.4"
"id": "tt7587890",
"title": "20. The Rookie",
"year": "2018-",
"rating": "8.0"
"id": "tt11563598",
"title": "21. A Complete Unknown",
"year": "2024",
"rating": "7.7"

Error: At [18].title: Values don’t match. Expected: “19. Graymail”. Actual: “19. The Recruit”

this kind of errors for some titles, even though i only applied Rating filter and nothing else, then why i’m getting different titles then the test cases?

---

Hello Sir, thank you for changing the question.

[@carlton](/u/carlton) I’m getting the below error:

```
Words like https, webbed, impact are missing (or not separated as words).

```

However, in the source PDF file itself these words are not available.

image description: The image shows a dark background with a grid of Latin words. Some words have a red squiggly line under them. Below the grid is an error message in red font.
image text: | quos | utrum | tredecim | valetudo | cras | videlicet | laudantium | aetas | canis | tantum | Error: Words like https, webbed, impact are missing (or not separated as words)

---

Copy the row name that is use to change and paste it in your answers

---

the ranking changes from time to time. you might need to scrape the data again.

---

i am facing issue in Q7.

I am using this command : “<https://api.github.com/search/users?q=location:Seattle+followers:>>120&sort=created&order=desc”

and the output on evaluating is : 2011-05-07T08:30:48Z

But i am getting the error :  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a webpage content with text describing a process to find the newest user's Github profile based on location, follower count, and creation date. The text also explains the impact of automating this data retrieval and filtering. There is an input field to enter the date, which is initially incorrect, and instructions on how to search using location and filters.
\*\*Image Text:\*\*
Using the GitHub API, find all users located in the city Seattle with over 120 followers.
When was the newest user's GitHub profile created?
1. API Integration and Data Retrieval: Leverage GitHub's search endpoints to query users by location and filter them by follower count.
2. Data Processing: From the returned list of GitHub users, isolate those profiles that meet the specified criteria.
3. Sort and Format: Identify the "newest" user by comparing the created\_at dates provided in the user profile data. Format the account creation date
in the ISO 8601 standard (e.g., "2024-01-01T00:00:00Z").
Impact
By automating this data retrieval and filtering process, CodeConnect gains several strategic advantages:
\* Targeted Recruitment: Quickly identify new, promising talent in key regions, allowing for more focused and timely recruitment campaigns.
\* Competitive Intelligence: Stay updated on emerging trends within local developer communities and adjust talent acquisition strategies accordingly.
\* Efficiency: Automating repetitive data collection tasks frees up time for recruiters to focus on engagement and relationship-building.
\* Data-Driven Decisions: Leverage standardized and reliable data to support strategic business decisions in recruitment and market research.
Enter the date (ISO 8601, e.g. "2024-01-01T00:00:00Z") when the newest user joined GitHub.
2011-05-07T08:30:48Z
Incorrect. Try again.
Search using location: and followers: filters, sort by joined descending, fetch the first url, and enter the created\\_at field. Ignore ultra-new users who
JUST joined, i.e. after 2/7/2025, 11:00:55 PM.

Can someone please help me on this ?

---

I am also facing the same issue. What is the problem here?  
image description: The image is a screenshot of a coding or data processing exercise. It provides instructions on how to retrieve and transform weather forecast data for London using an API. The main sections include API integration, weather data extraction, and data transformation. A sample output is shown, followed by a question asking for the JSON weather forecast description for London. An error message is displayed, indicating a property name mismatch. There's also a "Check" button.
image text: Due Sun, 9 Feb, 2025, 11:59 pm IST Score: 9/10 Check all Save
1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for London. Send a GET request to the locator service to obtain the city's
locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each
issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription.
The output would look like this:
{
}
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies"
// .. additional days
What is the JSON weather forecast description for London?
"2025-02-17": "Sunny and light winds",
"2025-02-18": "Sunny intervals and light winds",
"2025-02-19": "Sunny and light winds",
"2025-02-20": "Light cloud and light winds",
"2025-02-21": "Light rain and a gentle breeze"
Error: At root: Property name mismatch
Check

---

[@21F1005510](/u/21f1005510) Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

**Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:

```
[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]

```

… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by 2025-02-22T18:30:00Z.

---

I am getting the error in Q4 as “Error: At root: Property name mismatch”

what could me the cause of this error? Any please help.

[@carlton](/u/carlton)

Here's a description of the image:
The image shows a question asking for the JSON weather forecast description for Sao Paulo. It provides a code snippet representing the forecast, displaying weather conditions for several dates. An error message "Error: At root: Property name mismatch" is also displayed. Below the code, a blue "Check" button is visible.
image text:
What is the JSON weather forecast description for Sao Paulo?
{
"2025-02-08": "Partly cloudy and light winds",
"2025-02-09": "Thundery showers and a gentle breeze",
"2025-02-10": "Sunny and a gentle breeze",
"2025-02-11": "Thundery showers and light winds",
"2025-02-12": "Sunny intervals and a gentle breeze",
Error: At root: Property name mismatch
Check

---

This is the only thing which worked for me.

[@carlton](/u/carlton) Sir, can I suggest to replace the snapshot of example output which expects the year to be an integer and the ratings as to be floats (instead of actual evaluation which expects them to be strings). Also, it would help to clarify that “Movie 1” should carry the numerical prefix as reported in IMDB. The current example on the portal is:  
Here's a description of the image:
The image is of a dark background with text, presumably code. It seems to be formatted as a JSON array.
image text:
```
[
{ "id": "tt1234567", "title": "Movie 1", "year": 2021, "rating": 5.8 },
{ "id": "tt7654321", "title": "Movie 2", "year": 2019, "rating": 6.2 },
// ... more titles
]
```

---

Your dot of 2.9 may be the dot from alphabet or numeric one  
Try to copy the value and then replace it

---

Try to copy the error data  
The problem might be off dot  
check one dot is on right of m and other right of 0 in keyboard  
these two dots may represent different meanings

---

is it resolved?  
i too am getting the same error,even if it was working fine yesterday.

---

https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

---

Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?

In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.  
I would appreciate your guidance on these issues.

---

Good idea [@23f2005138](/u/23f2005138) and thanks. I fixed this. The example now reads:

```
[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },

```

… with the year and ratings quoted.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.

For the particular instance - `“2024–”`, it appears another season/part is announced, thats why it is written that way.

---

Thanks [@21f2000709](/u/21f2000709) for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

---

GA 4 Q2

My JSON matches the titles of the movies as in the website, but in portal it is showing error and expecting something different from what is given in the website. How to handle this ?

image description: A film's details are presented inside a red box, which includes the title, year, duration, rating, and a score. On the left side, a movie poster is visible.
image text: 2. Winnie-the-Pooh: Blood and Honey 2023 1h 24m Not Rated ★ 2.9 (33K) Rate 16 Metascore  
Here's a brief description of the image:
The image shows JSON data with an error message.
image text:
What is the JSON data?
"title": "25. Battlefield Earth",
"year": "2000",
"rating": "2.5"
}
]
Error: At [1].title: Values don't match. Expected: '2. Winnie the Pooh: Blood and Honey". Actual: "2. Winnie-the-Pooh: Blood and Honey"

contradiction :  
" 2. Winnie-the-Pooh: Blood and Honey" (in web page) & ( delivered by the JSON)  
" 2. Winnie the Pooh: Blood and Honey" (expected in portal ) & ( raising error statement )

Regards  
GOVADHANAN N

---

so just exchange it.

---

Thanks for your response.  
Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

---

thanks for this, was wondering why it wasn’t working!

---

image description : The image shows a code snippet with a JSON weather forecast, followed by a question about a specific city's weather forecast. An error message is displayed at the end.
image text: The output would look like this:
```
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
```
What is the JSON weather forecast description for Kuala Lumpur?
```
{"2025-02-01": "Thundery showers and light winds"}
```
Error: At root: Different number of properties

sir, we are getting this error. My Actual output is after get request on the given api i get only one day forcast data. I have show in above image

---

yes replace manually until you got correct ans . Error will suggest you what to change.

---

{  
“2025-02-08”: “Light snow and light winds”,  
“2025-02-09”: “Light snow and light winds”,  
“2025-02-10”: “Light cloud and light winds”,  
“2025-02-11”: “Sunny intervals and a gentle breeze”,  
“2025-02-12”: “Sunny and light winds”,  
“2025-02-13”: “Sunny and light winds”,  
“2025-02-14”: “Light snow and a gentle breeze”,  
“2025-02-15”: “Light snow and a gentle breeze”,  
“2025-02-16”: “Sleet and a gentle breeze”,  
“2025-02-17”: “Light rain and a gentle breeze”,  
“2025-02-18”: “Light rain showers and a gentle breeze”,  
“2025-02-19”: “Drizzle and a gentle breeze”,  
“2025-02-20”: “Light rain and light winds”,  
“2025-02-21”: “Light rain and light winds”  
}  
i got this after running my python script for question 4 but, got  
Error: At root: Property name mismatch" this error message

---

[@s.anand](/u/s.anand) sir,  
I don’t understand this error. In the website, the movie name doesn’t have a colon “:”, but in the result it is expecting so.

image description: The image contains a JSON formatted data structure representing movie information, and an error message. The movie information includes an ID, title, year, and rating. The error message specifies a mismatch in the title.
image text:
```json
},
{
"id": "tt8790086",
"title": "11. Kraven the Hunter",
"year": "2024",
"rating": "5.4"
Error: At [10].title: Values don't match. Expected: "11. Kraven: The Hunter". Actual: "11. Kraven the Hunter"
```

---

For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

---

here is the difference of ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .  
and in the question also it is mentioned that may be manually you need to correct. just give a try.

---

run your console script again and match the description.

---

yes, same happened with me . correct it manually.

---

In q10 links are not accessible through pdf and also creating problems while converting to markdown

---

image description: The image is a webpage featuring information on weather data integration for AgroTech Insights, a company specializing in agricultural technology. The page details the company's objectives, the task assigned, and provides sample outputs.
image text: Learn about the re package. Watch Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex). Learn about the datetime package. Watch Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones Weather Data Integration for AgroTech Insights AgroTech Insights is a leading agricultural technology company that provides data-driven solutions to farmers and agribusinesses. By leveraging advanced analytics and real- time data, AgroTech helps optimize crop yields, manage resources efficiently, and mitigate risks associated with adverse weather conditions. Accurate and timely weather forecasts are crucial for making informed decisions in agricultural planning and management. Farmers and agribusinesses rely heavily on precise weather information to plan planting schedules, irrigation, harvesting, and protect crops from extreme weather events. However, accessing and processing weather data from multiple sources can be time-consuming and technically challenging. AgroTech Insights seeks to automate the extraction and transformation of weather data to provide seamless, actionable insights to its clients. AgroTech Insights has partnered with various stakeholders to enhance its weather forecasting capabilities. One of the key requirements is to integrate weather forecast data for specific regions to support crop management strategies. For this purpose, AgroTech utilizes the BBC Weather API, a reliable source of detailed weather information. Your Task As part of this initiative, you are tasked with developing a system that automates the following: 1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Manila. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city). 2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId. 3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedweatherDescription. The output would look like this: { "2025-01-01": "Sunny with scattered clouds" "2025-01-02": "Partly cloudy with a chance of rain" "2025-01-03": "Overcast skies" // ... additional days } What is the JSON weather forecast description for Manila? "2025-02-16": "Sunny and a gentle breeze", "2025-02-17": "Sunny and a gentle breeze", "2025-02-18": "Sunny and a gentle breeze" "2025-02-19": "Sunny and a gentle breeze", "2025-02-20": "Sunny and a gentle breeze" } Check

Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.

---

The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

---

Thanks!.  
It is working now. I had to manually correct 5 movie titles to get it correct.

---

The image shows a text snippet of JSON data and an error message. The JSON data includes fields like "id", "title", "year", and "rating". The error message indicates a mismatch in the "year" field, where the expected value is "2025-" but the actual value is "2025-".
image text: What is the JSON data?
},
{
"id": "tt10078772",
"title": "9. Flight Risk",
"year": "2025",
"rating". "5.5"
Error: At [10].year: Values don't match. Expected: "2025-". Actual: "2025-"
  
What 's the solution?

---

Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.

Please refer the instruction.  
image description: The image features text and a button, likely from a website or application. The text is a warning about IMDb search results.
image text: IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.
Check

---

you can manually add space after the hyphen

---

I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

---

Double-check that the rating field in the JSON is indeed a float (`2.9`) and not a string (`"2.9"`) in your code.

---

That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.

But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

---

Write the code referencing the provided collab file and make sure to use the API key  
The output actually changes once in a while so you might need to run the code a few times before getting in right  
<https://tds.s-anand.net/#/bbc-weather-api-with-python>

---

your most recently saved score will be evaluated

---

I am getting this error again and again after running the code in collab this city `Nur-Sultan`?  
Here's a description of the image:
The image displays a Python error message related to a weather data retrieval attempt. The error message is "NameError: name 'location\_id' is not defined," and it appears the code is attempting to construct a URL to fetch weather data from the BBC website. The error message highlights the line of code where the problem occurs and provides a traceback.
image text:
Error: Could not find location ID for Nur-Sultan
NameError
Traceback (most recent call last)
<ipython-input-9-128760ee996a> in <cell line: 0>()
33
34 # BBC Weather URL
---> 35 weather\_url = f'https://www.bbc.com/weather/{location id}'
36
37 # Fetch weather data
NameError: name 'location\_id' is not defined

---

In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

---

Not able to get the missing links in Q10  
Any suggestions welcome please

---

For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

---

there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

---

I’m getting the same error in Q4:

Here's a description of the image:
The image is a user interface with a dark top portion and a white main area. The top part displays a sample JSON formatted text. The lower white part has the following elements: A question is presented "What is the JSON weather forecast description for Los Angeles?". Below this, a text box containing JSON formatted weather forecast information for several days is displayed. There's an error message "Error: At root: Property name mismatch". In the very bottom-left corner a button "Check" is visible.
image text:
```json
The output would look like this:
{
"2025-01-01": "Sunny with scattered clouds"
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
What is the JSON weather forecast description for Los Angeles?
"25-02-16": Sunny and light winds,
"25-02-17": "Sunny and light winds",
"25-02-18": "Sunny and light winds",
"25-02-19": "Sunny and light winds",
"25-02-20": "Sunny and light winds",
"25-02-21": "Sunny and light winds"
}
Error: At root: Property name mismatch
Check
```

---

How to actually do the HNRSS one…i can’t find much.

---

How did u do the links? I’m unable to do links

---

Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.

This is a format issue when the json is scrapped from the browser.

---

Request help on Q4 aboutBBC weather data, the instructions in the question tell us to use BBC broker API and get issueDate & enhancedWeatherdescription value pairs. However, it seems there are only 2 unique values of issueDate (not the expected 14 days)

Please clarify, sharing code and output below for reference.

Code:

```
import requests

url = "https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/" + getlocid('Bogota')
response = requests.get(url)
json_data=response.json()
print(f"The number of days data is {len(json_data['forecasts'])}")

weather_data = {}

for i in range(len(json_data['forecasts'])): # Use range to create an iterable sequence of indices
  issue_date = json_data['forecasts'][i]['summary']['issueDate']
  weather_description = json_data['forecasts'][i]['summary']['report']['enhancedWeatherDescription']
  weather_data[issue_date]=weather_description
  print("Iteration No. " + str(i))
  print(issue_date)
  print(weather_description)
  
print("Final Weather Data json below")
print(weather_data)

```

Output

```
The number of days data is 14
Iteration No. 0
2025-02-08T04:00:00-05:00
Light rain showers and a gentle breeze
Iteration No. 1
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 2
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 3
2025-02-08T04:00:00-05:00
Thundery showers and light winds
Iteration No. 4
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 5
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 6
2025-02-08T04:00:00-05:00
Light rain showers and light winds
Iteration No. 7
2025-02-08T04:00:00-05:00
Thundery showers and a gentle breeze
Iteration No. 8
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 9
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 10
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Iteration No. 11
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 12
2025-02-08T16:01:58-05:00
Thundery showers and light winds
Iteration No. 13
2025-02-08T16:01:58-05:00
Thundery showers and a gentle breeze
Final Weather Data json below
{'2025-02-08T04:00:00-05:00': 'Thundery showers and a gentle breeze', '2025-02-08T16:01:58-05:00': 'Thundery showers and a gentle breeze'}

```

Edit: For now, I have worked around with code posted by [@21f3002277](/u/21f3002277). But the doubt about the question remains

---

same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

---

I have got the same error as well, verified there are workflows run in my repo/actions/runs  
When I checked the reasons, it could be due to API limit exceeded in a hour, but tried even after some time but no workflows found.

Here's a description of the image:
The image shows a webpage with a dark theme, likely a workflow management page. It features a search bar for filtering workflow runs, and two workflow runs listed under "2 workflow runs". There is also a section to provide feedback.
image text: All workflows
Showing runs from all workflows
Help us improve GitHub Actions
Tell us how to make GitHub Actions work better for you with three quick questions.
2 workflow runs
✔ Action runs everyday
Action runs everyday #6: Scheduled
✔ Action runs everyday
Action runs everyday #5: Manually run by Rajalakshmi12
main
main
Q Filter workflow runs
Give feedback
X
Event
Status
Branch
Actor
2 hours ago
15s
2 hours ago
145

---

Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

---

Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

---

You can find some text blue in color and underline use some dumy url it will work

---

You can find some lines having second, third words are uniformly aligned. Those are tables

---

When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

---

In Q 6 I checked all the startups link at [Hacker News - Newest: "Startup"](https://hnrss.org/newest?q=Startup)… none is greater than 81 then how to submit that link… is there something i am missing

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) ,for question 3, even a random response is shown correct

image description: The image displays a section of a web application testing CORS configuration. It shows a question about the API endpoint URL, with the correct answer provided.
image text: 5. Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?
http://127.0.0.1:8000
Correct
We'll check by sending a request to this URL with ?country=... passing different countries.
Check

image description : A screenshot showing a web browser displaying "Pretty-print" and the number "44". The browser's address bar shows "127.0.0.1:8000/?country=india". There are tabs for "Mathematics for Da...", "BS-DS\_Jan 2025 Gr...", "Untitled1.ipynb - Co..." and a chat icon.
image text:
C
Mathematics for Da...
Pretty-print
44
i
127.0.0.1:8000/?country=india
BS-DS\_Jan 2025 Gr...
CO Untitled1.ipynb - Co... Ch

---

Sir I have solved Q2, But a problem arises that, At the index 11, in the IMdb website it is listed “The Recruit” but it is showing Expected: “Graymail”.  
Here's a description of the image:
The image displays a segment of data in a JSON-like format, presumably representing a list of items (movies or shows) with their associated attributes. Each entry has "id", "title", "year", and "rating". An error message at the bottom indicates a mismatch in the "title" field.
image text:
```json
{ "id": "tt26584495", "title": "8. Companion", "year": "2025", "rating": "7.4" },
{ "id": "tt13406094", "title": "9. The White Lotus", "year": "2021-", "rating": "8.0" },
{ "id": "tt26748649", "title": "10. High Potential", "year": "2024-", "rating": "7.6" },
{ "id": "tt28607951", "title": "11. Anora", "year": "2024", "rating": "7.8" },
{ "id": "tt16030542", "title": "12. The Recruit", "year": "2022- ", "rating": "7.4" },
{ "id": "tt7597900", "title": "13. The Rookie", "year": "2018-", "rating": "8.0" }
Error: At [11].title: Values don't match. Expected: "12. Graymail". Actual: "12. The Recruit"
```

How to fix this?

---

you have to manually change for a few mismatch.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png) s.anand:

> [@21F1005510](/u/21f1005510) Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.
>
> **Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly  
It might need around 6-7 amendments

---

The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.  
In your output, there are only two unique issueDate values:  
2025-02-08T04:00:00-05:00  
2025-02-08T16:01:58-05:00  
This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you need to modify your approach by using the actual forecast day for each day instead.

---

While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

---

I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.

Please help with the second issue.

1. For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.  
   How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.

> Error: No daily scheduled triggers found in workflows.

2. I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

---

image description: The image shows a dark background with text describing a JSON data structure, presumably about movies. It has a question "What is the JSON data?". Below the question, there's a block of JSON data enclosed in a red-bordered box, listing movie IDs, titles, and other details. The bottom part of the image displays an error message in red, indicating a mismatch in movie IDs, and specifying the expected and actual values.
image text: What is the JSON data?
{ "id": "tt0060196", "title": "The Good, the Bad and the Ugly", "year": "1966", "
{ "id": "tt0137523", "title": "Fight Club", "year": "1999", "rating": "8.8" },
{ "id": "tt0120737", "title": "The Lord of the Rings: The Fellowship of the Ring"
]
Error: At [0].id: Values don't match. Expected: "tt20221436". Actual: "tt0437179"
  
I have tried several times but still recieving this as error. Please help

---

image description: The image displays a web development interface. The upper section outlines five steps related to API development, fetching Wikipedia content, extracting headings, generating markdown outlines, and enabling CORS. Below, there's a prompt for entering the API endpoint URL, followed by "TypeError: Load failed". The main section displays console output with several errors related to blocked content and access control.
image text: 1. API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that accepts a country query parameter.
2. Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
3. Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, Ixml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6) from the page, maintaining order.
4. Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
5. Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?
http://localhost:8000/api/outline
TypeError: Load failed
We'll check by sending a request to this URL with ?country=... passing different countries.
Check
[blocked] The page at https://exam.sanand.workers.dev/tds-2025-01-ga4 requested insecure content from http://localhost:8000/api/outline?country=The+Bahamas. This content was blocked and must
► Not allowed to request resource
▼ Fetch API cannot load http://localhost:8000/api/outline?country=The+Bahamas due to access control checks.
f (anonymous function) - fetch.js:75
f (anonymous function) exam-tds-2025-01-ga4.js:183:10713
N enqueueJob
f d- exam-tds-2025-01-ga4.js:183:10857
f (anonymous function) - exam.js:331
f p- exam.js:339
f (anonymous function) exam.js:282
f sentryWrapped - helpers.ts:116
[blocked] The page at https://exam.sanand.workers.dev/tds-2025-01-ga4 requested insecure content from http://localhost:8000/api/outline?country=The+Bahamas. This content was blocked and must
► Not allowed to request resource
► Fetch API cannot load http://localhost:8000/api/outline?country=The+Bahamas due to access control checks.
[blocked] The page at https://exam.sanand.workers.dev/tds-2025-01-ga4 requested insecure content from http://localhost:8000/api/outline?country=The+Bahamas. This content was blocked and must
► Not allowed to request resource
► Fetch API cannot load http://localhost:8000/api/outline?country=The+Bahamas due to access control checks.
[blocked] The page at https://exam.sanand.workers.dev/tds-2025-01-ga4 requested insecure content from http://localhost:8000/api/outline?country=The+Bahamas. This content was blocked and must
► Not allowed to request resource
► Fetch API cannot load http://localhost:8000/api/outline?country=The+Bahamas due to access control checks.
  
I’m able to see the markdown response for different countries for question 3, GA 4 on my browser but I’m unable to submit it probably because of network issues. Can someone help me with a fix. Thank you.

---

Here's a description of the image:
The image is a section of text with code snippets and an error message, likely related to a programming assignment.
image text:
4. Submit: Submit the JSON data in the text box below.
Impact
By completing this assignment, you'll simulate a key component of a streaming service's content acquisition strategy. Your work will enable StreamFlix to
make informed decisions about which titles to license, ensuring that their catalog remains both diverse and aligned with subscriber preferences. This, in
turn, contributes to improved customer satisfaction and retention, driving the company's growth and success in a competitive market.
What is the JSON data?
{
"id": "tt26584495",
"title": "10. Companion - Die perfekte Begleitung",
"year": "2025",
"rating": "7.4"
},
Error: At [10].year: Values don't match. Expected: "2021-". Actual: "2021"
IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your
scraper code.
  
how to tackle this error as in 10 th movie year is 2025 but it is showing 2021

---

City in my question is `Nur-Sultan` .When i search `Nur-Sultan` city name in BBC weather page .its show nothing . when i search in google then show Nur Sultan become Astana . then i am going this city name "Astana ". and got location id 1526273. after i run in collab then showing error.  
Here's a description of the image:
The image displays a computer screen with code and an error message. The code appears to be Python, with comments indicating it's related to weather data and converting it to JSON format. An `IndexError` is reported, specifically "list index out of range," indicating a problem with accessing elements within a list. The traceback shows the error originating in the line trying to construct a weather URL, likely due to a missing or invalid 'id' element in the response data. Additional details show that the code execution was completed at 12:42 PM.
image text:
datelist = pd.date\_range(datetime.today(), periods=len(daily\_summary\_list)).tolist()
datelist = [date.date().strftime('%Y-%m-%d') for date in datelist]
# Map dates to descriptions
weather\_data = {date: desc for date, desc in zip(datelist, daily\_summary\_list)}
# Convert to JSON
weather\_json = json.dumps(weather\_data, indent=4)
print(weather\_json)
IndexError
Traceback (most recent call last)
<ipython-input-1-054dd394d4e3> in <cell line: 0>()
22 # Fetch location data
23 result = requests.get(location\_url).json()
---> 24 weather\_url = 'https://www.bbc.com/weather/' + result['response'] ['results'] ['results'][0]['id']
25
26 # Fetch weather data
IndexError: list index out of range
EN English (India)
English (India)
Finance headline
India Foreign Ex...
2s
completed at 12:42PM
Q Search

---

this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

---

while searching dont put any other filter other than asked in Problem statement.

---

image description: The image shows a question about the markdown content of a PDF, formatted with prettier@3.4.2. The markdown includes a heading, a paragraph, a sub-heading, two bullet points, and an error message. The text also mentions that it is difficult to get correct Markdown output from a PDF and manual corrections are often required.
image text: What is the markdown content of the PDF, formatted with prettier@3.4.2?
# Pauci Audentia Sperno Eum
Tracto adeptio somnus. Neque tantum desidero porro est civitas caute laboriosam valetudo.
## Key Points
- Vomito antiquus consequuntur
- Amplus curis subnecto
Error: Words like back, legislature, info are missing (or not separated as words)
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question
only checks a few basic things.
  
Can anyone help me with the 10th question. Whatever I changed with the code , it is asking something. I checked that these words are not present in the pdf itself

---

I didn’t get any error for Astana.  
The error may be due to incorrect loops in your code that’s why it’s going out of range, check for that.

image description: The image is a screenshot of a Jupyter Notebook interface, likely used for data analysis or programming. The notebook is titled "bbc-weather-scraping.ipynb" and shows weather data. The interface includes a menu bar, a toolbar, and a main area with code cells and output. The main area is showing a table of weather data.
image text: bbc-weather-scraping.ipynb ☆ Cannot save changes
File Edit View Insert Runtime Tools Help
+ Code + Text
Copy to Drive
7 25-02-16 -11° -14° Thick cloud and a gentle breeze
[99]
8 25-02-17 -11° -11° Light cloud and a gentle breeze
9 25-02-18 -7° -12° Light snow and a gentle breeze
10 25-02-19 -5° -11° Sunny and a moderate breeze
11 25-02-20 -7° -13° Sunny and a gentle breeze
12 25-02-21 -8° -14° Sunny and a gentle breeze
13 25-02-22 -8° -14° Light snow and a gentle breeze
Next steps: Generate code with df View recommended plots New interactive sheet
df.to\_json(orient='records')
Share
P
RAM
Disk
Gemini
↑↓
'[{"Date":"25-02-09", "High":"-10\\u00b0","Low":"-11\\u00b0","Summary":"Sunny intervals and light winds"},{"Date":"25-02-10","High":"-7\\u00b0","Low":"-10\\u00b0","Summary":"Mi sty and a moderate breeze"},{"Date":"25-02-11","High":"-6\\u00b0","Low":"-13\\u00b0","Summary": "Sunny and a gentle breeze"},{"Date":"25-02-12", "High":"-5\\u00b0","Low":"-7\\u0 0b0", "Summary": "Light snow and a fresh breeze"}, {"Date":"25-02-13", "High":"-7\\u00b0","Low":"-9\\u00b0","Summary":"Light snow and a fresh breeze"},{"Date":"25-02-14", "High":"- 8\\u00b0","Low":"-10\\u00b0","Summary":"Light snow and a moderate breeze"},{"Date":"25-02-15","High":"-8\\u00b0","Low":"-12\\u00b0","Summary": "Light snow and a gentle breez e"},{"Date":"25-02-16", "High":"-11\\u00b0","Low":"-14\\u00b0","Summary": "Thick cloud and a gentle breeze"},{"Date":"25-02-17","High":"-11\\u00b0","Low":"-11\\u00b0", "Summar y":"Light cloud and a gentle breeze"},{"Date":"25-02-18","High":"-7\\u00b0","Low":"-12\\u00b0","Summary": "Light snow and a gentle br...'

---

It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

---

what is this magic trick… please elaborate …

```
Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"

```

i dont see that value in data …

---

You can manually edit that. I also have to manually edit one entry to get the correct answer.

---

Hi,  
As mentioned in the question, you have to sort by “joined” so it should be “<https://api.github.com/search/users?q=location:Seattle+followers:>>120&sort=joined&order=desc”

---

There are two “Vienna”. The question4 is referring to which one?

---

Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

---

check if the action is commited

---

try copying the expected result and pasting it inside the quotations

---

Check the log of the daily commit .

---

Ahh, I have the same doubt too!

---

For the links, this format worked for me:  
[ < link text > ] (#)

---

Yes I got it now. Thank you!

---

it should be “2.9” instead of 2.9

---

looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

---

Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”

{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}

my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

---

I am getting missing links as error in the 10th question. How to do it?

---

Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

---

Yes happened to me too, refresh the page, mine got fixed!

---

Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

---

Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

---

u have used a apace (\_) after 2.9 which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

---

Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14 pairs.

---

Here's a description of the image:
The image shows a screenshot of a web browser displaying the BBC Weather website. The website is showing a weather forecast for Karachi, Pakistan, and a world map with weather forecasts for several other cities such as London, Chicago, Dakar, and others. The developer tools are open on the right side, showing the network activity.
image text:
M Inbox - 22
hnrss.org/
My Dashb
Graded A
Ex TDS 2025
GA4 - Dat
country\_a
BBC Weat
locator-se +
bbc.com/weather
☆
BBC
WEATHER
the latest Tates
Book Now →
X
R
Elements Console Sources Network
Performance >>
3 542 4
X
Home
News Sport
Business
Q
۲.۹☐ Preserve log☐ Disable cache No throttling
▼
企业
Y locat
Invert More filters
karachi
Karachi, Pakistan
Q X
All
Fetch/XHR Doc CSS JS Font Img Media Manifest WS Wasm Other
150,000 ms
50,000 ms
=
100,000 ms
200,000 ms
250,000 ms
300,000 ms
3511
WAS
Name
Status
Type
> locations?api\_key=AGbFAKx58hyjQScCXIYr... 200
xhr
Initiator
search.js:2
Size
Time
486 B
2.31 s
Weather forecasts for thousands of
locations around the world
London
Chicago
1/234 requests 486 B/600 kB transferred 255 B/4.8 MB resources
Console Al assistance X Issues X
Tbilisi
Dakar
San José C
Mombasa
Brasília
Type here to search
G+
X
Send feedback
Activate Windows
How can I help youco to Settings to activate Windows.
Chat messages and the selected network request are sent to Google and may be seen by human reviewers to improve this feature. This
is an experimental Al feature and won't always get it right. Learn about Al in DevTools
'They should not be...
ENG
04:36 PM
09-02-2025
10

* Open the BBC Weather website.
* Press `Ctrl + Shift + I`.
* Select the ‘Network’ menu.
* Select ‘Fetch/XHR’.
* Type ‘Karachi’ in the input field on the website. **Do not press Enter** while entering the location; just type the location. Pressing Enter might cause ‘location?api\_key=…’ to disappear.
* ‘location?api\_key=…’ will appear in the inspect menu.
* Double-click it to open a web page ([https://locator-service.api.bbci.co.uk/locations?api\_key={api\_key}](https://locator-service.api.bbci.co.uk/locations?api_key=%7Bapi_key%7D)). This will give the API.
* Alternatively, single-clicking ‘location?api\_key=…’ will open headers where you can see the Request URL and the API key.

---

type 2025 instead of only using 25 for the year

---

HOW TO DO SCRAPING USING GITHUB ACTIONS  
I’m getting no workflow runs error Sir

---

How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

---

[@22f3000657](/u/22f3000657)

you can try this-

<https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India>

change the city and country in the url

there will be a bounding\_box field: [min\_lat, max\_lat, min\_long, max\_long]

---

#question 10  
Hi, Can anyone help me with Question 10?  
No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

---

Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and putting the breakpoint followed by writing the code in the console to retrieve the expected answer

---

Here's a description of the image:
The image shows a user interface for entering a repository URL. It has an input field with an error message.
image text:
Enter your repository URL (Format: https://github.com/USER/REPO):
https://github.com/AryanTikam/AryanTikam
Error: Latest run does https://github.com/AryanTikam/AryanTikam/actions/runs/13225425496 not include 23f2001216@ds.study.iitm.ac.in in the name
  
Can’t seem to get this working, have tried many variations by now like including my email in each of the name sections in every possible permutation. Probably just some silly mistake I haven’t noticed yet but any help would be appreciated. On Linux Mint if that’s relevant.

main.yml:

```
name: Daily Commit Workflow

on:
  schedule:
    - cron: '10 17 * * *' 
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

steps:
      - name: Checkout repository
        uses: actions/checkout@v3

- name: Add commit using 23f2001216@ds.study.iitm.ac.in
        env:
          PAT: ${{ secrets.PAT }}  # PAT stored as a secret
        run: |
          git config --global user.name "Aryan"
          git config --global user.email "23f2001216@ds.study.iitm.ac.in"

echo "Daily commit on $(date)" >> daily-log.txt

git add daily-log.txt
          git commit -m "Automated daily commit on $(date)"

ls -la
          git status

git push origin main  
          git push "https://${{ secrets.PAT }}@github.com/${{ github.repository }}.git" main

```

---

Hi Team,

I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,  
Here's a brief description of the image:
The image displays JSON data along with an error message. The JSON data seems to be related to movie information, including the title "Venom: The Last Dance," year "2024," and a rating of "6.0." An error message indicates a title mismatch, and there are notes about regional variations and periodic updates.
image text: What is the JSON data? title": "10. Venom: The Last Dance", "year": "2024", "rating": "6.0" }, { "id": "tt30292390", Error: At [10].title: Values don't match. Expected: "11. Sebastian Fitzeks Der Heimweg". Actual: "11. The Calendar Killer" IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.
  
I took first 25 films which 5 to 6 rating, but json seems to be different.

Could anyone please tell me what i did wrong here?

---

Solved the above issue, please ignore it.

---

Believe it or not, I solved it

Here's a description of the image:
The image is a screenshot of a coding or technical exercise. There's a question at the top about markdown content, and a code snippet is presented, along with the phrase "Decumbo decumbo suadeo totidem apto." A checkmark is present, suggesting a correct answer. The text below explains the difficulty in obtaining correct Markdown output from a PDF.
image text: What is the markdown content of the PDF, formatted with prettier@3.4.2?
|adficio|chirographum|
|---|---|
|vitae|ipsam|
|spectaculum|claudeo|
|comes|celebrer|
Decumbo decumbo suadeo totidem apto.
Correct
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things.

---

In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

---

first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors

yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.

but i have an issue it gave me error that it does not contains the word “bash, javascript, whole redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

---

this is a changing dataset so make changes to your answer accordingly and you will get it correct

---

Do the necessary changes as it is said below as it is an everchanging dataset.  
You will get the answer correct once you make the changes asked after checking.

---

check you code and do the changes like max\_latitude  
replace [0] to [1]

---

Here's a description of the image:
The image presents a code-like interface. At the top, there's a snippet describing weather conditions for a few days in January 2025. Below that, it asks "What is the JSON weather forecast description for Nur-Sultan?" and provides a detailed forecast for February 2025, with descriptions such as "Light snow and a gentle breeze." An error message "TypeError: Cannot read properties of undefined (reading 'id')" is also present at the bottom. A "Check" button is visible.
image text:
```
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
What is the JSON weather forecast description for Nur-Sultan?
"2025-02-13": "Light snow and a fresh breeze",
"2025-02-14": "Light snow and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze",
"2025-02-19": "Light cloud and a gentle breeze",
"2025-02-20": "Light cloud and a gentle breeze",
"2025-02-21": "Sunny and a moderate breeze"
}
TypeError: Cannot read properties of undefined (reading 'id')
Check
```  
sir in Q4 i am getting this error:

```
TypeError: Cannot read properties of undefined (reading 'id')

```

please help me out with it.  
Additionally even if i write anything in the code block the err remains same!

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand) sir please help me out as only this question left.  
anyone facing this issue? let me know

```

{
     "25-02-09": "Partly cloudy and a moderate breeze",
     "25-02-10": "Sunny intervals and a moderate breeze",
     "25-02-11": "Sunny and a gentle breeze",
     "25-02-12": "Light snow and a fresh breeze",
     "25-02-13": "Light snow and a fresh breeze",
     "25-02-14": "Light snow and a gentle breeze",
     "25-02-15": "Light snow and a gentle breeze",
     "25-02-16": "Light snow and a gentle breeze",
     "25-02-17": "Light snow and a gentle breeze",
     "25-02-18": "Sunny intervals and a gentle breeze",
     "25-02-19": "Light cloud and a gentle breeze",
     "25-02-20": "Light cloud and a gentle breeze",
     "25-02-21": "Sunny and a moderate breeze"
}

```

---

in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.  
regards and thanks.

---

Here's a brief description of the image:
The image shows a step-by-step guide for developing an API. It includes instructions for API development, fetching Wikipedia content, extracting headings, generating a markdown outline, and enabling CORS. There's a prompt to input the URL of the API endpoint, along with an example. An error message "TypeError: Failed to fetch" is displayed.
image text:
```
## Contents
# Vanuatu
## Etymology
## History
### Prehistory
1. API Development: Choose any web framework (e.g., FastAPI) to develop the web application. Create an API endpoint (e.g., /api/outline) that
accepts a country query parameter.
2. Fetching Wikipedia Content: Find out the Wikipedia URL of the country and fetch the page's HTML.
3. Extracting Headings: Use an HTML parsing library (e.g., BeautifulSoup, Ixml) to parse the fetched Wikipedia page. Extract all headings (H1 to H6)
from the page, maintaining order.
4. Generating Markdown Outline: Convert the extracted headings into a Markdown-formatted outline. Headings should begin with #.
5. Enabling CORS: Configure the web application to include appropriate CORS headers, allowing GET requests from any origin.
What is the URL of your API endpoint?
http://127.0.0.1:8000/api/outline?country=france
TypeError: Failed to fetch
```
  
it is showing correct but if i reload the page or press ctrl+c in my terminal its showing this error what should i do now ??

---

Here's a brief description of the image:
The image is a webpage with text outlining a task related to media intelligence and Hacker News posts. The text explains the context of TechInsight Analytics and their need to automate the process of identifying and extracting relevant Hacker News posts. The task involves using the Hacker News RSS API to find posts about "WebRTC" with at least 30 points. A specific URL is provided as an incorrect answer.
image text:
6 Search Hacker News (1 mark)
Media Intelligence for TechInsight Analytics
Techinsight Analytics is a leading market research firm specializing in technology trends and media intelligence. The company provides actionable insights to tech companies,
startups, and investors by analyzing online discussions, news articles, and social media posts. One of their key data sources is Hacker News, a popular platform where tech
enthusiasts and professionals share and discuss the latest in technology, startups, and innovation.
In the rapidly evolving tech landscape, staying updated with the latest trends and public sentiments is crucial for Techinsight Analytics' clients. Manual monitoring of Hacker News
posts for specific topics and engagement levels is inefficient and error-prone due to the high volume of daily posts. To address this, Techinsight seeks to automate the process of
identifying and extracting relevant Hacker News posts that mention specific technology topics and have garnered significant attention (measured by points).
TechInsight Analytics has developed an internal tool that leverages the HNRSS API to fetch the latest Hacker News posts. The tool needs to perform the following tasks:
1. Topic Monitoring: Continuously monitor Hacker News for posts related to specific technology topics, such as "Artificial Intelligence," "Blockchain," or "Cybersecurity."
2. Engagement Filtering: Identify posts that have received a minimum number of points (votes) to ensure the content is highly engaging and relevant.
3. Data Extraction: Extract essential details from the qualifying posts, including the post's link for further analysis and reporting.
To achieve this, the team needs to create a program that:
Searches Hacker News for the latest posts mentioning a specified topic.
Filters these posts based on a minimum points threshold.
Retrieves and returns the link to the most relevant post.
Your Task
Search using the Hacker News RSS API for the latest Hacker News post mentioning WebRTC and having a minimum of 30 points. What is the link that it points to?
1. Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by
a minimum number of points.
2. Extract and Present Data: Extract the most recent <item> from this result. Get the <link> tag inside it.
3. Share the result: Type in just the URL in the answer.
What is the link to the latest Hacker News post mentioning WebRTC having at least 30 points?
https://news.ycombinator.com/item?id=41699323
Error: Incorrect link
①
Check

Respected Sir,  
How can I Solve this, I’m not able to solve this one

---

Hi,  
For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

---

Change it manually.  
add the expected answer

---

when you press ctrl+c it turns off the server and same goes for refresh.  
also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

---

ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

---

It is written in the ques to get the link in the link tag. Not the post link. Like this  
image description: The image shows an XML file structure with code that includes a title related to "Hacker News", article URLs, and specific dates and comments. The text is displayed on a dark background.
image text:
```
This XML file does not appear to have any style information associated with it. The document tree is shown below.
▼<rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0">
▼<channel>
<title>Hacker News - Newest: "LLM"</title>
<link>https://news.ycombinator.com/newest</link>
<description>Hacker News RSS</description>
<docs>https://hnrss.org/</docs>
<generator>hnrss v2.1.1</generator>
<lastBuildDate>Sun, 09 Feb 2025 08:44:00 +0000</lastBuildDate>
<atom:link href="https://hnrss.org/newest?points=78&q=LLM" rel="self" type="application/rss+xml"/>
▼<item>
▼<title>
<![CDATA[ DoppelBot: Replace Your CEO with an LLM ]]>
</title>
▼<description>
<![CDATA[ <p>Article URL: <a href="https://modal.com/docs/examples/slack-finetune">https://modal.com/docs/examples/slack-finetune</a></p>
<p>Commen
href="https://news.ycombinator.com/item?id=42933256">https://news.ycombinator.com/item?id=42933256</a></p> <p>Points: 232</p> <p># Comments: 116</p
</description>
<pubDate>Tue, 04 Feb 2025 15:08:21 +0000</pubDate>
<link>https://modal.com/docs/examples/slack-finetune</link>
<dc:creator>gk1</dc:creator>
<comments>https://news.ycombinator.com/item?id=42933256</comments>
<guid isPermaLink="false">https://news.ycombinator.com/item?id=42933256</guid>
</item>
▼<item>
```

---

Thank you bro, I will try this

---

not at all. your last saved marks will be considered

---

just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

---

extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

---

Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of  
class: wr-day-summary

---

Hi, please ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

---

In question 1 i am getting this error

```
 {
    "id": "tt21227864",
    "title": "2. You're Cordially Invited",
    "year": "2025",
    "rating": "5.5"
  }

```

my answer is in above format i tried changing to “2024-”, "2024- " to number tried after reloading the page but still i am getting  
Error: At [11].year: Values don’t match. Expected: “2024”. Actual: "2024– "

---

You have to manually change these thing  
from actual change to expected.  
For me, error was almost 10 times.

---

on your 11th or 12th instance change it  
write the actual value

---

If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

---

Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

---

Here's a description of the image:
\*\*image description:\*\* The image is a screenshot of a web page related to Markdown formatting. There's a navigation bar at the top showing the time remaining, score, and options to check and save. The main content discusses converting PDFs to Markdown, formatting, and submission. It highlights the "Impact" of the project with bullet points about enhancing productivity, improving quality, supporting scalability, and facilitating integration. Below, there's a code snippet that appears to be an incomplete or incorrect Markdown output. An error message "Missing code" is present.
\*\*image text:\*\*
03:08:26 left Score: 7/10 Check all Save
Markdown and ensuring their consistent formatting. This project is critical for supporting EduDocs' commitment to delivering high-quality, accessible educational resources to its clients.
q-pdf-to-markdown.pdf has the contents of a sample document.
1. Convert the PDF to Markdown: Extract the content from the PDF file. Accurately convert the extracted content into Markdown format, preserving the structure and formatting as much as possible.
2. Format the Markdown: Use Prettier version 3.4.2 to format the converted Markdown file.
3. Submit the Formatted Markdown: Provide the final, formatted Markdown file as your submission.
Impact
By completing this exercise, you will contribute to EduDocs Inc.'s mission of providing high-quality, accessible educational resources. Automating the PDF to Markdown conversion and ensuring consistent formatting:
\* Enhances Productivity: Reduces the time and effort required to prepare documentation for clients.
\* Improves Quality: Ensures all documents adhere to standardized formatting, enhancing readability and professionalism.
\* Supports Scalability: Enables EduDocs to handle larger volumes of documentation without compromising on quality.
\* Facilitates Integration: Makes it easier to integrate Markdown-formatted documents into various digital platforms and content management systems.
What is the markdown content of the PDF, formatted with prettier@3.4.2?
\[tricesimus admitto](https://example.com/tricesimus-admitto)
Suggero comes denique argentum.
Desipio crudelis antea quis.
\[adeptio colligo](https://example.com/adeptio-colligo)
Error: Missing code
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things.
  
i wrote everything that was there in the pdf file after converting to markdown, there is no code inside the pdf file then how does it expect to have code in markdown, can anyone help

---

Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

---

Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

---

The IMDB and weather questions was a pain along with the 10th question, wasted so much time [@s.anand](/u/s.anand) , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to sit and correct the JSON file and no comments on the 10th question’s part.

I am fine with the academia being challenging to study not the evalation making me manually edit solutions

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

yes change manually, there are slight changes which we have to do

---

For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

---

for second query i am getting this result as row 4 and 5 (Screenshot)… but when testing the results it shows

```
{"id":"tt22804850","title":"3. The Sand Castle","year":"2024","rating":"4.7"},
{"id":"tt10128846","title":"4. Megalopolis","year":"2024","rating":"4.8"},
{"id":"tt2322441","title":"5. Fifty Shades of Grey","year":"2015","rating":"4.2"},
{"id":"tt4978420","title":"6. Borderlands","year":"2024","rating":"4.6"},

```

Error: At [4].title: Values don’t match. Expected: “5. Cinquanta sfumature di grigio”. Actual: “5. Fifty Shades of Grey”  
image description: The image is a screenshot presenting movie information, with descriptions for "Megalopolis" and "Fifty Shades of Grey".
image text:
4. Megalopolis
2024 2h 18m 15
★4.8 (33K) Rate 55 Metascore
The city of New Rome faces the duel between Cesar Catilina, a brilliant artist in mayor Franklyn Cicero. Between them is Julia Cicero, with her loyalty divided bet
5. Fifty Shades of Grey
2015 2h 5m 18
4.2 (344K) Rate 46 Metascore
Literature student Anastasia Steele's life changes forever when she meets hands

---

image description: The image presents a JSON object formatted to describe weather forecast for Vienna. The object includes dates and weather descriptions. An error message "Error: At root: Different number of properties" appears at the bottom.
image text: What is the JSON weather forecast description for Vienna?
{
"2025-02-10": "Sunny and a gentle breeze",
"2025-02-11": "Sunny intervals and a gentle breeze",
"2025-02-12": "Sunny and a gentle breeze",
"2025-02-13": "Light cloud and a moderate breeze",
"2025-02-14": "Light cloud and a gentle breeze",
Error: At root: Different number of properties
  
sir earlier it was correct and now i submit it again after running my code it shows error. sir i have done it correct two times earlier. but now again as i click on save button it changed. these tasks are taking too much time and creating more difficulties. please look into this [@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

image description: The image displays a JSON data structure with an error message. The JSON data appears to be a list of movie titles, years, and ratings. The error message indicates that the value for the "title" key at index 8 does not match the expected value.
image text: What is the JSON data?
"title": "1. The Night Agent",
"year": "2023-",
"rating": "7.5"
},
{
Error: At [8].title: Values don't match. Expected: "9. Incorrect answer jalement invités". Actual: "9. You're Cordially Invited"

Hi Team ,

Are we expecting the result to match exactly as per the benchmark of qa4.

---

just edit some of the spellings in answers manually as per errors you get n you are good to go.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

> Cinquanta sfumature di grigio

It is just a translation of the same movie… it’s not different  
Copy paste the Expected: “title” and click on check  
It’ll work

---

image description: The image displays a section of a webpage, likely related to an online quiz or assessment. Key elements include a time remaining counter, score, and buttons to "Check all" and "Save." The text provides instructions about the quiz's hackable nature and encourages discussion on Discourse, offering bonus marks for relevant posts. The user's login information and a logout button are also visible. A loading icon is present at the bottom.
image text: 02:23:44 left Score: 0 Check all Save
7. It s nackable. It's possible to get the answer to some questions by nacking the code for this quiz. That's allowed.
Have questions? Join the discussion on Discourse
Bonus marks for posting on Discourse
To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment.
You are logged in as 23f2001305@ds.study.iitm.ac.in.
Logout

Saved responses are not being displayed and also page keeps refreshing…

---

@all, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

---

try refreshing the page and re-run the script. as the data gets updated the answer also changes.

---

refer to the link post,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png)
[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65) [Tools in Data Science](/c/courses/tds-kb/34)

> use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format.
> [@23f2004752](/u/23f2004752)

---

i 'm here for the bonus marks,

But since i am here. Just want to appreciate the course and your efforts towards this.

We need more “teachers” like you, who really puts an extra effort in the course.

And i have never seen any course cool as this,

* like appreciating tweaking things, using dev console to tweak things, keep the code checks on client side (*and as S Anand’s Student i have leveraged that freedom ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:"), gave client side answer checks’s code to `o1` and it reverse engineered the minifed code, and lots of question were solved by that only, but really curious on how others are doing this*)
* keeping the cutting edge tech in course, like function calling from OpenAI.  
  ( *i have seen some students solutions, they were using regex to solve that problem ![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=12 ":smiling_face_with_tear:")*)

Here's a description of the image:
The image is a screenshot from a website or platform related to an educational course. The page seems to offer information about earning bonus marks, recent saves, and user account details. The page is dark green.
Here's the text from the image:
Have questions? Join the discussion on Discourse
Bonus marks for posting on Discourse
To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] with a relevant question or reply will get 1 bonus mark on this graded assignment.
You are logged in as 22f2001394@ds.study.iitm.ac.in.
Logout
Recent saves (most recent is your official score)
Reload from 2/9/2025, 9:26:17 PM. Score: 10
Reload from 2/9/2025, 7:48:07 PM. Score: 8
Reload from 2/9/2025, 7:44:44 PM. Score: 8

---

why everytime question 2 answer is showing error in json?

---

What error are you getting [@Abhay222](/u/abhay222) ?

Can you post a screenshot or error details ?

---

Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

---

[@s.anand](/u/s.anand)  
There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

---

getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

yes this kind errors.

---

[@Abhay222](/u/abhay222) [@22f3002184](/u/22f3002184)

if you look closely the expected value is `2024-`  and actual that you are supplying is `2024`.  
Difference ? your value does have a `-` and a space at the end.  
reason ? you might be scraping it ? `trim()` or maybe using `innerText` to get tag’s text ?

---

it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

---

Thank you Tanya for pointing out this issue.  
Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

---

any reply regarding this please

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2000113/48/67775_2.png) 22f2000113:

> For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

the movie may have different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png)
[GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/171) [Tools in Data Science](/c/courses/tds-kb/34)

> We have removed that button, cause it was causing confusion among the students.
> If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.
> Regards,
> TDS TA

Read this

---

Try changing it manually. Some values keep changing due to change in server.

---

Alright so in Q4 of W4, We have to extract weather forecast data from bbc servers for a given city. The city I have been given Nur-Sultan is not present in the bbc data base, it appears the city is now known as Astana and is listed in the bbc database as Astana.  
Since Nur-Sultan doesn’t exist in the bbc database, all of my attempts to extract data for it were meet with failure. So I extracted the data for Astana and pasted it in the portal but that doesn’t work as well and throws the following error “TypeError: Cannot read properties of undefined (reading ‘id’)”  
What am I suppose to do? [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
image description: The image is a coding exercise or tutorial, featuring instructions and a code snippet for fetching and formatting weather forecast data. The top section presents instructions for API integration, data extraction, and transformation, with the goal of creating a JSON object containing weather forecasts for Nur-Sultan. Below the instructions, there's a sample JSON object, and then a question asking for the JSON weather forecast description for Nur-Sultan. There's a code box containing weather forecast details with an error message: "TypeError: Cannot read properties of undefined (reading 'id')". The interface elements include a timer, score, check all, and save buttons.
image text: 06:00:20 left Score: 3/10 Check all Save
1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Nur-Sultan. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city).
2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId.
3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedWeatherDescription.
The output would look like this:
{
"2025-01-01": "Sunny with scattered clouds",
"2025-01-02": "Partly cloudy with a chance of rain",
"2025-01-03": "Overcast skies",
// ... additional days
}
What is the JSON weather forecast description for Nur-Sultan?
{
"2025-02-09": "Partly cloudy and a moderate breeze",
"2025-02-10": "Sunny intervals and a moderate breeze",
"2025-02-11": "Sunny and a gentle breeze",
"2025-02-12": "Light snow and a fresh breeze",
"2025-02-13": "Light snow and a fresh breeze",
TypeError: Cannot read properties of undefined (reading 'id')
Check

Below is the data for Astana that I was able to extract, Since Nur-Sultan doesn’t exist in the bbc database:  
{  
“2025-02-09”: “Partly cloudy and a moderate breeze”,  
“2025-02-10”: “Sunny intervals and a moderate breeze”,  
“2025-02-11”: “Sunny and a gentle breeze”,  
“2025-02-12”: “Light snow and a fresh breeze”,  
“2025-02-13”: “Light snow and a fresh breeze”,  
“2025-02-14”: “Light snow and a gentle breeze”,  
“2025-02-15”: “Light snow and a gentle breeze”,  
“2025-02-16”: “Light snow and a gentle breeze”,  
“2025-02-17”: “Light cloud and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”,  
“2025-02-19”: “Light cloud and a gentle breeze”,  
“2025-02-20”: “Light cloud and a gentle breeze”,  
“2025-02-21”: “Sunny and a moderate breeze”,  
“2025-02-22”: “Light snow and a moderate breeze”  
}

---

same problem, could anyone help what is wrong.

---

[@AnvithaV](/u/anvithav) check this out

---

No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i clicked on save button again it got wrong.

---

What error are you getting ?

---

how to approach question 8 of ga4

---

For question #8. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

---

still the same {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},  
Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

Change the value manually

---

I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

---

Have you given your email id in name ?

---

Here's a description of the image:
The image shows a webpage with a dark theme, likely related to an online assessment or quiz platform. There are time remaining, score, and action buttons at the top. The user is logged in, and recent saves are displayed, along with questions.
image text:
01:37:59 left Score: 10 / 10 Check all Save
You are logged in as 23f2003807@ds.study.iitm.ac.in.
Logout
Recent saves (most recent is your official score)
Reload from 2/9/2025, 10:20:36 PM. Score: 10
Reload from 2/9/2025, 10:20:18 PM. Score: 10
Reload from 2/9/2025, 9:42:55 PM. Score: 7
Questions
1. Import HTML to Google Sheets (1 mark)
  
Completed GA4 with 10/10.  
I have also use tweak that the some answer and question are check and generate on client side.

---

See there is difference of hyphen . Correct it manually.

---

Just try re-running your code once and paste in the current response. Check if its working or not.

---

Change the slight differences manually accordingly with the expected values

---

I haven’t done MLP and BDM so should I drop TDS now

---

Hi,

I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.

anyone suggest some way how to do pdf to markdown correctly?

---

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

---

yes  
But still doesnt work

---

In q10 i am geeting …missing links- error  
Any idea how to correct this

---

Beyond the specific tools mentioned (like `IMPORTHTML` in Google Sheets or `httpx` and `lxml` in Python), what are the broader *ethical considerations* when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

---

image description: The image is a webpage with text instructions and a field for input. The text is asking to search for a link related to "WebAssembly" in the "Hacker News RSS API" and input the link in the provided field. An error message saying "Incorrect link" is present at the bottom of the input field.
image text:
• Retrieves and returns the link to the most relevant post.
Your Task
Search using the Hacker News RSS API for the latest Hacker News post mentioning WebAssembly and having a minimum of 86 points. What is the link that it points to?
1. Automate Data Retrieval: Utilize the HNRSS API to fetch the latest Hacker News posts. Use the URL relevant to fetching the latest posts, searching for topics and filtering by a minimum number of points.
2. Extract and Present Data: Extract the most recent from this result. Get the tag inside it.
3. Share the result: Type in just the URL in the answer.
What is the link to the latest Hacker News post mentioning WebAssembly having at least 86 points?
https://news.ycombinator.com/item?id=38790552
Error: Incorrect link
  
is everything fine with the answer format?? i am trying this for so long anything i want to change ??

---

What is the error are you facing ?

---

can someone help through this error!!  
Here's a description of the image:
The image shows a dark interface with a text box containing JSON data and an error message. The text box is framed with a red border. The error message suggests a mismatch in expected and actual values for the year.
image text:
What is the JSON data?
{"id":"tt8999762","title":"5. The Brutalist","year":"2024","rating":"8.0"},
{"id":"tt27657135","title":"6. Saturday Night", "year":"2024","rating":"7.0"},
{"id":"tt17526714","title":"7. The Substance","year":"2024","rating":"7.3"},
{"id":"tt10919420","title":"8. Squid Game", "year":"2021-2025","rating":"8.0"},
{"id":"tt21227864","title":"9. Un matrimonio di troppo","year":"2025","rating":"5.5"},
"id":"#26581105" "title":"10 Companion" "year"."2025" "rating"."71"
Error: At [10].year: Values don't match. Expected: "2021-". Actual: "2021-"

---

Check if you have made the query proprly. also, check if you taken the correct link from the item

---

in q10 i am getting error- missing links.  
can i get any explanation about this error so that i can figure out this ?  
[@Saransh\_Saini](/u/saransh_saini) as i left with this question only

---

Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

---

I have done that also but still getting same error

---

The one with blue line must be link here in the pdf.

---

After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

refer to this [@21f3000745](/u/21f3000745)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000804/48/87428_2.png) 22f3000804:

> can someone help through this error!!

if it is saying something has a mismatch, just spot the mismatch one by one and manually change it [@22f3000804](/u/22f3000804)

---

Here for the bonus marks, it was great solving the GA4.

---

After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

---

Thankyou , but now i am getting missing code error. What it means? [@23f2000573](/u/23f2000573)

---

You just have to add a space after a hyphen

---

Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

---

No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise [@Saransh\_Saini](/u/saransh_saini)

---

I am also facing the same error in this question

---

the answer format is correct the link is probably not the latest one, I had the same issue because my code was working only for the first 100 entries… you should try paginating your code so it can cover more entries

---

just change the values as itis coming in the error

---

change the name manually as the name is diiferent on imdb according to the region, I had the same issue…

---

are you able do it now? Reload and check

---

yes facing the same thing

---

you are missing code block

Normal : print(123)  
Code Block : `print(123)`

you can refer to week 2 q1 for the syntax of code block

---

image description: The image shows a dark gray screen with white text. The text is a question asking "What is the JSON data?". Below the question, a large block of JSON data is presented in white text. At the bottom of the screen, an error message in white text reads "TypeError: Cannot read properties of null (reading 'textContent')". The image also has a thin pink border. image text: What is the JSON data? Crow","year":"2024","rating":"4.7"},{"id":"tt1273235","title":"16. A Serbian Film","year":"2010","rating":"4.9"},{"id":"tt27165670","title":"17. Sugar Baby","year":"2024","rating":"4.5"},{"id":"tt11057302","title":"18. Madame Web","year":"2024","rating":"4.0"},{"id":"tt1467304","title":"19. The Human Centipede (First Sequence)","year":"2009","rating":"4.4"},{"id":"tt3605418","title":"20. Knock Knock","year":"2015","rating":"4.9"},{"id":"tt15128544","title":"21. Sunray: Fallen Soldier","year":"2024","rating":"4.3"},{"id":"tt27218960","title":"22. Y2K","year":"2024","rating":"4.8"},{"id":"tt14954666","title":"23. The Idol","year":"2023","rating":"4.4"}, {"id":"tt1333125","title":"24. Movie 43","year":"2013","rating":"4.4"},{"id":"tt0117765","title":"25. Striptease", "year":"1996","rating":"4.6"}] TypeError: Cannot read properties of null (reading 'textContent')
  
anyone have idea about this error?

---

Here's a description of the image:
The image presents a section titled "Impact," detailing the benefits of UrbanRide's data processing capabilities. It lists four key benefits, and includes a question regarding the maximum latitude of Riyadh in Saudi Arabia, along with an input field containing "27.7020999" and an error message.
image text: Impact
By automating the extraction and processing of bounding box data, UrbanRide can:
• Optimize Routing: Enhance route planning algorithms with precise geographical boundaries, reducing delivery times and operational costs.
• Improve Fleet Allocation: Allocate vehicles more effectively across defined service zones based on accurate city extents.
• Enhance Market Analysis: Gain deeper insights into regional performance, enabling targeted marketing and service improvements.
• Scale Operations: Seamlessly integrate new cities into their service network with minimal manual intervention, ensuring consistent data quality.
What is the maximum latitude of the bounding box of the city Riyadh in the country Saudi Arabia on the Nominatim API? Value of the maximum latitude
27.7020999
Error: Incorrect latitude. Check OSM ID ending with 8390
①
  
getting this error

---

Yes thankyou i noticed that code block.  
But now getting missig heading [@Saransh\_Saini](/u/saransh_saini)

---

[@carlton](/u/carlton) sir what about this question.

---

You have to go to the Settings tab, select Actions from the left panel and choose General from the drop-down list. Then scroll down completely and choose “Read and Write Permission” under the Workflow Permission section

---

Getting at root differnt number of properties for below

```

"2025-02-10": "Sunny intervals and a gentle breeze",
"2025-02-11": "Light rain showers and a gentle breeze",
"2025-02-12": "Thundery showers and a gentle breeze",
"2025-02-13": "Thundery showers and a moderate breeze",
"2025-02-14": "Sunny intervals and a gentle breeze",
"2025-02-15": "Drizzle and a gentle breeze",
"2025-02-16": "Sunny and a gentle breeze",
"2025-02-17": "Sunny intervals and a gentle breeze",
"2025-02-18": "Sunny intervals and a gentle breeze"}

```

---

I’m assuming it’s occurring because the text formatting for the JSON is incorrect. Try and put it in the correct format

---

I’ve reloaded a dozen time and even extracted the data again and again to account for any changes but it still doesn’t work.

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

> ```
> {"2025-02-10": "Sunny intervals and a gentle breeze",
> "2025-02-11": "Light rain showers and a gentle breeze",
> "2025-02-12": "Thundery showers and a gentle breeze",
> "2025-02-13": "Thundery showers and a moderate breeze",
> "2025-02-14": "Sunny intervals and a gentle breeze",
> "2025-02-15": "Drizzle and a gentle breeze",
> "2025-02-16": "Sunny and a gentle breeze",
> "2025-02-17": "Sunny intervals and a gentle breeze",
> "2025-02-18": "Sunny intervals and a gentle breeze"}
>
> ```

{“2025-02-09”: “Partly cloudy and light winds”,  
“2025-02-10”: “Sunny intervals and a gentle breeze”,  
“2025-02-11”: “Light rain showers and a gentle breeze”,  
“2025-02-12”: “Thundery showers and a gentle breeze”,  
“2025-02-13”: “Thundery showers and a moderate breeze”,  
“2025-02-14”: “Sunny intervals and a gentle breeze”,  
“2025-02-15”: “Drizzle and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny intervals and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”}

---

There needs to be two weeks worth of data so if it’s starting from the 9th it should be till the 22nd

---

make the edits clearly in the repository and then open it, the url that is then showed. Just copy and paste it into the box, it will work

---

what problem is their in ques 2 and 3

---

yeah same for me. seems we were unlucky ![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=12 ":frowning:")

---

What can I refer to for proper steps to solve Question 10?  
Thanks!

---

Q10 is giving errors even after doing everything

---

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23ds3000241/48/119137_2.png) 23ds3000241:

> o if it’s

getting values dont match for below now  
{“2025-02-09”: “Partly cloudy and light winds”,  
“2025-02-10”: “Sunny intervals and a gentle breeze”,  
“2025-02-11”: “Light rain showers and a gentle breeze”,  
“2025-02-12”: “Thundery showers and a gentle breeze”,  
“2025-02-13”: “Thundery showers and a moderate breeze”,  
“2025-02-14”: “Sunny intervals and a gentle breeze”,  
“2025-02-15”: “Drizzle and a gentle breeze”,  
“2025-02-16”: “Sunny and a gentle breeze”,  
“2025-02-17”: “Sunny intervals and a gentle breeze”,  
“2025-02-18”: “Sunny intervals and a gentle breeze”,  
“2025-02-19”: “Light cloud and a gentle breeze”,  
“2025-02-20”: “Sunny intervals and a moderate breeze”,  
“2025-02-21”: “Light rain showers and a moderate breeze”,  
“2025-02-22”: “Light cloud and a moderate breeze”}

---

thanks for the help…

---

[@23f3002537](/u/23f3002537), [@21f3000745](/u/21f3000745), [@Jeleshiya](/u/jeleshiya)

Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark.

Kind regards

---

sir what about bonus marks cuz my score was 9/10 due to q4(Nur-sultan).

---

The bonus mark will be processed afterwards. That is checked before the scores are pushed to portal.

---

Nominatim API gives me the bounding box of the location. How exactly the bounding box helps me to find the details of the location?

---

I am facing issues in Q9 , can you help me out?

---

const movies = ;

document.querySelectorAll(‘.sc-d5ea4b9d-0.ejavrk’).forEach((item, index) => {  
if (index >= 25) return; // Stop after collecting 25 movies

```
const titleElement = item.querySelector('.ipc-title__text');
const yearElement = item.querySelector('.sc-d5ea4b9d-7.URyjV.dli-title-metadata-item');
const ratingElement = item.querySelector('.ipc-rating-star--rating');

if (titleElement && yearElement) {
    const idMatch = item.querySelector('a[href*="/title/tt"]')?.href.match(/tt(\d+)/);
    const id = idMatch ? `tt${idMatch[1]}` : null;
    const title = titleElement.innerText.trim();
    //const yearText = yearElement.innerText.replace(/\D/g, "").trim(); // Remove non-numeric characters
    const yearText = yearElement.innerText.trim();
    const year = yearText ? yearText : null; // Keep year as a string
    const rating = ratingElement ? ratingElement.innerText.trim() : null; // Keep rating as a string

if (id && title && year && rating && parseFloat(rating) >= 3 && parseFloat(rating) <= 5) {
        movies.push({ id, title, year, rating });
    }
}

```

});

// Output JSON data with no spaces after colon  
console.log(JSON.stringify(movies, (key, value) => typeof value === ‘string’ ? value.trim() : value, 0));

---

Here's a description of the image:
The image is a screenshot of a webpage, likely a learning platform. It displays information about a graded assignment, the user's login details, and recent saves.
image text:
Ended at Sun, 9 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
Bonus marks for posting on Discourse
To encourage discussions, IITM BS students who reply to the discussion on GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]\_with a relevant
question or reply will get 1 bonus mark on this graded assignment.
You are logged in as 23f3000975@ds.study.iitm.ac.in.
Logout
Recent saves (most recent is your official score)
Reload from 9/2/2025, 8:04:05 pm. Score: 8
Reload from 9/2/2025, 8:03:25 pm. Score: 8
Reload from 9/2/2025, 4:03:58 pm. Score: 4
  
sir i have completed and saved the test but it shows score 0. and also  
image description: The image is a screenshot of a webpage related to an online course or assignment. It has a left sidebar with navigation options and a main content area with details about a graded assignment. The main content area has text related to the assignment.
image text:
Development Tools
Graded Assignment 3
<
Module 2:
Deployment Tools
• Module 3: Large
Language Models
Project 1
Module 4: Data
Sourcing
Graded Assignment 4
Assignment
Module 5: Data
Preparation
The due date for submitting this assignment has passed.
Due on 2025-02-05, 23:59 IST.
You may submit any number of times before the due date. The final submission will be considered for grading.
If you have any difficulty accessing the Graded Assignment, please check the following causes:
Ad blockers need to be disabled/removed.
The site requires cookies for authentication. So any cookie blocking/tracker blocking extensions or software may prevent access.
Javascript is required for the site to work correctly.
Chrome Browser is the recommended software to access the contents.
Disable any browser extensions that may be interfere with the site from working correctly.
Overly aggressive anti-virus software may also cause similar access problems.
You MUST use your Student Id (eg. 22f3xxxxxx@ds.study.iitm.ac.in) to do the Graded Assignment, otherwise your score will not be considered
for evaluation.
Graded Assignment 3 is available at this link: https://exam.sanand.workers.dev/tds-2025-01-ga3. Please attempt it.
  
the graded assignment is showing like i didn’t submit it. please check on this.

---

Your most recent score will be considered, as long as you saved it before the deadline

---

Here are the Discourse IDs that replied to this post. [@carlton](/u/carlton) could you please add 1 mark to them in the GA (not the overall score)?

* Please include only those are enrolled this term, obviously.
* If they didn’t attempt GA4, please include them anyway and give them 1/10.
* If they got 10/10 already, please add 1 mark anyway and give them 11/10.

```
21F1005510
21f2000296
21f2000588
21f2000709
21f2001369
21f3000745
21f3001379
21f3001797
21f3001993
21f3002277
22ds2000011
22ds3000157
22f1000120
22f1000535
22f2000008
22f2000113
22f2001590
22f2001640
22f3000079
22f3000519
22f3000586
22f3000639
22f3000657
22f3000804
22f3000910
22f3001011
22f3001315
22f3001754
22f3001840
22f3002034
22f3002175
22f3002184
22f3002723
22f3002771
23ds3000040
23ds3000149
23ds3000241
23f1000299
23f1000422
23f1000625
23f1001126
23f1001174
23f1001231
23f1001301
23f1001839
23f1002534
23f1002571
23f1003139
23f2000098
23f2000237
23f2000573
23f2000926
23f2001177
23f2001286
23f2001305
23f2001413
23f2001738
23f2002291
23f2003268
23f2003717
23f2003751
23f2003853
23f2004042
23f2004636
23f2004644
23f2004752
23f2004907
23f2004941
23f2005138
23f2005275
23f2005419
23f3001208
23f3001601
23f3001752
23f3002537
23F300327
23f3003594
23f3003871
23f3004024
23f3004114
23f3004162
24ds1000082_Vivek
24ds2000024
24ds2000108
24ds3000032
24ds3000090
24f2000695
24f2003130
Abhay222
ABHIJITH_VS
adeepu.here
Adityism
akashkunwar
anu2023
AnvithaV
AryanTikam
Atif01
carlton
daksh76
Deepanshutomar
GIRISH_VISHVESHVAR_B
gouthamnischay
H1Dd3n_xx
Haricharan
HARISH.S
iamsarthak
jashmevada
Jayeshbansal
Jeleshiya
JoelJeffrey
koustubhr
lakshaygarg654
Lokkiii
Megha
mohiit
Namannn28
namanshyamsukha
nayonika
Neelakandan
Nelson
nilaychugh
parthpatel
rabbaniIITB
Rehbar
Rohitb
rohitgarg
roy2003
Rrishit
Sagan
sandeepstele
Saransh_Saini
sarvan108
sha_512_av
ShahbaazSingh
sharma_abhay
ShivaniAdhiyaman
shivanshgupta0007
Siddhu3050
Suhani
swatikap
tanmaysahu295
tarundude02
Udipth
vaishnavi.k
Vedant22
vidushi
vidya19
yasharabhavi

```

---

Hello sir, my name is mentioned here however I did not get the bonus mark.

Warm regards,  
Nayonika Arora  
24ds1000090

---

ig, they have not updated.

not reflected on my portal too

---

Here's a brief description of the image:
The image is a discussion thread on a platform, likely a forum or online learning environment. The thread is titled "GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]". The user "A" has posted a question regarding an error occurring when running code related to a specific city. The user provides details of the error.
image text: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]
Courses
Tools in Data Science announcement term1-2025 graded-assignment week-4
Topics •
• My Posts
@Docs
: More
CATEGORIES
Courses
Operational Issues
Professionals Corner
All categories
TAGS
clarification
J
A
22f2000008
Reply
Jan 31
I am getting this error again and again after running the code in collab this city Nur-Sultan?
Error: Could not find location ID for Nur-Sultan
NameError
Traceback (most recent call last)
<ipython-input-9-128760ee996a> in <cell line: 0>()
33
34 # BBC Weather URL
---> 35 weather\_url = f'https://www.bbc.com/weather/{location id}'
36
37 # Fetch weather data
NameError: name 'location\_id' is not defined
EN English (India)
El Replyiav
10d
Reply
A
168/360
Feb 8
14m
  
As you can see in this screen shot i already tried this question and getting error so i posted it on discourse. But still i did not get any marks for attempting this question.  
i got only 9/10.

---

Hello [@s.anand](/u/s.anand) [@carlton](/u/carlton) Sir,  
As can be seen, my roll number is present in this list (21f2000588) and in GA4 I have got 10/10 but unfortunately, that bonus mark hasn’t been added (as can be seen from the score displayed on the dashboard). So I request you to add that bonus mark to the total kindly.

Hoping for a positive response.  
Thanks & Regards  
Digvijaysinh Chudasama  
21f2000588

---

[@22f2000008](/u/22f2000008) Your roll number is in the list shared by professor Anand.

---

---

image description: The image shows a dark mode discussion forum. There's a sidebar on the left for navigation and a discussion thread in the center. Key elements include user posts, replies, and a mention of 'Nur-Sultan parameter'.
image text: GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025] Courses Tools in Data Science announcement term1-2025 graded-assignment week-4 carlton rohitgarg ig, they have not updated. not reflected on my portal too 3h Jan 31 Topics • My Posts Docs More CATEGORIES Courses Operational Issues Professionals Corner All categories TAGS clarification carlton Course TA @23f3002537, @21f3000745, @Jeleshiya Anyone who received the Nur-Sultan parameter for this question and at least attempted it will get a mark. Kind regards 1 1 Reply ↑ Jump to post 360/364 Feb 18 1h 22f2000008 carlton 3h
  
I am not saying anything regarding bonus marks. I am asking GA4 q4 about  
Nur-Sultan in this question everyone getting error after post in discourse ,sir say who attempt this question get a marks .But i am not recieved this question marks

---

if a student has 10/10 and his name is in the bonus list, how would that look like in the dashboard?

I don’t think it is added in my case.

---

It will show up as 110 marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.

Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.

23f3002537@ds.study.iitm.ac.in  
23f3003875@ds.study.iitm.ac.in  
21f3002112@ds.study.iitm.ac.in  
23f2003437@ds.study.iitm.ac.in  
22f3002236@ds.study.iitm.ac.in  
22f3001705@ds.study.iitm.ac.in  
22f2000008@ds.study.iitm.ac.in  
21f1001892@ds.study.iitm.ac.in  
23f1002075@ds.study.iitm.ac.in  
23f1001126@ds.study.iitm.ac.in  
22f3002661@ds.study.iitm.ac.in  
22f2000506@ds.study.iitm.ac.in  
24f1002149@ds.study.iitm.ac.in  
23f2002473@ds.study.iitm.ac.in

Kind regards

---

Please refer to this reply.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/389) [Tools in Data Science](/c/courses/tds-kb/34)

> It will show up as 110 marks. Bonus marks are for all discourse posts on this thread that Anand has identified as valid. I have provided operations team with the update corrected scores. You will start seeing them in the dashboard soon.
> Also these are the list of students that have been affected by Nur-Sultan in their questions. These will get an automatic mark for that question if they attempted it. Note that this is not a bonus mark. This is a free mark.
> 23f3002537@ds.study.iitm.ac.in
> 23f3…

Kind regards

---

For those who didn’t submit but still need to practice the questions like to check if the answer is right, or cross-check the solutions for GA 4 and GA 5, is there a special link where the portal just checks the answer and says right or wrong. I wasn’t able to do GA4 or even try to attempt GA 5 before deadline, but i would like to go through the process of submitting etc. is there any link or solutions for GA 4 and GA5.

---

is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I understand that each set of students get different questions. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

