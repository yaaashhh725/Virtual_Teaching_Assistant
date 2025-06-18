# end-term-mock-tds-jan-25

**post_id:** 617737  
**author:** carlton  
**timestamp:** 2025-04-10T07:52:12.871Z

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

**post_id:** 617741  
**author:** carlton  
**timestamp:** 2025-04-10T07:55:57.345Z

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

**post_id:** 618104  
**author:** 22f3002723  
**timestamp:** 2025-04-11T05:30:28.919Z

### Module: Everyday Tools

**Q1: Spreadsheet Functions**

You have a dataset in Excel where column A contains full names in the format “Last Name, First Name”. Which function can you use to extract the first name into a separate column?

* A. `=LEFT(A1, FIND(",", A1)-1)`
* B. `=RIGHT(A1, LEN(A1) - FIND(",", A1))`
* C. `=MID(A1, FIND(",", A1)+2, LEN(A1))`
* D. `=SPLIT(A1, ",")`

**Answer**: C — The `MID` function extracts text from the middle of a string. By finding the position of the comma and adding 2 (to skip the comma and space), it extracts the first name. Option A extracts the last name, Option B results in an error due to incorrect syntax, and Option D is not a valid Excel function.

---

**post_id:** 618184  
**author:** 22f3001307  
**timestamp:** 2025-04-11T08:45:48.950Z

### Module: Data Sourcing

**Q2: Web Scraping Ethics**

When performing web scraping to collect data, which of the following practices is considered unethical?

* A. Respecting the website’s `robots.txt` file.
* B. Sending requests at a rate that mimics human browsing behavior.
* C. Scraping data from a website that requires login without permission.
* D. Citing the source of the data collected.

**Answer**: C — Scraping data from a website that requires login without permission violates the site’s terms of service and user privacy. Options A, B, and D are ethical practices that respect the website’s policies and data ownership.

---

**post_id:** 618380  
**author:** 23f2003751  
**timestamp:** 2025-04-11T19:56:15.807Z

### Module: Data Preparation

**Q3: Handling Missing Data**

In a dataset, you notice that several entries in the “Age” column are missing. Which method is generally **not** appropriate for handling these missing values?

* A. Replacing missing values with the mean age.
* B. Deleting rows with missing age values.
* C. Replacing missing values with a fixed age, such as 0.
* D. Leaving the missing values as they are without any action.

**Answer**: D — Leaving missing values unaddressed can lead to errors in analysis and modeling. Options A, B, and C are common strategies for handling missing data, depending on the context and the extent of the missingness.

---

**post_id:** 618392  
**author:** 22f3002248  
**timestamp:** 2025-04-12T00:18:31.370Z

### Module: Data Analysis

**Q4: Statistical Measures**

Which of the following statistical measures is **not** sensitive to extreme values (outliers) in a dataset?

* A. Mean
* B. Median
* C. Standard Deviation
* D. Range

**Answer**: B — The median represents the middle value of a dataset and is not affected by outliers. In contrast, the mean, standard deviation, and range can be significantly influenced by extreme values.

---

**post_id:** 618619  
**author:** 24ds3000061  
**timestamp:** 2025-04-12T11:48:23.569Z

### Module: Large Language Models

**Q5: Tokenization in NLP**

In Natural Language Processing, what is the primary purpose of tokenization?

* A. To translate text from one language to another.
* B. To split text into individual words or subwords.
* C. To encrypt text for secure communication.
* D. To summarize large texts into shorter versions.

**Answer**: B — Tokenization involves breaking down text into smaller components, such as words or subwords, which can then be processed by language models. This is a fundamental step in NLP tasks.

---

**post_id:** 618626  
**author:** Venkatesh_2k01  
**timestamp:** 2025-04-12T12:00:50.407Z

### Module: Geospatial and Network Analysis

**Q6: Geographic Coordinate Systems**

Which of the following coordinate systems is commonly used to represent locations on Earth’s surface?

* A. Cartesian Coordinate System
* B. Polar Coordinate System
* C. Geographic Coordinate System (Latitude and Longitude)
* D. Cylindrical Coordinate System

**Answer**: C — The Geographic Coordinate System uses latitude and longitude to specify locations on Earth’s surface. This system is widely used in geospatial analysis.

---

**post_id:** 618628  
**author:** Jivraj  
**timestamp:** 2025-04-12T12:09:15.641Z

### Module: Data Visualization

**Q7: Effective Data Visualization**

When creating a bar chart to compare the sales performance of different products, which practice should be avoided?

* A. Ordering bars from highest to lowest value.
* B. Using different colors for each bar without a legend.
* C. Starting the y-axis at zero.
* D. Labeling each bar with its exact value.

**Answer**: B — Using different colors for each bar without a legend can confuse the audience, as they may assume the colors represent different categories. Consistency and clarity are key in effective data visualization.

---

**post_id:** 618783  
**author:** 23f1002223  
**timestamp:** 2025-04-13T02:26:36.725Z

### Module: Everyday Tools

**Q8: VS Code Feature Use**

You are editing a Python script in Visual Studio Code and want to quickly find and edit all occurrences of a variable name in the current file. What feature should you use?

* A. Git integration
* B. Debug panel
* C. **Multi-cursor editing**
* D. Terminal commands

**Answer**: C — Multi-cursor editing allows you to place multiple cursors in a file and edit text in multiple locations at once. It is useful for refactoring variable names or repeated patterns.

---

