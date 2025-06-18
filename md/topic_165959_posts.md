# ga4-data-sourcing-discussion-thread-tds-jan-2025

**post_id:** 588325  
**author:** s.anand  
**timestamp:** 2025-01-31T16:13:36.640Z

# ga4-data-sourcing-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 4 - Data Sourcing](https://exam.sanand.workers.dev/tds-2025-01-ga4).

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: Sunday, February 9, 2025 6:29 PM

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

**post_id:** 588326  
**author:** s.anand  
**timestamp:** 2025-01-31T16:14:00.363Z

---

**post_id:** 588589  
**author:** 22f3001315  
**timestamp:** 2025-02-01T07:54:31.100Z

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

**post_id:** 588867  
**author:** 24ds2000024  
**timestamp:** 2025-02-01T18:26:06.664Z

I have the Same doubt.

---

**post_id:** 589057  
**author:** s.anand  
**timestamp:** 2025-02-02T05:30:16.417Z

[@22f3001315](/u/22f3001315) [@21f3002277](/u/21f3002277) [@24ds2000024](/u/24ds2000024) – please try again after reloading the page. The new error message will be clearer, like this:

```
Error: At [0].rating: Values don't match. Expected: "7.4". Actual: 7.4

```

FYI, we expect all values as strings, not numbers. That’s because the year can sometimes be a range for a TV series (e.g. 2021 - 2024) and the rating can sometimes be missing.

---

**post_id:** 589067  
**author:** 23f2000237  
**timestamp:** 2025-02-02T05:41:42.494Z

In Question 2, it is specifically said to filter the movies however, the evaluator is expecting a TV show there. Should we also include TV shows now?

edit: This is an everchanging dataset, so will our answers be saved, as, this json might not be in this order tomorrow?

---

**post_id:** 589072  
**author:** s.anand  
**timestamp:** 2025-02-02T05:45:48.804Z

[@23f2000237](/u/23f2000237) A good point. Yes, please include *all* titles. I’ve reworded the question accordingly. Thanks.

---

**post_id:** 589120  
**author:** 21f3002277  
**timestamp:** 2025-02-02T06:31:48.149Z

Q3. How to handle the error ? [@Jivraj](/u/jivraj)

TypeError: Cannot read properties of null (reading ‘0’)

```
http://127.0.0.1:8000/api/outline?country=Russia

{"outline":"## Contents\n# Russia\n## Etymology\n## History\n### Early history\n### Kievan Rus'\n### Grand Duchy of Moscow\n### Tsardom of Russia\n### Imperial Russia\n#### Great power and development of society, sciences, and arts\n#### Great liberal reforms and capitalism\n#### Constitutional monarchy and World War\n### Revolution and civil war\n### Soviet Union\n#### Command economy and Soviet society\n#### Stalinism and modernisation\n#### World War II and United Nations\n#### Superpower and Cold War\n#### Khrushchev Thaw reforms and economic development\n#### Period of developed socialism or Era of Stagnation\n#### Perestroika, democratisation and Russian sovereignty\n### Independent Russian Federation\n#### Transition to a market economy and political crises\n#### Modern liberal constitution, international cooperation and economic stabilisation\n#### Movement towards a modernised economy, political centralisation and democratic backsliding\n#### Invasion of Ukraine\n## Geography\n### Climate\n### Biodiversity\n## Government and politics\n### Political divisions\n### Foreign relations\n### Military\n### Human rights\n### Corruption\n### Law and crime\n## Economy\n### Transport and energy\n### Agriculture and fishery\n### Science and technology\n#### Space exploration\n### Tourism\n## Demographics\n### Language\n### Religion\n### Education\n### Health\n## Culture\n### Holidays\n### Art and architecture\n### Music\n### Literature and philosophy\n### Cuisine\n### Mass media and cinema\n### Sports\n## See also\n## Notes\n## References\n## Sources\n## Further reading\n## External links"}

```

error resolved

---

**post_id:** 589293  
**author:** 22f3001315  
**timestamp:** 2025-02-02T10:06:04.746Z

in my output which is correct  
there are two \n instead of one .

---

**post_id:** 589307  
**author:** 21f3002277  
**timestamp:** 2025-02-02T10:38:33.945Z

it should one(for newline), my code is working now

---

**post_id:** 589366  
**author:** 24ds2000024  
**timestamp:** 2025-02-02T11:54:35.123Z

Dear Sir,  
I was at 2/10 yesterday. After pasting JSON file of IMDB & reloading as suggested My marks updated to 3/10. Kindly confirm if I have got whole of IMDB question.

---

**post_id:** 589408  
**author:** 21f3002277  
**timestamp:** 2025-02-02T13:00:36.181Z

Q4. How to handle the error ? [@Jivraj](/u/jivraj)

Error: At 2025-02-05: Values don’t match

---

**post_id:** 590055  
**author:** 23f2003853  
**timestamp:** 2025-02-03T00:37:01.721Z

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

**post_id:** 590227  
**author:** 23f2000237  
**timestamp:** 2025-02-03T10:06:13.753Z

I have a doubt regarding the bonus mark. Suppose someone were to get 10/10 in the assignment, would their mark be recored as 11/10 or just 10?  
(Assuming they have interacted in this thread)

---

**post_id:** 590239  
**author:** s.anand  
**timestamp:** 2025-02-03T11:16:46.279Z

Anyone scoring 10/10 on GA4 and replying with a *relevant* message on this thread will get 11/10 ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

**post_id:** 590243  
**author:** 23f2003853  
**timestamp:** 2025-02-03T11:38:10.970Z

For me I just made filter of rating between 2 and 7 in site and typed in console as per video. with that data got in console worked fine.  
copy the coding and save in place use it for data extract when finally submit

---

**post_id:** 590374  
**author:** 22f2000113  
**timestamp:** 2025-02-03T16:46:46.395Z

For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name  
Here's a description of the image:
The image shows a search result page. On the left, there are search filters with "Title name" and a search bar filled with the text "Un matrimonio di troppo". The right side displays a graphic of a magnifying glass with an "X" through it, indicating "No results found". Below the graphic are the text "No results found" and "Please adjust your filters or start a new search".
image text: Search filters Expand all Title name Un matrimonio di troppo Title type X No results found Please adjust your filters or start a new search

---

**post_id:** 590429  
**author:** nilaychugh  
**timestamp:** 2025-02-04T03:28:57.489Z

how to get the BBC weather API key?

---

**post_id:** 590455  
**author:** JoelJeffrey  
**timestamp:** 2025-02-04T05:47:12.930Z

Just a quick query on the Bonus mark.

Would this be added to the final grade? Say for example, Someone get a full score in the first 4 assignments. So the total comes up to 39.5/39.5, and would be converted to 0.15 or 15 marks. Would the bonus mark be additional to that 15 or would the score change to 40.5/39.5 and then get normalised to 15?

---

**post_id:** 590467  
**author:** s.anand  
**timestamp:** 2025-02-04T06:15:20.501Z

[@JoelJeffrey](/u/joeljeffrey) It will be added to the GA4 marks, not the final grade. So, it’s roughly worth 0.15% on the total - not a full 1% on the total.

---

**post_id:** 590495  
**author:** 23f2003751  
**timestamp:** 2025-02-04T07:43:14.240Z

you can go and login using your email id in this below mentioned link

<https://home.openweathermap.org/api_keys>

---

**post_id:** 590508  
**author:** JoelJeffrey  
**timestamp:** 2025-02-04T08:14:26.582Z

Error: At [10].year: Values don’t match. Expected: "2025– ". Actual: “2025–”

Can someone help me with this?  
Thanks

Edit: Resolved

---

**post_id:** 590528  
**author:** 23f2003853  
**timestamp:** 2025-02-04T09:44:51.731Z

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

**post_id:** 590642  
**author:** 23f2000237  
**timestamp:** 2025-02-04T14:53:18.679Z

Have a step with your email id as its name. (Instead of checkout repository)  
Also make sure you give read and write permission so it commits without any error

---

**post_id:** 590658  
**author:** daksh76  
**timestamp:** 2025-02-04T16:03:52.872Z

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

**post_id:** 590665  
**author:** 22f2000113  
**timestamp:** 2025-02-04T16:15:39.892Z

dont remove the space after year- for example “year”: "2023- "

---

**post_id:** 590696  
**author:** 23f2004752  
**timestamp:** 2025-02-04T22:17:37.626Z

