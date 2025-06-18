# ga7-data-visualisation-discussion-thread-tds-jan-2025

Dear Learner,

This is the discussion thread for [Graded Assignment 7](https://forms.gle/8AMCa4oQ8JnpzemY7). Please post any queries related to it here.

Deadline: 2025-03-26T18:29:00Z

---

---

---

Is it compulsory to use microsoft powerpoint? Can we use google slides?

---

We will be using scripts to check the submissions. You will have to use PowerPoint.

Kind regards

---

Hi [@carlton](/u/carlton),  
I was working on GA7 as part of Task 4 in 7.1. In task 4.Sheet1, the columns include Series ID, Item, Year, Month, and Value. While I could extract Series ID and Item, I couldn’t locate Year, Month, or Value in the dataset. Could someone please assist me with this?  
image description: The image is a screenshot of a table, most likely from a spreadsheet program like Google Sheets or Microsoft Excel. The table contains data related to "PPI industry data" for pharmaceutical preparation manufacturing. The table has multiple rows, and each row has data in multiple columns. The first row displays information about Anticoagulants, hemostatics, and digitalis preparations. The second part displays information about Calcium channel blockers.
image text:
PPI industry data for Pharmaceutical preparation manufacturing-Anticoagulants, hemostatics, and digitalis preparations, not seasonally adjusted
Series Title
PPI industry data for Pharmaceutical preparation manufacturing-Anticoagulants, hemostatics, and digitalis preparations, not seasonally adjusted
Series ID
PCU3254123254127111
Seasonality
Not Seasonally Adjusted
Survey Name
PPI Industry Data
Measure Data Ty Anticoagulants, hemostatics, and digitalis preparations
Industry
Pharmaceutical preparation manufacturing
Item
Anticoagulants, hemostatics, and digitalis preparations
PPI industry data for Pharmaceutical preparation manufacturing-Calcium channel blockers, not seasonally adjusted
Series Title
PPI industry data for Pharmaceutical preparation manufacturing-Calcium channel blockers, not seasonally adjusted
Series ID
PCU3254123254127114
Seasonality
Not Seasonally Adjusted
Survey Name
PPI Industry Data
Measure Data Ty Calcium channel blockers
Industry
Pharmaceutical preparation manufacturing
Item
Calcium channel blockers

---

There is another dataset provided for the other records.

---

Here's a description of the image:
The image is a screenshot of a question presented in a digital form. It's framed by a light grey background with white space. The question, marked as "Question 7.1", involves analyzing pharmaceutical exports and asks for the creation of a Google Sheet workbook.
image text:
Your email will be recorded when you submit this form
Question 7.1
Scenario: A new political party, the Buddhi Daya Nyaay (BDN), wants to analyze the
impact of pharmaceutical exports to the US on India's economy. India's export of
Pharmaceuticals to the United States for FY 2024 reached ₹ 2,42,888 Crores. You
are tasked with creating an insightful analysis using provided CSV files.
Provided Files:
Industry Product Segment Information
Monthly Price Indices for Segments (Two-year data)
Tasks:
1. Create a new blank Google Sheet workbook, named ga.7.1.rollno (replace
'rollno' with your IITM roll number excluding the domain).
2. Share with editing rights to se2002@study.iitm.ac.in. If you do not do this
step first, on a blank workbook we will not consider your submission.
3. NOTE: Make sure the sheet names are exactly as given below:
4. Sheet1: Columns include Series ID, Item, Year, Month, and Value.
5. Sheet2: Create a pivot table with Item as rows, Year and Month as columns
following the same hierarchy stack and Value as values.

Monthly Price Indices file have those columns.

---

@[Jivraj](https://discourse.onlinedegree.iitm.ac.in/u/Jivraj)

In the GA 7.1 part it is said that we need data of which columns are  
![{7059D6FF-DF75-4B21-999A-29D23A297A90}](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fdec02b5239ef02c5198e250c8a2d6eb007b82.png)

but the dataset provided has no column named “Item”  
![{F9711583-E074-489A-AC90-154B9309F786}](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/1/a121b005d9edc2469571d46018f450882b3fcb81.png)

---

Thanks a lot for pointing out and sorry it’s my bad missed it.

---

Item is there in other sheet we might have to join them to get items.

---

We have to extract all id’s and their respective item from other sheet and add in first sheet with respect to id’s .

---

[@carlton](/u/carlton) Sir I don’t have Microsoft PowerPoint. What should I do ?

---

Use the free version on Microsoft 365

---

Below items don’t have prices.

| PCU3254123254127111 | Anticoagulants, hemostatics, and digitalis preparations |
| --- | --- |
| PCU3254123254127114 | Calcium channel blockers |
| PCU325412325412MM | Miscellaneous receipts |
| PCU325412325412D112OC | Other digestive or genito-urinary preparations, over-the-counter |
| PCU325412325412D113 | Antacids |
| PCU325412325412SS | Secondary products |
| PCU3254123254127112 | ACE inhibitors |

Some items don’t have prices for all 24 months.  
Although the assignment says 24 months (I assumed 2023 January to 2024 December) data, many items have prices for 2025 Jan as well.

> [Monthly Price Indices for Segments (Two-year data)](https://drive.google.com/file/d/1OrkZgDnx7uYjOxFW2XDrA5F0xFre_PCS/view?usp=drive_link)

Shall I delete the records for which price is not available?  
image description: This is a spreadsheet, likely in a program like Google Sheets or Microsoft Excel, detailing financial or statistical data, The top row displays headers such as "Year," "Month," "Total," and months labeled as "M01," "M02," "M03," "M04," and "M05" . The left-hand column, labeled "Item," lists various categories or items. Some of the entries under "Item" include "ACE inhibitors," "Analgesics," "Analgesics, over-the-counter," "Analgesics, prescription," "Antacids," and "Anti-acne preparations.". The values are displayed in a grid format. The values within the grid suggest a financial context, as they may represent sums of value.
image text: SUM of Value
Item
ACE inhibitors
Analgesics
Analgesics, over-the-counter
Analgesics, prescription
Antacids
Anti-acne preparations
Anticoagulants, hemostatics, and digitalis preparations
Anticonvulsants
Antidepressants
Antihistamines and bronchodilators, including antiasthmatics
Broad and medium spectrum antibiotics
Calcium channel blockers
Cancer therapy products
Hormones and oral contraceptives
Insulin/antidiabetes products
Miscellaneous receipts
Multivitamins
Other cardiovascular preparations
Other central nervous system and sense organs
Other digestive or genito-urinary preparations
Other digestive or genito-urinary preparations, over-the-counter
Other digestive or genito-urinary preparations, prescription
Other neoplasms, endocrine system, and metabolic diseases
Other parasitic and infective diseases
Other pharmaceutical preparations acting on the skin
Year
Month
Total
2023
M01
M02
M03
M04
M05
0
0
337.36
351.575
351.601
351.679
105.118
105.808
105.898
106.172
127.948
133.784
133.784
133.784
0
0
106.13
106.13
106.13
106.13
0
0
257.715
257.715
257.715
257.715
1311.062
1311.062
1311.062
1311.062
1150.643
1151.272
1151.272
1152.022
603.966
603.966
603.966
603.966
0
0
955.129
956.07
956.07
956.07
226.784
226.784
226.784
226.784
1645.533
1645.533
1645.55
1645.55
575.643
575.643
576.86
576.86
200.536
200.536
200.536
200.536
559.4
559.4
559.4
559.4
269.471
269.471
269.471
270.365
202.836
202.836
202.604
201.697
0
0
102.235
102.235
102.235
101.689
1104.296
1105.143
1105.143
1105.143
313.664
313.664
313.664
313.664
109.643
109.643
109.643
108.949

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

How to give the access to power point slides with the edit option ?

---

[@carlton](/u/carlton) Can you please advise regarding the ga.7.2 as the The current top 5 countries by GDP in 2014 from the dataset are actually aggregated economic groups (not individual countries). can i proceed with that or I need to filter only the individual countries

---

once i submitted the answers. but when i clicked on edit response and it deleted all the submitted answers. What to do in this case [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

---

Hi Tanya,

Both you responses have been recorded. So it has not been deleted. Its just the way google forms works, it does not reload your previous responses.

Kind regards

---

The question asked for top 5 countries. So that would be the approach for this question, not aggregated economic groups.

---

Hi [@carlton](/u/carlton) sir,  
I have received the bonus marks email with 5 additional HTML files for peer review. However, I noticed that one of these files was also included in the initial peer grading email.

Could you please clarify if I should fill out the peer review form for this particular file again, or should I skip it since it has already been graded?  
image description: The image is a screenshot of a Gmail inbox. The top of the screen has a search bar with "peer review" entered. The inbox displays a list of emails, with subjects related to "TDS Jan 25" and peer evaluations. Two of the emails have the same file attachment, highlighted in pink: "23f3003944.html". The right corner shows the user's profile picture with "IIT Madras".
image text:
Gmail
peer review
Mail Conversations Spaces From Any time Has attachment To Advanced search
Mail
C
1-29 of 29
Google Forms 9
Inbox TDS Jan 2025 - GA 7 Review - GA 7 Review Here's what was received. Edit response T... Edit your response
22t1 se2002
Inbox [TDS Jan 25] BONUS 5 Marks to T Score - submit 3 peer evaluations, so that you may be graded for your submission. Ple...
23f3003944.html
23f3001178.html
23f2001738.html
22t1 se2002
Inbox [TDS Jan 25] GA 7 Peer allocations - submit 3 peer evaluations, so that you may be graded for your submission. Please fi...
24f1002555.html
23f3003944.html
23f1001126.html

---

Hi Shambhavi, Thanks for the update. We will look into it.

Thanks once again

---

Sir,  
In case we are not provided access to view their respective sheets, we would have no option but to either leave the column blank or mark it as 0. However, if others have marked it differently based on their available information, there is a possibility that our responses may vary — potentially exceeding the permissible variance limit of ±33%.

In such a scenario, would this mean we would not be eligible for the bonus?

Additionally, it would be really helpful if a uniform approach or standard marking could be communicated for such cases where access is not granted. This would ensure consistency across all submissions and avoid discrepancies arising from random or subjective entries, which seems to be happening currently.

---

If you are not provided access, contact the peer. Their email is there in the html file. It’s in the peers interest **and** yours. That’s an important aspect of GA7, it’s to get people to work together and collaborate.  
Peer reviews like the real world is going to be messy. The way to reduce the messiness is to communicate with one another.

---

[@carlton](/u/carlton)  
sir can you please clarify what do we have to write in google form if there is no submission?

---

You have two options. Get in touch with the peer (you have their email address), this is the recommended approach. Or you could give them zero because you were not able to evaluate their submission.

---

