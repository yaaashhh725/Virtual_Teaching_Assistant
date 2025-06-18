# queries-regarding-end-term-exam-solutions

**post_id:** 619552  
**author:** 24f2003130  
**timestamp:** 2025-04-15T09:59:51.136Z

# queries-regarding-end-term-exam-solutions

Hi [@carlton](/u/carlton) and [@Jivraj](/u/jivraj) sir,

I appeared for the end term examination held on 13th April 2025 during the FN shift. I would like to bring to your attention that the exam interface did not provide an option for multiple selections. However, a few questions appeared to have multiple correct answers.

I have noted down the specific questions and the corresponding options I believe to be correct.So, kindly review them and let me know if there were any errors in my understanding of the questions. The questions are as follows:

image description: The image is a multiple-choice question. The question is about identifying a valid log entry format. The options provided contain log entry examples, some marked with an asterisk and some with a checkmark. The question specifies the correct marks and the question label.
image text: Question Number: 300 Question Id: 6406531231221 Question Type: MCQ
Correct Marks: 2
Question Label: Multiple Choice Question
Which of the following is a valid log entry based on the provided format?
Options:
6406534159824. 192.168.1.1 - - [12/Dec/2024:14:05:59 -0500] "GET /image.jpg HTTP/1.1" 200
1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/87.0.4280.88 Safari/537.36" www.s-anand.net 192.254.190.217
6406534159825. 192.168.1.1 - - [12/Dec/2024:14:05:59 -0500] "POST /image.jpg INVALID" 200
1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/87.0.4280.88 Safari/537.36" www.s-anand.net 192.254.190.217
6406534159826. 192.168.1.1 - - [12/Dec/2024:14:05:59 -0500] "PUT /image.jpg HTTP/1.1" OK
1234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/87.0.4280.88 Safari/537.36" www.s-anand.net 192.254.190.217
6406534159827. 203.0.113.7 -- [14/Dec/2024:16:45:11 -0500] "GET /index.html HTTP/1.1" 200
3500 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/90.0.4430.93 Safari/537.36" www.s-anand.net 192.254.190.219

Question 2: Fields needed to filter “POST requests under /images/ from 15:00 to 18:00 on Mondays”

To filter such logs, we need:

Time → for the hour and the day (Monday)  
Method → to filter POST  
URL → to filter /images/

So, the correct minimal set is:

> ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") Time, Method, URL

Time → needed ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:")  
Method → needed ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:")  
URL → needed ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:")  
Referer → not needed, but not harmful

So this option includes all the necessary fields, just with one extra — which doesn’t invalidate it.

Here's a description of the image:
The image is a multiple-choice question related to data filtering. The question asks which fields are necessary to filter POST requests for pages under /images/ from 15:00 to 18:00 on Mondays.
Four options are presented with different combinations of the fields: Time, Request, Method, URL, Status, Size, Referer and Server. The correct option is marked with a green checkmark.
image text:
Question Label: Multiple Choice Question
Which of the following fields are necessary to filter "POST requests made for pages under
/images/ from 15:00 to 18:00 on Mondays"?
Options:
6406534159828. Time, Request, Method, URL
6406534159829. Time, Method, Status, Size
6406534159830. Time, Method, URL, Referer
6406534159831. Time, Status, URL, Server

Acc to solutions only option 6406534159827 is valid:

Status is numeric (200)  
Method (GET), Protocol (HTTP/1.1), and URL (/index.html) are correct

All required fields are present and properly formatted

The other options were as follows:

9825 uses invalid protocol (INVALID)

9826 uses invalid status code (OK instead of numeric)

9824 has no critical issue — it is technically also valid (only uses a private IP 192.168.1.1, which is unusual but not invalid). So both 9824 and 9827 are valid, but the answer marked only 9827