Please anyone help me in doing q1 , my doubt is when i open the website [Advanced search](http://www.imdb.com/search/title) , i have click on movies and then do the coding part if not how to select titles of the movies as there is no movies on the page.

---

**post_id:** 590699  
**author:** 23f2004752  
**timestamp:** 2025-02-04T23:37:55.943Z

In q4 i got this error someone pls expalin “Error: At root: Property name mismatch”

---

**post_id:** 590732  
**author:** 23f2003751  
**timestamp:** 2025-02-05T06:21:04.530Z

```
Student marks - Group 100

| Maths | Physics | English | Economics | Biology |
|

---

**post_id:** 590733  
**author:** JoelJeffrey  
**timestamp:** 2025-02-05T06:25:36.507Z

-- |

---

**post_id:** 590735  
**author:** 23f2000237  
**timestamp:** 2025-02-05T06:40:23.675Z

---

**post_id:** 590739  
**author:** 23f2003751  
**timestamp:** 2025-02-05T07:00:03.570Z

- |

---

**post_id:** 590742  
**author:** Namannn28  
**timestamp:** 2025-02-05T07:10:34.357Z

---

**post_id:** 590747  
**author:** 23f2003751  
**timestamp:** 2025-02-05T07:21:08.047Z

- |

---

**post_id:** 590764  
**author:** 22f3001315  
**timestamp:** 2025-02-05T08:32:35.339Z

---

**post_id:** 590779  
**author:** 23f2003853  
**timestamp:** 2025-02-05T09:55:21.354Z

---

**post_id:** 590781  
**author:** 23f2003853  
**timestamp:** 2025-02-05T10:00:47.264Z

|

---

**post_id:** 590782  
**author:** 23f2003853  
**timestamp:** 2025-02-05T10:03:31.480Z

---

**post_id:** 590798  
**author:** 23f2003751  
**timestamp:** 2025-02-05T11:03:45.090Z

- |
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

**post_id:** 590870  
**author:** 23f2004752  
**timestamp:** 2025-02-05T14:04:46.408Z

For Q10, I am extracting the text first using PyMuPDF (fitz) and then using markdownify to convert it to markdown and finally prettier. However despite trying changing it from PyMuPDF to other text extraction libraries, I end up getting

> Incorrect. Try Again

errors

---

**post_id:** 590937  
**author:** gouthamnischay  
**timestamp:** 2025-02-05T17:37:33.037Z

I think you have used the wrong document, because, this is the marks list for Q9

---

**post_id:** 591019  
**author:** roy2003  
**timestamp:** 2025-02-06T03:41:58.369Z

which tool you are using ?

---

**post_id:** 591027  
**author:** 23f2003853  
**timestamp:** 2025-02-06T04:24:58.055Z

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

**post_id:** 591032  
**author:** 21f3002277  
**timestamp:** 2025-02-06T04:57:11.068Z

in the bbc question what should be starting and the ending date

---

**post_id:** 591035  
**author:** 23f2003853  
**timestamp:** 2025-02-06T05:10:27.978Z

you dont need the key you need that file used in 2 lecture videos just look for it.  
![:+1:](https://emoji.discourse-cdn.com/google/+1.png?v=12 ":+1:")

---

**post_id:** 591037  
**author:** carlton  
**timestamp:** 2025-02-06T05:14:57.186Z

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

**post_id:** 591042  
**author:** 21f3002277  
**timestamp:** 2025-02-06T05:26:10.352Z

Still the issue is there. Have posted screen shot.

---

**post_id:** 591052  
**author:** 23f2004752  
**timestamp:** 2025-02-06T05:42:11.105Z

what Mr. Sakthivel S said is correct. could you tell me what tool did you use to convert .md file. I have done as per links in question and used chatgpt also. but nothing is correct

---

**post_id:** 591057  
**author:** 21f3002277  
**timestamp:** 2025-02-06T05:50:34.894Z

Please give the solution if you got any…have you been able to solve the bbc weather question?

---

**post_id:** 591084  
**author:** 23f2003751  
**timestamp:** 2025-02-04T09:14:53.054Z

[@s.anand](/u/s.anand) [@carlton](/u/carlton)  
In question 8 i got error  
“Enter your repository URL (format: <https://github.com/USER/REPO>):  
<https://github.com/Ansh205/github-actions>  
Error: No workflow runs found”  
But i have successfully commited  
image description: The image showcases a workflow interface displaying the status of several automated processes. The interface is dark-themed, and the main content includes a list of workflow runs. The top area contains a search bar and filters to refine the view. The workflow runs are listed with their names, status (indicated by check marks or red crosses), branch, and recent activity timestamps.
image text: All workflows, Showing runs from all workflows, 4 workflow runs, Daily Commit Workflow, Daily Commit Workflow #4: Manually run by Ansh205, main, 5 minutes ago, 19s, Daily Commit Workflow, Daily Commit Workflow #3: Manually run by Ansh205, main, 37 minutes ago, 14s, Daily Commit Workflow, Daily Commit Workflow #2: Manually run by Ansh205, main, 54 minutes ago, 11s, Daily Commit Workflow, Daily Commit Workflow #1: Manually run by Ansh205, main, 1 hour ago, 14s, Q Filter workflow runs, Event, Status, Branch, Actor

---

**post_id:** 591083  
**author:** carlton  
**timestamp:** 2025-02-06T06:09:22.483Z

Just follow the links and notebooks given in the references.

---

**post_id:** 591089  
**author:** 23f2004752  
**timestamp:** 2025-02-06T06:15:48.956Z

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

**post_id:** 591092  
**author:** 21f2000588  
**timestamp:** 2025-02-06T06:19:39.985Z

---

**post_id:** 591093  
**author:** 23f2003853  
**timestamp:** 2025-02-06T06:21:39.845Z

---

**post_id:** 591098  
**author:** 23f2003853  
**timestamp:** 2025-02-06T06:23:50.056Z

---

**post_id:** 591102  
**author:** 22f2001640  
**timestamp:** 2025-02-06T06:29:16.352Z

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

**post_id:** 591103  
**author:** 21f2000588  
**timestamp:** 2025-02-06T06:30:07.514Z

what’s your directory structure, is it (.github/workflows/<filename.yaml>) and public

---

**post_id:** 591108  
**author:** 22f2001640  
**timestamp:** 2025-02-06T06:37:52.150Z

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

**post_id:** 591109  
**author:** 23f2004752  
**timestamp:** 2025-02-06T06:38:34.157Z

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

**post_id:** 591114  
**author:** 21f3002277  
**timestamp:** 2025-02-06T06:45:41.518Z

try with this

* name: Set up Git user (23f2003853@ds.study.iitm.ac.in)  
  run: |  
  git config --global user.name “GitHub Actions Bot”  
  git config --global user.email “23f2003853@ds.study.iitm.ac.in”

---

**post_id:** 591127  
**author:** JoelJeffrey  
**timestamp:** 2025-02-06T07:04:00.243Z

Thank you for your help , my repo was not public before and can you also help me in g4 i got this “Error: At root: Property name mismatch”

---

**post_id:** 591132  
**author:** 21f2000588  
**timestamp:** 2025-02-06T07:19:29.059Z

In g4 which Question have that error you are getting

---

**post_id:** 591138  
**author:** 21f3002277  
**timestamp:** 2025-02-06T07:42:32.535Z

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

**post_id:** 591145  
**author:** 23f2003853  
**timestamp:** 2025-02-06T08:10:06.762Z

Hi Tushar,

If you looked at the PDF you might have realised that students have been grouped. The question gives you a range for the groups 43-66. Including both groups implies both group 43 and 66 are included in your calculation.

kind regards

---

**post_id:** 591152  
**author:** 22f2001640  
**timestamp:** 2025-02-06T08:30:20.527Z

Question 4 "  
Sample output

{  
“25-02-04”: “Sunny intervals and light winds”,  
“25-02-05”: “Light rain and light winds”,

}  
Error: At root: Property name mismatch"

---

**post_id:** 591173  
**author:** 22f3001315  
**timestamp:** 2025-02-06T09:39:54.578Z

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

**post_id:** 591190  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:29:37.045Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png) 21f3002277:

> Set up Git user (23f2003853@ds.study.iitm.ac.in)

Still the same error appears

---

**post_id:** 591191  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:33:21.057Z

Thanks for providing clarification Sir

---

**post_id:** 591192  
**author:** 23f2003853  
**timestamp:** 2025-02-06T10:33:30.127Z

I am also facing same issue can’t resolve.

---

**post_id:** 591193  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:33:48.592Z

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

**post_id:** 591194  
**author:** 23f2003853  
**timestamp:** 2025-02-06T10:36:03.777Z

Issue resolved for me after following below step  
After creating the workflow:

* Trigger the workflow and wait for it to complete
* Ensure it appears as the **most recent action** in your repository
* Verify that it creates a commit during or within 5 minutes of the workflow run

---

**post_id:** 591195  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:36:09.371Z

In place of “name: Setup up GIT config” change to “name: add commit {your\_email}”

---

**post_id:** 591196  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:36:50.718Z

use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format.

[@23f2004752](/u/23f2004752)

---

**post_id:** 591197  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:42:30.147Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) could you please help me with this?

---

**post_id:** 591199  
**author:** 23f2003853  
**timestamp:** 2025-02-06T10:44:58.593Z

On running this colab with city = Mumbai,

I’m gettingh this error: Error: At root: Property name mismatch

---

**post_id:** 591200  
**author:** 21f2000588  
**timestamp:** 2025-02-06T10:47:32.686Z

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

**post_id:** 591204  
**author:** 23f2003853  
**timestamp:** 2025-02-06T10:56:41.910Z

can tell me in your .yml which are all place did you use your iitm email id. Because I got the error No executed job step matches 23f2003853@ds.study.ittm.ac.in. My commit was completed in 11 seconds

---

**post_id:** 591209  
**author:** 23f2004752  
**timestamp:** 2025-02-06T11:26:21.596Z

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

**post_id:** 591212  
**author:** 21f2000588  
**timestamp:** 2025-02-06T11:27:18.714Z

Incorrect. Try again.
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. Reformatting with Prettier helps standardize the output format for comparison.

---

**post_id:** 591251  
**author:** 24ds3000090  
**timestamp:** 2025-02-06T13:39:36.309Z

Same problem please help me too if you get it right.

---

**post_id:** 590704  
**author:** 23f2004752  
**timestamp:** 2025-02-05T03:03:39.499Z

Yes followed all these steps, and still the error is being seen,

Error: No executed job step matches 21f2000588@ds.study.iitm.ac.in

---

**post_id:** 591265  
**author:** carlton  
**timestamp:** 2025-02-06T14:01:32.303Z

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

**post_id:** 591266  
**author:** carlton  
**timestamp:** 2025-02-06T14:02:42.475Z

Now re-check you answer. May it will give link where the issue exists. if it gives url browsers the link and address.

---

**post_id:** 591276  
**author:** daksh76  
**timestamp:** 2025-02-06T15:06:08.271Z

Yes true same happened with me.

---

**post_id:** 591280  
**author:** carlton  
**timestamp:** 2025-02-06T15:13:07.942Z

re-check your answer again it may give an url. check the url

---

**post_id:** 591290  
**author:** gouthamnischay  
**timestamp:** 2025-02-06T16:42:32.860Z

Now on rechecking, the error message has changed to – “TypeError: Failed to fetch”

---

**post_id:** 591301  
**author:** 23f2004752  
**timestamp:** 2025-02-06T17:52:55.640Z

No its giving such error:  
image description: The image is a dark gray screenshot of a webpage. The webpage is prompting the user to enter their repository URL in a specific format. The entered URL is highlighted with an error message indicating a failure to fetch data. The check button is present at the bottom.
image text: Enter your repository URL (format: https://github.com/USER/REPO):
https://github.com/DigvijaysinhChudasamalITM/TDS\_GA\_4
TypeError: Failed to fetch
Check

---

**post_id:** 591322  
**author:** 23ds3000149  
**timestamp:** 2025-02-06T19:53:06.705Z

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

**post_id:** 591331  
**author:** Nelson  
**timestamp:** 2025-02-06T20:56:51.582Z

Check you Github account and browse Action for your repo. then check All Work flows. Ensure the first item is schedule triggered confirmation

---

**post_id:** 591418  
**author:** 23F300327  
**timestamp:** 2025-02-02T08:21:23.154Z

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

**post_id:** 591417  
**author:** carlton  
**timestamp:** 2025-02-07T03:25:45.448Z

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

**post_id:** 591469  
**author:** ShahbaazSingh  
**timestamp:** 2025-02-07T05:47:13.914Z

use name:email inside yml page

---

**post_id:** 591471  
**author:** 21f2000588  
**timestamp:** 2025-02-07T05:48:27.982Z

Yep done, thank you! ![:smiley:](https://emoji.discourse-cdn.com/google/smiley.png?v=12 ":smiley:")

---

**post_id:** 591472  
**author:** ShahbaazSingh  
**timestamp:** 2025-02-07T05:49:56.327Z

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

**post_id:** 591473  
**author:** 21f2000588  
**timestamp:** 2025-02-07T05:50:27.393Z

hey, can you help me in doing this i can’t able to do this.

---

**post_id:** 591475  
**author:** ShahbaazSingh  
**timestamp:** 2025-02-07T05:52:26.841Z

[@24ds3000090](/u/24ds3000090)

We will be changing this question. Even we found it hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards

---

**post_id:** 591476  
**author:** 21f2000588  
**timestamp:** 2025-02-07T05:54:22.421Z

[@JoelJeffrey](/u/joeljeffrey)

We will be changing this question. Even we found it pretty hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards

---

**post_id:** 591487  
**author:** s.anand  
**timestamp:** 2025-02-07T06:01:13.973Z

sir in the weather question could you provide from where do we get the bbc api because i have searched a lot and havent been able to find it

---

**post_id:** 591503  
**author:** 21f2000588  
**timestamp:** 2025-02-07T06:44:45.158Z

<https://tds.s-anand.net/#/bbc-weather-api-with-python>

---

**post_id:** 591517  
**author:** 23f2003751  
**timestamp:** 2025-02-07T07:33:28.651Z

try manually inspecting the output of the api and compare it with your script output.  
Or else try refreshing the browser and check.

---

**post_id:** 591544  
**author:** 23f2003853  
**timestamp:** 2025-02-07T08:36:08.903Z

[@carlton](/u/carlton)  
Previously i got correct on q2 but now i am getting the error when i refresh the page “TypeError: Cannot read properties of null (reading ‘textContent’)”

---

**post_id:** 591545  
**author:** 23f2003853  
**timestamp:** 2025-02-07T08:39:47.886Z

Please try city=“Mumbai” as a string literal.

---

**post_id:** 591549  
**author:** Nelson  
**timestamp:** 2025-02-07T08:52:02.503Z

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

**post_id:** 591551  
**author:** Nelson  
**timestamp:** 2025-02-07T08:55:44.029Z

## thema coruscus

* cupiditate celebrer
* argentum alius voro soluta
* sto decor capto suffoco acs tempus deludo deleo ventus odio

Sordeo tergo beatae coniecto ambitus carus. Vae tamdiu debilito verto confugo  
territo acies vos patria. Versus surgo degero vester tersus paulatim chirographum

| abeo | super | valetudo adhuc |
|

---

**post_id:** 591572  
**author:** 21f2000588  
**timestamp:** 2025-02-07T09:31:43.739Z

|

---

**post_id:** 591573  
**author:** 23f2003853  
**timestamp:** 2025-02-07T09:33:27.992Z

|

---

**post_id:** 591580  
**author:** Nelson  
**timestamp:** 2025-02-07T10:04:21.710Z

|
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

**post_id:** 591584  
**author:** 22f2001590  
**timestamp:** 2025-02-07T10:15:38.429Z

Hi Mishkat

Please refer to this post.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/carlton/48/56317_2.png)
[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/91) [Tools in Data Science](/c/courses/tds-kb/34)

> [@JoelJeffrey](/u/joeljeffrey)
> We will be changing this question. Even we found it pretty hard ![sweat_smile](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 "sweat_smile")
> Kind regards

Kind regards

---

**post_id:** 591585  
**author:** Nelson  
**timestamp:** 2025-02-07T10:16:40.485Z

[@s.anand](/u/s.anand) Sir the question 10 of the Graded Assignment 4 is very tough I have tried everything from custom python codes using different libraries to online converted and also formatted using prettier. Please sir guide me how to do the question.

---

**post_id:** 591596  
**author:** swatikap  
**timestamp:** 2025-02-07T10:30:52.807Z

Yep figured that, and after matching the data solved the error and got that question correct.  
Though thank you.

---

**post_id:** 591636  
**author:** Siddhu3050  
**timestamp:** 2025-02-07T11:06:49.504Z

[@s.anand](/u/s.anand) Sir I have done the question 2 of the graded assignment but I am very curious to know why the answers language gets periodically change. Is there some kind of backend code which is responsible for that or is something else ?

---

**post_id:** 591802  
**author:** carlton  
**timestamp:** 2025-02-07T15:06:56.278Z

Yes we’ll were facing this issue.

[@carlton](/u/carlton) sir mentioned yesterday that they will change the question.

"We will be changing this question. Even we found it hard ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

Kind regards"

So need to worry about that question for now.

---

**post_id:** 591805  
**author:** 23f2004752  
**timestamp:** 2025-02-07T15:08:16.074Z

OK, that is good to hear, you won’t believe that yesterday I was trying this question for 2 hours literally, it can be more also.

---

**post_id:** 591812  
**author:** 23f2004644  
**timestamp:** 2025-02-07T15:34:36.903Z

I was stuck at that question for 2 days, I tried multiple ways but was not able to format the content with prettier as expected, every time I was getting the error “Incorrect. Try again.”

---

**post_id:** 591815  
**author:** 23f2004636  
**timestamp:** 2025-02-07T15:49:48.266Z

On popular demand, I’ve made Q10 of GA4 easier (converting from PDF to Markdown). The question remains the same, but the check is more liberal and the error messages are more helpful. Please give it a shot now.

(FYI, one person *did* solve it. A colleague, not someone from the IITM DS program.)

---

**post_id:** 591818  
**author:** 23f3003594  
**timestamp:** 2025-02-07T16:00:15.001Z

Hello Sir, i tried but unfortunately after extracting the contents and formatting the contents and submitting it, it’s showing various errors like Missing links, Missing tables…

But on checking the file i wasn’t able to find any single table in the contents in that case what could be done to fix these errors?

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)

---

**post_id:** 591829  
**author:** 23f2004644  
**timestamp:** 2025-02-07T16:24:40.970Z

same issue with me as well

---

**post_id:** 591830  
**author:** 23f2004042  
**timestamp:** 2025-02-07T16:25:22.704Z

Sir I checked the pdf file, there is only one place unorder list is given and the same is available in my answer. But the system throws error Missing List (I tried with other symbols \* and + also) . Please inform me where I made mistake  
image description: The image displays the markdown content of a PDF formatted with prettier@3.4.2. There are four bullet points with phrases, and an error message "Missing lists".
image text: What is the markdown content of the PDF, formatted with prettier@3.4.2?
- cuppedia tamquam facilis confugo
- conservo depereo
- consectetur arx
- aeternus celebrer
Error: Missing lists

---

**post_id:** 591834  
**author:** 23f2004644  
**timestamp:** 2025-02-07T16:33:35.165Z

this is table. Check it  
image description: The image is a table with three columns and four rows. The first row contains three words: capitulus, deleniti, and pariatur. The subsequent rows contain words beneath each of the header words.
image text: capitulus deleniti pariatur voluptate barba bellum quaerat cedo cursus vestigium trans sortitus ait alioqui verumtamen

---

**post_id:** 591838  
**author:** 23f2003268  
**timestamp:** 2025-02-07T16:44:13.037Z

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
|

---

**post_id:** 591840  
**author:** 23f2004042  
**timestamp:** 2025-02-07T16:51:10.877Z

|

---

**post_id:** 591850  
**author:** sha_512_av  
**timestamp:** 2025-02-07T17:23:44.829Z

|

---

**post_id:** 591866  
**author:** 23f2004941  
**timestamp:** 2025-02-07T18:20:02.449Z

|

---

**post_id:** 591868  
**author:** 23f2005275  
**timestamp:** 2025-02-07T18:23:37.588Z

|

---

**post_id:** 591873  
**author:** daksh76  
**timestamp:** 2025-02-07T19:06:13.783Z

|
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

**post_id:** 591875  
**author:** 21F1005510  
**timestamp:** 2025-02-07T19:09:24.706Z

I checked many times. For me it says “Incorrect. Try again.”

---

**post_id:** 591877  
**author:** 23f2005138  
**timestamp:** 2025-02-07T19:28:00.399Z

Ya i know, i added tables, list, blockquote, code, tables have all been added still it’s showing errors. Not sure where am I going wrong.

---

**post_id:** 591880  
**author:** Atif01  
**timestamp:** 2025-02-07T20:01:46.758Z

Please refer video and document relating to Question 1 of Assignment 3. There it is mentioned how to mark bold, table etc., use those marks

---

**post_id:** 591884  
**author:** 23f2001413  
**timestamp:** 2025-02-07T20:38:38.238Z

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
|

---

**post_id:** 591885  
**author:** 23f2004941  
**timestamp:** 2025-02-07T20:46:04.301Z

---

**post_id:** 591886  
**author:** 23f2001413  
**timestamp:** 2025-02-07T22:02:11.674Z

---

**post_id:** 591968  
**author:** s.anand  
**timestamp:** 2025-02-08T03:23:12.990Z

---

**post_id:** 591972  
**author:** s.anand  
**timestamp:** 2025-02-08T03:31:12.813Z

---

**post_id:** 591982  
**author:** 23f1001174  
**timestamp:** 2025-02-08T04:54:21.666Z

---

**post_id:** 591998  
**author:** 23f2005138  
**timestamp:** 2025-02-08T05:37:22.199Z

- |

---

**post_id:** 592004  
**author:** 23f2004907  
**timestamp:** 2025-02-08T05:52:49.272Z

---

**post_id:** 592006  
**author:** 23f2004907  
**timestamp:** 2025-02-08T05:55:01.173Z

- |

---

**post_id:** 592007  
**author:** 23f1000422  
**timestamp:** 2025-02-08T06:10:10.342Z

---

**post_id:** 592008  
**author:** 23f1001174  
**timestamp:** 2025-02-08T06:13:28.798Z

---

**post_id:** 592019  
**author:** lakshaygarg654  
**timestamp:** 2025-02-08T06:40:39.010Z

|

---

**post_id:** 592021  
**author:** s.anand  
**timestamp:** 2025-02-08T06:45:07.380Z

---

**post_id:** 592049  
**author:** 21f2000709  
**timestamp:** 2025-02-08T07:56:59.322Z

---

**post_id:** 592057  
**author:** lakshaygarg654  
**timestamp:** 2025-02-08T08:27:29.717Z

|

---

**post_id:** 592059  
**author:** 21f3001379  
**timestamp:** 2025-02-08T08:28:27.587Z

---

**post_id:** 592064  
**author:** 22f3001315  
**timestamp:** 2025-02-08T08:40:07.981Z

---

**post_id:** 592065  
**author:** 21f3001379  
**timestamp:** 2025-02-08T08:44:44.640Z

---

**post_id:** 592071  
**author:** yasharabhavi  
**timestamp:** 2025-02-08T09:33:54.075Z

|
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

**post_id:** 592074  
**author:** 23f3003871  
**timestamp:** 2025-02-08T09:48:12.602Z

I am getting missing link error. I checked in the pdf file also, the blue color text seems a link but its not clickable.  
Any suggestion to move nearer to the actual solution.

---

**post_id:** 592115  
**author:** 21f3000745  
**timestamp:** 2025-02-08T11:45:56.252Z

You may try like this: cresco vomito

```
[cresco vomito](;;;)

```

---

**post_id:** 592123  
**author:** 22f3002771  
**timestamp:** 2025-02-08T12:13:42.491Z

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

**post_id:** 592125  
**author:** sarvan108  
**timestamp:** 2025-02-08T12:25:18.374Z

I think the idea behind this font is to make it difficult for people to manually work on the markdown file from scratch. I guess they want us to use the tools (like PyMuPDF4LLM, markitdown) they provided as resources to convert pdf into a markdown and then may be we can do some manual intervention to make it to the result as the scraping tools are not 100% accurate.

Could be another reason too. TAs’ can feel free to pitch in.

---

**post_id:** 592126  
**author:** lakshaygarg654  
**timestamp:** 2025-02-08T12:27:12.734Z

A post was merged into an existing topic: [Tds: assignment is not submitting](/t/tds-assignment-is-not-submitting/166189/21)

---

**post_id:** 592139  
**author:** 21f3000745  
**timestamp:** 2025-02-08T13:13:07.988Z

your last saved score (i.e.6 of your’s) will be official score and forgot about seek portal , it is not meant for this type of assignment.

---

**post_id:** 592141  
**author:** 21f3000745  
**timestamp:** 2025-02-08T13:14:34.661Z

Thank you for the update! I gave Q10 another shot, and I was able to solve it this time. The more liberal checks and improved error messages made a big difference in understanding where I was going wrong.  
Thank again.

---

**post_id:** 592144  
**author:** 21f3000745  
**timestamp:** 2025-02-08T13:15:53.963Z

Can we use hacking to get answers to some questions? Has anyone ever done it?

---

**post_id:** 592148  
**author:** 22f3000079  
**timestamp:** 2025-02-08T13:20:13.430Z

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

**post_id:** 592154  
**author:** akashkunwar  
**timestamp:** 2025-02-08T13:26:41.508Z

```

---

**post_id:** 592167  
**author:** 21f3001379  
**timestamp:** 2025-02-08T13:53:07.468Z

In the pdf you see some blue color font for specific words write that word in format

```
[word](#)

```

---

**post_id:** 592168  
**author:** 23f2000926  
**timestamp:** 2025-02-08T13:56:29.524Z

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

**post_id:** 592172  
**author:** sarvan108  
**timestamp:** 2025-02-08T14:00:19.459Z

Replace actual text to expected text until you got correct

---

**post_id:** 592174  
**author:** Deepanshutomar  
**timestamp:** 2025-02-08T14:12:53.748Z

same kind of error is arising with me too.Any suggestion what is wrong with it??

---

**post_id:** 592175  
**author:** Neelakandan  
**timestamp:** 2025-02-08T14:15:05.761Z

the rating should be treated as string.  
Format is as “2.9” instead of number 2.9

---

**post_id:** 592176  
**author:** 23f2002291  
**timestamp:** 2025-02-08T14:15:27.390Z

Yes it can be done. Got the 10th one correct by implementing breakpoint by printing the expected answer which is being used to validate the user answer in the js script.

---

**post_id:** 592210  
**author:** 23ds3000149  
**timestamp:** 2025-02-08T15:27:30.122Z

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

**post_id:** 592233  
**author:** 23f1001839  
**timestamp:** 2025-02-08T16:50:28.081Z

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

**post_id:** 592234  
**author:** 24f2003130  
**timestamp:** 2025-02-08T16:55:58.503Z

sir how will we know if we have been awarded with the bonus mark. Will it be reflected in our ga score and the marks would be 11/10 or will it be added later

---

**post_id:** 592235  
**author:** 24f2003130  
**timestamp:** 2025-02-08T17:02:30.525Z

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

**post_id:** 592259  
**author:** 23f2001738  
**timestamp:** 2025-02-08T18:05:32.112Z

Hello Sir, thank you for changing the question.

[@carlton](/u/carlton) I’m getting the below error:

```
Words like https, webbed, impact are missing (or not separated as words).

```

However, in the source PDF file itself these words are not available.

image description: The image shows a dark background with a grid of Latin words. Some words have a red squiggly line under them. Below the grid is an error message in red font.
image text: | quos | utrum | tredecim | valetudo | cras | videlicet | laudantium | aetas | canis | tantum | Error: Words like https, webbed, impact are missing (or not separated as words)

---

**post_id:** 592263  
**author:** 22f2000008  
**timestamp:** 2025-02-08T18:26:01.657Z

Copy the row name that is use to change and paste it in your answers

---

**post_id:** 592271  
**author:** 22f3002034  
**timestamp:** 2025-02-08T18:38:24.317Z

the ranking changes from time to time. you might need to scrape the data again.

---

**post_id:** 592280  
**author:** 22f3001840  
**timestamp:** 2025-02-08T18:44:53.523Z

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

**post_id:** 592287  
**author:** anu2023  
**timestamp:** 2025-02-08T19:11:13.889Z

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

**post_id:** 592289  
**author:** Jayeshbansal  
**timestamp:** 2025-02-08T19:15:03.641Z

[@21F1005510](/u/21f1005510) Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.

**Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

**post_id:** 592290  
**author:** swatikap  
**timestamp:** 2025-02-08T19:19:06.435Z

To evaluate the bonus mark for replying to this Discourse topic, At around the time of the deadline, we’ll close this thread, load all posts here, and run this in the Console:

```
[...new Set($$('.names a[href^="/u/"]').map(d => d.textContent))]

```

… to get the Discourse IDs who posted. Then we’ll match it to the email IDs and pass it to the operations team who will add it to the portal by 2025-02-22T18:30:00Z.

---

**post_id:** 592293  
**author:** 24f2000695  
**timestamp:** 2025-02-08T19:39:26.546Z

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

**post_id:** 592296  
**author:** 24f2000695  
**timestamp:** 2025-02-08T19:40:40.906Z

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

**post_id:** 592312  
**author:** tanmaysahu295  
**timestamp:** 2025-02-08T20:31:47.253Z

Your dot of 2.9 may be the dot from alphabet or numeric one  
Try to copy the value and then replace it

---

**post_id:** 592316  
**author:** koustubhr  
**timestamp:** 2025-02-08T21:53:13.622Z

Try to copy the error data  
The problem might be off dot  
check one dot is on right of m and other right of 0 in keyboard  
these two dots may represent different meanings

---

**post_id:** 592318  
**author:** Suhani  
**timestamp:** 2025-02-08T23:18:04.439Z

is it resolved?  
i too am getting the same error,even if it was working fine yesterday.

---

**post_id:** 592323  
**author:** 23ds3000149  
**timestamp:** 2025-02-09T00:48:22.810Z

https will be part of the link (provided ‘link’ is one of the checkpoints of evaluation)

---

**post_id:** 592324  
**author:** 23f2003853  
**timestamp:** 2025-02-09T01:05:38.835Z

Sir, In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I use different classes to extract values for various fields. Could there be any other element on the portal affecting this extraction?

In Q4, one of my classmates is encountering a “root property” error despite using the same extraction method as I do. Upon checking, I found that this issue occurs because the city’s time is displayed as the previous day compared to our time. The portal results seem to be based on the city’s actual time rather than IST.  
I would appreciate your guidance on these issues.

---

**post_id:** 592325  
**author:** 23f2003853  
**timestamp:** 2025-02-09T01:12:34.834Z

Good idea [@23f2005138](/u/23f2005138) and thanks. I fixed this. The example now reads:

```
[
  { "id": "tt1234567", "title": "Movie 1", "year": "2021", "rating": "5.8" },
  { "id": "tt7654321", "title": "Movie 2", "year": "2019", "rating": "6.2" },

```

… with the year and ratings quoted.

---

**post_id:** 592326  
**author:** 23f2003853  
**timestamp:** 2025-02-09T01:30:53.176Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> In Graded Assignment - 4 >> Q2, the year I extracted appears as “2024,” whereas the expected value on the portal is “2024–”. I have manually adjusted several values based on the expected format. This issue is specific to the year field.

I guess for the year part, there are certain series having multiple seasons, for which hyphenated “years” are given.

For the particular instance - `“2024–”`, it appears another season/part is announced, thats why it is written that way.

---

**post_id:** 592327  
**author:** 23f2003853  
**timestamp:** 2025-02-09T01:35:35.603Z

Thanks [@21f2000709](/u/21f2000709) for this information. I figure out where i made mistake. During writing console code I added to remove non numeric values in year field which i guess removed that hyphen (“–”). I will rectify that.

---

**post_id:** 592337  
**author:** Suhani  
**timestamp:** 2025-02-09T02:30:28.306Z

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

**post_id:** 592338  
**author:** Udipth  
**timestamp:** 2025-02-09T02:41:28.911Z

so just exchange it.

---

**post_id:** 592343  
**author:** 23f2000573  
**timestamp:** 2025-02-09T03:33:18.398Z

Thanks for your response.  
Many such titles have contradiction from what is expected and what is there in the website. This case the samples are 25 your approach is accepted to some extent, but on a larger sample space, need to work it right !

---

**post_id:** 592344  
**author:** 23f2001286  
**timestamp:** 2025-02-09T03:42:07.409Z

thanks for this, was wondering why it wasn’t working!

---

**post_id:** 592346  
**author:** 23f2000573  
**timestamp:** 2025-02-09T03:45:34.625Z

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

**post_id:** 592368  
**author:** 24f2003130  
**timestamp:** 2025-02-09T05:52:35.938Z

yes replace manually until you got correct ans . Error will suggest you what to change.

---

**post_id:** 592375  
**author:** 24f2003130  
**timestamp:** 2025-02-09T06:13:36.894Z

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

**post_id:** 592378  
**author:** rabbaniIITB  
**timestamp:** 2025-02-09T06:20:28.925Z

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

**post_id:** 592386  
**author:** 21f3001993  
**timestamp:** 2025-02-09T06:34:11.908Z

For this question, you may use the Google Colab file referenced in the assignment. This file will provide you with the date and description. Additionally, you can generate a weather location ID for the city specified in your assignment. Using this ID, you will obtain the weather URL, which you can then use to verify the date and description.

---

**post_id:** 592389  
**author:** sharma_abhay  
**timestamp:** 2025-02-09T06:45:07.273Z

here is the difference of ‘:’ in the expected ans. so make it manually correct . i did the same and got correct ans .  
and in the question also it is mentioned that may be manually you need to correct. just give a try.

---

**post_id:** 592391  
**author:** 22ds3000157  
**timestamp:** 2025-02-09T07:01:02.715Z

run your console script again and match the description.

---

**post_id:** 592394  
**author:** 23f3001601  
**timestamp:** 2025-02-09T07:07:11.747Z

yes, same happened with me . correct it manually.

---

**post_id:** 592398  
**author:** 22f2000008  
**timestamp:** 2025-02-09T07:21:17.635Z

In q10 links are not accessible through pdf and also creating problems while converting to markdown

---

**post_id:** 592420  
**author:** 23f1000299  
**timestamp:** 2025-02-09T07:49:44.486Z

image description: The image is a webpage featuring information on weather data integration for AgroTech Insights, a company specializing in agricultural technology. The page details the company's objectives, the task assigned, and provides sample outputs.
image text: Learn about the re package. Watch Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex). Learn about the datetime package. Watch Python Tutorial: Datetime Module - How to work with Dates, Times, Timedeltas, and Timezones Weather Data Integration for AgroTech Insights AgroTech Insights is a leading agricultural technology company that provides data-driven solutions to farmers and agribusinesses. By leveraging advanced analytics and real- time data, AgroTech helps optimize crop yields, manage resources efficiently, and mitigate risks associated with adverse weather conditions. Accurate and timely weather forecasts are crucial for making informed decisions in agricultural planning and management. Farmers and agribusinesses rely heavily on precise weather information to plan planting schedules, irrigation, harvesting, and protect crops from extreme weather events. However, accessing and processing weather data from multiple sources can be time-consuming and technically challenging. AgroTech Insights seeks to automate the extraction and transformation of weather data to provide seamless, actionable insights to its clients. AgroTech Insights has partnered with various stakeholders to enhance its weather forecasting capabilities. One of the key requirements is to integrate weather forecast data for specific regions to support crop management strategies. For this purpose, AgroTech utilizes the BBC Weather API, a reliable source of detailed weather information. Your Task As part of this initiative, you are tasked with developing a system that automates the following: 1. API Integration and Data Retrieval: Use the BBC Weather API to fetch the weather forecast for Manila. Send a GET request to the locator service to obtain the city's locationId. Include necessary query parameters such as API key, locale, filters, and search term (city). 2. Weather Data Extraction: Retrieve the weather forecast data using the obtained locationId. Send a GET request to the weather broker API endpoint with the locationId. 3. Data Transformation: Extract the issueDate and enhancedweatherDescription from each day's forecast. Iterate through the forecasts array in the API response and map each issueDate to its corresponding enhancedweatherDescription. Create a JSON object where each key is the issueDate and the value is the enhancedweatherDescription. The output would look like this: { "2025-01-01": "Sunny with scattered clouds" "2025-01-02": "Partly cloudy with a chance of rain" "2025-01-03": "Overcast skies" // ... additional days } What is the JSON weather forecast description for Manila? "2025-02-16": "Sunny and a gentle breeze", "2025-02-17": "Sunny and a gentle breeze", "2025-02-18": "Sunny and a gentle breeze" "2025-02-19": "Sunny and a gentle breeze", "2025-02-20": "Sunny and a gentle breeze" } Check

Why question 4 starts failing. It was working correct yesterday. Because of it I am getting 9/10 marks.

---

**post_id:** 592421  
**author:** 22f3001315  
**timestamp:** 2025-02-09T07:49:53.990Z

The result is dynamic with changes made in the API. So try re-executing your code today and it will automatically solve. Your code is right ! Just make a re-run and things will work out ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

**post_id:** 592422  
**author:** 23f1000299  
**timestamp:** 2025-02-09T07:54:08.648Z

try running the console again and it will work, make sure the data matches with the one in api as it changes regularly

---

**post_id:** 592426  
**author:** 23f1001231  
**timestamp:** 2025-02-09T08:06:59.795Z

Thanks!.  
It is working now. I had to manually correct 5 movie titles to get it correct.

---

**post_id:** 592433  
**author:** lakshaygarg654  
**timestamp:** 2025-02-09T08:14:05.998Z

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

**post_id:** 592437  
**author:** 23f3004114  
**timestamp:** 2025-02-09T08:21:43.386Z

Titles (from the output json) should be replaced by the titles which shows in the error message “Expected”. It can only be done manually. There may be multiple titles need to be translated by this method.

Please refer the instruction.  
image description: The image features text and a button, likely from a website or application. The text is a warning about IMDb search results.
image text: IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.
Check

---

**post_id:** 592439  
**author:** 23f1001231  
**timestamp:** 2025-02-09T08:32:10.545Z

you can manually add space after the hyphen

---

**post_id:** 592443  
**author:** swatikap  
**timestamp:** 2025-02-09T08:39:35.814Z

I face the same error, also thinking of issueDate, the value seems to be constant in every loop inside forecasts array (is it because the data is issed on that particular date) that gives same issue date key across the json outcome. Anyways the new json with same issueDate also gives the same Root error

---

**post_id:** 592444  
**author:** sarvan108  
**timestamp:** 2025-02-09T08:41:16.475Z

Double-check that the rating field in the JSON is indeed a float (`2.9`) and not a string (`"2.9"`) in your code.

---

**post_id:** 592453  
**author:** 23f2003853  
**timestamp:** 2025-02-09T09:05:31.841Z

That is perhaps to ensure we don’t manually write the markdown for the pdf. Converting the pdf to markdown and getting the correct output is extremely hard, I tried doing that multiple times yet wasn’t able to get that right by the original method.

But since it is mentioned that the GAA is hackable and we are allowed to do so, for some of the questions, therefore you can try solving that by establishing a breakpoint in the sources and then write the code in the console to get the expected output.

---

**post_id:** 592462  
**author:** 22f3000586  
**timestamp:** 2025-02-09T09:32:07.046Z

Write the code referencing the provided collab file and make sure to use the API key  
The output actually changes once in a while so you might need to run the code a few times before getting in right  
<https://tds.s-anand.net/#/bbc-weather-api-with-python>

---

**post_id:** 592470  
**author:** tarundude02  
**timestamp:** 2025-02-09T09:40:39.232Z

your most recently saved score will be evaluated

---

**post_id:** 592471  
**author:** 22f3000519  
**timestamp:** 2025-02-09T09:42:45.371Z

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

---

**post_id:** 592472  
**author:** ShivaniAdhiyaman  
**timestamp:** 2025-02-09T09:47:37.836Z

> 35 weather\_url = f'https://www.bbc.com/weather/{location id}'
36
37 # Fetch weather data
NameError: name 'location\_id' is not defined

---

**post_id:** 592476  
**author:** anu2023  
**timestamp:** 2025-02-09T09:55:06.651Z

In the second question are we supposed to edit the JSON manually until we reach a correct answer ? I think the expected result has some difference from what shows up in the website

---

**post_id:** 592477  
**author:** anu2023  
**timestamp:** 2025-02-09T09:58:40.634Z

Not able to get the missing links in Q10  
Any suggestions welcome please

---

**post_id:** 592478  
**author:** HARISH.S  
**timestamp:** 2025-02-09T09:59:13.731Z

For question 10 I’ve tried everything. Links and headings work fine, but I’m not able to fix the “missing tables” issue (I’ve also tried using pdfplumber and tabulate). In the pdf as well, I don’t see any tables, any hints or suggestions would be very helpful. Thanks!

---

**post_id:** 592480  
**author:** 24ds1000082_Vivek  
**timestamp:** 2025-02-09T10:01:39.752Z

there is no location id mentioned as it is mentioned of the different city. please check the city for which you need to find the location id and then proceed

---

**post_id:** 592497  
**author:** 21f2000296  
**timestamp:** 2025-02-09T10:24:24.121Z

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

**post_id:** 592498  
**author:** nayonika  
**timestamp:** 2025-02-09T10:24:39.839Z

How to actually do the HNRSS one…i can’t find much.

---

**post_id:** 592507  
**author:** 23f1002571  
**timestamp:** 2025-02-09T10:30:18.333Z

How did u do the links? I’m unable to do links

---

**post_id:** 592509  
**author:** 23f1002571  
**timestamp:** 2025-02-09T10:31:15.219Z

Just copy paste the expected value in place of actual value in json. Keep doing this eventually it would be the answer would be correct.

This is a format issue when the json is scrapped from the browser.

---

**post_id:** 592511  
**author:** 23f2003853  
**timestamp:** 2025-02-09T10:36:15.286Z

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

**post_id:** 592515  
**author:** 23f3004114  
**timestamp:** 2025-02-09T10:41:30.178Z

same with me. In the project it is written that the form should be submitted but there’s no question in the portal.

---

**post_id:** 592522  
**author:** 22f3001754  
**timestamp:** 2025-02-09T10:53:10.517Z

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

**post_id:** 592534  
**author:** koustubhr  
**timestamp:** 2025-02-09T11:09:57.380Z

Manual correction will not work. Try to extract - from the console. I did it like that it was not working then I extracted from console then it worked

---

**post_id:** 592536  
**author:** ABHIJITH_VS  
**timestamp:** 2025-02-09T11:11:32.436Z

Please ensure that your .yml file should have step name as your email Id. then Manually trigger the task (don’t wait till the scheduled time), ensure it was committed within 5 minutes and that commit should be top most item in all workflows. Then check it, it will work

---

**post_id:** 592546  
**author:** HARISH.S  
**timestamp:** 2025-02-09T11:22:34.616Z

You can find some text blue in color and underline use some dumy url it will work

---

**post_id:** 592548  
**author:** 23f3004024  
**timestamp:** 2025-02-09T11:28:01.981Z

You can find some lines having second, third words are uniformly aligned. Those are tables

---

**post_id:** 592553  
**author:** 22f3000657  
**timestamp:** 2025-02-09T11:37:59.808Z

When I resave the questions, the previously correct questions turn wrong which is extremely frustrating and time taking. I wish there is an option which saves the correct answer and does not require us to have multiple processes running in our pc even after getting the answer right previously.

---

**post_id:** 592556  
**author:** iamsarthak  
**timestamp:** 2025-02-09T11:42:26.613Z

In Q 6 I checked all the startups link at [Hacker News - Newest: "Startup"](https://hnrss.org/newest?q=Startup)… none is greater than 81 then how to submit that link… is there something i am missing

---

**post_id:** 592560  
**author:** 24ds3000032  
**timestamp:** 2025-02-09T11:43:05.537Z

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

**post_id:** 592586  
**author:** 24f2003130  
**timestamp:** 2025-02-09T12:11:40.484Z

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

**post_id:** 592591  
**author:** AryanTikam  
**timestamp:** 2025-02-09T12:15:53.311Z

you have to manually change for a few mismatch.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/s.anand/48/15264_2.png) s.anand:

> [@21F1005510](/u/21f1005510) Actually, some IMDb titles have multiple names. For example, [The Recruit](https://www.imdb.com/title/tt16030542/) is [also known as Graymail in India](https://www.imdb.com/title/tt16030542/releaseinfo/?ref_=tt_dt_aka#akas). My server checks from a different region from yours. Hence the need for manual corrections for a few titles.
>
> **Why didn’t I pick an exercise that could be fully automated?** Because this is how real-life data sourcing is. It’s never perfect. You often need to create workflows where you’re able to quickly correct such errors in automation.

---

**post_id:** 592604  
**author:** 23f2005419  
**timestamp:** 2025-02-09T12:29:57.475Z

Yes …due to the location difference the search results are different for everyone therefore you need to adjust it accordingly  
It might need around 6-7 amendments

---

**post_id:** 592607  
**author:** 23f2005419  
**timestamp:** 2025-02-09T12:36:29.100Z

The API is returning 14 days of forecast data, as evidenced by the output However, the issueDate values are not unique for each day. Instead, they represent the time when the forecast was issued or updated.  
In your output, there are only two unique issueDate values:  
2025-02-08T04:00:00-05:00  
2025-02-08T16:01:58-05:00  
This means the forecast was updated twice on February 8, 2025, once at 04:00 AM and again at 4:01 PM (both in EST timezone) …To get a unique weather description for each day, you need to modify your approach by using the actual forecast day for each day instead.

---

**post_id:** 592616  
**author:** 23f2003717  
**timestamp:** 2025-02-09T12:52:04.835Z

While submitting solution, do I need to keep all the local servers running/local URLs like 127.0.0.0 stuff, else I am getting one question as correct & the other one mentions unable to fetch data!? So that means I need to run them in different different ports?

---

**post_id:** 592618  
**author:** 23f2001177  
**timestamp:** 2025-02-09T12:54:22.008Z

I posted this error message but now the first issue got resolved but I am still keeping it in my post so that if anyone faces same issue, they can try if they can fix it similar to how it worked for me.

Please help with the second issue.

1. For Q8, the workflow is running on Github and commiting the scraped results to the json file (which is so amazing for me btw!). But I am getting this error for my public repo.  
   How it got resolved: I set up fixed time for cron schedule instead of every 5 min. Now it works.

> Error: No daily scheduled triggers found in workflows.

2. I had all correct results for Q1 to Q7 till yesterday but it keeps giving errors even when I reload same file for some questions. Do I need to keep addressing those errors or if once correct and saved, I can ignore those?

---

**post_id:** 592624  
**author:** 23f2003717  
**timestamp:** 2025-02-09T13:00:26.515Z

image description: The image shows a dark background with text describing a JSON data structure, presumably about movies. It has a question "What is the JSON data?". Below the question, there's a block of JSON data enclosed in a red-bordered box, listing movie IDs, titles, and other details. The bottom part of the image displays an error message in red, indicating a mismatch in movie IDs, and specifying the expected and actual values.
image text: What is the JSON data?
{ "id": "tt0060196", "title": "The Good, the Bad and the Ugly", "year": "1966", "
{ "id": "tt0137523", "title": "Fight Club", "year": "1999", "rating": "8.8" },
{ "id": "tt0120737", "title": "The Lord of the Rings: The Fellowship of the Ring"
]
Error: At [0].id: Values don't match. Expected: "tt20221436". Actual: "tt0437179"
  
I have tried several times but still recieving this as error. Please help

---

**post_id:** 592625  
**author:** Vedant22  
**timestamp:** 2025-02-09T13:01:11.101Z

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

**post_id:** 592629  
**author:** Vedant22  
**timestamp:** 2025-02-09T13:02:38.460Z

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

**post_id:** 592631  
**author:** Vedant22  
**timestamp:** 2025-02-09T13:04:14.674Z

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

---

**post_id:** 592632  
**author:** 23f3002537  
**timestamp:** 2025-02-09T13:04:24.869Z

> 24 weather\_url = 'https://www.bbc.com/weather/' + result['response'] ['results'] ['results'][0]['id']
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

**post_id:** 592641  
**author:** 23f2000098  
**timestamp:** 2025-02-09T13:13:32.686Z

this error comes, whenever you answer the other ones and click save. Please answer this question lastly, and submit immediately. it changes within a second. If it continues means, do manual correction and change according to the “expected”

---

**post_id:** 592647  
**author:** 23f2000098  
**timestamp:** 2025-02-09T13:18:09.159Z

while searching dont put any other filter other than asked in Problem statement.

---

**post_id:** 592684  
**author:** Haricharan  
**timestamp:** 2025-02-09T13:34:26.111Z

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

**post_id:** 592689  
**author:** 23f2005419  
**timestamp:** 2025-02-09T13:39:15.522Z

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

**post_id:** 592691  
**author:** H1Dd3n_xx  
**timestamp:** 2025-02-09T13:40:26.226Z

It worked for me; only 4–5 values caused errors, which I fixed manually. Additionally, I corrected the console code, which now provides the correct result.

---

**post_id:** 592704  
**author:** 23f3002537  
**timestamp:** 2025-02-09T13:51:57.206Z

what is this magic trick… please elaborate …

```
Error: At [10].id: Values don't match. Expected: "tt16027074". Actual: "tt8008948"

```

i dont see that value in data …

---

**post_id:** 592707  
**author:** 23f2000098  
**timestamp:** 2025-02-09T13:54:54.255Z

You can manually edit that. I also have to manually edit one entry to get the correct answer.

---

**post_id:** 592721  
**author:** 23f1001231  
**timestamp:** 2025-02-09T14:06:29.442Z

Hi,  
As mentioned in the question, you have to sort by “joined” so it should be “<https://api.github.com/search/users?q=location:Seattle+followers:>>120&sort=joined&order=desc”

---

**post_id:** 592725  
**author:** Haricharan  
**timestamp:** 2025-02-09T14:08:38.790Z

There are two “Vienna”. The question4 is referring to which one?

---

**post_id:** 592727  
**author:** 23f3002537  
**timestamp:** 2025-02-09T14:11:14.190Z

Manually make correction in your answer as provided in the error message. If no such words are available insert those and check

---

**post_id:** 592730  
**author:** 23f3004162  
**timestamp:** 2025-02-09T14:18:30.851Z

check if the action is commited

---

**post_id:** 592734  
**author:** 23f3004024  
**timestamp:** 2025-02-09T14:21:38.216Z

try copying the expected result and pasting it inside the quotations

---

**post_id:** 592736  
**author:** 23ds3000149  
**timestamp:** 2025-02-09T14:22:18.004Z

Check the log of the daily commit .

---

**post_id:** 592750  
**author:** 23ds3000149  
**timestamp:** 2025-02-09T14:35:34.384Z

Ahh, I have the same doubt too!

---

**post_id:** 592768  
**author:** GIRISH_VISHVESHVAR_B  
**timestamp:** 2025-02-09T14:47:12.663Z

For the links, this format worked for me:  
[ < link text > ] (#)

---

**post_id:** 592801  
**author:** Sagan  
**timestamp:** 2025-02-09T15:05:50.845Z

Yes I got it now. Thank you!

---

**post_id:** 592803  
**author:** Sagan  
**timestamp:** 2025-02-09T15:06:58.477Z

it should be “2.9” instead of 2.9

---

**post_id:** 592809  
**author:** 22f1000120  
**timestamp:** 2025-02-09T15:11:37.467Z

looks like formatting or the passed conditions have some issue… can you check and verify it once and see?

---

**post_id:** 592820  
**author:** 22f3000639  
**timestamp:** 2025-02-09T15:21:41.857Z

Error: At [3].title: Values don’t match. Expected: “4. 365 Days - Noch Ein Tag”. Actual: “4. The Next 365 Days”

{“id”: “tt21106646”, “title”: “4. The Next 365 Days”, “rating”: “2.9”, “year”: “2022”}

my result , there is no any entry with “4. 365 Days - Noch Ein Tag” on IMDB

---

**post_id:** 592821  
**author:** Haricharan  
**timestamp:** 2025-02-09T15:22:57.529Z

I am getting missing links as error in the 10th question. How to do it?

---

**post_id:** 592851  
**author:** Rrishit  
**timestamp:** 2025-02-09T15:36:39.718Z

Mine is giving 1/10 on running without even writing anything? This is happening for Q3? Is it just a glitch?

---

**post_id:** 592864  
**author:** Rrishit  
**timestamp:** 2025-02-09T15:41:57.385Z

Yes happened to me too, refresh the page, mine got fixed!

---

**post_id:** 592869  
**author:** sandeepstele  
**timestamp:** 2025-02-09T15:43:25.700Z

Check you pdf you can find a word with blue colour and underline. Give some dummy link and use link mark with the word

---

**post_id:** 592877  
**author:** 21f3000745  
**timestamp:** 2025-02-09T15:46:29.876Z

Best way to solve Q2 is , look at the network tab in dev tools and get the url used for assessment and get data from it .

---

**post_id:** 592879  
**author:** 22f3001011  
**timestamp:** 2025-02-09T15:46:42.193Z

u have used a apace (\_) after 2.9 which is not visible at front that’s why it is throwing error , it should be just (“2.9”) not ("2.9 ")

---

**post_id:** 592886  
**author:** 22f3002723  
**timestamp:** 2025-02-09T15:50:47.039Z

Agreed and I have tweaked my approach to get the correct answer. But I feel the question instructions should be adjusted accordingly - the question says to get every issueDate and enhancedweatherDescription key value pair - but only 2 such pairs exist ; whereas in the final answer it is forecast date & weather description total 14 pairs.

---

**post_id:** 592901  
**author:** 21f3000745  
**timestamp:** 2025-02-09T15:58:59.656Z

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

**post_id:** 592902  
**author:** 22ds2000011  
**timestamp:** 2025-02-09T15:59:12.855Z

type 2025 instead of only using 25 for the year

---

**post_id:** 592913  
**author:** 23f3002537  
**timestamp:** 2025-02-09T16:04:51.693Z

HOW TO DO SCRAPING USING GITHUB ACTIONS  
I’m getting no workflow runs error Sir

---

**post_id:** 592917  
**author:** 23f1000625  
**timestamp:** 2025-02-09T16:05:40.244Z

How to resolve “Error: Incorrect latitude. Check OSM ID ending with 2077”

---

**post_id:** 592924  
**author:** 23f2001305  
**timestamp:** 2025-02-09T16:09:30.499Z

[@22f3000657](/u/22f3000657)

you can try this-

<https://nominatim.openstreetmap.org/search?format=jsonv2&city=Chennai&country=India>

change the city and country in the url

there will be a bounding\_box field: [min\_lat, max\_lat, min\_long, max\_long]

---

**post_id:** 592925  
**author:** namanshyamsukha  
**timestamp:** 2025-02-09T16:09:48.477Z

#question 10  
Hi, Can anyone help me with Question 10?  
No matter how i try to post the markdown, it is always showing that either the words are missing or are different from the original. I have tried every possible way i could think of but it is not working.

---

**post_id:** 592928  
**author:** gouthamnischay  
**timestamp:** 2025-02-09T16:10:43.735Z

Getting this question right is a tough nut to crack…so I would rather suggest you to do using the developer tools by inspecting the source code and putting the breakpoint followed by writing the code in the console to retrieve the expected answer

---

**post_id:** 592934  
**author:** 21f3002277  
**timestamp:** 2025-02-09T16:13:55.561Z

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

**post_id:** 592938  
**author:** rohitgarg  
**timestamp:** 2025-02-09T16:15:41.126Z

Hi Team,

I have made the JSON from the IMDB website using JS, But do i miss any filter conditions,  
Here's a brief description of the image:
The image displays JSON data along with an error message. The JSON data seems to be related to movie information, including the title "Venom: The Last Dance," year "2024," and a rating of "6.0." An error message indicates a title mismatch, and there are notes about regional variations and periodic updates.
image text: What is the JSON data? title": "10. Venom: The Last Dance", "year": "2024", "rating": "6.0" }, { "id": "tt30292390", Error: At [10].title: Values don't match. Expected: "11. Sebastian Fitzeks Der Heimweg". Actual: "11. The Calendar Killer" IMDb search results may differ by region. You may need to manually translate titles. Results may also change periodically. You may need to re-run your scraper code.
  
I took first 25 films which 5 to 6 rating, but json seems to be different.

Could anyone please tell me what i did wrong here?

---

**post_id:** 592942  
**author:** Abhay222  
**timestamp:** 2025-02-09T16:17:12.810Z

Solved the above issue, please ignore it.

---

**post_id:** 592949  
**author:** rohitgarg  
**timestamp:** 2025-02-09T16:20:29.219Z

Believe it or not, I solved it

Here's a description of the image:
The image is a screenshot of a coding or technical exercise. There's a question at the top about markdown content, and a code snippet is presented, along with the phrase "Decumbo decumbo suadeo totidem apto." A checkmark is present, suggesting a correct answer. The text below explains the difficulty in obtaining correct Markdown output from a PDF.
image text: What is the markdown content of the PDF, formatted with prettier@3.4.2?
|adficio|chirographum|
|

---

**post_id:** 592950  
**author:** Jeleshiya  
**timestamp:** 2025-02-09T16:20:47.342Z

|

---

**post_id:** 592953  
**author:** parthpatel  
**timestamp:** 2025-02-09T16:23:37.267Z

|
|vitae|ipsam|
|spectaculum|claudeo|
|comes|celebrer|
Decumbo decumbo suadeo totidem apto.
Correct
It is very hard to get the correct Markdown output from a PDF. Any method you use will likely require manual corrections. To make it easy, this question only checks a few basic things.

---

**post_id:** 592954  
**author:** 22f3002184  
**timestamp:** 2025-02-09T16:23:43.629Z

In the 10th question, how do we add headings and links to the markdown output?(getting error: Headings missing)

---

**post_id:** 592960  
**author:** Abhay222  
**timestamp:** 2025-02-09T16:25:24.448Z

first convert it roughly to md file then use ai and tell it to add (all the errors one by one). and slowly it will solve all the errors

yes i know it is not the correct way to convert pdf to md file but its just a way to trick the checking system.

but i have an issue it gave me error that it does not contains the word “bash, javascript, whole redesign, net, suasoria” which is not in the actual pdf, but i added it and it worked. it was just pure trial and error.

---

**post_id:** 592968  
**author:** rohitgarg  
**timestamp:** 2025-02-09T16:29:06.442Z

this is a changing dataset so make changes to your answer accordingly and you will get it correct

---

**post_id:** 592971  
**author:** adeepu.here  
**timestamp:** 2025-02-09T16:30:02.184Z

Do the necessary changes as it is said below as it is an everchanging dataset.  
You will get the answer correct once you make the changes asked after checking.

---

**post_id:** 592973  
**author:** Saransh_Saini  
**timestamp:** 2025-02-09T16:30:25.035Z

check you code and do the changes like max\_latitude  
replace [0] to [1]

---

**post_id:** 592978  
**author:** 23f2000098  
**timestamp:** 2025-02-09T16:33:41.438Z

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

**post_id:** 592982  
**author:** 23f1001301  
**timestamp:** 2025-02-09T16:34:55.919Z

in my dashboard there is no submit button for ga2,3,and 4 as well and if i check for scores in grades tab for ga2 and ga3 it was given as not submitted , does everyone facing the same ?? if the submit button is visible for anyone plss guide me to rectify that.  
regards and thanks.

---

**post_id:** 592984  
**author:** Saransh_Saini  
**timestamp:** 2025-02-09T16:35:18.237Z

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

**post_id:** 592991  
**author:** nayonika  
**timestamp:** 2025-02-09T16:40:31.628Z

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

**post_id:** 592995  
**author:** 23f1001126  
**timestamp:** 2025-02-09T16:42:06.985Z

Hi,  
For the 4th question, We can get the necessary information issueDate and its description from Summary itself right? or am I seeing the stuff in the wrong place?

---

**post_id:** 592996  
**author:** AnvithaV  
**timestamp:** 2025-02-09T16:42:55.994Z

Change it manually.  
add the expected answer

---

**post_id:** 593009  
**author:** rohitgarg  
**timestamp:** 2025-02-09T16:48:37.375Z

when you press ctrl+c it turns off the server and same goes for refresh.  
also you dont need to manually write ?country… just write till outline and turn on the server n you are good to go.

---

**post_id:** 593014  
**author:** 21f3000745  
**timestamp:** 2025-02-09T16:50:23.681Z

ok this is fine for now and its showing correct also but at the time of evaluation will my server runs??

---

**post_id:** 593020  
**author:** 21f3000745  
**timestamp:** 2025-02-09T16:52:32.951Z

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

**post_id:** 593023  
**author:** vidya19  
**timestamp:** 2025-02-09T16:52:52.617Z

Thank you bro, I will try this

---

**post_id:** 593024  
**author:** 23ds3000040  
**timestamp:** 2025-02-09T16:53:06.031Z

not at all. your last saved marks will be considered

---

**post_id:** 593028  
**author:** 22f3002184  
**timestamp:** 2025-02-09T16:55:01.459Z

just replace value instead of it. same problem I also that time I check code and modify serval time I faced same error. so just ignore it and replace expected value instead of actual value in our Json.

---

**post_id:** 593029  
**author:** 23f1002534  
**timestamp:** 2025-02-09T16:55:45.350Z

extract the pdf to markdown format using chatgpt then add links,tables and one blockquote

---

**post_id:** 593030  
**author:** 24ds2000108  
**timestamp:** 2025-02-09T16:55:51.950Z

Try to use the key ‘enhancedWeatherDescription’ parsing through the summary object (or) use the BeautifulSoup to find ‘div’ with attributes of  
class: wr-day-summary

---

**post_id:** 593031  
**author:** 21f3000745  
**timestamp:** 2025-02-09T16:56:34.118Z

Hi, please ensure that your repository is public, if private the response would be 404. If workflow runs is not found, it might be that the number of API calls to your profile/repo might have exceeded, it usually gets reset at the end of the day. Please try again after sometime)

---

**post_id:** 593034  
**author:** jashmevada  
**timestamp:** 2025-02-09T16:57:04.532Z

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

**post_id:** 593036  
**author:** 21f3000745  
**timestamp:** 2025-02-09T16:57:11.845Z

You have to manually change these thing  
from actual change to expected.  
For me, error was almost 10 times.

---

**post_id:** 593039  
**author:** Saransh_Saini  
**timestamp:** 2025-02-09T16:57:35.122Z

on your 11th or 12th instance change it  
write the actual value

---

**post_id:** 593040  
**author:** 23f1002534  
**timestamp:** 2025-02-09T16:58:00.163Z

If you have submitted on the assignment site and saved it in time, then that score is the actual score and will be updated directly on the student dashboard.

---

**post_id:** 593043  
**author:** 23f1003139  
**timestamp:** 2025-02-09T17:01:51.864Z

Your answer is correct. Just add a space after the hyphen—it will resolve the problem. Or you can copy and paste from here: '2025– '.

---

**post_id:** 593053  
**author:** 23f2005419  
**timestamp:** 2025-02-09T17:06:00.951Z

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

**post_id:** 593060  
**author:** 23f2000573  
**timestamp:** 2025-02-09T17:08:16.185Z

Yeah! His issue is genuine. Arnav’s JSON seems to be correct, yet these are some issues faced by him.

---

**post_id:** 593062  
**author:** 24ds2000108  
**timestamp:** 2025-02-09T17:08:23.051Z

Yeah! even I am facing this issue. Despite lot of efforts, last question markdown seems to always incorrect. It is always throwing any sort of error for no reason.

---

**post_id:** 593068  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:10:40.176Z

The IMDB and weather questions was a pain along with the 10th question, wasted so much time [@s.anand](/u/s.anand) , the questions were nowhere tough, it was the problems with the evaluation part i had spend hours just to sit and correct the JSON file and no comments on the 10th question’s part.

I am fine with the academia being challenging to study not the evalation making me manually edit solutions

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

**post_id:** 593073  
**author:** 22f1000535  
**timestamp:** 2025-02-09T17:12:23.430Z

yes change manually, there are slight changes which we have to do

---

**post_id:** 593075  
**author:** 23f2000098  
**timestamp:** 2025-02-09T17:12:57.853Z

For the 8th question, i am getting an error that tells me i have not run the action, though i manually triggered it and confirmed the commit was made. Cant figure out whats wrong.

---

**post_id:** 593085  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:18:23.735Z

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

**post_id:** 593088  
**author:** 22f3000804  
**timestamp:** 2025-02-09T17:20:50.330Z

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

**post_id:** 593093  
**author:** 23f2000573  
**timestamp:** 2025-02-09T17:22:36.650Z

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

**post_id:** 593094  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:22:37.064Z

just edit some of the spellings in answers manually as per errors you get n you are good to go.

---

**post_id:** 593095  
**author:** jashmevada  
**timestamp:** 2025-02-09T17:23:01.174Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

> Cinquanta sfumature di grigio

It is just a translation of the same movie… it’s not different  
Copy paste the Expected: “title” and click on check  
It’ll work

---

**post_id:** 593097  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:23:44.720Z

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

**post_id:** 593099  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:24:22.138Z

@all, in q4 Actually the answer data is sync with current weather description therefore the answer changes. Make sure to update your json file before submitting.

---

**post_id:** 593102  
**author:** 23f2005419  
**timestamp:** 2025-02-09T17:25:39.334Z

try refreshing the page and re-run the script. as the data gets updated the answer also changes.

---

**post_id:** 593103  
**author:** 23f2000573  
**timestamp:** 2025-02-09T17:25:58.086Z

refer to the link post,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png)
[GA4 - Data Sourcing - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga4-data-sourcing-discussion-thread-tds-jan-2025/165959/65) [Tools in Data Science](/c/courses/tds-kb/34)

> use this [Google Colab](https://colab.research.google.com/drive/1X5IO8K1Xf8Wh7SOZelSrFAfZgRG-mv4A?usp=sharing) with the city name to get the Json Body just change the date format.
> [@23f2004752](/u/23f2004752)

---

**post_id:** 593125  
**author:** 21f3001797  
**timestamp:** 2025-02-09T17:34:04.509Z

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

**post_id:** 593130  
**author:** Megha  
**timestamp:** 2025-02-09T17:36:09.369Z

why everytime question 2 answer is showing error in json?

---

**post_id:** 593144  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:39:48.455Z

What error are you getting [@Abhay222](/u/abhay222) ?

Can you post a screenshot or error details ?

---

**post_id:** 593151  
**author:** 23f3001752  
**timestamp:** 2025-02-09T17:41:44.880Z

Is it safe to skip Q4 for those who got the city named Nur-Sultan, since it has been renamed to Astana, and the answer for Astana is incorrect in the portal?

---

**post_id:** 593157  
**author:** Saransh_Saini  
**timestamp:** 2025-02-09T17:46:11.087Z

[@s.anand](/u/s.anand)  
There is possibly wrong evaluation in q6 as it is taking in 2nd latest link as the correct answer. I might be wrong, but the latest one is giving me incorrect evaluation while the 2nd latest is giving me the correct score.

---

**post_id:** 593167  
**author:** 21f3000745  
**timestamp:** 2025-02-09T17:49:43.501Z

getting the same issue Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

**post_id:** 593171  
**author:** 21f2001369  
**timestamp:** 2025-02-09T17:52:19.318Z

yes this kind errors.

---

**post_id:** 593188  
**author:** vidushi  
**timestamp:** 2025-02-09T18:00:21.016Z

[@Abhay222](/u/abhay222) [@22f3002184](/u/22f3002184)

if you look closely the expected value is `2024-`  and actual that you are supplying is `2024`.  
Difference ? your value does have a `-` and a space at the end.  
reason ? you might be scraping it ? `trim()` or maybe using `innerText` to get tag’s text ?

---

**post_id:** 593189  
**author:** Adityism  
**timestamp:** 2025-02-09T18:00:29.669Z

it seems we are intended to provide country specific versions for Individual students simulating being an analyst for MNC in various locations. Clearly you got Spain and I seem to have gotten France, although it doesn’t seem to be mentioned in the question itself.

---

**post_id:** 593207  
**author:** vidushi  
**timestamp:** 2025-02-09T18:06:17.921Z

Thank you Tanya for pointing out this issue.  
Just tell me this, has your city changed? If yes then what was it earlier and what is it now.

---

**post_id:** 593208  
**author:** 23f3002537  
**timestamp:** 2025-02-09T18:06:48.092Z

any reply regarding this please

---

**post_id:** 593210  
**author:** 22f3002184  
**timestamp:** 2025-02-09T18:08:17.696Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2000113/48/67775_2.png) 22f2000113:

> For question 2 getting Error: At [8].title: Values don’t match. Expected: “9. Un matrimonio di troppo”. Actual: “9. You’re Cordially Invited” But this movie is not found when searched by name

the movie may have different title on IMDb (perhaps in another language) according to region which is why there isnt an exact match u can manually format it to get marks

---

**post_id:** 593218  
**author:** 23f2000573  
**timestamp:** 2025-02-09T18:10:54.794Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/saransh_saini/48/123495_2.png)
[GA2 - Deployment Tools - Discussion Thread [TDS Jan 2025]](https://discourse.onlinedegree.iitm.ac.in/t/ga2-deployment-tools-discussion-thread-tds-jan-2025/161120/171) [Tools in Data Science](/c/courses/tds-kb/34)

> We have removed that button, cause it was causing confusion among the students.
> If you have saved your answers on the TDS portal then you need not worry, you will be marked. The button was just there to ensure you saw the assignment on the TDS portal.
> Regards,
> TDS TA

Read this

---

**post_id:** 593220  
**author:** 22f3000910  
**timestamp:** 2025-02-09T18:11:10.464Z

Try changing it manually. Some values keep changing due to change in server.

---

**post_id:** 593228  
**author:** 22f3002184  
**timestamp:** 2025-02-09T18:13:12.352Z

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

**post_id:** 593231  
**author:** 21f3000745  
**timestamp:** 2025-02-09T18:13:35.541Z

same problem, could anyone help what is wrong.

---

**post_id:** 593232  
**author:** 23f3002537  
**timestamp:** 2025-02-09T18:13:40.353Z

[@AnvithaV](/u/anvithav) check this out

---

**post_id:** 593233  
**author:** 23f3001752  
**timestamp:** 2025-02-09T18:13:51.114Z

No the city is same as before. But i think it fetches the latest data. As i saved it yesterday it was correct. But today when i clicked on save button again it got wrong.

---

**post_id:** 593240  
**author:** 22f3002723  
**timestamp:** 2025-02-09T18:17:00.243Z

What error are you getting ?

---

**post_id:** 593242  
**author:** 23ds3000241  
**timestamp:** 2025-02-09T18:18:19.669Z

how to approach question 8 of ga4

---

**post_id:** 593247  
**author:** 23f1001126  
**timestamp:** 2025-02-09T18:20:37.267Z

For question #8. Can I use the .github/workflows that I created for the previous assignments or i need to create a new workflow?

---

**post_id:** 593249  
**author:** 22f3002723  
**timestamp:** 2025-02-09T18:20:50.841Z

still the same {“id”:“tt24871974”,“title”:“12. Subservience”,“year”:“2024”,“rating”:“5.4”},  
Error: At [12].year: Values don’t match. Expected: "2024– ". Actual: “2024”

---

**post_id:** 593254  
**author:** 23ds3000241  
**timestamp:** 2025-02-09T18:23:16.226Z

Change the value manually

---

**post_id:** 593259  
**author:** shivanshgupta0007  
**timestamp:** 2025-02-09T18:24:45.474Z

I am still not sure why the github action question is not working for me. I have manually triggered the workflow multiple times but i keep getting the same ‘name’ error even though it has been specified in the code. Can somebody kindly help?

---

**post_id:** 593261  
**author:** mohiit  
**timestamp:** 2025-02-09T18:25:05.322Z

Have you given your email id in name ?

---

**post_id:** 593262  
**author:** 23f3002537  
**timestamp:** 2025-02-09T18:25:08.080Z

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

**post_id:** 593265  
**author:** 22f3002175  
**timestamp:** 2025-02-09T18:27:55.976Z

See there is difference of hyphen . Correct it manually.

---

**post_id:** 593270  
**author:** Rohitb  
**timestamp:** 2025-02-09T18:30:30.946Z

Just try re-running your code once and paste in the current response. Check if its working or not.

---

**post_id:** 593271  
**author:** 22f3002723  
**timestamp:** 2025-02-09T18:30:52.842Z

Change the slight differences manually accordingly with the expected values

---

**post_id:** 593274  
**author:** 22f3002723  
**timestamp:** 2025-02-09T18:32:09.036Z

I haven’t done MLP and BDM so should I drop TDS now

---

**post_id:** 593345  
**author:** carlton  
**timestamp:** 2025-02-10T05:09:13.069Z

Hi,

I couldn’t able to create markdown from pdf, it showing missing links, but i couldn’t able to find the link in pdf either. I think i’m missing something.

anyone suggest some way how to do pdf to markdown correctly?

---

**post_id:** 593528  
**author:** 23f3002537  
**timestamp:** 2025-02-10T12:19:48.767Z

if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

---

**post_id:** 593703  
**author:** carlton  
**timestamp:** 2025-02-11T03:21:36.200Z

yes  
But still doesnt work

---

**post_id:** 593777  
**author:** vaishnavi.k  
**timestamp:** 2025-02-11T08:51:36.710Z

In q10 i am geeting …missing links- error  
Any idea how to correct this

---

**post_id:** 593779  
**author:** Rehbar  
**timestamp:** 2025-02-11T08:51:42.895Z

Beyond the specific tools mentioned (like `IMPORTHTML` in Google Sheets or `httpx` and `lxml` in Python), what are the broader *ethical considerations* when scraping data from websites, and how can developers ensure they are acting responsibly and respecting website owners’ rights and resources?

---

**post_id:** 593781  
**author:** Lokkiii  
**timestamp:** 2025-02-11T08:51:45.993Z

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

**post_id:** 593895  
**author:** HARISH.S  
**timestamp:** 2025-02-11T16:03:33.614Z

What is the error are you facing ?

---

**post_id:** 593943  
**author:** 23f3001208  
**timestamp:** 2025-02-11T18:41:15.166Z

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

**post_id:** 594679  
**author:** s.anand  
**timestamp:** 2025-02-13T19:20:06.743Z

Check if you have made the query proprly. also, check if you taken the correct link from the item

---

**post_id:** 596704  
**author:** nayonika  
**timestamp:** 2025-02-18T13:13:08.478Z

in q10 i am getting error- missing links.  
can i get any explanation about this error so that i can figure out this ?  
[@Saransh\_Saini](/u/saransh_saini) as i left with this question only

---

**post_id:** 596713  
**author:** rohitgarg  
**timestamp:** 2025-02-18T13:26:28.016Z

Pdf content one link, I think your converting method was unable to convert link into markdown format , add it manual from pdf.

---

**post_id:** 596723  
**author:** 22f2000008  
**timestamp:** 2025-02-18T13:49:29.368Z

I have done that also but still getting same error

---

**post_id:** 596735  
**author:** 21f2000588  
**timestamp:** 2025-02-18T14:12:47.049Z

The one with blue line must be link here in the pdf.

---

**post_id:** 596759  
**author:** Jivraj  
**timestamp:** 2025-02-18T15:43:57.703Z

After that it asking to add tables, i added the same but the issue ‘Missing Tables’ exists

---

**post_id:** 596760  
**author:** Jivraj  
**timestamp:** 2025-02-18T15:44:03.726Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2000573/48/68306_2.png) 23f2000573:

> if it says something is missing, just add the same. refer to week-2 question 1 for markdown syntax if necessary

refer to this [@21f3000745](/u/21f3000745)

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000804/48/87428_2.png) 22f3000804:

