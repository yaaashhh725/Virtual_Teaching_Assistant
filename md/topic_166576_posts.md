# ga5-data-preparation-discussion-thread-tds-jan-2025

**post_id:** 592179  
**author:** s.anand  
**timestamp:** 2025-02-08T14:39:41.571Z

# ga5-data-preparation-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 5 - Data Preparation](https://exam.sanand.workers.dev/tds-2025-01-ga5).

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline: 2025-02-15T18:30:00Z

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini) [@carlton](/u/carlton)

---

**post_id:** 592180  
**author:** s.anand  
**timestamp:** 2025-02-08T14:40:01.609Z

---

**post_id:** 593372  
**author:** 23f1002630  
**timestamp:** 2025-02-10T06:17:22.155Z

image description: The image is a screenshot of a webpage, likely related to an online assessment or learning platform. The layout consists of a dark gray background with several colored boxes displaying information.
image text: You are logged in as 23f1002630@ds.study.iitm.ac.in. Logout Recent saves (most recent is your official score) No recent saves C Loading questions... Error! Sorry, we couldn't load the questions. That's strange. Cannot read properties of undefined (reading '1') Please contact the exam team for assistance.
  
i can’t load my questions

---

**post_id:** 593409  
**author:** s.anand  
**timestamp:** 2025-02-10T07:29:12.849Z

[@23f1002630](/u/23f1002630) - thanks for raising this. It’s fixed and won’t re-occur for anyone.

**What happened?** I picked random duration from the video of 10-40 seconds, but forgot to ensure that the end time should not exceed the video length. That’s what I fixed.

---

**post_id:** 593506  
**author:** 23f1002630  
**timestamp:** 2025-02-10T11:25:56.044Z

Here's a description of the image:
The image is a screenshot of a webpage or application interface. It has a dark background and features several rectangular boxes of different colors.
\* \*\*Top Box:\*\* Green box that displays "Recent saves (most recent is your official score)" and "No recent saves".
\* \*\*Middle Box:\*\* Blue box displaying a loading indicator and the text "Loading questions...".
\* \*\*Bottom Box:\*\* Red box displaying "Error!" and a detailed error message explaining that the questions could not be loaded and giving more information about the error. It also prompts the user to contact the exam team for assistance.
\* \*\*Buttons:\*\* At the bottom of the screen, there are two buttons: "Check all" (green) and "Save" (blue).
image text: Recent saves (most recent is your official score)
No recent saves
Loading questions...
Error!
Sorry, we couldn't load the questions. That's strange.
Cannot read properties of undefined (reading '1')
Please contact the exam team for assistance.
Check all Save  
It was solved but again I’m facing the same issue

---

**post_id:** 593671  
**author:** 23f1002630  
**timestamp:** 2025-02-10T18:54:19.804Z

[@s.anand](/u/s.anand) [@Jivraj](/u/jivraj) I’m still facing the issue.

---

**post_id:** 593896  
**author:** nilaychugh  
**timestamp:** 2025-02-11T16:21:34.546Z

i guess there’s some issue in 5th question as i have correctly filtered the data in OpenRefine 2-3 times but still getting incorrect in the portal.

---

**post_id:** 594108  
**author:** carlton  
**timestamp:** 2025-02-12T12:52:01.867Z

OpenRefine question has historically been a tricky question to get right. Check out some past TA sessions in previous term for solving it, or previous discourse posts.

Kind regards

---

**post_id:** 594381  
**author:** 22f3001315  
**timestamp:** 2025-02-13T08:51:51.360Z

DOUBT IN -Q 9 Sir [@carlton](/u/carlton)

```
Miranda followed the elusive figure.  In the dim corridor,......................

```

I listened it ,every words and spellings are matching still this error:

**Error: Words are too different**

---

**post_id:** 594585  
**author:** Nelson  
**timestamp:** 2025-02-13T13:56:56.738Z

## Cleaning Data with OpenRefine

Kindly check the question and the answer. I found below cities for São Paulo.

However, it says my answer is incorrect.

> How many units of Bacon were sold in São Paulo on transactions with at least 151 units?

```
city
Sao Paolo
Sao Paoulo
Sao Paulo
Sao Pualo
Sau Paulo
São Paulo

```

image description: The image shows a table from a spreadsheet, likely Microsoft Excel or a similar program. The table has three columns labeled "city", "product", and "sales". The "city" column lists the name "Sau Paulo" repeatedly. The "product" column lists "Bacon" for all rows. The "sales" column contains numerical values. A row is highlighted to show the total sales for the product "Bacon" for "Sau Paulo" which amounts to 2871. The filters are shown on top of the column names.
image text:
A
B
C
1 city product sales
249 Sau Paulo Bacon 488
1125 Sao Pualo Bacon 522
1448 Sao Paoulo Bacon 650
1930 Sao Paolo Bacon 275
2278 Sao Pualo Bacon 936
2502 2871

---

**post_id:** 595055  
**author:** 23f1003186  
**timestamp:** 2025-02-14T16:15:42.519Z

Wrong / Confusing question Prof

The top line mentions “Saturdays” whereas the bottom line mentions “Sundays”

Please clarify “SUNDAY” or “SATURDAY”?

