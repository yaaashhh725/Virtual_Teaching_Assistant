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

I’m also facing same kind of issue in Q3, GA5, while cross checked answer from different methods getting same result 1603, which is showing incorrect.  
Kindly check this issue.  
Thanks

---

The same issue is being faced by many students, not only for this condition, but others as well. Please look into it

---

actually i got 130 as answer. but the answer accepted by the portal was 129. i felt like, i have to change one or two numbers front and back, i tried the same before. it worked ![:sweat_smile:](https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12 ":sweat_smile:")

---

For the same question? But it shouldnt be +1 -1 to get the correct answer right.

---

Hi [@muskan2431](/u/muskan2431) we are running some checks.

Please bear with us,  
Kind regards

---

We have determined that some students were affected by GA5 Q3. Whoever we have identified as having received the incorrect assessment will receive 1 mark for that particular question. These are the students that we have identified as been assessed incorrectly:

| SN | Email |
| --- | --- |
| 1 | 21f1000131@ds.study.iitm.ac.in |
| 2 | 21f1001484@ds.study.iitm.ac.in |
| 3 | 21f1001631@ds.study.iitm.ac.in |
| 4 | 21f1001729@ds.study.iitm.ac.in |
| 5 | 21f1001890@ds.study.iitm.ac.in |
| 6 | 21f1002734@ds.study.iitm.ac.in |
| 7 | 21f1002773@ds.study.iitm.ac.in |
| 8 | 21f1003135@ds.study.iitm.ac.in |
| 9 | 21f1003475@ds.study.iitm.ac.in |
| 10 | 21f1003816@ds.study.iitm.ac.in |
| 11 | 21f1005422@ds.study.iitm.ac.in |
| 12 | 21f1005510@ds.study.iitm.ac.in |
| 13 | 21f1006234@ds.study.iitm.ac.in |
| 14 | 21f1006309@ds.study.iitm.ac.in |
| 15 | 21f1006867@ds.study.iitm.ac.in |
| 16 | 21f2000525@ds.study.iitm.ac.in |
| 17 | 21f2000913@ds.study.iitm.ac.in |
| 18 | 21f2000998@ds.study.iitm.ac.in |
| 19 | 21f2001061@ds.study.iitm.ac.in |
| 20 | 21f2001080@ds.study.iitm.ac.in |
| 21 | 21f2001543@ds.study.iitm.ac.in |
| 22 | 21f3000311@ds.study.iitm.ac.in |
| 23 | 21f3000355@ds.study.iitm.ac.in |
| 24 | 21f3000512@ds.study.iitm.ac.in |
| 25 | 21f3000591@ds.study.iitm.ac.in |
| 26 | 21f3000687@ds.study.iitm.ac.in |
| 27 | 21f3000813@ds.study.iitm.ac.in |
| 28 | 21f3001091@ds.study.iitm.ac.in |
| 29 | 21f3001161@ds.study.iitm.ac.in |
| 30 | 21f3001936@ds.study.iitm.ac.in |
| 31 | 21f3001965@ds.study.iitm.ac.in |
| 32 | 21f3002158@ds.study.iitm.ac.in |
| 33 | 21f3002431@ds.study.iitm.ac.in |
| 34 | 21f3002444@ds.study.iitm.ac.in |
| 35 | 21f3002647@ds.study.iitm.ac.in |
| 36 | 21f3002782@ds.study.iitm.ac.in |
| 37 | 21f3003195@ds.study.iitm.ac.in |
| 38 | 22ds2000011@ds.study.iitm.ac.in |
| 39 | 22f1000376@ds.study.iitm.ac.in |
| 40 | 22f1000821@ds.study.iitm.ac.in |
| 41 | 22f1000902@ds.study.iitm.ac.in |
| 42 | 22f1000935@ds.study.iitm.ac.in |
| 43 | 22f1000989@ds.study.iitm.ac.in |
| 44 | 22f1001095@ds.study.iitm.ac.in |
| 45 | 22f1001316@ds.study.iitm.ac.in |
| 46 | 22f1001391@ds.study.iitm.ac.in |
| 47 | 22f1001416@ds.study.iitm.ac.in |
| 48 | 22f1001438@ds.study.iitm.ac.in |
| 49 | 22f1001542@ds.study.iitm.ac.in |
| 50 | 22f1001551@ds.study.iitm.ac.in |
| 51 | 22f1001552@ds.study.iitm.ac.in |
| 52 | 22f1001862@ds.study.iitm.ac.in |
| 53 | 22f2000108@ds.study.iitm.ac.in |
| 54 | 22f2000113@ds.study.iitm.ac.in |
| 55 | 22f2000116@ds.study.iitm.ac.in |
| 56 | 22f2000273@ds.study.iitm.ac.in |
| 57 | 22f2000467@ds.study.iitm.ac.in |
| 58 | 22f2000813@ds.study.iitm.ac.in |
| 59 | 22f2000898@ds.study.iitm.ac.in |
| 60 | 22f2000946@ds.study.iitm.ac.in |
| 61 | 22f2001041@ds.study.iitm.ac.in |
| 62 | 22f2001336@ds.study.iitm.ac.in |
| 63 | 22f2001532@ds.study.iitm.ac.in |
| 64 | 22f2001590@ds.study.iitm.ac.in |
| 65 | 22f3000275@ds.study.iitm.ac.in |
| 66 | 22f3000337@ds.study.iitm.ac.in |
| 67 | 22f3000419@ds.study.iitm.ac.in |
| 68 | 22f3000422@ds.study.iitm.ac.in |
| 69 | 22f3000487@ds.study.iitm.ac.in |
| 70 | 22f3000563@ds.study.iitm.ac.in |
| 71 | 22f3000694@ds.study.iitm.ac.in |
| 72 | 22f3000814@ds.study.iitm.ac.in |
| 73 | 22f3000819@ds.study.iitm.ac.in |
| 74 | 22f3000831@ds.study.iitm.ac.in |
| 75 | 22f3000833@ds.study.iitm.ac.in |
| 76 | 22f3001050@ds.study.iitm.ac.in |
| 77 | 22f3001074@ds.study.iitm.ac.in |
| 78 | 22f3001108@ds.study.iitm.ac.in |
| 79 | 22f3001278@ds.study.iitm.ac.in |
| 80 | 22f3001316@ds.study.iitm.ac.in |
| 81 | 22f3001675@ds.study.iitm.ac.in |
| 82 | 22f3001688@ds.study.iitm.ac.in |
| 83 | 22f3001777@ds.study.iitm.ac.in |
| 84 | 22f3001834@ds.study.iitm.ac.in |
| 85 | 22f3001930@ds.study.iitm.ac.in |
| 86 | 22f3001961@ds.study.iitm.ac.in |
| 87 | 22f3001967@ds.study.iitm.ac.in |
| 88 | 22f3002011@ds.study.iitm.ac.in |
| 89 | 22f3002175@ds.study.iitm.ac.in |
| 90 | 22f3002184@ds.study.iitm.ac.in |
| 91 | 22f3002236@ds.study.iitm.ac.in |
| 92 | 22f3002265@ds.study.iitm.ac.in |
| 93 | 22f3002291@ds.study.iitm.ac.in |
| 94 | 22f3002307@ds.study.iitm.ac.in |
| 95 | 22f3002394@ds.study.iitm.ac.in |
| 96 | 22f3002447@ds.study.iitm.ac.in |
| 97 | 22f3002498@ds.study.iitm.ac.in |
| 98 | 22f3002565@ds.study.iitm.ac.in |
| 99 | 22f3002634@ds.study.iitm.ac.in |
| 100 | 22f3002712@ds.study.iitm.ac.in |
| 101 | 22f3002813@ds.study.iitm.ac.in |
| 102 | 22f3002844@ds.study.iitm.ac.in |
| 103 | 22f3002948@ds.study.iitm.ac.in |
| 104 | 22f3003003@ds.study.iitm.ac.in |
| 105 | 22f3003237@ds.study.iitm.ac.in |
| 106 | 23ds1000032@ds.study.iitm.ac.in |
| 107 | 23ds2000055@ds.study.iitm.ac.in |
| 108 | 23ds2000069@ds.study.iitm.ac.in |
| 109 | 23ds3000146@ds.study.iitm.ac.in |
| 110 | 23ds3000149@ds.study.iitm.ac.in |
| 111 | 23ds3000224@ds.study.iitm.ac.in |
| 112 | 23f1000232@ds.study.iitm.ac.in |
| 113 | 23f1000257@ds.study.iitm.ac.in |
| 114 | 23f1000292@ds.study.iitm.ac.in |
| 115 | 23f1000587@ds.study.iitm.ac.in |
| 116 | 23f1000776@ds.study.iitm.ac.in |
| 117 | 23f1000813@ds.study.iitm.ac.in |
| 118 | 23f1000844@ds.study.iitm.ac.in |
| 119 | 23f1001472@ds.study.iitm.ac.in |
| 120 | 23f1001651@ds.study.iitm.ac.in |
| 121 | 23f1001684@ds.study.iitm.ac.in |
| 122 | 23f1001788@ds.study.iitm.ac.in |
| 123 | 23f1001861@ds.study.iitm.ac.in |
| 124 | 23f1002075@ds.study.iitm.ac.in |
| 125 | 23f1002114@ds.study.iitm.ac.in |
| 126 | 23f1002279@ds.study.iitm.ac.in |
| 127 | 23f1002345@ds.study.iitm.ac.in |
| 128 | 23f1002362@ds.study.iitm.ac.in |
| 129 | 23f1002535@ds.study.iitm.ac.in |
| 130 | 23f1002563@ds.study.iitm.ac.in |
| 131 | 23f1002586@ds.study.iitm.ac.in |
| 132 | 23f1002630@ds.study.iitm.ac.in |
| 133 | 23f1002929@ds.study.iitm.ac.in |
| 134 | 23f1003000@ds.study.iitm.ac.in |
| 135 | 23f1003115@ds.study.iitm.ac.in |
| 136 | 23f2000119@ds.study.iitm.ac.in |
| 137 | 23f2000273@ds.study.iitm.ac.in |
| 138 | 23f2000762@ds.study.iitm.ac.in |
| 139 | 23f2000794@ds.study.iitm.ac.in |
| 140 | 23f2000822@ds.study.iitm.ac.in |
| 141 | 23f2000926@ds.study.iitm.ac.in |
| 142 | 23f2000942@ds.study.iitm.ac.in |
| 143 | 23f2001274@ds.study.iitm.ac.in |
| 144 | 23f2001347@ds.study.iitm.ac.in |
| 145 | 23f2001494@ds.study.iitm.ac.in |
| 146 | 23f2001529@ds.study.iitm.ac.in |
| 147 | 23f2001539@ds.study.iitm.ac.in |
| 148 | 23f2001661@ds.study.iitm.ac.in |
| 149 | 23f2001960@ds.study.iitm.ac.in |
| 150 | 23f2001992@ds.study.iitm.ac.in |
| 151 | 23f2002034@ds.study.iitm.ac.in |
| 152 | 23f2002121@ds.study.iitm.ac.in |
| 153 | 23f2002865@ds.study.iitm.ac.in |
| 154 | 23f2002939@ds.study.iitm.ac.in |
| 155 | 23f2003529@ds.study.iitm.ac.in |
| 156 | 23f2003751@ds.study.iitm.ac.in |
| 157 | 23f2003893@ds.study.iitm.ac.in |
| 158 | 23f2004115@ds.study.iitm.ac.in |
| 159 | 23f2004244@ds.study.iitm.ac.in |
| 160 | 23f2004366@ds.study.iitm.ac.in |
| 161 | 23f2004443@ds.study.iitm.ac.in |
| 162 | 23f2004473@ds.study.iitm.ac.in |
| 163 | 23f2004510@ds.study.iitm.ac.in |
| 164 | 23f2004637@ds.study.iitm.ac.in |
| 165 | 23f2004770@ds.study.iitm.ac.in |
| 166 | 23f2004793@ds.study.iitm.ac.in |
| 167 | 23f2004936@ds.study.iitm.ac.in |
| 168 | 23f2004979@ds.study.iitm.ac.in |
| 169 | 23f2005010@ds.study.iitm.ac.in |
| 170 | 23f2005193@ds.study.iitm.ac.in |
| 171 | 23f2005325@ds.study.iitm.ac.in |
| 172 | 23f2005398@ds.study.iitm.ac.in |
| 173 | 23f2005474@ds.study.iitm.ac.in |
| 174 | 23f2005525@ds.study.iitm.ac.in |
| 175 | 23f2005665@ds.study.iitm.ac.in |
| 176 | 23f2005701@ds.study.iitm.ac.in |
| 177 | 23f2005706@ds.study.iitm.ac.in |
| 178 | 23f2005738@ds.study.iitm.ac.in |
| 179 | 23f3000975@ds.study.iitm.ac.in |
| 180 | 23f3001271@ds.study.iitm.ac.in |
| 181 | 23f3001462@ds.study.iitm.ac.in |
| 182 | 23f3001572@ds.study.iitm.ac.in |
| 183 | 23f3001745@ds.study.iitm.ac.in |
| 184 | 23f3001752@ds.study.iitm.ac.in |
| 185 | 23f3001764@ds.study.iitm.ac.in |
| 186 | 23f3001848@ds.study.iitm.ac.in |
| 187 | 23f3002196@ds.study.iitm.ac.in |
| 188 | 23f3002427@ds.study.iitm.ac.in |
| 189 | 23f3002537@ds.study.iitm.ac.in |
| 190 | 23f3002643@ds.study.iitm.ac.in |
| 191 | 23f3003016@ds.study.iitm.ac.in |
| 192 | 23f3003027@ds.study.iitm.ac.in |
| 193 | 23f3003871@ds.study.iitm.ac.in |
| 194 | 23f3004013@ds.study.iitm.ac.in |
| 195 | 23f3004024@ds.study.iitm.ac.in |
| 196 | 23f3004066@ds.study.iitm.ac.in |
| 197 | 23f3004134@ds.study.iitm.ac.in |
| 198 | 23f3004230@ds.study.iitm.ac.in |
| 199 | 23f3004238@ds.study.iitm.ac.in |
| 200 | 23f3004264@ds.study.iitm.ac.in |
| 201 | 23f3004394@ds.study.iitm.ac.in |
| 202 | 23f3004444@ds.study.iitm.ac.in |
| 203 | 24ds1000079@ds.study.iitm.ac.in |
| 204 | 24ds2000062@ds.study.iitm.ac.in |
| 205 | 24ds2000101@ds.study.iitm.ac.in |
| 206 | 24ds2000112@ds.study.iitm.ac.in |
| 207 | 24ds3000028@ds.study.iitm.ac.in |
| 208 | 24ds3000031@ds.study.iitm.ac.in |
| 209 | 24ds3000074@ds.study.iitm.ac.in |
| 210 | 24f1000010@ds.study.iitm.ac.in |
| 211 | 24f1000400@ds.study.iitm.ac.in |
| 212 | 24f1000784@ds.study.iitm.ac.in |
| 213 | 24f1000925@ds.study.iitm.ac.in |
| 214 | 24f1001396@ds.study.iitm.ac.in |
| 215 | 24f1001439@ds.study.iitm.ac.in |
| 216 | 24f1001520@ds.study.iitm.ac.in |
| 217 | 24f1002390@ds.study.iitm.ac.in |
| 218 | 24f1002474@ds.study.iitm.ac.in |
| 219 | 24f2000994@ds.study.iitm.ac.in |
| 220 | 24f2002746@ds.study.iitm.ac.in |
| 221 | 24f2003375@ds.study.iitm.ac.in |
| 222 | 24f2004863@ds.study.iitm.ac.in |

Kind regards,  
TDS Team

---