> can someone help through this error!!

if it is saying something has a mismatch, just spot the mismatch one by one and manually change it [@22f3000804](/u/22f3000804)

---

**post_id:** 596779  
**author:** 22f2000008  
**timestamp:** 2025-02-18T16:50:40.193Z

Here for the bonus marks, it was great solving the GA4.

---

**post_id:** 596812  
**author:** iamsarthak  
**timestamp:** 2025-02-18T23:42:37.819Z

After you click the link, a page containing all the questions will appear. Attempt them and save it on that particular page using your IITM email ID. Through your ID, submissions will be taken.

---

**post_id:** 596902  
**author:** carlton  
**timestamp:** 2025-02-19T06:57:41.395Z

Thankyou , but now i am getting missing code error. What it means? [@23f2000573](/u/23f2000573)

---

**post_id:** 596904  
**author:** carlton  
**timestamp:** 2025-02-19T06:58:58.390Z

You just have to add a space after a hyphen

---

**post_id:** 596924  
**author:** 23f1002382  
**timestamp:** 2025-02-19T08:10:42.117Z

Check if you are using table formating where there is a table, also there is perhaps a code block in the pdf where a small section of text is in different font than the rest.

---

**post_id:** 598870  
**author:** 23f1002382  
**timestamp:** 2025-02-24T05:46:12.726Z

No there is no code block in the pdf. Now i m getting missing code error. Why this error can arise [@Saransh\_Saini](/u/saransh_saini)

---