image description: The image is a screenshot of a multiple-choice question. The question is about HTTP methods and idempotency. The correct mark for the question is 2. The options are POST, PUT, GET, and DELETE. The correct answer is PUT, indicated by a checkmark. The sub-section number is 4, and the sub-section ID is 640653189815. Question shuffling is allowed.
image text: Correct Marks : 2
Question Label: Multiple Choice Question
Which HTTP method is idempotent, meaning multiple identical requests have the same effect as a single request?
Options :
6406534159747. POST
6406534159748. PUT
6406534159749. GET
6406534159750. DELETE
Sub-Section Number : 4
Sub-Section Id : 640653189815
Question Shuffling Allowed: Yes
  
Correct Answer(s):

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") PUT – Correct: It replaces the resource entirely. Multiple identical PUTs = same result.

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") GET – Also correct: It only fetches data, no side-effects. Multiple GETs = same result.

![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14 ":white_check_mark:") DELETE – Technically correct: Deleting the same resource multiple times has the same result as deleting once (resource stays deleted).

---

**post_id:** 619868  
**author:** koustubhr  
**timestamp:** 2025-04-15T17:19:29.506Z

Incorrect Answer:

![:cross_mark:](https://emoji.discourse-cdn.com/google/cross_mark.png?v=14 ":cross_mark:") POST – Not idempotent. Each POST usually creates a new resource or changes server state.

(This is the mistake on my part that I put the ans as POST as I thought since 3/4 are idempotent and one is not I should select the odd one out but I hope this could be resolved)

Thank you

---

**post_id:** 619891  
**author:** 22f3000819  
**timestamp:** 2025-04-15T18:13:03.725Z

Agree & second all thoughts shared by [@24f2003130](/u/24f2003130) above.

* I also wanted to clarify on this question on filtered entries. The question mentions that a list filtered\_entries is being created , and with the way the question is structured it seems like the filtering conditions mentioned in the question have already been applied. In that case `len(filtered entries)` seems to be correct. However the right answer is marked ‘None of these’ .  
  Here's a description of the image:
  The image is a multiple-choice question, likely from a computer science or programming exam. It starts with the question number, ID and the type is MCQ (multiple choice question), that has 1 mark. The question is about finding the best way to count the number of requests with a 404 status code for pages under /error/. It then lists the options:
  image text:
  Question Number : 309 Question Id : 6406531231230 Question Type : MCQ
  Correct Marks : 1
  Question Label : Multiple Choice Question
  After filtering the log entries (in a list filtered\_entries), which of the following is the best way to
  count the number of requests with a 404 status code for pages under /error/?
  Options :
  6406534159860. Use len(filtered\_entries)
  6406534159861. Use len(entries)
  6406534159862. Use sum(1 for entry in entries)
  6406534159863. None of these
* The valid log entry had me stumped too, option 1 and 4 both look absolutely fine yet only option 4 is marked correct.
* Also, only POST request is not idempotent, all other requests are idempotent yet only PUT is marked correct.

Request you to please clarify and consider these points.

---

**post_id:** 620130  
**author:** iamprasna  
**timestamp:** 2025-04-16T10:08:58.668Z

Yes [@carlton](/u/carlton) the wording of the question made it seem like the filters were already applied on the list `filtered_entries`.

---

**post_id:** 620133  
**author:** 24f2003130  
**timestamp:** 2025-04-16T10:15:01.944Z

# Clarifications on Queries

1. **Which of the following is a valid log entry based on the provided format?**  
   Due to a technical issue in the portal, both options 1 and 4 are correct answers. The final scoring has been adjusted accordingly, and full marks will be awarded for either response.
2. **HTTP method is idempotent**  
   This question has been excluded from scoring as three methods (GET, PUT, and DELETE) are idempotent, with only POST being non-idempotent.
3. **Entries with 404 status code**  
   Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.
4. **Which of the following fields are necessary to filter “POST requests made for pages under /images/ from 15:00 to 18:00 on Mondays”?**  
   Option A (Time, Request, Method, URL) is correct because:

* Option B includes Size and Status, which aren’t needed for filtering by time, method, and URL
* Option C includes Referer, which is unnecessary unless filtering by source page
* Option D includes Status and Server, which aren’t relevant for this specific filtering requirement

---

**post_id:** 620467  
**author:** 22f3000819  
**timestamp:** 2025-04-16T18:28:35.206Z

Thank you for the clarification provided regarding Question 4 and resolution of errors in other questions. I understand the reasoning behind choosing Option A (Time, Request, Method, URL). However, I respectfully believe Option C (Time, Method, URL, Referer) is more accurate for the following reasons:

1. Redundancy in Option A:  
   The Request field already contains the HTTP method, URL, and protocol (e.g., “POST /images/logo.png HTTP/1.1”). Including both Request and separate Method and URL fields introduces redundancy. If we already extract Method and URL separately for filtering, the full Request field becomes unnecessary.
2. Simplicity in Filtering:  
   Filtering for “POST requests under /images/” from 15:00 to 18:00 on Mondays can be done using:

Time → for checking the hour and weekday.

Method → to filter only POST.

URL → to ensure the request is under /images/.

Thus, Option C (Time, Method, URL, Referer) already includes all needed fields. While Referer is not essential, it doesn’t interfere with the filtering and might be useful in future extended filtering cases (e.g., source tracking). Therefore, Option C is complete and accurate without being redundant.

3. Consistency with Log Parsing Practices:  
   In most log analysis scripts or systems (e.g., Python’s re or pandas parsing of logs), Method and URL are parsed from Request for separate use. This further supports the idea that including Request alongside Method and URL is not best practice.

---

**post_id:** 620472  
**author:** 24f2003130  
**timestamp:** 2025-04-16T18:47:03.645Z

Sir, regarding point 3, score-checker tells a different story. While all the other changes have been made with the same reflecting in the score, that question still says “The question and answer remain the same . No changes required”, which is different from your post.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/4/0/404e7b25f4155d41d4939b07fd45fa3c120beadd_2_690x31.png)  
Here's a description of the image:
The image shows a multiple-choice question from a test. The question asks about counting requests with a 404 status code for pages under /error/. There are four options provided.
image text:
Question Number: 309 Question Id : 6406531231230 Question Type : MCQ
Correct Marks : 1
Question Label: Multiple Choice Question
After filtering the log entries (in a list filtered\_entries), which of the following is the best way to
count the number of requests with a 404 status code for pages under /error/?
Options:
6406534159860. \* Use len (filtered\_entries)
6406534159861. \* Use len(entries)
6406534159862. \* Use sum(1 for entry in entries)
6406534159863. None of these

