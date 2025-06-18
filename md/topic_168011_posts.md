# q3-ga5-not-accepting-right-answer

**post_id:** 598100  
**author:** muskan2431  
**timestamp:** 2025-02-21T18:32:17.871Z

# q3-ga5-not-accepting-right-answer

Here's a brief description of the image:
The image is a text-based problem or exercise, likely related to data analysis or web server logs. It provides a description of the data fields in each row, including IP address, time, request, status, and more. The user is then asked a specific question about the number of successful GET requests under certain conditions. The user provided an answer, but it's marked as "Incorrect."
image text:
Each row has these fields:
IP: The IP address of the visitor
• Remote logname: The remote logname of the visitor. Typically "-"
• Remote user: The remote user of the visitor. Typically "-"
• Time: The time of the visit. E.g. [01/May/2024:00:00:00 +0000]. Not that this is not quoted and you need to handle this.
• Request: The request made by the visitor. E.g. GET /blog/ HTTP/1.1. It has 3 space-separated parts, namely (a) Method: The HTTP method. E.g. GET (b) URL: The URL visited.
E.g. /blog/ (c) Protocol: The HTTP protocol. E.g. HTTP/1.1
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
What is the number of successful GET requests for pages under /blog/ from 1:00 until before 15:00 on Mondays?
1603
Error: Incorrect answer
①
  
It seems that the question in *Graded Assignment 5 for TDS* is producing incorrect results despite the same logic working correctly for other variations of the problem. Please check into this question once as I have cross checked with many of the students and chatgpt and all of us faced this issue in this question. Thanks!  
[@carlton](/u/carlton) [@s.anand](/u/s.anand)

code to take reference from:

```
import gzip
import pandas as pd
from datetime import datetime

log_path = 's-anand.net-May-2024.gz'
start_time = datetime.strptime('01:00:00', '%H:%M:%S').time()
end_time = datetime.strptime('15:00:00', '%H:%M:%S').time()
log_data = []

def parse_log(line):
    parts = line.split(' ')
    log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
    method, url, status = parts[5][1:], parts[6], int(parts[8])
    return log_time, method, url, status

with gzip.open(log_path, 'rt') as file:
    for entry in file:
        log_time, method, url, status = parse_log(entry)
        if method == 'GET' and url.startswith('/blog/') and 200 <= status < 300:
            if log_time.weekday() == 0 and start_time <= log_time.time() < end_time:
                log_data.append(entry)

print(f"Successful GET requests: {len(log_data)}")

```

ps: I shared code after the deadline hopefully no issues there! ![:laughing:](https://emoji.discourse-cdn.com/google/laughing.png?v=12 ":laughing:")

---

**post_id:** 598177  
**author:** amitchaurasia  
**timestamp:** 2025-02-22T04:08:00.787Z

I’m also facing same kind of issue in Q3, GA5, while cross checked answer from different methods getting same result 1603, which is showing incorrect.  
Kindly check this issue.  
Thanks

---

**post_id:** 598240  
**author:** Aryxn  
**timestamp:** 2025-02-22T05:52:55.677Z

The same issue is being faced by many students, not only for this condition, but others as well. Please look into it

---

**post_id:** 598344  
**author:** 23f2000573  
**timestamp:** 2025-02-22T08:28:29.532Z

actually i got 130 as answer. but the answer accepted by the portal was 129. i felt like, i have to change one or two numbers front and back, i tried the same before. it worked ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

---

**post_id:** 598383  
**author:** muskan2431  
**timestamp:** 2025-02-22T09:57:39.167Z

For the same question? But it shouldnt be +1 -1 to get the correct answer right.

---

**post_id:** 598948  
**author:** carlton  
**timestamp:** 2025-02-24T11:48:02.411Z

Hi [@muskan2431](/u/muskan2431) we are running some checks.

Please bear with us,  
Kind regards

---

**post_id:** 599493  
**author:** carlton  
**timestamp:** 2025-02-25T11:13:32.454Z

We have determined that some students were affected by GA5 Q3. Whoever we have identified as having received the incorrect assessment will receive 1 mark for that particular question. These are the students that we have identified as been assessed incorrectly:

| SN | Email |
|

---

