# end-term-mock-tds-jan-25

# Mock Exam: Tools in Data Science

#### The end term and the mock has been created using the TDS GPT Assistant. Since the GPT has ALL the GAs, Course Content Modules, Live Session Transcriptions (its works like RAG), it is really able to help you prepare for the end term. Use it!

Therefore you can also create your own mocks.

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/9/694ce72c03000e3ef7ba33ce5f9f14d721099bcb.png)
[ChatGPT](https://chatgpt.com/g/g-mZqKVxKDx-iitm-tds-teaching-assistant)

### [ChatGPT - IITM TDS Teaching Assistant](https://chatgpt.com/g/g-mZqKVxKDx-iitm-tds-teaching-assistant)

TA for IIT Madras' Data Science course, guiding students with questions.

Below are variant questions across various topics relevant to the course. These questions have been curated from the topics areas we are focussing on. Therefore it will be very similar in content to the end term.

> What it does not contain: Scenario based questions. These are complex to construct. We will address the topics for these questions in the live session.

* LLMs
* Pandas
* Git, Docker, Bash

---

### Q1: HTTP Method Semantics

Which HTTP method is **not idempotent**, meaning repeated identical requests **may** result in different outcomes each time?

* A. GET
* B. PUT
* C. POST
* D. DELETE

**Answer**: C. POST

### Q2: IDE Features

Which feature is **least likely** to be found in a standard code editor or IDE?

* A. Code formatting tools
* B. Integrated terminal
* C. Git integration
* D. Cloud hosting of Docker containers

**Answer**: D. Cloud hosting of Docker containers

### Q3: Pandas Summary Methods

You have a DataFrame with a `region` column. To get a quick summary of how many entries are in each region, which method is most useful?

* A. df.describe()
* B. df[“region”].value\_counts()
* C. df.count()
* D. df.groupby(“region”).sum()

**Answer**: B. df[“region”].value\_counts()

### Q4: Python Exception Scope

You want to safely open a file, handle any errors, and ensure the file is always closed in Python. Which pattern should you use?

* A. `try: open(...)` then `finally: close()`
* B. `open()` and then `except`
* C. `open()` and then `raise`
* D. Use `with open(...) as f:` block

**Answer**: D. Use `with open(...) as f:` block

### Q5: Chrome DevTools - Debugging

A frontend developer wants to trace JavaScript function calls step-by-step. Which **Chrome DevTools** panel should they use?

* A. Console
* B. Application
* C. Sources
* D. Elements

**Answer**: C. Sources

### Q6: Data Cleaning Tools

You are cleaning survey responses and want to automatically match similar text entries like “NYC”, “New York City”, and “newyorkcity”. Which approach/tool would be most effective?

* A. `TRIM()` in Excel
* B. Manual Find and Replace
* C. Fuzzy matching or clustering in OpenRefine
* D. COUNTIF()

**Answer**: C. Fuzzy matching or clustering in OpenRefine

### Q7: Geospatial Libraries

Which pair of Python libraries is best suited for **geospatial analysis** and **rendering static maps**?

* A. pandas and seaborn
* B. geopandas and matplotlib
* C. folium and flask
* D. sklearn and dash

**Answer**: B. geopandas and matplotlib

### Q8: Statistical Significance

A psychologist tests if a training program changes memory performance and finds a p-value of **0.08**. What can be concluded at the 0.05 significance level?

* A. The result is highly significant
* B. The null hypothesis must be rejected
* C. There is insufficient evidence to reject the null hypothesis
* D. The program is proven to work

**Answer**: C. There is insufficient evidence to reject the null hypothesis

### Q9: Purpose of Kumu

What is a key use case for a tool like **Kumu**?

* A. Animating time series
* B. Designing deep learning models
* C. Visualizing stakeholder networks and system relationships
* D. Performing statistical analysis

**Answer**: C. Visualizing stakeholder networks and system relationships

### Q10: DevTools Performance Diagnostics

To diagnose a slow webpage, you want to **analyze scripts, rendering times, and long tasks**. Which DevTools panel provides a timeline-based view?

* A. Elements
* B. Performance
* C. Network
* D. Lighthouse

**Answer**: B. Performance

### Q11: Git Configuration

Which of the following files helps configure a Git project’s name, email, and default branch?

* A. `.gitignore`
* B. `.gitattributes`
* C. `.git/config`
* D. `README.md`

**Answer**: C. `.git/config`

### Q13: Safe HTTP Method

Which HTTP method is considered **safe**, meaning it is only used for retrieval and **must not change** server state?

* A. GET
* B. DELETE
* C. PATCH
* D. POST

**Answer**: A. GET

### Q14: Deduplicating Text Entries

A dataset has entries like “IBM”, “I.B.M.”, and “International Business Machines”. What is the best tool to cluster these for cleaning?

* A. Excel TRIM
* B. OpenRefine using key collision or fingerprinting
* C. pandas merge()
* D. CONCATENATE()

**Answer**: B. OpenRefine using key collision or fingerprinting

### Q15: Geospatial + Interactive Mapping

A conservation biologist wants to visualize real-time animal tracking data on an interactive map. Which libraries would be best?

* A. geopandas and plotly
* B. folium and pandas
* C. seaborn and shapely
* D. rasterio and altair

**Answer**: B. folium and pandas

### Q16: Pandas - Filtering Unique Entries

You have a DataFrame of customer orders and want to list only those customers who ordered **once**. Which Pandas method chain is most suitable?

* A. df.groupby(“customer”).sum()
* B. df[“customer”].value\_counts() == 1
* C. df.drop\_duplicates()
* D. df[“customer”].nunique()

**Answer**: B. df[“customer”].value\_counts() == 1

### Q17: Purpose of Kumu in System Design

How does Kumu help in system design or stakeholder mapping?

* A. Organizing spreadsheets
* B. Identifying leverage points in complex systems through visual maps
* C. Rendering line graphs
* D. Sending notifications

**Answer**: B. Identifying leverage points in complex systems through visual maps

### Q18: Python Exception - Multiple Handlers

Which structure allows Python to handle different types of exceptions separately?

* A. `try`…`finally`
* B. `if`…`else`
* C. Multiple `except` blocks
* D. Nested `try` blocks

**Answer**: C. Multiple `except` blocks

### Q19: Understanding Statistical Power

If a study has **low statistical power**, what is most likely to occur?

* A. False positive (Type I error)
* B. False negative (Type II error)
* C. Confounding
* D. Multicollinearity

**Answer**: B. False negative (Type II error)

### Q20: Git Basics - Staging Area

Which Git command moves modified files to the **staging area**?

* A. git push
* B. git add
* C. git fetch
* D. git init

**Answer**: B. git add

### Q21: Chrome DevTools - Local Storage

Where can you inspect **local storage** items (e.g. tokens, preferences) in Chrome DevTools?

* A. Console
* B. Application > Local Storage
* C. Elements
* D. Sources

**Answer**: B. Application > Local Storage

### Q22: Chrome DevTools - JS Performance

Which DevTools feature helps measure execution time of scripts and CPU usage?

* A. Console
* B. Network
* C. Performance
* D. Application

**Answer**: C. Performance

### Q23: Excel Data Import - Scientific Notation Issue

You import a CSV file where product IDs like `"1E10"` are being interpreted as scientific notation in Excel. What is the best way to preserve these IDs as text?

* A. Format the column as General
* B. Use `=TEXT(A1, "0")` after import
* C. Set column format to Text during import or Text-to-Columns
* D. Change regional settings

**Answer**: C. Set column format to Text during import or Text-to-Columns

---

### Module: Everyday Tools

**Q1: Spreadsheet Functions**

You have a dataset in Excel where column A contains full names in the format “Last Name, First Name”. Which function can you use to extract the first name into a separate column?

* A. `=LEFT(A1, FIND(",", A1)-1)`
* B. `=RIGHT(A1, LEN(A1) - FIND(",", A1))`
* C. `=MID(A1, FIND(",", A1)+2, LEN(A1))`
* D. `=SPLIT(A1, ",")`

**Answer**: C — The `MID` function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

---

### Module: Data Sourcing

**Q2: Web Scraping Ethics**

When performing web scraping to collect data, which of the following practices is considered unethical?

* A. Respecting the website’s `robots.txt` file.
* B. Sending requests at a rate that mimics human browsing behavior.
* C. Scraping data from a website that requires login without permission.
* D. Citing the source of the data collected.

**Answer**: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

---

### Module: Data Preparation

**Q3: Handling Missing Data**

In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally **not** appropriate for handling these missing values?

* A. Replacing missing values with the mean age.
* B. Deleting rows with missing age values.
* C. Replacing missing values with a fixed age, such as 0.
* D. Leaving the missing values as they are without any action.

**Answer**: D — Leaving missing values unaddressed can lead to errors in analysis and modeling. Options A, B, and C are common strategies for handling missing data, depending on the context and the extent of the missingness.

---

### Module: Data Analysis

**Q4: Statistical Measures**

Which of the following statistical measures is **not** sensitive to extreme values (outliers) in a dataset?

* A. Mean
* B. Median
* C. Standard Deviation
* D. Range

**Answer**: B — The median represents the middle value of a dataset and is not affected by outliers. In contrast, the mean, standard deviation, and range can be significantly influenced by extreme values.

---

### Module: Large Language Models

**Q5: Tokenization in NLP**

In Natural Language Processing, what is the primary purpose of tokenization?

* A. To translate text from one language to another.
* B. To split text into individual words or subwords.
* C. To encrypt text for secure communication.
* D. To summarize large texts into shorter versions.

**Answer**: B — Tokenization involves breaking down text into smaller components, such as words or subwords, which can then be processed by language models. This is a fundamental step in NLP tasks.

---

### Module: Geospatial and Network Analysis

**Q6: Geographic Coordinate Systems**

Which of the following coordinate systems is commonly used to represent locations on Earth’s surface?

* A. Cartesian Coordinate System
* B. Polar Coordinate System
* C. Geographic Coordinate System (Latitude and Longitude)
* D. Cylindrical Coordinate System

**Answer**: C — The Geographic Coordinate System uses latitude and longitude to specify locations on Earth’s surface. This system is widely used in geospatial analysis.

---

### Module: Data Visualization

**Q7: Effective Data Visualization**

When creating a bar chart to compare the sales performance of different products, which practice should be avoided?

* A. Ordering bars from highest to lowest value.
* B. Using different colors for each bar without a legend.
* C. Starting the y-axis at zero.
* D. Labeling each bar with its exact value.

**Answer**: B — Using different colors for each bar without a legend can confuse the audience, as they may assume the colors represent different categories. Consistency and clarity are key in effective data visualization.

---

### Module: Everyday Tools

**Q8: VS Code Feature Use**

You are editing a Python script in Visual Studio Code and want to quickly find and edit all occurrences of a variable name in the current file. What feature should you use?

* A. Git integration
* B. Debug panel
* C. **Multi-cursor editing**
* D. Terminal commands

**Answer**: C — Multi-cursor editing allows you to place multiple cursors in a file and edit text in multiple locations at once. It is useful for refactoring variable names or repeated patterns.

---

### Module: Data Sourcing

**Q9: Data API Identification**

Which of the following data sources is most likely to provide structured data accessible via an API?

* A. A scanned PDF document
* B. A screenshot of a chart
* C. **The World Bank data portal**
* D. A newspaper article

**Answer**: C — The World Bank data portal provides structured datasets accessible via APIs. The other options involve unstructured or image-based content not suitable for direct data access.

---

### Module: Data Preparation

**Q10: Data Type Conversion in Excel**

You imported a CSV file into Excel, and one of the columns containing numbers is treated as text. What is the easiest way to convert it into numeric format?

* A. Use the CONCAT function
* B. Format the column as Text
* C. **Use the VALUE() function**
* D. Use SUBSTITUTE()

**Answer**: C — The VALUE function converts text that appears as numbers into actual numeric values. This is useful when data is imported with formatting issues.

---

### Module: Data Analysis

**Q11: Outlier Detection**

You are analyzing a dataset of employee salaries. Which visualization is best for quickly identifying outliers?

* A. Line chart
* B. **Box plot**
* C. Histogram
* D. Pie chart

**Answer**: B — A box plot clearly shows the spread of data and highlights outliers as individual points beyond the whiskers.

---

### Module: Large Language Models

**Q12: Prompt Engineering Strategy**

To get consistent, structured responses from a language model when extracting key information, which approach is most effective?

* A. Ask the model to “summarize” the text
* B. Use open-ended questions
* C. **Use system messages and JSON schema formatting**
* D. Provide only one-word inputs

**Answer**: C — System messages and structured output formats like JSON schemas guide the model to generate reliable and consistent structured responses.

---

### Module: Geospatial and Network Analysis

**Q13: Network Centrality**

In a social network graph of coworkers, which metric best identifies the person who connects the most groups together?

* A. Degree centrality
* B. Closeness centrality
* C. **Betweenness centrality**
* D. Eigenvector centrality

**Answer**: C — Betweenness centrality measures how often a node appears on shortest paths between other nodes, highlighting connectors or “bridges” in the network.

---

### Module: Data Visualization

**Q14: Choosing the Right Chart**

You want to show how the composition of a marketing budget changes across three years. Which visualization is most appropriate?

* A. Pie charts for each year
* B. Scatter plots
* C. **Stacked bar chart**
* D. Line chart

**Answer**: C — A stacked bar chart shows parts of a whole across different categories and time periods, making it easier to compare budget composition over years.

---

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
any link for last term’s end term question answer

---

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/8/7/874d0312bcd327ca91ab204f36071f2c8fef3dd5.png)
[quizpractice.space](https://quizpractice.space/exam/7a6ff569-f50c-40e7-a08b-f5c334392600)

![](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/f/0fe1fe85fe70c59ec7887abe416fffdf379ffcf3_2_690x362.png)

### [Practise End Term Quiz Question Papers](https://quizpractice.space/exam/7a6ff569-f50c-40e7-a08b-f5c334392600)

Practice with IITM's online BS degree question papers and quizzes to improve your preparation.

---

So here is more questions in the form of a little quiz (shared by someone in the group,DM for Credit ![:smiling_face_with_three_hearts:](https://emoji.discourse-cdn.com/google/smiling_face_with_three_hearts.png?v=14 ":smiling_face_with_three_hearts:"))

[gkmfrombs.github.io](https://gkmfrombs.github.io/tds_quiz/)

### [Quiz from PDF](https://gkmfrombs.github.io/tds_quiz/)

That has 350 questions if you don’t want to go through all of them(it’s pretty time consuming)  
in that case just do this PDF.(This pdf contains all the questions that is a bit conceptual i would say and some questions which i failed to do ![:smiling_face_with_tear:](https://emoji.discourse-cdn.com/google/smiling_face_with_tear.png?v=14 ":smiling_face_with_tear:") )

[accounts.google.com](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1TdXX4mcWaA-ugY9nL0hm1zTa_SJGic3T%2Fview%3Fusp%3Dsharing&followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1TdXX4mcWaA-ugY9nL0hm1zTa_SJGic3T%2Fview%3Fusp%3Dsharing&ifkv=AXH0vVsCl9rHQxcRPKDEBdF3oOkGtLRjZ-BFKdcccxSGUFkdSijsEgmjtYG0tuTwCSdBHRs3zNjm3g&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1894439260%3A1744401916671974)

### [Google Drive: Sign-in](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1TdXX4mcWaA-ugY9nL0hm1zTa_SJGic3T%2Fview%3Fusp%3Dsharing&followup=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1TdXX4mcWaA-ugY9nL0hm1zTa_SJGic3T%2Fview%3Fusp%3Dsharing&ifkv=AXH0vVsCl9rHQxcRPKDEBdF3oOkGtLRjZ-BFKdcccxSGUFkdSijsEgmjtYG0tuTwCSdBHRs3zNjm3g&osid=1&passive=1209600&service=wise&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1894439260%3A1744401916671974)

Access Google Drive with a Google account (for personal use) or Google Workspace account (for business use).

(If you know context to the pdf’s name,we are friends ![:grin:](https://emoji.discourse-cdn.com/google/grin.png?v=14 ":grin:"))

Thank you,  
Kindeeesstt Regards,(hopefully the last post on discourse for TDS),  
Tushar Jalan

---

Thank you for your efforts  
Thanks

Edit: Opened in incognito and it worked.

---

Hi [@carlton](/u/carlton) please upload the recording of Thursday’s TDS session on the YouTube playlist

---

[@carlton](/u/carlton) sir i have done the 350 questions . i am able to answer 80% of the questions on my own, correctly. will end term also be similar to these questions? are pyqs any helpful ?

---

[Live Session - TDS - 2025/04/10 20:00 GMT+05:30 - Recording - Google Drive](https://drive.google.com/file/d/1nzmGBhYoIxY9ZRMoO5yksi3E7GH5xXub/view)

Access recording through this gdrive link

---

Thank you for the questions sir.

---