Can you please look into it?

Thanks  
Regards,  
Shivaditya

---

**post_id:** 620477  
**author:** 22f3000819  
**timestamp:** 2025-04-16T19:04:11.803Z

[@iamprasna](/u/iamprasna) sir , the scores have been updated on the dashboard as well and the answer for the question in point 3 is still the same

Additionally , sir I have attached the snapshot of a dec’24 TDS PYQ which is a replica of this question and the answer for the same is mention the first option.

image description: The image is a multiple-choice question. The question is about counting successful GET requests after filtering log entries. The correct answer is indicated with a green checkmark.
image text: Question Number: 351 Question Id: 6406531040283 Question Type: MCQ
Correct Marks: 1
Question Label: Multiple Choice Question
After filtering the log entries (in a list
filtered\_entries), which of the following
is the best way to count the number of successful
GET requests for pages under /telugump3/?
Options:
6406533514340. Use len (filtered\_entries)
6406533514341. Use len (entries)
6406533514342. Use sum (1 for entry in entries)
6406533514343. Use count(filtered\_entries)

The link for the same has been attached for your referance

[drive.google.com](https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk)

### [IIT M FOUNDATION DIPLOMA FN EXAM QDF2 22 Dec 2024.pdf](https://drive.google.com/file/d/13RkOKhfalx4uVu7gqFYUncvJ9_-lYMMX/view?usp=drivesdk)

Google Drive file.

---

**post_id:** 620539  
**author:** 24f2003130  
**timestamp:** 2025-04-17T04:17:09.060Z

That’s a great find. They’re the same question with just different parameters. Please look into it [@iamprasna](/u/iamprasna) sir.

---

**post_id:** 620540  
**author:** swatikap  
**timestamp:** 2025-04-17T04:20:13.544Z