image description: The image is a document that details a data analysis task focused on website traffic analysis for a website called s-anand.net. The primary goal is to determine the number of successful GET requests for the "telugu" section of the website during specific timeframes on Saturdays. The document outlines the context, the author's intent, the data source, the task requirements, and the data fields available for analysis.
image text: Peak Usage Analysis for Regional Content
s-anand.net is a personal website that had region-specific music content. One of the site's key sections is telugu, which hosts music files and is especially popular among
the local audience. The website is powered by robust Apache web servers that record detailed access logs. These logs are essential for understanding user behavior, server
load, and content engagement.
The author noticed unusual traffic patterns during weekend evenings. To better tailor their content and optimize server resources, they need to know precisely how many
successful requests are made to the telugu section during peak hours on Saturdays. Specifically, they are interested in:
• Time Window: From 13 until before 23.
• Request Type: Only GET requests.
• Success Criteria: Requests that return HTTP status codes between 200 and 299.
• Data Source: The logs for May 2024 stored in a GZipped Apache log file containing 258,074 rows.
The challenge is further complicated by the nature of the log file:
• The logs are recorded in the GMT-0500 timezone.
• The file format is non-standard in that fields are separated by spaces, with most fields quoted by double quotes, except the Time field.
• Some lines have minor formatting issues (41 rows have unique quoting due to how quotes are escaped).
Your Task
As a data analyst, you are tasked with determining how many successful GET requests for pages under telugu were made on Saturdays between 13 and 23 during May
2024. This metric will help:
• Scale Resources: Ensure that servers can handle the peak load during these critical hours.
• Content Planning: Determine the popularity of regional content to decide on future content investments.
• Marketing Insights: Tailor promotional strategies for peak usage times.
This GZipped Apache log file (61MB) has 258,074 rows. Each row is an Apache web log entry for the site s-anand.net in May 2024.
Each row has these fields:
• IP: The IP address of the visitor
• Remote logname: The remote logname of the visitor. Typically "-"
• Remote user: The remote user of the visitor. Typically "-"
• Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
• Request: The request made by the visitor. E.g. GET/blog/HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL
visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
• Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
• Size: The size of the response in bytes. E.g. 1234
• Referer: The referer URL. E.g. https://s-anand.net/
• User agent: The browser used. This will contain spaces and might have escaped quotes.
• Vhost: The virtual host. E.g. s-anand.net
• Server: The IP address of the server.
The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)
All data is in the GMT-0500 timezone and the questions are based in this same timezone.
By determining the number of successful GET requests under the defined conditions, we'll be able to:
• Optimize Infrastructure: Scale server resources effectively during peak traffic times, reducing downtime and improving user experience.
• Strategize Content Delivery: Identify popular content segments and adjust digital content strategies to better serve the audience.
• Improve Marketing Efforts: Focus marketing initiatives on peak usage windows to maximize engagement and conversion.
What is the number of successful GET requests for pages under /telugu/from 13:00 until before 23:00 on Sundays?

---

**post_id:** 595057  
**author:** 23f1003186  
**timestamp:** 2025-02-14T16:19:36.462Z

Update: I tried for both (thank god for filters in Excel) and Sunday is what the question is asking for. The Instruction above for “Saturday” is incorrect- maybe the logic generating different questions for different students can be tweaked-

Thank you

---

**post_id:** 595100  
**author:** 23f1003186  
**timestamp:** 2025-02-14T17:47:55.912Z

I’ve attempted this question several times and I’m fairly certain that the answer to this question is incorrect. I’d be grateful if the answer to this question was re-checked. I can share the answer I’m certain about here, however I do not think it would be prudent to do so given this is a public forum.

Please consider my request and double check-

[@Jivraj](/u/jivraj), [@carlton](/u/carlton)

Thank you

image description: The image is a case study description about recovering sales data for ReceiptRevive Analytics. It details the issues with processing legacy sales data, the client RetailFlow Inc., and the task of the data recovery analyst to develop a program to parse sales data, validate and cleanup data, and calculate total sales. It also lists the benefits of successful data recovery and provides a link to download the data.
image text: Case Study: Recovering Sales Data for ReceiptRevive Analytics
ReceiptRevive Analytics is a data recovery and business intelligence firm specializing in processing legacy sales data from paper receipts. Many of the client companies have archives of receipts from past years, which have been digitized using OCR (Optical Character Recognition) techniques. However, due to the condition of some receipts (e.g., torn, faded, or partially damaged), the OCR process sometimes produces incomplete JSON data. These imperfections can lead to truncated fields or missing values, which complicates the process of data aggregation and analysis.
One of ReceiptRevive's major clients, RetailFlow Inc., operates numerous brick-and-mortar stores and has an extensive archive of old receipts. RetailFlow Inc. needs to recover total sales information from a subset of these digitized receipts to analyze historical sales performance. The provided JSON data contains 100 rows, with each row representing a sales entry. Each entry is expected to include four keys:
• city: The city where the sale was made.
• product: The product that was sold.
• sales: The number of units sold (or sales revenue).
• id: A unique identifier for the receipt.
Due to damage to some receipts during the digitization process, the JSON entries are truncated at the end, and the id field is missing. Despite this, RetailFlow Inc. is primarily interested in the aggregate sales value.
Your Task
As a data recovery analyst at ReceiptRevive Analytics, your task is to develop a program that will:
1. Parse the Sales Data:
Read the provided JSON file containing 100 rows of sales data. Despite the truncated data (specifically the missing id), you must accurately extract the sales figures from each row.
2. Data Validation and Cleanup:
Ensure that the data is properly handled even if some fields are incomplete. Since the id is missing for some entries, your focus will be solely on the sales values.
3. Calculate Total Sales:
Sum the sales values across all 100 rows to provide a single aggregate figure that represents the total sales recorded.
By successfully recovering and aggregating the sales data, ReceiptRevive Analytics will enable RetailFlow Inc. to:
• Reconstruct Historical Sales Data: Gain insights into past sales performance even when original receipts are damaged.
• Inform Business Decisions: Use the recovered data to understand sales trends, adjust inventory, and plan future promotions.
• Enhance Data Recovery Processes: Improve methods for handling imperfect OCR data, reducing future data loss and increasing data accuracy.
• Build Client Trust: Demonstrate the ability to extract valuable insights from challenging datasets, thereby reinforcing client confidence in ReceiptRevive's services.
Download the data from q-parse-partial-json.jsonl

---

**post_id:** 595527  
**author:** 23f2003717  
**timestamp:** 2025-02-15T16:24:23.831Z

Here's a description of the image:
The image shows a table of data, likely from a spreadsheet program. The table contains data about sales information. The table headers are: "Country (Normalised)", "DATE", "Product", "Sales", and "Cost". The data includes dates, product names (all "Kappa"), sales figures, and associated costs. The "Country (Normalised)" column lists "United Arab Emirates" for all entries.
image text:
Country (Normalised) DATE Product Sales Cost
United Arab Emirates 2023-07-02 Kappa 1314.00 4892.00
United Arab Emirates 03-15-2023 Kappa 4853.00 1589.00
United Arab Emirates 2023-04-02 Kappa 8676.00 3877.00
United Arab Emirates 06-29-2022 Kappa 9370.00 2214.00
United Arab Emirates 2023-02-04 Kappa 5488.00 2744.00
United Arab Emirates 2023-07-13 Kappa 2433.00 773.00
United Arab Emirates 2023-10-18 Kappa 8974.00 4668.00
United Arab Emirates 03-28-2023 Kappa 2107.00 1358.00
United Arab Emirates 03-22-2023 Kappa 3709.00 4661.00
United Arab Emirates 11-17-2023 Kappa 4646.00 2323.00
United Arab Emirates 2023-10-13 Kappa 6021.00 2223.00
United Arab Emirates 2023-04-06 Kappa 2331.00 3795.00
United Arab Emirates 2022-10-11 Kappa 6307.00 287.00
United Arab Emirates 2023-05-29 Kappa 8272.00 3516.00
United Arab Emirates 2022-06-04 Kappa 7810.00 4755.00
United Arab Emirates 2023-01-15 Kappa 2029.00 4891.00
United Arab Emirates 2023-04-28 Kappa 6254.00 3127.00
  
