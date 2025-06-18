# ga1-development-tools-discussion-thread-tds-jan-2025

**post_id:** 575342  
**author:** s.anand  
**timestamp:** 2025-01-02T02:30:03.720Z

# ga1-development-tools-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 1 - Development Tools](https://exam.sanand.workers.dev/tds-2025-01-ga1).

---

**post_id:** 575344  
**author:** s.anand  
**timestamp:** 2025-01-02T02:46:01.490Z

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](/c/docs-discourse/45)! ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

**post_id:** 575782  
**author:** 21f2000370  
**timestamp:** 2025-01-05T04:01:42.024Z

Deadline: 26 Jan 2025, midnight IST

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Please keep an eye on this thread for support.

---

**post_id:** 575795  
**author:** Jivraj  
**timestamp:** 2025-01-05T05:50:28.537Z

---

**post_id:** 575815  
**author:** 21f2000370  
**timestamp:** 2025-01-05T07:56:17.410Z

Here is a description of the image:
image description: The image shows task 16, Move and rename files(0.5 marks). The task describes downloading q-move-rename-files.zip and using mv to move files into an empty folder and renaming them, replacing each digit with the next. The last line is a question "What does running grep .\* | LC\_ALL=C sort | sha256sum in bash on that folder show?"
image text: Move and rename files (0.5 marks)
Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next (i.e. a19b.txt becomes a20b.txt)
What does running grep .\* | LC\_ALL=C sort | sha256sum in bash on that folder show?  
For question 16 of GA1, It says "Rename all files replacing each digit with the next "  
Accepted answer is working only if file names are renamed as  
2h3q9x.txt → 3h4q0x.txt  
eb209nmlca.txt → eb310nmlca.txt  
That means if digit is 9 then next digit should be 0. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) let me know if this is what is expected. since 9->10 or 209 → 210 is not working

---

**post_id:** 576111  
**author:** carlton  
**timestamp:** 2025-01-08T03:45:23.020Z

Hi anant,

Question mentions every digit should be replaced by next one.

In that case 209 would get replaced by 310

---

**post_id:** 576239  
**author:** 23f2003790  
**timestamp:** 2025-01-09T07:32:49.658Z

Hello Sir, When I am following that logic to rename files, assessment check is giving error “Incorrect. Try again.”

---

**post_id:** 576242  
**author:** Jivraj  
**timestamp:** 2025-01-09T08:21:13.611Z

[@21f2000370](/u/21f2000370) Since you have managed to get all the answers correct, I presume there are no further issues w/ Q16.

---

**post_id:** 577689  
**author:** 21f2000370  
**timestamp:** 2025-01-11T08:15:14.939Z

Hi, I am unable to access Graded Assignment 1. Every time I click on the given link, all I can see is this page. Please advise.  
Here is a description of the image:
The image is a document that seems to be an assignment brief. It has the title, the deadline and some instructions.
image text: Tools in Data Science - Graded Assignment 1
Deadline:
Note: Every page reload randomizes the quiz. So don't copy answers from previous attempts. You can submit multiple times.

---

**post_id:** 577736  
**author:** Jivraj  
**timestamp:** 2025-01-11T09:03:17.493Z

Possible reasons for this issue.

1. Disable/remove Ad blocker
2. Disable/remove Tracking blocker (Allow third party cookies)
3. Use Chrome browser
4. Disable Browser extensions

---

**post_id:** 577946  
**author:** 23f1002698  
**timestamp:** 2025-01-11T14:56:07.023Z

As I highlighted earlier, Its not accepting the answer if I follow correct logic for renaming for example 209->210, but it is accepting if rename as 209->310

---

**post_id:** 577949  
**author:** 23f1002630  
**timestamp:** 2025-01-11T15:48:35.599Z

Hi Anant,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f2000370/48/87_2.png) 21f2000370:

> Here is a description of the image:
> image description: A screenshot of a question from a test asking to move and rename files with bash commands. It shows the test number and mark allocation and gives instructions on file renaming and usage of commands grep, sort and sha256sum.
> image text: 16 Move and rename files (0.5 marks)
> Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next (i.e. a19b.txt becomes a20b.txt)
> What does running grep .\* | LC\_ALL=C sort | sha256sum in bash on that folder show?

Here in question, it’s mentioned to replace every digit with next digit, that’s why 209 would be 310.

---

**post_id:** 577987  
**author:** carlton  
**timestamp:** 2025-01-11T17:45:23.526Z

In attempting the third question, I’m unable to download the npm package as it requires docker. When trying to install docker from the installer, it freezes in the verifying package stage. Can somebody please help solve my problem?

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

**post_id:** 577990  
**author:** carlton  
**timestamp:** 2025-01-11T17:48:02.553Z

Image description: A CSS selector question is asked with a text field to input answer.
Image text: Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value
attributes?
Sum of data-value attributes:  
Which HTML content we want to take?

---

**post_id:** 577991  
**author:** 23F300327  
**timestamp:** 2025-01-11T17:02:23.063Z

Hi Suhani,

npm does not require docker.

Kind regards

---

**post_id:** 578158  
**author:** 21f3001993  
**timestamp:** 2025-01-12T07:45:04.116Z

Hi Hisham,

Its described in the question. There is a hidden element hiding somewhere after that question. You would have to inspect the DOM to find it.

---

**post_id:** 578520  
**author:** Samra  
**timestamp:** 2025-01-12T11:13:59.536Z