[@carlton](/u/carlton) sir and [@Jivraj](/u/jivraj) sir please look into this question and clarify this

Thank you

---

**post_id:** 620544  
**author:** 24f2003130  
**timestamp:** 2025-04-17T04:22:31.946Z

Hi,  
From where are you checking the transcripts? I’m not able to see the answer transcripts in the score checker app.  
image description: This is a screenshot of a score checker interface. It displays a table with the following columns: Email, Hallticket, Course Code, Total Score, and View. The information presented is about the scores of the user. There is also a message at the top saying "This is before the sign-off of scores; it may change after the sign-off.". The header also contains navigation links like Transcript, Home, and Logout.
image text: SCORE CHECKER EMAIL 23ds3000185@ds.study.iitm.ac.in This is before the sign-off of scores; it may change after the sign-off. HALLTICKET S2DAD23DS3000185 Transcript Home ➡ Logout COURSE CODE SE2002 TOTAL SCORE 70 VIEW

---

**post_id:** 620546  
**author:** swatikap  
**timestamp:** 2025-04-17T04:25:22.034Z

Click on the eye button …then you will be able to view your transcript

---

**post_id:** 620547  
**author:** 24f2003130  
**timestamp:** 2025-04-17T04:28:25.475Z

Thanks for the reply, but I only see the question id’s and answer id’s, not able to find the transcripts.  
This is a table of results from a score checker. The table shows the question number, type, result, score, selected option, correct option, mark, modification of the question and remarks. The fourth row is highlighted and indicates that option 3 and option 2 must be awarded with marks.
image text: SCORE CHECKER
S.NO. Question ID Question Type Result Score Selected Option Correct Option Mark Modification of Question Remarks
1 6406531252398 MCQ C 0 6406534219005 6406534219005 0 Not Modified -
2 6406531252407 MCQ W 0 6406534219039 6406534219040 1.00 Not Modified -
3 6406531252404 MCQ C 1.00 6406534219029 6406534219029 1.00 Not Modified -
4 6406531252403 MCQ C 1.00 6406534219025 6406534219024 1.00 6406531252403 Option 3 and option 2 must be awarded with marks
5 6406531252408 MCQ C 1.00 6406534219044 6406534219044 1.00 Not Modified -
6 6406531252406 MCQ C 1.00 6406534219036 6406534219036 1.00 Not Modified -
7 6406531252409 MCQ C 1.00 6406534219049 6406534219049 1.00 Not Modified -
8 6406531252399 MCQ C 1.00 6406534219008 6406534219008 1.00 Not Modified -
9 6406531252402 MCQ W 0 6406534219019 6406534219020 1.00 Not Modified Remains the same
10 6406531252410 MCQ W 0 6406534219053 6406534219052 1.00 Not Modified -
11 6406531252401 MCQ W 0 6406534219017 6406534219015 1.00 Not Modified -

---

**post_id:** 621044  
**author:** 22f3000819  
**timestamp:** 2025-04-17T18:05:30.227Z

It seems that the option to download the answer key has been removed. However, you could consider reaching out to someone in the group or checking the dashboard for solution pdf of question paper. You can then match the questions in order, even if the IDs don’t align exactly—it should still give you a general idea. From there, you can proceed accordingly.

---

**post_id:** 621914  
**author:** iamprasna  
**timestamp:** 2025-04-21T10:46:35.817Z

[@iamprasna](/u/iamprasna) [@carlton](/u/carlton) Please look into it once. According to point 3 of [@iamprasna](/u/iamprasna)’s post, I should get full credit for that question and it will take me to a perfect 100 score in ET from the current 97. I brought this into attention before the scores were pushed to the dashboard.

Regards,  
Shivaditya

---

**post_id:** 621957  
**author:** 24f2003130  
**timestamp:** 2025-04-21T13:51:30.076Z

The correction has been done to the following question for both the FN and AN sessions. You must be able to see the change in scores shortly

1. **Entries with 404 status code**  
   Although the instructions did not explicitly state that filters applied for status code 404, we acknowledge this ambiguity. Full credit will be awarded for both option 1 and option 4.

---