this is my data before date filter - for question 1 please conform am i doing correct. and tell how to do the date filtering as some are in mm-dd-yyyy or yyyy-mm-dd format.

as this data is less i did it manually

| SUM OF COST | 14891.00 |
|

---

**post_id:** 595540  
**author:** s.anand  
**timestamp:** 2025-02-15T16:45:07.123Z

|

---

**post_id:** 595564  
**author:** 23f1003186  
**timestamp:** 2025-02-15T17:05:24.887Z

|
| SUM OF SALES | 31004.00 |
| TOTAL | 45895.00 |
| TOTAL MARGIN | 0.351083996 |

but this is not correct please guide

---

**post_id:** 595571  
**author:** s.anand  
**timestamp:** 2025-02-15T17:13:23.480Z

[@23f1003186](/u/23f1003186) – thanks for flagging this. You’re right. I’ve fixed this error. ![:pray:](https://emoji.discourse-cdn.com/google/pray.png?v=12 ":pray:")

---

**post_id:** 595576  
**author:** 23f2003717  
**timestamp:** 2025-02-15T17:19:27.591Z

Any signal for this question?

[@s.anand](/u/s.anand) [@carlton](/u/carlton)

---

**post_id:** 595702  
**author:** 23f2004752  
**timestamp:** 2025-02-15T23:22:12.712Z

[@23f1003186](/u/23f1003186) thanks again for flagging this. This is fixed, too. ![:pray:](https://emoji.discourse-cdn.com/google/pray.png?v=12 ":pray:")

---

**post_id:** 595747  
**author:** 23f2003717  
**timestamp:** 2025-02-16T04:42:44.483Z

tried google sheets - it autoformatted my date data, also i realized later i was applying the formula the wrong way.

Here's a description of the image:
The image presents a table with data related to sales, organized by country and date. The table includes columns for "Country (Normalised)", "DATE", "Product", "Sales", and "Cost". The data displayed pertains to the United Arab Emirates, with specific dates, a product named "Kappa", and corresponding sales and cost figures.
image text:
Country (Normalised) DATE Product Sales Cost
United Arab Emirates 2023-02-07 Kappa 1314.00 4892.00
United Arab Emirates 2022-06-29 Kappa 9370.00 2214.00
United Arab Emirates 2023-02-04 Kappa 5488.00 2744.00
United Arab Emirates 2022-11-10 Kappa 6307.00 287.00
United Arab Emirates 2022-06-04 Kappa 7810.00 4755.00
United Arab Emirates 2023-01-15 Kappa 2029.00 4891.00
  
Date formatted and filtered successfully

---

**post_id:** 595979  
**author:** 22f3001315  
**timestamp:** 2025-02-16T13:52:28.891Z

Can you provide the link for that session.

---

**post_id:** 595983  
**author:** 22f3001315  
**timestamp:** 2025-02-16T13:56:30.308Z

image description: The image is a table that shows the sales data for computers in London. The table has three columns: city, product, and sales. The city is London. The product is Computer. The sales figures are: 406, 916, 821, 457, 922, 610, 111, 109, 866, and 975.
image text:
\_-\_-city
- product
- sales
London Computer 406
London Computer 916
London Computer 821
London Computer 457
London Computer 922
London Computer 610
London Computer 111
London Computer 109
London Computer 866
London Computer 975

How many units of Computer were sold in London on transactions with at least 39 units?  
please check my answer is not correct - (6193)

please guide

---

**post_id:** 595999  
**author:** 23f2002592  
**timestamp:** 2025-02-16T14:15:04.290Z

How many units of Computer were sold in Shenzhen on transactions with at least 43 units?

| city | product | sales |
|

---

**post_id:** 596142  
**author:** 23f2004752  
**timestamp:** 2025-02-16T17:02:59.166Z

|

---

**post_id:** 596509  
**author:** carlton  
**timestamp:** 2025-02-18T04:21:53.103Z

|

---

**post_id:** 596567  
**author:** 22f3001315  
**timestamp:** 2025-02-18T05:48:36.523Z

|
| Shenzheen | Computer | 296 |
| Shenzhen | Computer | 824 |
| ShenZhen | Computer | 931 |
| Shenzheen | Computer | 976 |
| Shenzheen | Computer | 108 |
| Shenzheen | Computer | 623 |
| Shenzen | Computer | 386 |
| Shenzheen | Computer | 827 |
|  |  | 4971 |

why is this incorrect ? what am i missing ? [@s.anand](/u/s.anand) [@carlton](/u/carlton)

---

**post_id:** 596689  
**author:** ShahbaazSingh  
**timestamp:** 2025-02-18T12:23:57.766Z

This one is matching every word still that error . why sir [@s.anand](/u/s.anand)

---

**post_id:** 596731  
**author:** 23f2004912  
**timestamp:** 2025-02-18T14:06:03.082Z

yes I`m also getting the incorrect answer for question 5 even though I have clustered the city jakarta correctly.  
How many units of Bike were sold in Jakarta on transactions with at least 163 units?

---

**post_id:** 596739  
**author:** lakshaygarg654  
**timestamp:** 2025-02-18T14:44:43.999Z

Same for me . I am also getting error of the answer i am getting from OpenRefine

---

**post_id:** 596942  
**author:** 23f2000098  
**timestamp:** 2025-02-19T09:33:34.904Z

---

**post_id:** 596979  
**author:** 23ds1000022  
**timestamp:** 2025-02-19T08:24:26.521Z

Sir please check Q 5,8,9 also

---

**post_id:** 596975  
**author:** Jivraj  
**timestamp:** 2025-02-19T10:48:39.486Z

[@s.anand](/u/s.anand) [@carlton](/u/carlton) I have tried every method for the 5th question even brute force still I am getting same answer but it is saying incorrect.

---

**post_id:** 596996  
**author:** 23f3001601  
**timestamp:** 2025-02-19T11:07:26.313Z

[@carlton](/u/carlton) i am also not able to do que 5th question …  
Any hint

---

**post_id:** 597009  
**author:** 23ds1000022  
**timestamp:** 2025-02-19T11:30:59.015Z

Respected [@carlton](/u/carlton)  
I am facing an issue with GA5 Q5, as my answer is being marked incorrect despite multiple attempts. I have processed data at OpenRefine .  
To ensure accuracy, I also tried a manual approach by converting the JSON file to Excel and filtering the data, but I arrived at the same answer each time. However, the assignment portal still shows it as incorrect.  
Sir Could you please check portal expected answer for this question.  
Thankyou

---

**post_id:** 597106  
**author:** 22f2000113  
**timestamp:** 2025-02-19T13:59:18.136Z

[@carlton](/u/carlton) Respected sir,  
I have tried the 5 th question n no. of times but getting error as incorrect answer can i get any guidance on this please. Thankyou

---

**post_id:** 597114  
**author:** Udipth  
**timestamp:** 2025-02-19T14:23:22.401Z

[@jivraj](/u/jivraj) , [@carlton](/u/carlton), [@s.anand](/u/s.anand)  
q5 give same answer which i am getting is incorrect. but i tried manually, python and openrefine, excel everything gives the same answer. please look into it.

---

**post_id:** 597131  
**author:** nilaychugh  
**timestamp:** 2025-02-19T15:45:17.806Z

We have noted this issue and are looking into it.

---

**post_id:** 597134  
**author:** Saransh_Saini  
**timestamp:** 2025-02-19T15:56:24.710Z

In Question 8  
I am getting this error  
Please tell me how do i tackle this errror  
Error: At root: Array length mismatch

---

**post_id:** 597161  
**author:** Algsoch  
**timestamp:** 2025-02-19T16:56:47.689Z

thanku sir also q6 i got 52747 after cleaning the json and trying to extract using all methods 96 lines where reconstructed. but portal keep saying wrong for evry answer.pls check on this also

---

**post_id:** 597165  
**author:** Udipth  
**timestamp:** 2025-02-19T17:11:49.323Z

Q5 I tried with openfire and python script , both are giving me same answer but its not accepted please check . Also in task the ask is to identify " **Top-Performing City:** Determine which city has the highest total unit sales for the selected product and report the unit sales number." but on top of input box question is different “How many units of Table were sold in Mexico City on transactions with at least 159 units?”

---

**post_id:** 597169  
**author:** Saransh_Saini  
**timestamp:** 2025-02-19T17:23:55.406Z

i think there is some bug in Q 1… it shows correct if in percentage I pass comma instead of decimal. kindly check. secondly by multiple logics i checked q 5 & Q 6… but it shows incorrect only. Kindly help

---

**post_id:** 597175  
**author:** lakshaygarg654  
**timestamp:** 2025-02-19T17:35:57.454Z

can we get more specified error in q9? it just says, words are too different.

---

**post_id:** 597221  
**author:** carlton  
**timestamp:** 2025-02-20T03:21:58.527Z

# This message is for everyone struggling with Q5

Due to a backend error, the script was incorrectly evaluating your answers. That problem has been fixed and you must check once again.  
If you are still getting it incorrect, better watch [Open Refine - Live Session](https://drive.google.com/file/d/1iTygvMAQdNY9O09An0LZMyt2sFZufcLl/view?usp=sharing&t=4431)

---

**post_id:** 597225  
**author:** carlton  
**timestamp:** 2025-02-20T03:31:24.326Z

hellor sir my answer is 4764 after so many verification like excel python open refine etc but still it was saying it is wrong sir check answer please question no 4 related to 1. **Aggregate Sales by City:** After clustering city names, group the filtered sales entries by city and calculate the total units sold for each city.  
2. **Identify the Top-Performing City:** Determine which city has the highest total unit sales for the selected product and report the unit sales number.

By performing this analysis, GlobalRetail Insights will be able to:

* **Improve Data Accuracy:** Correct mis-spellings and inconsistencies in the dataset, leading to more reliable insights.
* **Target Marketing Efforts:** Identify high-performing regions for the specific product, enabling targeted promotional strategies.
* **Optimize Inventory Management:** Ensure that inventory allocations reflect the true demand in each region, reducing wastage and stockouts.
* **Drive Strategic Decision-Making:** Provide actionable intelligence to clients that supports strategic planning and competitive advantage in the market.

How many units of Bacon were sold in Beijing on transactions with at least 28 units?

---

**post_id:** 597255  
**author:** daksh76  
**timestamp:** 2025-02-20T05:33:29.345Z

Here's a brief description of the image:
The image is a screenshot of a web page related to API keys. It displays a "Get API key" page within the Google AI Studio interface. The page provides information on testing the Gemini API and includes a code snippet for testing. There is also a section displaying the user's API keys. There is also an error message.
image text:
aistudio.google.com/app/u/2/apikey?pli=1
I Studio
Get API key
ey
rompt
API keys
Quickly test the Gemini API
ealtime
API quickstart guide
pps
odel
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?ke
-H 'Content-Type: application/json' \
-X POST \
-d '{
e chat history
"contents": [{
Gallery
"parts":[{"text": "Explain how AI works"}]
}]
}'
mentation
er forum
Use code with caution.
og NEW
Create API key
Your API keys are listed below. You can also view and manage your project and API keys in Google Cloud.
Project number
Project name
API key
Created
APPLICATION\_ERROR;google.cloud.resourcemanager.v3/ProjectsV3.CreateProject;com.google.apps.
Resource Manager project creation is disabled. Contact your administrator to enable this setting in th
information.;AppErrorCode=9;StartTimeMs=1739985063200;unknown;ResFormat=uncompressed
[2002:a05:6a04:459d:b0:271:d3d1:83e3]:4004
Remember to use API keys securely. Don't share or embed them in public code. Use of Gemini API from a billing-
  
I am getting this error when trying to generate API key… Who I need to connect to allow me generate a key on my iitm email id

---

**post_id:** 597259  
**author:** carlton  
**timestamp:** 2025-02-20T05:41:41.335Z

Hi [@Algsoch](/u/algsoch)  
I have checked your dataset along with your params, and its perfectly correct. Try again and check your step.  
Otherwise go and watch 18-Feb Live Session

---

**post_id:** 597263  
**author:** lakshaygarg654  
**timestamp:** 2025-02-20T06:00:14.975Z

[@Saransh\_Saini](/u/saransh_saini)  
Q5 fixed, thanks for fixing the issue.

Now we are struggling with Q8.  
MY q8 is : Write a DuckDB SQL query to find all posts IDs after 2025-01-09T12:36:14.085Z with at least 1 comment with 4 useful stars, sorted. The result should be a table with a single column called `post_id` , and the relevant post IDs should be sorted in ascending order.  
when i use below query, i get some some result, a table of post\_id but error : **Error**: At root: Array length mismatch  
**Reason**: below query checking only 1st comment (`$[0]` refers to the first comment in the array) we have to check all comments not 1st.  
But when i change the query to check any one comment its giving different types of error.

```
WITH filtered_posts AS (
  SELECT post_id
  FROM social_media
  WHERE timestamp >= '2025-01-09T09:48:01.303Z'
    AND EXISTS (
      SELECT 1
      FROM social_media AS sm
      WHERE json_extract_path_text(sm.comments, '$[0].stars.useful') IS NOT NULL
        AND CAST(json_extract_path_text(sm.comments, '$[0].stars.useful') AS INTEGER) > 4
    )
)
SELECT post_id
FROM filtered_posts
ORDER BY post_id ASC;

```

Kindly check if any issue with Q8.  
May be my query is wrong or may be not.

Thankyou

---

**post_id:** 597269  
**author:** carlton  
**timestamp:** 2025-02-20T06:18:50.624Z

[@lakshaygarg654](/u/lakshaygarg654)

Your query construction is unnecessarily complicated and therefore will be difficult to debug.

Query construction is best done by thinking what you want at the end.  
In this case its an ordered `post_id`

So thats where you begin:

```
SELECT post_id
FROM (
...
)
ORDER BY post_id

```

Doing this, produces the actual result without giving the logic yet.

Then at each stage you add the next stage of complexity.  
You will still need the `post_id` for the *outermost layer* so you have to continue extracting it from the *inner layers* of the nested query.

```
...
...
FROM (
   SELECT post_id, ( ... ) as max_stars
   FROM social_media
   WHERE time_stamp >= (whatever the parameter you have been given)
      AND max_stars >= (whatever the parameter for min stars you have been given)
)
...
...

```

Then the final layer of the nest

```
...
...
(

) as max_stars
...
...

```

You are not expecting me to solve the whole question right? (Hint: the inner most extraction involves JSON or “structure” extraction, which is a powerful capability)

But I hope you understand the logic of SQL which is a very elegant set theory language which is why it has lasted for over 4 decades.

Think clearly at each stage what do you need. Start with the answer and work backwards, extracting at each stage the logical items you require for the outer layer to be functional.

Kind regards

---

**post_id:** 597270  
**author:** carlton  
**timestamp:** 2025-02-20T06:20:14.458Z

Its been done. You will get a more detailed error now. And we have relaxed the number of errors allowed (it actually did have a tolerance limit but it was fairly tight)

---

**post_id:** 597271  
**author:** lakshaygarg654  
**timestamp:** 2025-02-20T06:22:37.305Z

sir even after applying this logic im getting error at root: array length mismatch

---

**post_id:** 597357  
**author:** 23ds2000092  
**timestamp:** 2025-02-20T10:09:25.727Z

[@daksh76](/u/daksh76) thats because your innermost logic layer must not return a long list of results.

If you think about it logically each row cannot have a column field where one of the columns is a whole row of results right?

Thats why you are getting the error.

Check your innermost layer is returning a single value or a row of results.

Kind regards

---

**post_id:** 597379  
**author:** carlton  
**timestamp:** 2025-02-20T11:33:15.878Z

Thank you for your response [@carlton](/u/carlton). You are absolutely right—my query was unnecessarily complex. Initially, I attempted a simpler approach, using various JSON extraction functions. However, I encountered multiple errors, including:

1. **`json_extract`**: *“Table Function with name ‘json\_extract’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
2. **`json_each`**: *“Table Function with name ‘json\_each’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*
3. **`json_extract_path_text`**: *“Table Function with name ‘json\_extract\_path\_text’ is not in the catalog. A function by this name exists in the JSON extension but is of a different type, namely Scalar Function.”*

Since the simple approach did not work, I attempted a more complex query to achieve the desired result. However, that too did not yield the expected output. To gain better insight, I extracted ten values into a table using the console and then reconstructed the query accordingly. Unfortunately, I am still facing issues related to functions not being recognized in the catalog.  
I would appreciate any guidance on resolving this issue. I do not need the exact answer; I just want to know if there is any issue with the portal for **Q8**.

Thankyou

---

**post_id:** 597381  
**author:** 23ds2000092  
**timestamp:** 2025-02-20T11:39:57.548Z

[@lakshaygarg654](/u/lakshaygarg654)

This might help ![:wink:](https://emoji.discourse-cdn.com/google/wink.png?v=12 ":wink:")

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/b/dbed28f087dded14082a3554f8ca07d4b80dc25b.png)
[DuckDB](https://duckdb.org/docs/sql/query_syntax/unnest.html)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/f/9feb8d9eda659046c7b46bc317f582e1cf29fb2b_2_690x362.jpeg)

### [Unnesting](https://duckdb.org/docs/sql/query_syntax/unnest.html)

Examples Unnest a list, generating 3 rows (1, 2, 3): SELECT unnest([1, 2, 3]); Unnesting a struct, generating two columns (a, b): SELECT unnest({'a': 42, 'b': 84}); Recursive unnest of a list of structs: SELECT unnest([{'a': 42, 'b': 84}, {'a': 100,...

Kind regards

---

**post_id:** 597382  
**author:** 23f2004313  
**timestamp:** 2025-02-20T11:20:14.335Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/lakshaygarg654/48/129814_2.png) lakshaygarg654:

> I just want to know if there is any issue with the portal for **Q8**.

Nope no issues with portal for Q8

---

**post_id:** 597380  
**author:** carlton  
**timestamp:** 2025-02-20T11:39:56.594Z

Thanks [@carlton](/u/carlton)  
I found the correct query.

---

**post_id:** 597387  
**author:** 23f2004313  
**timestamp:** 2025-02-20T11:43:19.595Z

I am still getting the answer as incorrect, though the answer for my dataset : 1187 (951+236) is correct. Would you be able to check again please?

---

**post_id:** 597394  
**author:** carlton  
**timestamp:** 2025-02-20T11:54:05.994Z

[@23ds2000092](/u/23ds2000092)  
Can you just logout and login and reload your GA? (maybe clear cookies and cache) Because I get the correct answer for your GA.

Kind regards

---

**post_id:** 597430  
**author:** 24f2003130  
**timestamp:** 2025-02-20T13:35:18.214Z

Done. it works now. thanks!

---

**post_id:** 597455  
**author:** Jayeshbansal  
**timestamp:** 2025-02-20T14:48:33.358Z

image description: The image is a document providing instructions for improving sales data accuracy for RetailWise Inc. It describes the context, challenges, and specific tasks needed to clean and analyze sales data from an Excel file.
image text: Improving Sales Data Accuracy for RetailWise Inc.
RetailWise Inc. is a retail analytics firm that supports companies in optimizing their pricing, margins, and inventory decisions. Their reports depend on accurate historical sales data, but legacy data sources are often messy. Recently, RetailWise received an Excel sheet containing 1,000 transaction records that were generated from scanned receipts. Due to OCR inconsistencies and legacy formatting issues, the data in the Excel sheet is not clean.
The Excel file has these columns, and they are messy:
• Customer Name: Contains leading/trailing spaces.
• Country: Uses inconsistent representations. Instead of 2-letter abbreviations, it also contains other values like "USA" vs. "US", "UK" vs. "U.K", "Fra" for France, "Bra" for Brazil, "Ind" for India.
• Date: Uses mixed formats like "MM-DD-YYYY", "YYYY/MM/DD", etc.
• Product: Includes a product name followed by a slash and a random code (e.g., "Theta/5x01vd"). Only the product name part (before the slash) is relevant.
• Sales and Cost: Contain extra spaces and the currency string ("USD"). In some rows, the Cost field is missing. When the cost is missing, it should be treated as 50% of the Sales value.
• TransactionID: Though formatted as four-digit numbers, this field may have inconsistent spacing.
Your Task
You need to clean this Excel data and calculate the total margin for all transactions that satisfy the following criteria:
• Time Filter: Sales that occurred up to and including a specified date (Tue Jun 14 2022 04:52:52 GMT+0530 (India Standard Time)).
• Product Filter: Transactions for a specific product (Theta). (Use only the product name before the slash.)
• Country Filter: Transactions from a specific country (US), after standardizing the country names.
The total margin is defined as:
Total Margin = (Total Sales - Total Cost) / Total Sales
Your solution should address the following challenges:
1. Trim and Normalize Strings: Remove extra spaces from the Customer Name and Country fields. Map inconsistent country names (e.g., "USA", "U.S.A", "US") to a standardized format.
2. Standardize Date Formats: Detect and convert dates from "MM-DD-YYYY" and "YYYY/MM/DD" into a consistent date format (e.g., ISO 8601).
3. Extract the Product Name: From the Product field, extract the portion before the slash (e.g., extract "Theta" from "Theta/5x01vd").
4. Clean and Convert Sales and Cost: Remove the "USD" text and extra spaces from the Sales and Cost fields. Convert these fields to numerical values. Handle missing Cost values appropriately (50% of Sales).
5. Filter the Data: Include only transactions up to and including Tue Jun 14 2022 04:52:52 GMT+0530 (India Standard Time), matching product Theta, and country US.
6. Calculate the Margin: Sum the Sales and Cost for the filtered transactions. Compute the overall margin using the formula provided.
By cleaning the data and calculating accurate margins, RetailWise Inc. can:
• Improve Decision Making: Provide clients with reliable margin analyses to optimize pricing and inventory.
• Enhance Reporting: Ensure historical data is consistent and accurate, boosting stakeholder confidence.
• Streamline Operations: Reduce the manual effort needed to clean data from legacy sources.
Download the Sales Excel file: q-clean-up-excel-sales-data.xlsx
What is the total margin for transactions before Tue Jun 14 2022 04:52:52 GMT+0530 (India Standard Time) for Theta sold in US (which may be spelt in different ways)?
0.0
Error: Incorrect answer
You can enter the margin as a percentage (e.g. 12.34%) or a decimal (e.g. 0.1234).
  
In this question, I am asked to find the total margin for transactions before **Tue, Jun 14, 2022, 04:52:52 GMT+0530 (India Standard Time)** for **Theta** sold in **the US** (which may be spelled in different ways).

However, when I filter in Excel for **US** and **Theta**, there are no entries for **Sales** and **Cost**. But **0** as the answer is not accepted—it says the answer is incorrect.

(I cross-checked this using GPT.)

---

**post_id:** 597462  
**author:** Algsoch  
**timestamp:** 2025-02-20T15:09:11.708Z

[@23f2004313](/u/23f2004313)

US is also called

United States  
United States of America  
USA

These are all valid references to US

Kind regards

---

**post_id:** 597465  
**author:** Algsoch  
**timestamp:** 2025-02-20T15:11:02.705Z

I have replaced all the different names of US (all ) as “US” .  
also sorted the dates as asked in the question .

---

**post_id:** 597466  
**author:** Algsoch  
**timestamp:** 2025-02-20T15:15:04.145Z

I have checked your GA and I do get sales entries for the criteria in your GA.  
Please remember that this module is about data cleaning. And that data needs to be sanitised before you start filtering.

Kind regards

---

**post_id:** 597521  
**author:** 23f2003413  
**timestamp:** 2025-02-20T16:51:25.392Z

[@carlton](/u/carlton) Sir , I have tried reconstructing the image in ques 10 multiple times and even still the output shows error: image pixels do not match…how can I fix this?  
Here's a description of the image:
This image showcases a futuristic cityscape at night. Tall, sleek skyscrapers with neon lights dominate the scene. Flying vehicles are visible in the sky, and roadways with light trails crisscross the city. The overall atmosphere is vibrant, with a color palette of blues, purples, and pinks.
image text: None

Edit: I got it correct

---

**post_id:** 597544  
**author:** 24f2003130  
**timestamp:** 2025-02-20T17:24:10.305Z

i am also facing the same problem and i have cross verified the pixels but it is still showing the same

---

**post_id:** 597549  
**author:** Jivraj  
**timestamp:** 2025-02-20T17:33:18.129Z

Now my answer is same and correct i think problem was in TDS matching question like it was matched to other number now programmer correct it and matched to correct value like 4764

---

**post_id:** 597558  
**author:** Jayeshbansal  
**timestamp:** 2025-02-20T17:58:51.598Z

image description: The image is a collage composed of various interconnected elements, presented in a sepia color scheme. The collage features several stylized portraits of individuals, alongside diagrams, gears, and textual elements. The individual portraits are interspersed throughout the composition. The diagrams and gears appear to be symbolic, perhaps representing concepts of design or engineering. The text elements are scattered throughout, adding further context to the image.
image text: UTY WOLA
Энка по ипиентите ми
שונונות 101
АПОСТКОМОВНE DELATHINAGO
TBSUN BRECHT ОРОО
BATEKIDOUINO HOFLE EAANING
Rirtutmitt
A SUTICAE
LODOU
MABGE NOR
Ο ετσιτέστη
VIRON CAMO
ZAI
ADOBIM EXEBIONEO
JENGTEBROGRAND  
this is my image i coded corrrect mapped to correct pixel but it was saying pixel do not match what is meaning of it

---

**post_id:** 597701  
**author:** bhashwar_sengupta  
**timestamp:** 2025-02-21T06:16:52.406Z

sorry i found correct answer i was thinking differently

---

**post_id:** 597704  
**author:** 23f2003413  
**timestamp:** 2025-02-21T06:17:43.112Z

can someone share the answer for the 9th question as i am facing some errors

---

**post_id:** 597724  
**author:** 23f3004024  
**timestamp:** 2025-02-21T06:55:36.025Z

Create your gemini api, convert the video into MP4 and then write the Collab code for the question or ask gpt to write it for you…finally run it on google collab

---

**post_id:** 597737  
**author:** 23f3004114  
**timestamp:** 2025-02-21T07:27:57.245Z

Hi [@Algsoch](/u/algsoch) [@24f2003130](/u/24f2003130)

While saving image you might need to pass lossless = True as argument.

`img.save("filename", lossless=True)`

kind regards

---

**post_id:** 597752  
**author:** 23f3004114  
**timestamp:** 2025-02-21T07:49:59.333Z

u can use openai whisper free and use yt-dlp package to extract the video and using whisper convert it

---

**post_id:** 597754  
**author:** 23f3004114  
**timestamp:** 2025-02-21T07:50:53.403Z

For Q8, I wrote the following query,

```
SELECT smo.post_id
FROM social_media as smo
WHERE smo.timestamp >= '2024-11-15T06:02:28.656Z'
AND EXISTS (
   SELECT 1
   FROM LATERAL (
       SELECT UNNEST(json_extract(comments, '$[*]'))
       FROM social_media as sm
       WHERE sm.post_id = smo.post_id
       ) AS c(value)
    WHERE json_extract(c.value, '$.stars.useful')::DOUBLE = 4)
order by smo.post_id;

```

What it does is for each post\_id, checks the timestamp and then checks the presence of a json object in comments that has 4 stars useful rating for this post\_id. Finally returns all the post\_id’s in ascending order.

But it’s giving me an `Array length mismatch` error. I’m stuck here. Any hints would be helpful. [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

P.S. I also noticed that the timestamp given in the question keeps changing with each page reload. But the output from the query stays the same.

---

**post_id:** 597825  
**author:** Jivraj  
**timestamp:** 2025-02-21T10:02:46.400Z

yeah i did the same but the transcript was not the same. it had many differences

---

**post_id:** 597896  
**author:** 21f3001379  
**timestamp:** 2025-02-21T13:21:23.359Z

Sir [@s.anand](/u/s.anand) [@carlton](/u/carlton) the answer is correct but still getting as incorrect sir  
image description: The image shows a webpage with a question related to HTTP requests. The page has a question about successful GET requests for pages under a specific URL and time frame. An answer box is present with the user input "2316," and the error message "Incorrect answer".
image text:
• Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited. E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
• Status: The HTTP status code. If 200 <= Status < 300 it is a successful request
• Size: The size of the response in bytes. E.g. 1234
• Referer: The referer URL. E.g. https://s-anand.net/
• User agent: The browser used. This will contain spaces and might have escaped quotes.
• Vhost: The virtual host. E.g. s-anand.net
• Server: The IP address of the server.
The fields are separated by spaces and quoted by double quotes ("). Unlike CSV files, quoted fields are escaped via \" and not "". (This impacts 41 rows.)
All data is in the GMT-0500 timezone and the questions are based in this same timezone.
By determining the number of successful GET requests under the defined conditions, we'll be able to:
• Optimize Infrastructure: Scale server resources effectively during peak traffic times, reducing downtime and improving user experience.
• Strategize Content Delivery: Identify popular content segments and adjust digital content strategies to better serve the audience.
• Improve Marketing Efforts: Focus marketing initiatives on peak usage windows to maximize engagement and conversion.
What is the number of successful GET requests for pages under /malayalammp3/ from 10:00 until before 17:00 on Saturdays?
2316
Error: Incorrect answer
Check
  
after trying python codes chatgpt i tried using linux commands  
bash-5.2$ zgrep ‘GET /malayalammp3/’ s-anand.net-May-2024.gz   
| grep -E ‘[(04|11|18|25)/May/2024:(10|11|12|13|14|15|16):[0-5][0-9]:[0-5][0-9]’   
| grep -E ’ “(GET|POST) .\* HTTP/1.[01]” (2[0-9][0-9]) ’ | wc -l  
2316  
i’m getting 2316 but when i enter in the answer box it says incorrect

---

**post_id:** 597907  
**author:** 23f3004114  
**timestamp:** 2025-02-21T13:43:41.687Z

Q9 , extracted text from yt and processed the srt file, getting 77 differences adding any word the diff count is increasing . Please tell what i am missing here.

---

**post_id:** 597922  
**author:** 22f3002498  
**timestamp:** 2025-02-21T14:02:24.904Z

downloading and using this image will given an error, better generate it yourself.

---

**post_id:** 597932  
**author:** 24f2003130  
**timestamp:** 2025-02-21T14:12:22.441Z

AE means UAE and so on…

---

**post_id:** 597958  
**author:** Jayeshbansal  
**timestamp:** 2025-02-21T14:50:35.844Z

Hi [@23f3004114](/u/23f3004114)

Question 9 might not be solved 100% automatically, Manually listen to audio once or twice and correct few things.

Kind regards

---

**post_id:** 597969  
**author:** Rrishit  
**timestamp:** 2025-02-21T15:00:51.144Z

**Q9**

Note : I found that punctuations are also checked. So make sure you include punctuations inside the paragraph wherever it is effective according to the voice in the paragraph

---

**post_id:** 597974  
**author:** 23f3004024  
**timestamp:** 2025-02-21T15:07:41.000Z

[@21f3001379](/u/21f3001379) [@Jivraj](/u/jivraj) , thank you for the replies ![:heart:](https://emoji.discourse-cdn.com/google/heart.png?v=12 ":heart:"). i stopped after 8/10. need to prepare for Quiz 1.

---

**post_id:** 597982  
**author:** 22f3002498  
**timestamp:** 2025-02-21T15:12:55.673Z

This case is the same with me

---

**post_id:** 597983  
**author:** Jaideep  
**timestamp:** 2025-02-21T15:14:01.655Z

Yeah I did…I am done with that

---

**post_id:** 598021  
**author:** 22f3002498  
**timestamp:** 2025-02-21T16:18:50.474Z

it is asking successful GET requests, you can know if a request is successful or not by checking the status data given in the file

---

**post_id:** 598086  
**author:** 23f2004636  
**timestamp:** 2025-02-21T17:47:52.518Z

Sir, Q8 is giving errors everytime.

---

**post_id:** 598087  
**author:** 22f2000113  
**timestamp:** 2025-02-21T17:52:10.732Z

It’s mentioned that 200-299 is successful requests

---

**post_id:** 598105  
**author:** 22f3002813  
**timestamp:** 2025-02-21T18:36:54.160Z

[@carlton](/u/carlton) My answer for question 3 seems correct but it shows incorrect. Could you please clarify.

---

**post_id:** 598106  
**author:** 23f3004024  
**timestamp:** 2025-02-21T18:38:01.291Z

No, for me It ran successfully and gave me the correct answer  
Try to use an LLM I have used qwen 2.5 max if you are not comfortable with that stick to chatgpt and your console for debugging

---

**post_id:** 598140  
**author:** 22f3002498  
**timestamp:** 2025-02-22T00:35:40.515Z

Is the issue still pertaining for you?

---

**post_id:** 598141  
**author:** 22f3002498  
**timestamp:** 2025-02-22T00:36:33.922Z

Are there bonus marks for GA5?

---

**post_id:** 598199  
**author:** swapnila04  
**timestamp:** 2025-02-22T04:48:06.113Z

I am also facing same issue with Q3. I tried with with shell as well as python script to find GET requests for pages under **/telugu/** from **11:00** until before **20:00** on Mondays

---

**post_id:** 598766  
**author:** Algsoch  
**timestamp:** 2025-02-23T14:10:48.269Z

Hello sir,  
With each passing assignment we are learning many new tools.  
This way of teaching is actually amazing as it will make us remember for long.  
Fortunate to be a part of this course!  
Thanks to the team

---

**post_id:** 598869  
**author:** 23f1002382  
**timestamp:** 2025-02-24T05:44:46.473Z

Yes … For u … u fixed it???

---

**post_id:** 599117  
**author:** 23f1002709  
**timestamp:** 2025-02-24T16:09:24.346Z

No  
I couldn’t fix it

---

**post_id:** 599196  
**author:** Jivraj  
**timestamp:** 2025-02-24T20:20:54.776Z

That question is same for me.

---

**post_id:** 599197  
**author:** Jivraj  
**timestamp:** 2025-02-24T20:21:29.900Z

**QUESTION 9**

I was supposed to transcribe the audio of the provided video for a certain time period. After several attempts my submission still generated differences from the supposed answers. I have tried all forms of re-punctuations but the error wont budge. I even compared the generated transcript with the actual audio several times. I BELIEVE MY ANSWER IS CORRECT. If not I wish to know what the correct answer is. Because compared to the video I have provided the exact and well punctuated transcription of the audio between 397.2 and 505.5 seconds.

Here was my transcription - " Determined to confront the mystery, Miranda followed the elusive figure. In the dim corridor, fleeting glimpses of determination and hidden sorrow emerged, challenging her assumptions of friends and foes alike. The pursuit led her to a narrow, winding passage beneath the chapel. In the oppressive darkness, the air grew cold and heavy, and every echo of her footsteps seemed to whisper warnings of secrets best left undisturbed.

In a subterranean chamber, the shadow finally halted. The figure’s voice emerged from the gloom, “You are close to the truth, but be warned some secrets, once uncovered, can never be buried again.”

The mysterious stranger introduced himself as Victor, a former confidant of Edmund. His words painted a tale of coercion and betrayal—a network of hidden alliances that had forced Edmond into an impossible choice.

Victor detailed clandestine meetings, cryptic codes, and a secret society that manipulated fate from behind the scenes. Miranda listened, each revelation tightening the knots of suspicion around her mind.

From within his warm coat, Victor produced a faded journal brimming with names, dates, and enigmatic symbols. Its contents mirrored Edmund’s diary, strengthening the case for a conspiracy rooted in treachery. The journal hinted at a hidden hall beneath the manor, where the secret society stored evidence of their manipulations.

Miranda’s pulse quickened at the thought of unmasking those responsible for decades of deceit. Returning to the manor’s main hall, Miranda retraced her steps with renewed resolve. Every shadow in the corridor now seemed charged with meaning, each creak of wood a prelude to further revelations. In the manor’s basement, beneath a concealed panel, Miranda discovered another revelation "

---

**post_id:** 599198  
**author:** Jivraj  
**timestamp:** 2025-02-24T20:22:21.934Z

Can anyone provide solution of question 5 related to duckdb module  
please

---

**post_id:** 599200  
**author:** Jivraj  
**timestamp:** 2025-02-24T20:27:11.504Z

is there anyway to practice the assignments and check answers even though the deadline for the assignment passes? or is the answer given somewhere just for learning sake. I had exams and would like do week 4,week 5 before week 6 and doing the assignment is a huge part in learning, any on the just doing the assignments or answers for the assignments? I understand that each set of students get different questions. [@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

**post_id:** 599201  
**author:** Jivraj  
**timestamp:** 2025-02-24T20:32:06.446Z

image description: The image is a webpage with instructions for a quiz. The top has a red bar showing the end time and score. The main content includes a list of instructions, a "Have questions?" section with a link to Discourse, and a user login information. There is also a "Recent saves" section showing past attempts.
image text: Ended at Fri, 21 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
TDS 2025 Jan GA5 - Data F
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You c
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. U
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz
Have questions? Join the discussion on Discourse
You are logged in as 23f1002709@ds.study.iitm.ac.in.
Logout
Recent saves (most recent is your official score)
Reload from 2/21/2025, 4:40:22 PM. Score: 10
Reload from 2/21/2025, 4:40:20 PM. Score: 10
Reload from 2/21/2025, 4:40:14 PM. Score: 10
  
recent score shows the points, but overall score is 0. Please take a look.

---

**post_id:** 599346  
**author:** 23f1002382  
**timestamp:** 2025-02-25T06:51:01.549Z

You can load answers using reload button on every assignment.  
You can enable check answers button.

---

**post_id:** 602912  
**author:** HARISH.S  
**timestamp:** 2025-03-02T12:29:46.578Z

No need to worry about that.

---

**post_id:** 602915  
**author:** Jivraj  
**timestamp:** 2025-03-03T08:13:30.879Z

```
SELECT DISTINCT post_id 
FROM (
   SELECT timestamp, post_id, UNNEST (comments->'$[*].stars.useful') AS useful
   FROM social_media
) AS temp
WHERE useful >= 2.0 
   AND timestamp > '2024-12-08T05:30:31.073Z'

```

---

**post_id:** 603351  
**author:** carlton  
**timestamp:** 2025-03-04T09:21:02.853Z

Hi [@22f3002498](/u/22f3002498)

Yes, there is some issues with question3 we are working on it.

Thanks and kind regards

---

**post_id:** 605775  
**author:** Jivraj  
**timestamp:** 2025-03-11T22:41:00.273Z

Hi [@23f3004024](/u/23f3004024)

There is some problem with question 3 of GA5, we are working on it. Marks will be pushed to dashboard once we resolve this issue.

Thanks and kind regards

---