Here is a description of the image:
The screenshot shows a webpage for a graded assignment on CSS selectors. It includes information on the different types of CSS selectors, such as basic, attribute, and combinator selectors. The page also includes an interactive tool to practice CSS selector skills. The question on the page is "Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value attributes?". The answer provided of "482" is incorrect.
image text: The Mozilla Developer Network (MDN) provides detailed documentation on the three main types of selectors:
• Basic CSS selectors: Learn about element (div), class (.container), ID (#header), and universal (\*) selectors
• Attribute selectors: Target elements based on their attributes or attribute values ([type="text"])
• Combinators: Use relationships between elements (div > p, div + p, div ~ p)
Practice your CSS selector skills with this interactive tool:
• CSS Diner: A fun game that teaches CSS selectors through increasingly challenging levels
Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value
attributes?
Sum of data-value attributes:
482
Incorrect. Try again.  
[@s.anand](/u/s.anand) please guide me through this question, my answer is showing incorrect

---

**post_id:** 578991  
**author:** Jivraj  
**timestamp:** 2025-01-12T21:29:25.964Z

Hello Sir. I am unable to install uv in my windows system. Whenever I run the code provided at the reference link in Powershell, my anti-virus system sends a message that it was blocked. Even after blocking Real-time security, uv does not display. What am I doing wrong?

---

**post_id:** 578993  
**author:** Jivraj  
**timestamp:** 2025-01-12T21:32:38.881Z

Hi, I’m unable to view assignments. below is the screenshot for your reference.  
Here is a description of the image:
The image shows an error message. The error indicates that the site cannot be reached.
image text: This site can't be reached
exam.sanand.workers.dev unexpectedly closed the connection.
Try:
Checking the connection
Checking the proxy and the firewall
Running Windows Network Diagnostics
ERR\_CONNECTION\_CLOSED
Reload
Details

Please suggest me a way to view it. I have allowed third-party cookies as well.

Thanks

---

**post_id:** 578994  
**author:** Jivraj  
**timestamp:** 2025-01-12T21:34:19.477Z

Hi manmeet,

I don’t know about solution to this.  
Some network setting might be causing problem.

Alternatively you can make use of GitHub codespaces which provides 120 hours of free run time in a month. With GitHub codespaces you can use Ubuntu os, and visually it gives you feel of vs code. You can also active your GitHub student developer pack and get 180 hours of GitHub codespaces and some more benefits such as cloud resources and domains.

I have done all questions of week1 and week2 on codespaces only, codespaces works very well if you have good internet connection.

---

**post_id:** 579005  
**author:** 21f3001993  
**timestamp:** 2025-01-13T00:51:15.378Z

Hi samra,

Try installing some other browser see if that works.

---

**post_id:** 579120  
**author:** Nelson  
**timestamp:** 2025-01-13T06:35:28.617Z

Hi mishkat,

Without sharing code, can you pls share your approach how you are trying to solve this question.

---

**post_id:** 579142  
**author:** carlton  
**timestamp:** 2025-01-13T07:21:41.338Z

Ok, thanks. I turned off many security features including anti-virus system’s security and windows security options etc. Then it allowed me to download uv on the system. Now it is running, and I got output as json for Q2.

---

**post_id:** 579152  
**author:** Nelson  
**timestamp:** 2025-01-13T07:43:26.594Z

2 days ago I attempted TDS 2025 Jan GA1 - Development Tools and scored 8.5. I didn’t submit as I wanted to attempt incorrect answer questions.  
When I logged in today it says score is 0.  
Shall I submit or not? Do I have to attempt all questions again?  
Why the assignment and submissions are two separate pages/links?  
If [seek] ([Nptel Seekh](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002)) can access [TDS exam] ([Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga1)) then why we need to submit from seek?

---

**post_id:** 579182  
**author:** carlton  
**timestamp:** 2025-01-13T09:05:08.554Z

The seek portal question is to confirm that the student has seen the GA. It does not actually give you a score. Otherwise students sometimes claim that they looked and did not find any GAs (this has happened in the past). Hence the two stage verification. You still need to ![Screenshot 2025-01-13 at 12.50.02](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/6/d67654c30e9fe72ff5970775fa393eaec8204779.png) the submissions to get a score for the GA.

The actual GA questions are on <https://exam.sanand.workers.dev/> via the seek portal or  
on the [Tools in Data Science](https://tds.s-anand.net/#/) introduction page.

Its just a more robust way of ensuring that students have indeed viewed the GAs.

As far your submission goes, we have your last submission and the score. ![:white_check_mark:](https://emoji.discourse-cdn.com/google/white_check_mark.png?v=12 ":white_check_mark:")

We will check on our end why your submission has not reloaded into your browser.  
Normally these are stored in session storage. So if your browser has deleted them, it might have not loaded from our back end server. [@s.anand](/u/s.anand) will be able to confirm the reason for this problem.

**For the time being if you are making a fresh submission, just fill in all the answers in again, so that your latest submission will be marked correctly.**

Kind regards

---

**post_id:** 579195  
**author:** carlton  
**timestamp:** 2025-01-13T09:26:22.507Z

Thanks [@carlton](/u/carlton).  
I answered questions on <https://exam.sanand.workers.dev/> but didn’t click on the button “Submit Answers” on seek as my answers for 2 questions were incorrect.  
My question is whether I need to submit on seek to save answers on Exam? (I checked my score and saved it on the exam site.)

---

**post_id:** 579264  
**author:** Nelson  
**timestamp:** 2025-01-13T12:52:10.903Z

Hi [@Nelson](/u/nelson)

Your answers on the [exam](https://exam.sanand.workers.dev/) site that have been submitted will be saved and used as the basis for your score. Saying yes/no on seek does not materially impact scoring. Its just an awareness question. Even if you answered yes on the seek portal, you can still revise your answers on the exam site. The final submission is always whats locked in for the score (until the deadline passes).

Kind regards

---

**post_id:** 579294  
**author:** Jivraj  
**timestamp:** 2025-01-13T13:53:22.401Z

It might be because you are not adding up the correct tags with attribute `data-value`. There may be other tags within the same DOM and having the attribute `data-value`.

Kind regards

---

**post_id:** 579347  
**author:** roy2003  
**timestamp:** 2025-01-13T15:55:39.878Z

I am stuck with the last question. SQLite question.  
It gives the error:

```
Error: Got [[121510.39]]...

```

Is it possible to have a more descriptive error? It’s a simple SQL query. I tried various options in my query. I didn’t succeed. ![:thinking:](https://emoji.discourse-cdn.com/google/thinking.png?v=12 ":thinking:")

---

**post_id:** 579358  
**author:** roy2003  
**timestamp:** 2025-01-13T16:09:20.419Z

Hi Nelson,

I checked your set of questions, you are using wrong query to get answer.

kind regards

---

**post_id:** 579359  
**author:** Jivraj  
**timestamp:** 2025-01-13T16:09:33.840Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
In this picture for the given question i have tried in python and chatgpt both are giving same answer still showing wrong. GA1 question  
Here is the image description: The image shows a coding problem asking how many Wednesdays occur between August 9, 1986, and June 19, 2012. The user's input of "1349" is marked as incorrect. The image includes Python code to calculate the number of Wednesdays, which also results in "1349".
image text: "How many Wednesdays are there in the date range 1986-08-09 to 2012-06-19?" and "Number of Wednesdays: 1349"

---

**post_id:** 579363  
**author:** roy2003  
**timestamp:** 2025-01-13T16:12:22.390Z

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
The same issue is happening in the question 12 of GA1. I have given the answer by using collab and gemini , its giving the proper result but showing wrong.  
Here's a description of the image:
\*\*Image description:\*\*
The image shows code written in what appears to be a Python environment. On the right of the screen is a video titled "COMPUTER STUFF THEY DIDN'T TEACH YOU" about character encoding, Unicode, and UTF-8. Underneath the video, there are instructions to download and process three data files with different encodings, and the expected outcome (31512).
\*\*Image text:\*\*
```
# Read the CSV files.
try:
with open(csv\_file\_1\_path, 'rb') as f: # Open in binary mode
rawdata = f.read()
encoding = chardet.detect(rawdata)['encoding'] # Detect encoding
with open(csv\_file\_1\_path, 'r', encoding=encoding) as csv\_file\_1: # Use detected encoding
csv\_data\_1 = csv\_file\_1.read()
# Repeat for csv\_file\_2\_path using the same pattern
with open(csv\_file\_2\_path, 'rb') as f:
rawdata = f.read()
encoding = chardet.detect(rawdata)['encoding']
with open(csv\_file\_2\_path, 'r', encoding=encoding) as csv\_file\_2:
csv\_data\_2 = csv\_file\_2.read()
except FileNotFoundError:
print("Error: One or both of the CSV files could not be found.")
return None
except UnicodeDecodeError:
print("Error: Could not decode one or both of the CSV files.")
return None
# Read the TXT file.
try:
with open(txt\_file\_path, 'rb') as f: # Open in binary mode to detect encoding
rawdata = f.read()
encoding = chardet.detect(rawdata)['encoding'] # Detect encoding
with open(txt\_file\_path, 'r', encoding=encoding) as txt\_file: # Open in text mode with detected encoding
txt\_data = txt\_file.read() # Read the content of the file
except FileNotFoundError:
print("Error: The TXT file could not be found.")
return None
except UnicodeDecodeError:
print("Error: Could not decode the TXT file.")
return None
# Return the contents of the files.
return csv\_data\_1, csv\_data\_2, txt\_data
# Call the function to read the files.
file\_contents = read\_files()
#print("Content of the first CSV file:\n", csv\_data\_1)
#print("\nContent of the second CSV file:\n", csv\_data\_2)
#print("\nContent of the TXT file:\n", txt\_data)
# Combine the content of all files into a single string
all\_content = csv\_data\_1 + csv\_data\_2 + txt\_data
# Split the content into lines
lines = all\_content.split('\n')
# Initialize the total sum
total\_sum = 0
# Iterate through each line
for line in lines:
# Split the line into symbol and value, handling potential extra spaces
try:
parts = line.strip().split(',')
symbol = parts[0].strip() # Remove leading/trailing spaces from symbol
value = parts[1].strip() # Remove leading/trailing spaces from value
# Check if the symbol matches the criteria (using a more robust check)
if symbol in ['€','£','# Euro symbol variations
]: # Add any other known variations of the target symbols
# Convert the value to a number and add it to the total sum
total\_sum += float(value)
except (IndexError, ValueError):
# Ignore lines with incorrect formatting or non-numeric values
pass
# Print the total sum
print("The sum of all values associated with the specified symbols is:", total\_sum)
Enter the path to the first CSV file: /content/data1.csv
Enter the path to the second CSV file: /content/data2.csv
Enter the path to the TXT file: /content/data3.txt
The sum of all values associated with the specified symbols is: 31512.0
COMPUTER STUFF
THEY DIDN'T TEACH YOU
Code Pages, Character Encoding,
Unicode, UTF-8 and the BOM
PART 2
Download and process the files in q-unicode-data.zip which contains three files with diff
data1.csv: CSV file encoded in CP-1252
data2.csv: CSV file encoded in UTF-8
data3.txt: Tab-separated file encoded in UTF-16
Each file has 2 columns: symbol and value. Sum up all the values where the symbol match
What is the sum of all values associated with these symbols?
31512
Try again
```

---

**post_id:** 579370  
**author:** Jivraj  
**timestamp:** 2025-01-13T16:20:28.415Z

Hi Shouvik,

Your code seems correct to me. I think there is an extra space before your answer in input box.

Btw instead of using a while loop, there is a much more optimal, which uses difference of dates and doesn’t require a loop at all. Try to figure it out.

kind regards

---

**post_id:** 579372  
**author:** roy2003  
**timestamp:** 2025-01-13T16:24:09.236Z

yeah thank you sir. now please say for the 2nd problem

---

**post_id:** 579373  
**author:** roy2003  
**timestamp:** 2025-01-13T16:28:28.341Z

Try copy pasting exact symbols `— OR † OR €` Can you share code in code block, it’s difficult to read symbols that are present.

Also have a look at what `all_content` variable contains, see if there are some problem with content.

---

**post_id:** 579413  
**author:** Samra  
**timestamp:** 2025-01-13T18:44:00.191Z

```
!pip install chardet==5.1.0  # Install the chardet library

```

```
import chardet
def read_files():
  """Gets two CSV files and one TXT file from the user and reads them.

Returns:
    A tuple containing the contents of the three files.
  """
    # Get the file paths from the user.
  csv_file_1_path = input("Enter the path to the first CSV file: ")
  csv_file_2_path = input("Enter the path to the second CSV file: ")
  txt_file_path = input("Enter the path to the TXT file: ")

# ... (Get file paths from user - same as before)

# Read the CSV files.
  try:
    with open(csv_file_1_path, 'rb') as f:  # Open in binary mode
      rawdata = f.read()
      encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(csv_file_1_path, 'r', encoding=encoding) as csv_file_1:  # Use detected encoding
      csv_data_1 = csv_file_1.read()

# Repeat for csv_file_2_path using the same pattern
    with open(csv_file_2_path, 'rb') as f:
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']
    with open(csv_file_2_path, 'r', encoding=encoding) as csv_file_2:
        csv_data_2 = csv_file_2.read()

except FileNotFoundError:
    print("Error: One or both of the CSV files could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode one or both of the CSV files.")
    return None

# Read the TXT file.
  try:
    with open(txt_file_path, 'rb') as f:  # Open in binary mode to detect encoding
        rawdata = f.read()
        encoding = chardet.detect(rawdata)['encoding']  # Detect encoding
    with open(txt_file_path, 'r', encoding=encoding) as txt_file:  # Open in text mode with detected encoding
        txt_data = txt_file.read() # Read the content of the file
  except FileNotFoundError:
    print("Error: The TXT file could not be found.")
    return None
  except UnicodeDecodeError:
    print("Error: Could not decode the TXT file.")
    return None

# Return the contents of the files.
  return csv_data_1, csv_data_2, txt_data

# Call the function to read the files.
file_contents = read_files()
if file_contents:
  csv_data_1, csv_data_2, txt_data = file_contents
  #print("Content of the first CSV file:\n", csv_data_1)
  #print("\nContent of the second CSV file:\n", csv_data_2)
  #print("\nContent of the TXT file:\n", txt_data)

# Combine the content of all files into a single string
  all_content = csv_data_1 + csv_data_2 + txt_data

# Split the content into lines
  lines = all_content.split('\n')

# Initialize the total sum
  total_sum = 0

# Iterate through each line
  for line in lines:
    # Split the line into symbol and value, handling potential extra spaces
    try:
      parts = line.strip().split(',')
      symbol = parts[0].strip()  # Remove leading/trailing spaces from symbol
      value = parts[1].strip()   # Remove leading/trailing spaces from value

# Check if the symbol matches the criteria (using a more robust check)
      if symbol in ['€', 'ˆ', '’'  # Euro symbol variations
                     # Add any other known variations of the target symbols
                   ]:
        # Convert the value to a number and add it to the total sum
        total_sum += float(value)

except (IndexError, ValueError):
      # Ignore lines with incorrect formatting or non-numeric values
      pass

# Print the total sum
  print("The sum of all values associated with the specified symbols is:", total_sum)

```

---

**post_id:** 579457  
**author:** Nelson  
**timestamp:** 2025-01-14T05:16:52.135Z

i have given all the symbols correctly sir

---

**post_id:** 579585  
**author:** s.anand  
**timestamp:** 2025-01-14T09:44:05.573Z

Hi Jivraj,

I have tried with a different browser, but still not working. Below is the screenshot for your reference.  
Here is the image description: The image shows an error screen with the message "Your connection was interrupted. A network change was detected. ERR\_NETWORK\_CHANGED." There is a "Refresh" button below the message. An icon of an unplugged network cable is visible on the top left.
Image text: Your connection was interrupted
A network change was detected.
ERR\_NETWORK\_CHANGED
Refresh

Thanks

---

**post_id:** 579626  
**author:** Jivraj  
**timestamp:** 2025-01-14T11:29:34.668Z

One unicode character is in both UPPERCASE and lowercase. Do a case sensitive search.

---

**post_id:** 579703  
**author:** siva.bhaskaran  
**timestamp:** 2025-01-14T14:09:51.502Z

[@Samra](/u/samra) this is almost certainly due to a (typically corporate) firewall or antivirus. Please try with a personal laptop from a public / home network.

(I face this problem at office often. Once, our company’s firewall blocked our own company website ![:confused:](https://emoji.discourse-cdn.com/google/confused.png?v=12 ":confused:"))

---

**post_id:** 579750  
**author:** Samra  
**timestamp:** 2025-01-14T16:07:42.455Z

Hi Nelson,

I checked with your dataset for this particular question. Using correct query I am able to get correct answer. Pls check sql query that you are using.

Kind regards

---

**post_id:** 579774  
**author:** jkmadathil  
**timestamp:** 2025-01-14T17:01:24.559Z

What is the windows equivalent of sha256sum?

```
npx -y prettier@3.4.2 README.md | sha256sum.
sha256sum. : The term 'sha256sum.' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct 
and try again.
At line:1 char:35
+ npx -y prettier@3.4.2 README.md | sha256sum.
+                                   ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (sha256sum.:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

```

---

**post_id:** 579779  
**author:** jkmadathil  
**timestamp:** 2025-01-14T17:16:08.652Z

[@s.anand](/u/s.anand) Actually, I’m using a personal laptop. Is this country dependent or restricted?

---

**post_id:** 579782  
**author:** siva.bhaskaran  
**timestamp:** 2025-01-14T17:23:26.237Z

Check [this link from akamai](https://techdocs.akamai.com/download-ctr/docs/verify-checksum#:~:text=In%20a%20command%20line%2C%20run,in%20the%20Download%20Center%20interface.)

---

**post_id:** 579784  
**author:** siva.bhaskaran  
**timestamp:** 2025-01-14T17:28:24.767Z

Did you try the following:

* `ping exam.sanand.workers.dev`
* `tracert exam.sanand.workers.dev`

This is what I got while doing this:

```
ping exam.sanand.workers.dev

Pinging exam.sanand.workers.dev [104.21.31.149] with 32 bytes of data:
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=8ms TTL=58
Reply from 104.21.31.149: bytes=32 time=9ms TTL=58

Ping statistics for 104.21.31.149:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 8ms, Maximum = 9ms, Average = 8ms

```

```
tracert exam.sanand.workers.dev

Tracing route to exam.sanand.workers.dev [104.21.31.149]
over a maximum of 30 hops:

1     2 ms     2 ms     2 ms  192.168.18.1
  2     5 ms     6 ms     4 ms  10.122.0.1
  3     *        *        6 ms  172.17.0.2
  4     5 ms     5 ms     4 ms  172.17.0.109
  5    16 ms     8 ms     8 ms  10.8.1.2
  6    21 ms     8 ms     8 ms  103.70.37.171
  7    10 ms     8 ms     8 ms  104.21.31.149

Trace complete.

```

You could also [try switching Google Public DNS](https://developers.google.com/speed/public-dns/docs/using) and see if the site is getting picked up in your next query.

### Helpful Resources

1. [Ping+Tracert](https://www.okta.com/identity-101/ping-trace/#:~:text=Ping%20traceroute%20test.%20Traceroute%20is%20like%20a,takes%20them%20to%20get%20from%20each%20point.) for troubleshooting network connections
2. [Product pages](https://docs.nexthink.com/platform/user-guide/applications/managing-applications/configuring-web-applications/common-web-application-errors/err_network_changed) for `err_network_changed` error
3. [Network Troubleshooting](https://www.comptia.org/content/guides/a-guide-to-network-troubleshooting) skills and commands

---

**post_id:** 579785  
**author:** jkmadathil  
**timestamp:** 2025-01-14T17:30:56.568Z

Thank you JK. I have another question. I should have asked that before this

```
npx -y prettier@3.4.2 README.md 
npm ERR! code E404
npm ERR! 404 Not Found - GET https://registry.npmjs.org/README.md - Not found
npm ERR! 404 
npm ERR! 404  'README.md@latest' is not in the npm registry.
npm ERR! 404 Your package name is not valid, because 
npm ERR! 404  1. name can no longer contain capital letters
npm ERR! 404
npm ERR! 404 Note that you can also install from a
npm ERR! 404 tarball, folder, http url, or git url.

npm ERR! A complete log of this run can be found in:
npm ERR!     C:\Users\sivab\AppData\Roaming\npm-cache\_logs\2025-01-14T17_22_04_622Z-debug.log
Install for [ 'README.md@latest' ] failed with code 1

```

This is throwing an error. Please help

---

**post_id:** 579869  
**author:** 23f2000237  
**timestamp:** 2025-01-15T05:06:11.291Z

**This is regarding Question 11.**

I have extracted all the elements and added them manually. Tried all the options. Not even one appears to be correct . I evne tried ChatGPT which gave the answer as 411. Which of the following should be chosen?

```
<div class="d-none" title="This is the hidden element with the data-value attributes">
        <div class="bar baz" data-value="17">
          <div class="baz foo" data-value="29"></div>
          <div class="foo" data-value="20"></div>
        </div>
        <div class="bar foo baz" data-value="71">
          <div class="foo" data-value="48"></div>
          <span class="foo" data-value="30"></span>
          <div class="foo bar" data-value="90">
            <div class="bar" data-value="8"></div>
            <div class="" data-value="48"></div>
          </div>
        </div>
        <div class="baz foo" data-value="58">
          <div class="baz foo" data-value="19"></div>
          <div class="foo bar" data-value="76"></div>
        </div>
        <div class="bar baz" data-value="89">
          <div class="foo bar" data-value="38"></div>
          <div class="foo bar" data-value="9"></div>
        </div>
      </div>

```

---

**post_id:** 579893  
**author:** s.anand  
**timestamp:** 2025-01-15T06:33:32.561Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/siva.bhaskaran/48/12463_2.png) siva.bhaskaran:

> `npx -y prettier@3.4.2 README.md`

Shouldn’t it be `npx -y prettier@3.4.2 --write README.md` or `npx prettier README.md` (Depending on whether to write or read)?

Apologies, I may not know full context of the question, as I haven’t attempted GA1 fully yet

---

**post_id:** 580021  
**author:** 23f1002382  
**timestamp:** 2025-01-15T12:46:45.751Z

I had this same doubt, I tried by adding the “span” tag’s value too it showed correct for me. I’d suggest you to try that.

---

**post_id:** 580630  
**author:** daksh76  
**timestamp:** 2025-01-16T15:27:41.211Z

Oh, good catch, [@23f2000237](/u/23f2000237) and [@siva.bhaskaran](/u/siva.bhaskaran) - I made a mistake in the evaluation script. It included the `span`.

I fixed it. Note: None of the earlier answers are affected, i.e. if you got it right earlier, it’ll stay right.

---

**post_id:** 580631  
**author:** daksh76  
**timestamp:** 2025-01-16T15:29:18.243Z

7. **It’s hackable**. It’s possible to get the answer to *some* questions by hacking the code for this quiz. That’s allowed.

What does exactly mean, if someone could elaborate without giving it away, please?  
[@carlton](/u/carlton)

---

**post_id:** 580955  
**author:** 23F3002987_J_SRI_BAL  
**timestamp:** 2025-01-17T10:39:40.125Z

I have tried but still am unable to do only that question if someone can help me with the code because everytime im getting a different answer its my last question

---

**post_id:** 581403  
**author:** Jivraj  
**timestamp:** 2025-01-17T22:25:12.477Z

[@21f2000370](/u/21f2000370) i hope you wouldve completed it

---

**post_id:** 581546  
**author:** daksh76  
**timestamp:** 2025-01-18T08:28:25.019Z

Use Git bash the problem will be resolved

---

**post_id:** 581584  
**author:** 24DS1000121_ULAGAOOZ  
**timestamp:** 2025-01-18T09:57:08.186Z

Hi Daksh,

Did you solve it or still facing some issues with it ?

Kind regards

---

**post_id:** 581612  
**author:** 24f1002359  
**timestamp:** 2025-01-18T11:40:38.844Z

im still facing issue in that questioneven after watching the youtube video given and taking help of chatgpt im unable to solve that question only

---

**post_id:** 581723  
**author:** Divya1  
**timestamp:** 2025-01-18T17:41:31.939Z

Hello Gentlemen Instructors,

In all the video lectures, I am first required to download the tools, install them on my computer ? Is it not going to overload my computer’s RAM etc.,  
In one of the classes, you said that there is something - colab like cloud wherein we can go and practice without overloading our own computers. Will you please let me know how to go about it ??  
Thanks and regards,  
ULAGAOOZHIAN,  
France  
24ds1000121

---

**post_id:** 581819  
**author:** huzaifa  
**timestamp:** 2025-01-19T05:53:14.881Z

Here is the image description: Image shows a powershell terminal with text regarding hash algorithms and file paths.
image text: PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
>>
PS C:\Users\kaiff> Get-FileHash -Path formatted.md -Algorithm SHA256
>>
Algorithm Hash Path
SHA256 216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175 C:\Users\kaiff\formatted.md
PS C:\Users\kaiff> npx -y prettier@3.4.2 "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md" > formatted.md
• >> Get-FileHash -Path formatted.md -Algorithm SHA256
>>
Algorithm Hash Path
SHA256 216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175 C:\Users\kaiff\formatted.md
PS C:\Users\kaiff> npx -y prettier@3.4.2 "F:\BS DATA SCIENCE\Diploma Level\TERM 2\TDS\README.md" > formatted.md
>>
PS C:\Users\kaiff> certutil -hashfile formatted.md SHA256
>>
SHA256 hash of formatted.md:
216375d6f5a1daf9eb6350251e9f0a7395a0b2988d58ed6e57d9568e8b1ad175
CertUtil: -hashfile command completed successfully.
PS C:\Users\kaiff>

In question 3 of GA-1 while checking the answer it’s showing incorrect answer.

216375D6F5A1DAF9EB6350251E9F0A7395A0B2988D58ED6E57D9568E8B1AD175

This was the output which I got after the execution of the given code in the question.Kindly guide If I did some error or error in entering the value.

---

**post_id:** 581952  
**author:** 23f2005067  
**timestamp:** 2025-01-19T10:52:20.968Z

how to calculate How many Wednesdays are there in the date range 1981-08-30 to 2017-07-17?

The dates are in the year-month-day format. Include both the start and end date in your count. You can do this using any tool (e.g. Excel, Python, JavaScript, manually).

---

**post_id:** 581956  
**author:** 23f2003751  
**timestamp:** 2025-01-19T10:58:50.978Z

=SUM(TAKE(SORTBY({3,7,13,8,7,7,11,11,13,14,0,13,9,14,10,7}, {10,9,13,2,11,8,16,14,7,15,5,4,6,1,3,12}), 1, 16))

I do not have the required excel version can someone please tell how can I find the solution to this one?

---

**post_id:** 581980  
**author:** s.anand  
**timestamp:** 2025-01-19T12:20:46.664Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
Sir i have saved the answers 2 days ago and scored around 7.5 . now when i open the portal today it is showing as 0 and all the answers has been cleared. how can i restore it.

---

**post_id:** 582040  
**author:** 23f2005067  
**timestamp:** 2025-01-19T13:47:07.641Z

yes same issue with me as well.2 3 days back i have answered and saved all the questions and today it is showing me 0 and all the answers are gone

---

**post_id:** 582261  
**author:** Rohitkumar7463  
**timestamp:** 2025-01-19T17:02:23.982Z

[@23f2005067](/u/23f2005067) [@23f2003751](/u/23f2003751) I added a “Recent saves” feature.

This will show the time and score for the last 3 times you saved. You can load from any of these.

Here is a description of the image:
The image displays a list of recent saves. Each entry shows a "Reload" button, followed by the date and time of the save and the corresponding score. The first entry is from 19/1/2025, 8:17:25 pm with a score of 1.25, the second is from 19/1/2025, 8:01:54 pm with a score of 0.25 and the third is from 14/1/2025, 9:23:11 pm with a score of 0.
image text: Recent saves
Reload from 19/1/2025, 8:17:25 pm. Score: 1.25
Reload from 19/1/2025, 8:01:54 pm. Score: 0.25
Reload from 14/1/2025, 9:23:11 pm. Score: 0

Do remember to click the “Check” button to calculate your score. That is not automatic.

Please check this out and let me know if there are any bugs. Thanks.

---

**post_id:** 582210  
**author:** 23f2003845  
**timestamp:** 2025-01-20T05:27:14.301Z

Here is the image description: The image displays a mobile screen showing a list of programming questions and recent saves, with a deadline set for January 26, 2025.
image text: Due Sun, 26 Jan, 2025, 11:59 pm IST
Recent saves
Reload from 19/01/2025, 16:22:36. Score: 0
Reload from 19/01/2025, 16:16:38. Score: 0
Reload from 19/01/2025, 16:16:02. Score: 0
Questions
1. VS Code Version (0.25 marks)
2. Make HTTP requests with uv (1 mark)
3. Run command with npx (0.5 marks)
4. Use Google Sheets (0.25 marks)
5. Use Excel (0.25 marks)
6. Use DevTools (0.5 marks)
7. Count Wednesdays (0.5 marks)
8. Extract CSV from a ZIP (0.25 marks)
9. Use JSON (0.75 marks)
10. Multi-cursor edits to convert to JSON (0.5
marks)
11. CSS selectors (0.5 marks)
12. Process files with different encodings (1 mark)
13. Use GitHub (0.5 marks)
14. Replace across files (0.75 marks)
15. List files and attributes (0.75 marks)
16. Move and rename files (0.5 marks)
17. Compare files (0.5 marks)  
Sir i might already clicked 3 save todays. So the previous clicks dates are of today. And the same 0 score is showing this.

---

**post_id:** 582264  
**author:** carlton  
**timestamp:** 2025-01-20T07:26:25.067Z

Sha256sum is not recognized as an internal or external command how to solve this plzz answer  
[@carlton](/u/carlton)

---

**post_id:** 582366  
**author:** iamsarthak  
**timestamp:** 2025-01-20T12:44:15.933Z

If you are on windows, you might not be able to use sha256sum.

Here are two disussions that might help you out.

* [Discussion 1](https://stackoverflow.com/questions/72087842/windows-equivalent-to-sha256sum-c-cryptographic-hash-digest-file-recursive)
* [Discussion 2](https://stackoverflow.com/questions/11746287/compare-filehash-in-powershell)

---

**post_id:** 582375  
**author:** s.anand  
**timestamp:** 2025-01-20T13:09:10.672Z

[@Rohitkumar7463](/u/rohitkumar7463) [@23f2003845](/u/23f2003845)

If you are on Windows Powershell  
Then instead of `sha256sum` you can simply use `Get-FileHash`

Send the output of the `npx -y prettier@3.4.2 README.md` to a text file eg. `output.txt` and then use `Get-FileHash` on powershell with the `output.txt` and it will use sha256 by default and give you the exact same output.  
You might be able to pipe the data directly to `Get-FileHash` but I have not tried direct piping. The above method works guaranteed.

Kind regards

---

**post_id:** 582382  
**author:** 23f2000573  
**timestamp:** 2025-01-20T13:16:50.351Z

[@s.anand](/u/s.anand) Sir

as you said in the previous post, the evaluation script is also updated based on errors other students point out.

I am submitting my answers as soon as the GA is released and stopping once I get 10/10.

Will you reevaluate the answers once the deadline is over? Or the marks I see right now will be set in stone?

If you will, then it will be based on the updated evaluation script which can reduce my marks.

Here is a description of the image:
The image shows a screen capture of an interface with a green background and white text indicating a score of 10/10. Below this, a section titled "Recent saves" lists a save point labeled "Reload" from "20/1/2025, 6:05:24 PM" with a score of 10.
image text: 6 Jan 2025 at 11:59 PM IST Score: 10 / 10
Recent saves
Reload from 20/1/2025, 6:05:24 PM. Score: 10

---

**post_id:** 582391  
**author:** s.anand  
**timestamp:** 2025-01-20T13:22:56.326Z

[@iamsarthak](/u/iamsarthak) – as long as you don’t save again, your score will stay 10, even if I modify the evaluation script ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

We don’t re-evaluate previous results in the graded assignments.

---

**post_id:** 582427  
**author:** Rohitkumar7463  
**timestamp:** 2025-01-20T15:16:02.988Z

[@s.anand](/u/s.anand) sir,

Question 15 is under the section for linux

I got the file which needs to be processed to answer the question

Here is the image description: Table with columns labeled "Length", "Date", "Time", and "Name" with some data under them.
image text: Length Date Time Name
4094 2004-03-10 07:49 file0.txt
8410 2007-02-11 18:46 file1.txt
8062 2000-01-26 13:40 file2.txt
9748 2010-09-27 00:34 file3.txt

I can solve this now using pandas.

From learning perspective, is this question aimed at making students to use something like awk or is it fine if i can carry on with pandas?

---

**post_id:** 582480  
**author:** Divya1  
**timestamp:** 2025-01-20T17:05:52.439Z

[@23f2000573](/u/23f2000573) You can solve it with any tool you’re comfortable with, including pandas.

But since you *already* know how to do it with pandas, I suggest you explore how to do it with something like `awk` (or any other tool) to get a broader exposure into different approaches.

---

**post_id:** 582510  
**author:** 23f1002382  
**timestamp:** 2025-01-20T18:28:45.385Z

Here is a description of the image and the text found :
image description: The image shows a PowerShell terminal output. The user navigates to the "downloads" directory and encounters an error when trying to change directory to "Downloads" because it doesn't exist. Subsequently, a command using "npx" and "prettier" is executed, and the Get-FileHash command is used to calculate the hash of the file named "output.txt" , the hash algorithm is SHA256 and it displays its value.
image text: Try the new cross-platform PowerShell https://aka.ms/pscore6
PS C:\Users\HP> cd downloads
PS C:\Users\HP\downloads> cd Downloads
Read: Cannot find path 'C:\Users\HP\downloads\Downloads' because it does not exist.
At linesl cher:1
cd Dounloads
→ CategoryInfo
eption
: ObjectNotFound: (C:\Users\HP\downloads\Downloads:String) [Set-Locat
- FullyQualifiedErrorId: PathNot Found, Microsoft.PowerShell.Commands.SetLocationCommand
PS C:\Users\HP\downloads> npx -y prettier@3.4.2 README.md >output.txt
PS C:\Users\HP\downloads > Get-FileHash.\output.txt
Algorithm
SHA256
Hash
7EA1921069EAA2FDA9F6B5143A291C894CDC59E6CF6DBAA9EC8FFD4449A8F7E5
Path
C:\Users\HP
PS C:\Users\HP\downloads>>>>
>> Algorithm
>>>
>> SHA256
Hash
7EA1921069EAA2FDA9F6B5143A291C894CDC59E6CF6DBAA9EC8FFD4449A8F7E5
Path
C:\Users\  
Sir is it right of sha sum question

---

**post_id:** 582511  
**author:** 23f2000573  
**timestamp:** 2025-01-20T18:31:41.213Z

to pass the graded 1 how much points are required for 10 ?

---

**post_id:** 582562  
**author:** carlton  
**timestamp:** 2025-01-21T04:01:30.251Z

use chatgpt for the solution(sum(take(sortby))), it will give you the wrong answer but explain the concepts, use that go to colab and code one solution(will take abt 2 mins)

---

**post_id:** 582689  
**author:** 22f1000535  
**timestamp:** 2025-01-21T09:57:52.249Z

I used

<https://www.microsoft365.com/launch/excel?auth=1>

---

**post_id:** 582989  
**author:** gokulvasudevan.s  
**timestamp:** 2025-01-21T21:18:33.350Z

[@Rohitkumar7463](/u/rohitkumar7463) The hash code is exactly what you see under the column Hash,

7E…E5

Thats the Hash code for the file output.txt

A Hash is a *nearly* unique representation of some data within some range dependent on the type of hashing algorithm and the amount of unique pieces of data that need to be encoded. (just my colloquial definition of it, i am sure you are able to ask GPT to give you a much better explanation)

Kind regards

---

**post_id:** 582996  
**author:** 24f1001769  
**timestamp:** 2025-01-22T00:55:39.421Z

**Time Zone Issues with the “List Files and Attributes” Question**

quick heads‐up about Question 15 (the one asking for files at least 8143 bytes, modified on or after Sun, 19 Nov 2006, 7:38 am GMT‑5). I’m physically in a different time zone, but I eventually discovered the question seems to expect you to be located in India and to interpret that files date/time accordingly.  
I got the correct answer once i localized the files timestamp to IST.

thanks

---

**post_id:** 583634  
**author:** 23f3002537  
**timestamp:** 2025-01-22T16:45:35.859Z

GA1 Q18. What is the total sales of all the items in the “Gold” ticket type? Write SQL to calculate it.

I always get the answer in a nested array. Error: Got [[51006.69]]…  
I could not use cursor in that shell, to extract the value also.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Please help me with this.

---

**post_id:** 583746  
**author:** Sudhishnarayan  
**timestamp:** 2025-01-22T17:49:14.094Z

image description: The image shows a JSON data structure containing email address and headers among other things. The "email" value is "241001769@ds.study.iitm.ac.in" and the "url" value is "https://httpbin.org/get?email=241001769%40ds.study.iitm.ac.in".
image text: "args": {
{
"email": "241001769@ds.study.iitm.ac.in"
},
"headers": {
},
"Accept":
"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US, en;q=0.9,en-IN;q=0.8",
"Dnt": "1",
"Host": "httpbin.org",
"Priority": "u=0, i",
"Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "\"Windows\"",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
"X-Amzn-Trace-Id": "Root=1-67903bee-5b25fdd838b5abb00263808c"
"origin": "45.118.156.154",
"url": "https://httpbin.org/get?email=241001769%40ds.study.iitm.ac.in"
}  
I am getting error in the uv question.  
I have got the output json but I cant understand what part do I need to submit in the answer section.

---

**post_id:** 583765  
**author:** Sudhishnarayan  
**timestamp:** 2025-01-22T17:56:51.809Z

image description: The image shows instructions for a task about moving and renaming files and input box with user input and incorrect mark in red indicating that the user input is wrong with the message "Incorrect. Try again."
image text:
Move and rename files (0.5 marks)
Download q-move-rename-files.zip and extract it. Use mv to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt.
What does running grep \* LC\_ALL=C sort | sha256sum in bash on that folder show?
f1056c0b734ac835d17e8129fe9dc9a85ebcca45a82de42b13d18b7816808b7d \*
Incorrect. Try again.  
Sir I’m facing issue in this question even though i have done every thing as it mentioned. Can I get hint of the mistake for my code snippet.  
My code: -

```
mkdir all_files
find parent/ -type f -exec mv {} all_files/ \;
for file in all_files/*; do
    new_name=$(echo "$file" | sed 's/[0-9]/\n&\n/g' | awk '
    { 
        if ($0 ~ /^[0-9]$/) print ($0 == "9") ? 0 : $0+1; 
        else print $0 
    }' | tr -d "\n")
    mv "$file" "$new_name"
done

```

---

**post_id:** 583848  
**author:** Yogesh1  
**timestamp:** 2025-01-23T03:08:20.003Z

Good Evening, I have a doubt regarding the SQL Question I have attached my query. Please clarify me where I got wrong. I tried changing the gold string to lower and checking it. Even, that didn’t work.  
Here is the image description:
The image shows a SQL query inside a code editor with an error. The user wants to calculate the total sales of all items in the "Gold" ticket type. The query is:
```sql
SELECT SUM(Units\*Price) FROM tickets WHERE TYPE == 'Gold';
```
However, the query resulted in an error which is `Error: Got [[42810.5]]...`
The image also gives instructions to ignore spaces and treat misspellings as "Gold", also calculate sales as Units \* Price and sum them up.
image text: SELECT SUM(Units\*Price) FROM tickets WHERE TYPE == 'Gold';
Error: Got [[42810.5]]...
Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units \* Price, and sum them up.  
Thank You.

---

**post_id:** 583940  
**author:** 23f3002537  
**timestamp:** 2025-01-23T07:05:58.642Z

I have another doubt regarding the CSS Selector question. I know how to select elements using CSS Selector but i don’t know how to get the sum using CSS Selectors as it cannot perform arithmetic operations. And also, I didn’t understand the question completely about the ‘hidden element’. Please clarify it. Thank you so much.  
Here is the description of the image:
The image shows a prompt related to CSS selectors asking to find all `<div>` elements with a "foo" class within a hidden element and calculate the sum of their "data-value" attributes. There is an input field for the user to enter the sum. The feedback given indicates that the previous attempt was "Incorrect. Try again."
image text: Let's make sure you know how to select elements using CSS selectors. Find all <div>s having a foo class in the hidden element below. What's the sum of their data-value
attributes?
Sum of data-value attributes:
Incorrect. Try again.

---

**post_id:** 583941  
**author:** 23f3002537  
**timestamp:** 2025-01-23T07:08:00.410Z

It can be GOLD,gold, or even GoLD.

" Get all rows where the Type is “Gold”. Ignore spaces and treat mis-spellings like GOLD, gold, etc. as “Gold”. Calculate the sales as Units \* Price, and sum them up. "

---

**post_id:** 584306  
**author:** 22f2001175  
**timestamp:** 2025-01-24T05:03:53.843Z

Try to go through the given video of css selector and go through all foo classes carefully(using inspect) and sum them up!

---

**post_id:** 584470  
**author:** 23f1001754  
**timestamp:** 2025-01-24T10:37:08.553Z

Try to remove the White spaces in your code!

---

**post_id:** 584693  
**author:** Jivraj  
**timestamp:** 2025-01-25T05:04:27.652Z

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
sir i have gone through the process of solving the ques but still ans is showing wrong even i have used chatgpt and used cmd also. the cmd is is showing the result still ans is wrong  
Here are the bounding box detections:
```json
[
{"box\_2d": [102, 0, 247, 154], "label": "text"},
{"box\_2d": [102, 154, 248, 221], "label": "text"},
{"box\_2d": [250, 0, 368, 1000], "label": "text"},
{"box\_2d": [773, 41, 787, 253], "label": "text"},
{"box\_2d": [773, 253, 787, 257], "label": "text"},
{"box\_2d": [799, 39, 813, 716], "label": "text"},
{"box\_2d": [824, 38, 837, 633], "label": "text"},
{"box\_2d": [879, 38, 894, 927], "label": "text"}
]
```
image description: A task that requires downloading a zip file, extracting it, and using a tool such as ls to list files and find the total size of files with specific size and modification date requirements. The answer provided was incorrect, with a warning against copying directly from the ZIP or using Windows Explorer for extraction due to timestamp issues. The suggestion is to use tools like unzip or 7-Zip. Also present in the image is a command line/terminal output with file size, counts and parameters.
image text: 24-01-2025 09:57 to 24-01-2025 09:57
5950 file84.txt
7732 file85.txt
9867 file86.txt
1061 file87.txt
2870 file88.txt
6786 file89.txt
9749 file9.txt
1070 file90.txt
3308 file91.txt
3452 file92.txt
5286 file93.txt
2852 file94.txt
9044 file95.txt
8630 file96.txt
4636 file97.txt
7559 file98.txt
2698 file99.txt
100 File(s)
513187 bytes
2 Dir(s)
74610814976 bytes free
C:\Users\lakshika\Downloads\q-list-files-attributes>for /F "tokens=5\*" %A in ('dir /T:W/-C ^| findstr /R "^[ ]\*[1-9][0-9]{3,}"') do @echo %A %B
C:\Users\lakshika\Downloads\q-list-files-attributes>powershell -Command "& { Get-ChildItem -Path -File | Where-Object { $\_.Length -ge 1235 and $\_.LastWriteTime -ge '11/06/2019 10:48:00' } | Measure-Object -Property Length -Sum }"
Count : 91
Average:
Sum : 507182
Maximum :
Minimum:
Property: Length
C:\Users\lakshika\Downloads\q-list-files-attributes>powershell -Command "& { Get-ChildItem -Path -File | Where-Object { $\_.Length -ge 1235 and $\_.LastWriteTime -ge '11/06/2019 10:48:00' } | Out-File -FilePath result.txt }"
C:\Users\lakshika\Downloads\q-list-files-attributes>
List files and attributes (0.75 marks)
Download q-list-files-attributes.zip and extract it. Use 1s with options to list all files in the folder along with their date and file size.
What's the total size of all files at least 1235 bytes large and modified on or after Wed, 6 Nov, 2019, 10:48 am IST?
507182
Incorrect. Try again.
Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps.

---

**post_id:** 584707  
**author:** Jivraj  
**timestamp:** 2025-01-25T05:40:24.502Z

In GA1, Question no: 9.  
when i sort the json it says incorrect. but i validated that json using validator and also manually

admin : could you pls validate my answer pls

---

**post_id:** 584709  
**author:** Jivraj  
**timestamp:** 2025-01-25T05:46:17.852Z

You need to submit whole json becausae In this image `headers` is part of response, not request headers.

---

**post_id:** 584719  
**author:** Jivraj  
**timestamp:** 2025-01-25T06:05:38.597Z

Hi Arnav,

I tried your script on your dataset.  
Problem might be you are not executing `grep . * | LC_ALL=C sort | sha256sum` in correct directory, you would need to execute it from `all_files` directory also there should not be any extra file other than that gets generated.

---

**post_id:** 584730  
**author:** 23f1001754  
**timestamp:** 2025-01-25T06:39:59.261Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f2001175/48/114560_2.png) 22f2001175:

> Here's a description of the image you provided:
> \*\*Image Description:\*\*
> The image shows a computer screen displaying command-line interface (CLI) output and a snippet of a web page. The CLI output seems to be results from running commands related to file listing and manipulation in a directory. The webpage part seems to be part of an online assessment or exercise related to listing files and their attributes from a downloaded ZIP file. There's an input field where an answer has been entered ("507182"), which is marked as incorrect.
> \*\*Image Text:\*\*
> \* \*\*CLI Output:\*\* A series of date-time stamps followed by file names (e.g., "24-01-2025 09:57 5950 file84.txt"), along with directory counts and byte information. There are also PowerShell commands being executed to filter and measure file attributes.
> \* \*\*Webpage Text:\*\*
> \* "List files and attributes (0.75 marks)"
> \* "Download q-list-files-attributes.zip and extract it. Use 1s with options to list all files in the folder along with their date and file size."
> \* "What's the total size of all files at least 1235 bytes large and modified on or after Wed, 6 Nov, 2019, 10:48 am IST?"
> \* "507182" (as an answer input)
> \* "Incorrect. Try again."
> \* "Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps."
>
> Untitled design1414×2000 349 KB

Time of modification of each of these files is 14 Jan 2025 which might be the day you unzipped them. Depending upon what software you use it might change modification date while unzipping. use unzip command line tool or winrar extractor, these are 2 tools we have tested.

kind regards

---

**post_id:** 584732  
**author:** Sakshi6479  
**timestamp:** 2025-01-24T13:26:45.607Z

Hi Saravanan,

I noticed an issue with your submission. In the question, there is a name `Bob`, but it doesn’t appear in your answer after applying the required sorting. Since the data for each student is dynamically generated and unique, the answer you submitted seems inconsistent with your dataset.

We encourage collaboration among students, but copying answers is not acceptable. Instead, I suggest reaching out to your friend to understand the script they used, run it on your dataset, and ensure you fully grasp the solution.

kind regards

---

**post_id:** 584798  
**author:** 25ds1000038  
**timestamp:** 2025-01-25T09:05:37.365Z

Thanks lot jivraj. i updated my script and answers too

Thanks

---

**post_id:** 584906  
**author:** 23f2002592  
**timestamp:** 2025-01-25T11:42:28.917Z

Here's the image description:
The image shows a screen with text "JSON Hash" at the top followed by several lines of data that appears to be a long string of alphanumeric characters and symbols, resembling a hash output. Below it, there is a button with text "Hash" and the error message "Error: Expected property name or '}' in JSON at position 1 (line 1 column 2)".
image text:
JSON Hash
потајка: DCIVYWY, Z: IMG, Zylw: 169GFKIVIX, C: IXYVIDASET, v: Can, Mup: URUSIQI, SIYNcajti F, QUI: CHINI46M, MTQIKIM:
ybCLb85bY2, aNbP76ziv: sBQOK1, 4×5UK: Ee, OlJsMcBmN: AM, c: f87lhjpU, vxl2xROEf: 6AtHge, D9Oh3u: CNMccZwTjM, WYQ:
BoTRdy, 34jW0iee: N80sybsVoR, bSmt6kBkBH: Do9KIGnT, Amcn: hwK7xwwS, r: V0hRife, fu4VxHz: 1ER5wrY, j5dT4: j5B, w: czu,
TesBfbosJr: QOD, HGMF: Cy7le, E: 4Vg6, VArd1Mw: uSoz9wyUny, e: M5At5z5K, h2k: Ud1, bV: qCDIEQKq, AeYpQ8n: EnbvW,
jZvNt2oUe: nHUIFvSA, 5Bc: i3LQYi04J, d7xZ4: B, dr74a49z: VSZBxKgr, qLBei3zM: nTw1DPI51, TBd: 0MWuzufrAc, YUhsxyO1y:
XOFE, KF: veDbq, 8RmIU84ag: sMQ2k, 7EfO9Nvh: VLPwC94, dnOyE: q1kX5uF, 7NU: pHx2g58Ze3, t9ov7: BgbO398, 4hr: z7, jm:
7vG7, Tlp3: mZeYwNHj, 5Sy3mG: TCearJVzqK, f7CZ: Z}
Hash
Error: Expected property name or '}' in JSON at position 1 (line 1 column 2)  
In the question 10 what should be the correct format for jason data as I edited the data according to given conditions but in Hash I am facing problem again and again

Also, in Q11 What is meaning of element below given in the question " Let’s make sure you know how to select elements using CSS selectors. Find all `<div>` s having a `foo` class in the hidden element below. What’s the sum of their `data-value` attributes?"

---

**post_id:** 585183  
**author:** 23f2000098  
**timestamp:** 2025-01-25T18:32:03.063Z

Here is the image description: The image shows a question about the terminal output of `code -s`.
image text: AI Editors: Copilot, Cursor
Note: AI Editors like Cursor, Cody, and GitHub Copilot use LLMs to help you write code faster.
These are built on top of VS Code. These are now a standard tool in every developer's toolkit. Please use them.
Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below.
What is the output of code -s?
Incorrect. Try again.  
what sort of response am i supposed to put ?? the response i am getting ,it says incorrect, basically after doing code -s ,i get like info about the version of vs code and info about cpu gpu etc…

---

**post_id:** 585200  
**author:** 23f2001188  
**timestamp:** 2025-01-25T18:55:30.353Z

Here is a description of the image:
The image shows a task description with steps, followed by a question about running a command in bash. Below the question, there's an incorrect answer and a message indicating that the answer is incorrect.
image text: Download q-replace-across-files.zip and unzip it into a new folder, then replace all "IITM" (in upper, lower, or mixed case) with "IIT Madras" in all files. Leave everything as-is-
don't change the line endings.
What does running cat \* | sha256sum in that folder show in bash?
63144b28ad1d2bd5b9b4b0855cab6a4a4fa8d57ed2ed826b4f5b36d12ae97347
Incorrect. Try again.

The answer is wrong but I have done every step correctly. Help

---

**post_id:** 585208  
**author:** 23f2000098  
**timestamp:** 2025-01-25T19:24:50.295Z

Here is a description of the image:
The image shows a visual of uv package and project manager with running commands and text along with errors.
image text: Running uv run --with httpie https [URL] installs the Python package httpie and sends a HTTPS request to the URL.
Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter email set to 23f2000098@ds.study.iitm.ac.in
What is the JSON output of the command? (Paste only the JSON body, not the headers)
{'args':{'email':'23f2000098@ds.study.iitm.ac.in'},'origin':'106.197.103.245','url':'https://httpbin.org/get?email=23f2000098%40ds.study.iitm.ac.in'}
SyntaxError: Expected property name or '}' in JSON at position 1 (line 1 column 2)  
Not sure how to resolve this error… any sugessions ?

---

**post_id:** 585216  
**author:** Sakshi6479  
**timestamp:** 2025-01-25T19:45:45.630Z

first convert in into jason using bash or other terminal then paste the converted json content to this page and generate the json hash

---

**post_id:** 585248  
**author:** sarvan108  
**timestamp:** 2025-01-25T22:26:09.529Z

I am getting errors for the host part please guide me

---

**post_id:** 585249  
**author:** sarvan108  
**timestamp:** 2025-01-25T22:33:14.271Z

But I have converted the file as it says in the question still i am getting error that I am unable to understand. Can you just tell me please what formatted answer should be that is just the type of answer it’s asking?

---

**post_id:** 585252  
**author:** sarvan108  
**timestamp:** 2025-01-25T22:44:44.192Z

I tried this. For me still the answer is incorrect.

Here is a description of the image:
The image is a screenshot of a terminal window showing a series of commands being executed in a PowerShell environment. The user first changes the directory to downloads then uses certutil to generate SHA256 hash of README.md. Subsequently, the user installs prettier and writes the reformatted content to output.txt. Finally, the SHA256 hash of output.txt is determined.
image text:
PS C:\Users\sarva> cd downloads
PS C:\Users\sarva\downloads> certutil -hashfile C:\Users\sarva\downloads\README.md SHA256
SHA256 hash of C:\Users\sarva\downloads\README.md:
eef23369e30d7bd99173ef4988c65a59b80bf56f60da4c9ab95c1903be312317
CertUtil: -hashfile command completed successfully.
PS C:\Users\sarva\downloads> npx -y prettier@3.4.2 README.md > output.txt
PS C:\Users\sarva\downloads > Get-FileHash -Algorithm SHA256 output.txt
Algorithm

---

**post_id:** 585506  
**author:** 24f1001769  
**timestamp:** 2025-01-26T09:33:05.487Z

---

**post_id:** 585530  
**author:** 23f2001188  
**timestamp:** 2025-01-26T10:10:21.039Z

---

**post_id:** 585575  
**author:** 23f2001188  
**timestamp:** 2025-01-26T10:59:36.818Z

-
SHA256
Hash

---

**post_id:** 585991  
**author:** 23f2003921  
**timestamp:** 2025-01-26T15:24:26.021Z

---

**post_id:** 586432  
**author:** 23f2000098  
**timestamp:** 2025-01-26T18:11:25.002Z

---

**post_id:** 586473  
**author:** Nomad  
**timestamp:** 2025-01-26T18:34:51.478Z

-
CECFD0A2DC971DE14A28CABF98ED854A9E6C7A94BD788AB0D10F5D991A4FA054
Path

---

**post_id:** 586528  
**author:** 21f3000745  
**timestamp:** 2025-01-25T08:24:31.783Z

---

**post_id:** 584795  
**author:** Saransh_Saini  
**timestamp:** 2025-01-25T09:03:21.149Z

---

**post_id:** 585081  
**author:** 21f3000745  
**timestamp:** 2025-01-25T16:02:51.992Z

-
C:\Users\sarva\downloads\outp...

---

**post_id:** 585113  
**author:** Saransh_Saini  
**timestamp:** 2025-01-25T16:44:17.023Z

Finally. Got the correct one in bit dash.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/c/0c8befb5185c68f63c51334b862b93b39fb13b58.png)

---

**post_id:** 585132  
**author:** 21f3000745  
**timestamp:** 2025-01-25T17:09:51.432Z

I ran this directly in the console and got the correct answer.

// Select all

and  elements with the ‘foo’ class  
const fooElements = document.querySelectorAll(“div.foo, span.foo”);

// Initialize a variable to store the sum  
let sum = 0;

// Iterate through the selected elements  
fooElements.forEach(element => {  
// Get the ‘data-value’ attribute and convert it to a number  
const value = parseFloat(element.getAttribute(“data-value”));

// Add the value to the sum  
if (!isNaN(value)) {  
sum += value;  
}  
});

console.log(“Sum of data-value attributes:”, sum);

---

**post_id:** 585414  
**author:** 21f3000745  
**timestamp:** 2025-01-26T07:29:05.341Z

[@Jivraj](/u/jivraj) Sir I have tried pasting the entire json but I am still getting incoorect answer

---

**post_id:** 586795  
**author:** Divya1  
**timestamp:** 2025-01-27T13:46:00.779Z

6630ecbfc252fa2bd39d26737fc1d4e1d22574c8792112b28cdf4ff128d4c605

---

**post_id:** 586819  
**author:** 23f3004114  
**timestamp:** 2025-01-27T14:44:32.781Z

Here's a description of the image:
The image shows a question with a text box for answering. An attempt to answer the question is shown in the text box, but the answer is incorrect. The question is about finding the total size of files that meet certain criteria.
image text:
Download q-list-files-attributes.zip and extract it. Use 1s with options to list all files in the
folder along with their date and file size.
What's the total size of all files at least 2404 bytes large and modified on or after Mon, 18
Mar, 2002, 1:02 am IST?
485969
Incorrect. Try again.
Don't copy from inside the ZIP file or use Windows Explorer to unzip. That destroys the
timestamps. Extract using unzip, 7-Zip or similar utilities and check the timestamps.  
help me with this

---

**post_id:** 587077  
**author:** carlton  
**timestamp:** 2025-01-28T08:04:54.160Z

## Q18 GA1

I don’t get what’s wrong with this:  
Here is the image description: The image shows a question with the table tickets in a SQLite database that has columns type, units, and price. It also shows the SQL query to find the total sales of items in "Gold" ticket type. The query has an error as the output starts with "Error: Got [[124944.59]]...".
image text: There is a tickets table in a SQLite database that has columns type, units, and price. Each row is a customer bid for a concert ticket.
type
units
price
Silver
589
1
gold
559
1.18
gold
74
1.03
gold
361
1.76
BRONZE
673
1.94
What is the total sales of all the items in the "Gold" ticket type? Write SQL to calculate it.
select sum(units\*price)
from tickets
where type='gold' collate nocase;
Error: Got [[124944.59]]...
Get all rows where the Type is "Gold". Ignore spaces and treat mis-spellings like GOLD, gold, etc. as "Gold". Calculate the sales as Units \* Price, and sum them up.

Can anyone help me understand? Thanks

---

**post_id:** 587385  
**author:** 22f3001740  
**timestamp:** 2025-01-29T05:20:50.309Z

Here's a description of the image:
The image shows instructions to use npx and prettier. It mentions downloading "README.md" and running a command involving npx, prettier, and README.md. It also asks for the output of a command, presenting a SHA256 hash.
Image text:
Let's make sure you know how to use npx and prettier.
Download README.md. In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md |
sha256sum.
What is the output of the command?
SHA256
AC06784D6825497650083DDFD6746A2CDD561B6A1FF45241C6A354035244A75C  
i dont know what is the error is plss guide me

---

**post_id:** 587512  
**author:** 23f1000751  
**timestamp:** 2025-01-29T12:41:00.221Z

I have attempted the quiz, but missed marking this question - I have seen the Graded Assignment 1 available at [this link](https://exam.sanand.workers.dev/tds-2025-01-ga1) and have attempted it. Hope the scores saved would be considered

---

**post_id:** 588093  
**author:** 22f3001740  
**timestamp:** 2025-01-31T03:27:35.397Z

Here is the image description: The image shows a question from a quiz, "Multi-cursor edits to convert to JSON (0.5 marks)". It instructs to download a file and use multi-cursors to convert it into a single JSON object. It asks for the result when the JSON is pasted at a given URL and the hash button is clicked. An incorrect answer is provided.
image text:
10 Multi-cursor edits to convert to JSON (0.5 marks)
Download q-multi-cursor-json.txt and use multi-cursors and convert it into a single JSON object, where key=value pairs are converted into {key: value, key: value, ...}.
What's the result when you paste the JSON at tools-in-data-science.pages.dev/jsonhash and click the Hash button?
c0b9426a7f358720f193d3806497ec0d81d10d835085d0f284f804bf3a6a1536
Incorrect. Try again.  
i am not getting why my answer is showing incorrect.  
can you help me in this ? [@Saransh\_Saini](/u/saransh_saini) [@Jivraj](/u/jivraj)

---

**post_id:** 588096  
**author:** carlton  
**timestamp:** 2025-01-31T03:47:24.324Z

Check the structure of your json object. It should be {key1: value1, key2: value2}. Also make sure you enclose the keys and values in double-quotes, and after every key-value pair put a comma.

---

**post_id:** 588128  
**author:** 22f3001740  
**timestamp:** 2025-01-31T05:46:24.047Z

i am doing so only … i can send u the example -  
{ “0”: “wEfsmtde”,  
“83”: “NghqzO3DL”,  
“NqN7EcM”: “I”,  
“vFD2C”: “KAB”}  
i am not able to find what’s the mistake

---

**post_id:** 596939  
**author:** 23f3001601  
**timestamp:** 2025-02-19T09:23:01.247Z

Your format seems to be correct, but cause you are still facing that problem then these are the few reasons I can think of

1. Check the entire JSON object and make sure that each and every element follows this format.
2. Use Chrome for getting that hash code, it could be the case that some other browser may not be pasting the object as intended.

---

**post_id:** 596943  
**author:** 23f1003186  
**timestamp:** 2025-02-19T09:33:43.694Z

Okay, i will go through my json object once.  
And for hash code i am using chrome only

---

**post_id:** 597013  
**author:** Jivraj  
**timestamp:** 2025-02-19T11:36:55.423Z

It worked.  
Thank you

---

**post_id:** 597151  
**author:** 23f2001286  
**timestamp:** 2025-02-19T16:32:55.050Z

After passing the deadline , my scores aren’t there …Is it same for all?

Here's a description of the image:
The image is a screenshot of a page, likely from an online quiz or assignment. It features a title, instructions, and advice regarding the quiz.
image text: Ended at Sun, 26 Jan, 2025, 11:59 pm IST
TDS 2025 Jan GA1 - Development To
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times.
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated.
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters.
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser.
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you wan
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed.
Should you take TDS this term?
• If this assignment takes you under 2 hours to complete, you will likely do OK in TDS.
• If you score above 8 / 10, you might get an S or A grade, with effort and luck.

---

**post_id:** 597152  
**author:** 23f2001286  
**timestamp:** 2025-02-19T16:33:47.136Z

wow, thats so true… ![:rofl:](https://emoji.discourse-cdn.com/google/rofl.png?v=12 ":rofl:")

---

**post_id:** 597162  
**author:** carlton  
**timestamp:** 2025-02-19T17:06:25.239Z

3 posts were merged into an existing topic: [Graded assignment 1 - Submission not shown](/t/graded-assignment-1-submission-not-shown/165396/13)

---

**post_id:** 597163  
**author:** carlton  
**timestamp:** 2025-02-19T17:07:56.951Z

Here's a description of the image:
The image shows a user interface displaying login information and recent saves. The user is logged in as "22f3001740@ds.study.iitm.ac.in." There's a "Logout" button. Below, a "Recent saves" section lists three save entries with the option to "Reload" each one, along with timestamps and scores.
image text: You are logged in as 22f3001740@ds.study.iitm.ac.in.
Logout
Recent saves
Reload from 1/23/2025, 9:33:02 PM. Score: 8
Reload from 1/23/2025, 9:32:59 PM. Score: 8
Reload from 1/23/2025, 9:32:55 PM. Score: 8

Hi Sir,

I completed the GA 1 before the time and saved it as mentioned above, but forgot to give “submit” button on iit bs week 1 graded assignment portal.

Will it might be a problem ?

I

---

**post_id:** 625648  
**author:** carlton  
**timestamp:** 2025-05-13T03:59:38.899Z

I have seen the Graded Assignment 1 available at [this link](https://exam.sanand.workers.dev/tds-2025-01-ga1) and have attempted it.

Yes

No

i have forgot the submit here on the portal but i have got 9 marks on the test will it be a problem in my marks?

---

**post_id:** 625644  
**author:** carlton  
**timestamp:** 2025-05-13T03:57:21.710Z

Hi [@Jivraj](/u/jivraj) sir,

For me, in dashboard , it is showing the assignment was not submitted.

image description: This image shows details of an online assignment module. It displays the assignment name, due date, and submission status. It also shows the user's score, peer average, and median score. Below that it shows the logged in user along with a logout button. Followed by recent saves that are reloaded at different times with the respective scores.
image text: Module 1: Development Tools
Assignment
Graded Assignment 1
Assessment (Due: 26 Jan 2025)
Not Submitted
Your Score Peer Average Median Score
99% 100
You are logged in as 22f3001740@ds.study.iitm.ac.in.
Logout
Recent saves
Reload from 1/23/2025, 9:33:02 PM. Score: 8
Reload from 1/23/2025, 9:32:59 PM. Score: 8
Reload from 1/23/2025, 9:32:55 PM. Score: 8

But I have completed it and got saved before the deadline

I havent answered the (yes / No ) in seek portal. If that might be a reason ?

Can you please help me resolve this issue

---

**post_id:** 625645  
**author:** carlton  
**timestamp:** 2025-05-13T03:57:56.589Z

Dear Sai,

This is NOT the picture of your dashboard.

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3001740/48/83411_2.png) 22f3001740:

> Here is a description of the image:
> The image shows a part of the page which appears to be the learning management system, there is text about recent saves and logged in status of a person.
> image text: Module 1: Development Tools
> Assignment
> Graded Assignment 1
> Assessment (Due: 26 Jan 2025)
> Not Submitted
> You are logged in as 22f3001740@ds.study.iitm.ac.in.
> Logout
> Recent saves
> Reload from 1/23/2025, 9:33:02 PM. Score: 8
> Reload from 1/23/2025, 9:32:59 PM. Score: 8
> Reload from 1/23/2025, 9:32:55 PM. Score: 8
> Your Score
> Peer Average Median Score
> 99%
> 100

This picture is the score in your seek portal.

The dashboard has the final correct score. Please check your dashboard.  
The dashboard has all your courses on it, when you log in.

Kind regards

---

**post_id:** 625649  
**author:** carlton  
**timestamp:** 2025-05-13T04:00:05.963Z

Got it , Thank you sir

---

