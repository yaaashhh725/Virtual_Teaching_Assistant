# ga3-large-language-models-discussion-thread-tds-jan-2025

**post_id:** 579668  
**author:** s.anand  
**timestamp:** 2025-01-14T13:00:03.324Z

# ga3-large-language-models-discussion-thread-tds-jan-2025

Please post any questions related to [Graded Assignment 3 - Large Language Models](https://exam.sanand.workers.dev/tds-2025-01-ga3).

---

**post_id:** 579673  
**author:** s.anand  
**timestamp:** 2025-01-14T13:06:47.583Z

## Important Instruction

Please use markdown code formatting (fenced code blocks) when sharing code in Discourse posts. This makes the code much easier to read and differentiate from non-code text. It also makes it easier for people to copy code snippets and run it themselves. See below code for example

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

Visit this link for more details: [Extended Syntax | Markdown Guide](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks).

A friendly suggestion: kindly go through [Discourse Docs](/c/docs-discourse/45)! ![:slight_smile:](https://emoji.discourse-cdn.com/google/slight_smile.png?v=12 ":slight_smile:")

---

**post_id:** 580013  
**author:** nilaychugh  
**timestamp:** 2025-01-15T12:20:05.475Z

Deadline: Sunday, February 2, 2025 6:29 PM

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

**post_id:** 580073  
**author:** Jivraj  
**timestamp:** 2025-01-15T14:59:06.607Z

---

**post_id:** 581443  
**author:** nilaychugh  
**timestamp:** 2025-01-18T04:43:01.431Z

how to get the dummy API key?

---

**post_id:** 581855  
**author:** 22f3001315  
**timestamp:** 2025-01-19T07:36:55.428Z

Hi Nilay,

In order to make a api call to openai chat completions you are required to send authentication information(openai key) in headers. For first question of GA3 you don’t have to send actual(working) api key, any dummy api key would work(you can put your name, or tds anything works)

kind regards

---

**post_id:** 582119  
**author:** 22f3001315  
**timestamp:** 2025-01-19T16:53:34.970Z

which API should i use in 7th question

---

**post_id:** 582598  
**author:** Jivraj  
**timestamp:** 2025-01-21T07:02:52.278Z

need help in question 4th. how can i correct this json body? sir [@Jivraj](/u/jivraj)

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": "Extract text from this image."
    },
    {
      "role": "user",
      "content": {
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

```

error:The JSON body must have 1 message

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": {
        "text": "Extract text from this image.",
        "image_url": "data:image/png;base64,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"
      }
    }
  ]
}

```

Error: The message must have a 2 content parts

---

**post_id:** 582639  
**author:** 22f3001315  
**timestamp:** 2025-01-21T08:21:45.804Z

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir plz see it once.

---

**post_id:** 582722  
**author:** 22f3002034  
**timestamp:** 2025-01-21T11:25:57.882Z

Hi [@22f3001315](/u/22f3001315) ,

You are almost correct, there are very minor changes that needs to be made.

Take help from Chat GPT or use this documentation which have correct json body [Vision - OpenAI API](https://platform.openai.com/docs/guides/vision).

Kind regards  
Jivraj

---

**post_id:** 582744  
**author:** 23f2000237  
**timestamp:** 2025-01-21T12:01:17.870Z

it worked thanks sir

---

**post_id:** 582749  
**author:** carlton  
**timestamp:** 2025-01-21T12:06:09.235Z

Are we supposed to buy open ai api key ?

---

**post_id:** 582810  
**author:** nilaychugh  
**timestamp:** 2025-01-21T14:30:30.322Z

No, if you scroll down to the last question, we can get our Ai Proxy key

---

**post_id:** 583185  
**author:** Jivraj  
**timestamp:** 2025-01-22T09:13:43.408Z

[@nilaychugh](/u/nilaychugh) [@22f3002034](/u/22f3002034)

The API key is available at <https://aiproxy.sanand.workers.dev/>

The instructions on how to use the token is given at [GitHub - sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

You cannot use this token directly with Open AI or any other gpt. These are only valid via the API exposed by the above instructions.

You get a limit of $1. Use with care.

Kind regards

---

**post_id:** 583854  
**author:** nilaychugh  
**timestamp:** 2025-01-23T03:52:39.679Z

but the embedding model that is said to be used is text embedding 3 small, which is the model of OpenAI

---

**post_id:** 583913  
**author:** 21f3002277  
**timestamp:** 2025-01-23T06:09:55.493Z

Hi Nilay,

Yes you would need to use `text-embedding-3-small` model of openai for embedding questions.

Kind regards  
Jivraj

---

**post_id:** 583919  
**author:** 21f3002277  
**timestamp:** 2025-01-23T06:17:12.711Z

i have a doubt, while submitting the GA3, both 7th and 8th questions require the API url to be active and connected right, but its not possible as both the URLs use same port, so if we check my 7th question URL is running right now, it’ll show as correct, but then if i run 8th question URL, the 7th question will automatically show the error, **is there any solution to this problem?**

---

**post_id:** 584032  
**author:** Jivraj  
**timestamp:** 2025-01-23T10:58:14.611Z

Q5. How to handle the error ? sir [@Jivraj](/u/jivraj)

Error: The first input does not match the first text exactly

---

**post_id:** 584038  
**author:** Jivraj  
**timestamp:** 2025-01-23T11:05:13.578Z

Q4. How to handle this error? [@Jivraj](/u/jivraj)

```
{
  "id": "chatcmpl-AshDCPwSiXNao1QXmCxCmi63GifFx",
  "object": "chat.completion",
  "created": 1737599182,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image contains an email address and a number. The email address appears to be associated with an educational institution, and the number seems to be a numerical sequence.",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 592,
    "completion_tokens": 33,
    "total_tokens": 625,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.05490624000000001,
  "cost": 0.001974,
  "monthlyRequests": 14,
  "costError": "crypto.createHash is not a function"
}

```

Error: Model must be gpt-4o-mini

---

**post_id:** 584042  
**author:** Jivraj  
**timestamp:** 2025-01-23T11:07:22.861Z

Hi Nilay,

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/nilaychugh/48/84996_2.png) nilaychugh:

> both the URLs use same port,

You can run two servers on different port numbers.

---

**post_id:** 584257  
**author:** 21f3002277  
**timestamp:** 2025-01-24T01:17:21.325Z

Hi Vikash,

I looked at your answers in backend. In answer you submitted response from openai, but you need to submit json object which is required for sending a request to LLM.

Kind regards

---

**post_id:** 584261  
**author:** 21f3002277  
**timestamp:** 2025-01-24T02:02:04.952Z

You made same mistake here, instead of response use json body that’s required for sending request to LLM.

Kind regards

---

**post_id:** 584413  
**author:** 22f3000445  
**timestamp:** 2025-01-24T08:17:52.778Z

Q4. how to handle this error ? [@Jivraj](/u/jivraj)

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image"},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,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DOYQc83d7la67bar84q8XbP//qXbYYfS9YuJSdsaR+6nbLvsUsfWGWeU7n3vK93225du881L96Uvla4X6JP3+8X35P173KPeW77mwd12K92mm5bujW+sfVQ5+kX/ZNzvumvp+kXOanZa6KVeyqz8/cJ1UrfpuSOvvPLKK691+1rWM/UiPyLDokEPe1gp1752jYaJdvVOr/QOYhKV6x3UJDLXcGSlF9mld7aTiJBt38XSO9FJtEz02fa3yNdVrlLKXe5Sj9/YdhYNl6fImoi6yOed7lSjaragHaF46ENrNPl736vpeyFQeqc62SoXLRX9Ug/b7I78qIfomyi9yJ4ovnv2AmGSv8iX4yreEzkUlWcX+ftpK7t3ymdxm9vU4wei3yKM8h2D3dRZBE19+4VAudKV5j6cws6E6NxrXlMjbHe9a42GDukFwCTiLwpnO/+Rj6z2m4a9eqFUHve4GiV0nTqHsNIwLh05GY4P85D5qBfNk503O12i24udr0S8Rfnt8Pnc+DVOhuPctXZS+gXAJK37iNr3Yn0SDfe5a8whyvTyl9fovflDeey63fe+9ViOeUC+5gjjWEReOaVXN0d6+oXI5IiifO3APeQh9SiiHZ42j4q2mx/tNngtFrsadvfa/BlCCGHlsayintPYaqtSXvjCKlL9bbvYNjBnw7FxVqedVtOffnp1UEccUR3btttWB0hoNzgmDorod/SmHV0hwglbju/JTy7lEY+o29TuxcnJ2zEZIrhfzUxenKb3CFvHcjhc5eNELQo4T+WwnW3r3Ra1ow62vpVb3u5BuMuLo1W+612vlMMPr2W3pS5PL+J+ww3rVj+RrlzS7r9/KQ96UCkbbDBXyR5pLDIc/yEglHcM2/e22ZV1111XCYsx1IN9iZeddqr3bmdnm+0//ekqMHbeuQp/9T7wwCqGHvCAUp71rGpzP9lfWmW3SCF2iBcor8WLYwy77VbbcvvtSzn44LpAmsYC69BDa7r2evSj63GZ1j/mQ7scdVQVQO1aYu3446sAme4vjj886lHVbur8speVcthhdRFKgEE9LG4II/3KZyCKCCj97V73qvfae+9a91ZONhu7FmxicaiPKt+pp859MIdjF45GPP7xtW21i2MXjlYcdFA9EmI8WZgph7zYyZERotHRiPZyf+Vj95afoxePfeyq9w85ZLw9xrC4bNe213xt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u8WDcehevqFFP4N89S12sTg3P8h/DAsSbUzAa2NtpY+ab/R3/VAZlGVN5ivzhbpb7LKxvsuW7qeNzFe+KrKNafmbGyyEzQ36pHmEgCfS1U2ZlE1gwNgzBo1X+Rqn6ihw0fLV/7S7er3ylXWh6z35e1lUSMtGymtctP5rblAffYE9jTMP5hvr2mwabehBdu2hb3n+pbVHCCGEdc/6z+iZ+30R9J5zDeCEOCNb2y1SxBkMX8QTAeQnZzQNB+w6IpjAGDobwsJ1RI17EJTSi4o5KiE/ESwvQqaJT++7VnpOlMDg8OSvTMQgIShti5qrByEqL2mJGPcWfSNIiC9pOUjOVDpnpznT6Tq7H8HgGk6YEyUy50ur/mzkvsrN6fudIFUvkVR1mQ/p2cc95Dmd1t/qR0BZCBElykRsEBTqomzawAKC4PK58hNpIoUELQFMzItEawf3IrIJEW3CXkSUa7xEdC0MfO4lrfZodVdeUVR2bEK/CSeiSX6u0dZ+tnt6sZdrLQq0G7vJm4iRnl3dX1rl1fby8H4rp2vZTb2l0b6u97l+qAxso/8RWu5pgae9Wr8BMW4hpg677FLzcr2+wl7Ekn5EQOqbriWOjRll1j5NZLqXeiqrdmA35VGXVh79Vzptp96Qj/5i4el3+EwaaV2jTyuLhZI6EI3SKo/f3bONEfck+tlI2V3vxdbqp0+61qulN548N6HfqNOwLdm9oX3YktD2ub6u3Pog+zfkIW/9hG2kHYPd2YltXKMu+p1+RZy7lh3WdL5qc4Z2YBt1dQ/XmT/YZ1gvNvFSFnaSn3rpO+zo+jYvaW92kM41ymzMeVhXmZugl177yMtPZVEm5dMeFpDq4zN9zk+fqa+08tHX9Nv2z6XGBH1D2ZSTzZV92B4hhBDWLcsaqQ+zA4EpSuzbLU45pQovAp6wJ0LGFlzO4Ypc2zEQ+SMUnGUf23X5X8UCzy6Qc9QEn3+IRQgRRyGEEEIIS0VEfVgN0VPHPrxEAX0LjSiwiOE0jhE4AuIIgsikozSivqFGvD0E6Qy1o1L+dszDgieEEEIIYamJqA+r0b41gxh1BthZZed7HROaxvEIItU/9RGlF50fi+j/L+IM9xFH1HPRjo3sums9389OIYQQQghLTUR9GIW4d7beA4B+OkYyTTtfTtyH1fEQoqNJvlnEmWjnrJ0dDyGEEEJYDiLqQwghhBBCmHHyuF4IIYQQQggzTkR9CCGEEEIIM84aHr8JIYQQQgghrDQSqQ8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYcaJqA8hhBBCCGHGiagPIYQQQghhxomoDyGEEEIIYaYp5f8A91ro9coVvFcAAAAASUVORK5CYII=" }
        }
      ]
    }
  ]
}

```

Error: The image\_url.url must be the base64 data URL of the image

---

**post_id:** 584421  
**author:** 23f2000237  
**timestamp:** 2025-01-24T08:37:26.081Z

Q8. how to handle the error ? [@Jivraj](/u/jivraj)

<http://127.0.0.1:8000/execute?q=Expense+balance+for+emp+52094>

{“name”: “expense\_balance”, “arguments”: “{“employee\_id”: 52094}”}

TypeError: Failed to fetch

---

**post_id:** 584453  
**author:** 22f3000445  
**timestamp:** 2025-01-24T10:06:51.736Z

Here's a description of the image:
The image is a screenshot of a webpage or application, likely related to an exam or assignment. It features a dark theme with green accents.
\* \*\*Top Bar:\*\* A green bar at the top indicates the date/time due, the score achieved, and options to "Check" and "Save".
\* \*\*Recent Saves:\*\* A section showing recent save times and scores.
\* \*\*Questions:\*\* A numbered list of questions, presumably for an exam or assignment. The question titles relate to various LLM (Large Language Model) concepts.
image text:
Due Sun, 2 Feb, 2025, 11:59 pm IST Score: 2.75 / 8.5 Check Save
Recent saves
Reload from 24/1/2025, 12:25:51 pm. Score: 2.75
Reload from 24/1/2025, 12:25:51 pm. Score: 2.75
Reload from 24/1/2025, 12:25:51 pm. Score: 2.75
Questions
1. LLM Sentiment Analysis (1 mark)
2. LLM Token Cost (0.75 marks)
3. Generate addresses with LLMs (1 mark)
4. LLM Vision (1 mark)
5. LLM Embeddings (0.75 marks)
6. Embedding Similarity (1 mark)
7. Vector Databases (1.5 marks)
8. Function Calling (1.5 marks)
9. Get an LLM to say Yes (1 mark)

Why is my score is out of 8.5? It should be 9.5 right?  
It was 9.5 before a reload.

---

**post_id:** 584459  
**author:** 22f3000445  
**timestamp:** 2025-01-24T10:17:59.703Z

You should answer the third question every time the site reloads

---

**post_id:** 586911  
**author:** Jivraj  
**timestamp:** 2025-01-27T22:32:35.315Z

image description: The image displays a programming environment with Python code-related tasks. It presents a string of embedding values and instructions to write a Python function most\_similar (embeddings). An error message indicates a "NameError" due to the function not being defined.
image text: embeddings = {"Packaging was excellent.": [-0.01674579456448555,-0.06481242924928665,-0.24050545692443848,0.042519159615039825,0.14857585728
Your task is to write a Python function most\_similar (embeddings) that will calculate the cosine similarity between each pair of these embeddings and
return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.
Write your Python code here:
PythonError: Traceback (most recent call last): File "/lib/python312.zip/\_pyodide/\_base.py", line 523, in eval\_code.run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File
"/lib/python312.zip/\_pyodide/\_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "<exec>", line 5, in
<module> NameError: name 'most\_similar' is not defined

For question no.6, there was some pre-written code there, right?  
I am not able to see it now.

---

**post_id:** 586942  
**author:** sharma_abhay  
**timestamp:** 2025-01-28T04:11:34.779Z

image description: The image shows a terminal window with text indicating an error related to OpenAI API usage. The error message states that the user has exceeded their current quota and advises checking their plan and billing details. It also provides a link to the documentation. The terminal is dark, with text in a light font color.
image text:
• PS C:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS> python -u "c:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS\request.py"
{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read t
he docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient\_quota', 'param': None, 'code': 'insufficient
quota'}}
• PS C:\Users\Varad\OneDrive\Documents\Desktop\Temp\TDS>

I am getting insufficient\_quota message for the 2nd question

---

**post_id:** 587025  
**author:** carlton  
**timestamp:** 2025-01-28T06:51:33.648Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/21f3002277/48/12741_2.png) 21f3002277:

> The image\_url.url must be the base64 data URL of the image

I tried downloading image for your dataset it is 2.36 KB in size.  
Using base64 encoded string from `image_url.url` in your code when decoded comes out to be 8.18 KB, when I encoded image from your dataset and decoded it was 2.36 KB.  
Here's a description of the image:
\*\*Image Description:\*\*
The image is a screenshot of a webpage displaying Base64 encoded data and its decoded preview along with file information. The top section shows a text area with the Base64 data, buttons for "copy," "clear," and "download", and the beginning of the data which includes the image header. Below that is a button "Decode Base64 to Image". The next section shows the "Preview Image" area with the text "21f3002277@ds.study.iitm.ac.in 92893354" highlighted with a yellow background. Lastly, there's a "File Info" section detailing the resolution, MIME type, extension, size, download link, and bit depth of the decoded image.
\*\*Image Text:\*\*
```
Base64\*
copy clear download
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVUAAABCCAYAAADXEilpAAAAAXNSROIArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADSMAAA7DAcd
vqGQAACBJSURBVHhe7d0H1CxF2cbxQsw5YkZBQcWMAXNAEUxgAARFRUVBUVQEMSGiIqKAARUwo6JgzmIWDJhzzoo5B0wE++vf1Ba375zeZS/s3rvz+fzPmbO7M9XVVW+F
96m3qmfX63pKCCGEEEIIYWY5z9zPEEIIIYQQwowSUR9CCCGEEMKME1EfQgghhBDCjBNRH0IIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEE
MKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQgghhBDCjBNRHOIIIYQQwowTUR9CCCGEEMKME1EfQg
ghhBDCjLNe1zP3+yJYb+5nCCGEEEIIYaWQSHOIIYQQQggzzrJH6v/731L+/vdSTjihlJ/9rJR//au+f8ELlrL11qVc85q1XPSi9b1p/v3vUn7961JOPLGUW9yilI03LuX
855/7sEden/98ff3nP6Vc8Yq1bL11KRe5SCnf+1YpJ50017Bno41KuelNS91ss7k35jjjjFL++MdS3vWuUn7/+/r3xS9eynWuU8od71DL2fCZOnzsY6X861f1vbF6sKi0
Decode Base64 to Image
Preview Image | Toggle Background Color
21f3002277@ds.study.iitm.ac.in 92893354
File Info
• Resolution: 757×66
• MIME type: image/png
• Extension: png
• Size: 8.18 KB
• Download: image.png
• Bit depth: 8
```

Hints : check if encoding is correct.

---

**post_id:** 587062  
**author:** 23f2003853  
**timestamp:** 2025-01-28T07:44:51.739Z

Is it required to give SCT for the ROE of this course?

Thank you.

---

**post_id:** 587070  
**author:** carlton  
**timestamp:** 2025-01-28T07:59:50.162Z

SCT is not required for ROE. ROE is not proctored.

Kind regards

---

**post_id:** 587175  
**author:** Jivraj  
**timestamp:** 2025-01-28T11:38:08.793Z

This is regarding Question 2 I tried to find number of tokens for the message. Using chatgpt identified the followings are valid English words for the given text in the question **D** **m** **Ay** **E r u y Vy** **V Ky** **P** **c**. then, checked with <https://platform.openai.com/tokenizer>. whatever number given by it seems to wrong.  
[@Jivraj](/u/jivraj) could you inform me where I did mistake

---

**post_id:** 587180  
**author:** 23f2003853  
**timestamp:** 2025-01-28T11:48:12.076Z

[@23f2003853](/u/23f2003853) You have to find the input tokens from the json response you receive from the proxy.

---

**post_id:** 587188  
**author:** Jivraj  
**timestamp:** 2025-01-28T12:05:37.192Z

Hi VIKASH,

This problem must be because CORS not enabled or you are running your application inside wsl, if you using WSL then you would need to identify ipaddress of WSL and use it in place of `127.0.0.1`

kind regards

---

**post_id:** 587193  
**author:** Jivraj  
**timestamp:** 2025-01-28T12:17:58.201Z

Sir, from where can I learn to locate the json response

---

**post_id:** 587196  
**author:** Jivraj  
**timestamp:** 2025-01-28T12:20:15.821Z

Hi [@23f2003853](/u/23f2003853) ,

You can learn from [Python’s Requests Library (Guide) – Real Python](https://realpython.com/python-requests/) tutorial about how to use requests module and see responses.

kind regards

---

**post_id:** 587325  
**author:** Divya1  
**timestamp:** 2025-01-28T18:05:18.879Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000445/48/96290_2.png) 22f3000445:

> I am getting insufficient\_quota message for the 2nd question

Which url are you using to send request to openai.

---

**post_id:** 587371  
**author:** 23f2002592  
**timestamp:** 2025-01-29T04:19:54.016Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3000445/48/96290_2.png) 22f3000445:

> For question no.6, there was some pre-written code there, right?

pre-written code is not required for question 6.

---

**post_id:** 587379  
**author:** 23f2002592  
**timestamp:** 2025-01-29T04:49:26.483Z

In the 6th question ,as I open the graded assignment all the time the new question is generated (NUMERICAL DATA) and the previous answer shows as incorrect answer

My doubt is that should I again and again answer the same quetion(6) all the time until the due passes?  
Is there any alternative ways to look after this problem?

---

**post_id:** 587575  
**author:** Jivraj  
**timestamp:** 2025-01-29T15:28:56.065Z

image description: The image is a screenshot of a code editor, likely displaying a Python script interacting with an API. The script includes a JSON payload with a "user" role and a content section that lists several strings. The code then attempts to send a POST request to an API endpoint. The image shows an error response indicating an "insufficient quota" with a status code of 429.
image text:
```json
{
"messages": [
{
"role": "user",
"content": "List only the valid English words from these: B2k, D, Glr, ywpIvSQ, CR3XFA, dSVNJZip,
"dWq, zP, G31jC0, VHXlo, 1Su, aAZw, pfqBkqU, wRUPIr, Go, n1Da, OMdJGxaVBk, OlrrH6x,
"8zKs, UCX, 6XxK2bUYV4, A, jJxz, gv, P, xkyD, qn54iR2t"
}
]
}
response = requests.post(url, headers=headers, json=data)
# Check for successful response
if response.status\_code == 200:
print(json.dumps(response.json(), indent=4))
else:
print(f"Request failed with status code: {response.status\_code}")
print(response.text) # Print the error response for debugging
Request failed with status code: 429
{
"error": {
"message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/gui
"type": "insufficient\_quota",
"param": null,
"code": "insufficient\_quota"
}
}
```

how to solve???

---

**post_id:** 587577  
**author:** Jivraj  
**timestamp:** 2025-01-29T15:30:02.829Z

getting quota full message for 7th question. How to get the answers then?

---

**post_id:** 587882  
**author:** 23f2003853  
**timestamp:** 2025-01-30T12:16:03.021Z

Hi [@Divya1](/u/divya1) ,

Question 6 requires to write a generic code for finding most similar pair. If your code is doing so, pls mention exact steps that you have used to arrive at answer.

---

**post_id:** 588058  
**author:** Jivraj  
**timestamp:** 2025-01-30T21:04:36.088Z

[sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy)

Are you using this document?

---

**post_id:** 588067  
**author:** 23f2003853  
**timestamp:** 2025-01-31T00:15:29.928Z

each time when I run the following code it gives me different number. None of the answer is correct. can help to fix the issue  
image description: The image shows a computer screen displaying code related to chat completions, likely for a GPT-4 model, with headers, a list of input strings, and checks for successful requests.
image text: url="https://api.openai.com/v1/chat/completions" use chat completions endpoint for GPT-4 headers= { "Authorization": "Bearer (key)", "Content-Type": "application/json" } # List of input strings user\_message = "" # list only the valid English words from these: qvyrz205, qXg1bF, zyciA3M, Jfcu, G51w4, D, NQbwiz7, Jbhxc0, 2dtR75, m, k5, INOucde, sjgxm1, ucruq456, V64, 9, ?v7vtu, reowd2, ay, AmllBpjj, e, ehclc5, tizt, vckk # Prepare the payload for chat API (gpt-4 model) data = { "model": "gpt-40-mini", # Use the gpt-4 model "messages": [ {"role": "user", "content": user\_message} ], # Messages format } # Send the POST request to OpenAI API response = requests.post(url, headers=headers, json=data) # Parse the JSON response response\_json = response.json() # Check if the request was successful if response.status\_code == 200: input\_tokens = response\_json.get("usage",{}).get("total\_tokens", "N/A") print(f"Input tokens used: {input\_tokens}") else: print(f"Request failed with status code {response.status\_code}: {response\_json}") Input tokens used: 544 Activate Windows Go to Settings to activate Windows.

---

**post_id:** 588214  
**author:** 24f2006531  
**timestamp:** 2025-01-31T09:20:32.841Z

Hi [@23f2003853](/u/23f2003853) ,

Please join tomorrow’s session, we can take it there, I am not sure why you facing this problem.

---

**post_id:** 588213  
**author:** carlton  
**timestamp:** 2025-01-31T09:37:36.551Z

Sure Sir. I am providing you the code below

```
import json
import os

api_key = key

# Set up the endpoint and headers
url = "https://api.openai.com/v1/chat/completions"  # Use chat completions endpoint for GPT-4
headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

# List of input strings
user_message = """
List only the valid English words from these: Q5YpaFZ0S, qZXgs13f, zyCiAjPh, JfcKU, G51N4, D, 9GbmmI27, jbdnhCd, 2dTr75, m, kS, lhO3Uc8e, SjpEmLl, u1cnuqk50, W54, 9, 7YWtUR, reoWxE2, Ay, ANRl2pFjL, E, 4hcE4cB, TZ2t, vck6a, Sb6vQ5K, CzQ, T5lYjxy1m, 2D, yG7PLW, mvgHmixMqn, YOPzsuhQ3, nSF7e6zFF, J60xA5WVp3, oz, vJM, vp2Zrsr, 59wiruyNzq, r, 8N, wv, z, MAKFrf5, 2L, 1IwLjzNpma, 5N20N7Zuq, 9dVp, tmUao0x, u, QRxy67, y, jrIvOZ, t3i, rptivNJF, Vy, 5WWaC1u, WC, xfoGYp, 350c94lf, Pc9oNu, 1bOnLseHUm, aguOp0jxE, Tbz, qX, 9amaVxKFh, bnBkkNN5jc, o7N4y6, V, Ky, ewWw0qcLnw, bbD7MBGM7x, c0l, P, TMFOMvW, c, THRovqGNKb, BV, XIZcX, J0rDx3c, DxEvjEh, j9, Db5Hij, vpSJyCeyh, Z, D, yWpxiOwRXx, 7NeZN1GVE, Y, Lq6Pk, BCJT
"""

# Prepare the payload for Chat API (gpt-4o-mini model)
data = {
    "model": "gpt-4o-mini",  
    "messages": [{"role": "user", "content": user_message}],

}

# Send the POST request to OpenAI API
response = requests.post(url, headers=headers, json=data)

# Parse the JSON response
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    input_tokens = response_json.get("usage", {}).get("total_tokens", "N/A")
    print(f"Input tokens used: {input_tokens}")
else:
    print(f"Request failed with status code {response.status_code}: {response_json}")```
```

---

**post_id:** 588228  
**author:** 21f2000588  
**timestamp:** 2025-01-31T10:42:36.589Z

Hello Sir,

I am unable to recieve a proper output for q1 of ga3.  
This is my test message. Its been given in two lines.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/0/60deb1fe7cda3d6876df481d07803e66d1974e45.png)

The below is my code for the question.

```
import httpx

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": "Bearer api_key",
    "Content-Type": "application/json"
}

system_message = "Analyze the input message if it's  GOOD , BAD or NEUTRAL."
user_message = "2 b7 rkS94mn4  AM dNG4j EVevK24Ev VEpI G LeeHS"

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": system_message},  # System message
        {"role": "user", "content": user_message}       # One user message
    ],
    "temperature": 0.7
}

response = httpx.post(url, headers=headers, json=payload)

response.raise_for_status()

result = response.json()

for choice in result["choices"]:
    print("AI Response:", choice["message"]["content"])

```

I tried to put the two test lines as two user messages but received an error stating that the json body must contain only 2 messages with one mandatorily being a system message. With that in mind, i also tried the alternative

`user_message = "2 b7 rkS94mn4 \n AM dNG4j EVevK24Ev VEpI G LeeHS"`

The error message i keep receiving is as below.

![image](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/4/740853eca092fd94814c5c4cb8cc4ddb5f10eba3.png)

Kindly advice on how to proceed.

Thanks and Regards  
Shalini

---

**post_id:** 588278  
**author:** Yogesh1  
**timestamp:** 2025-01-31T14:24:33.385Z

Hi Shalini,

Your `user_message` is incorrect. I looked at your exact GA and it works if you make sure your `user_message` is precisely what is given to you.

Hint: How do you store a multi-line variable in python?

Kind regards

---

**post_id:** 588283  
**author:** carlton  
**timestamp:** 2025-01-31T14:40:38.508Z

Hello, could anyone please confirm that GA 3 is worth 9.5 points? Since our GAs are typically 10 marks apiece, I wanted to inquire about and obtain clarification on this.  
Thank you in advance.

---

**post_id:** 588333  
**author:** 22f2000113  
**timestamp:** 2025-01-31T16:31:15.592Z

I was unable to make the answer box in Question 3 visible. I was only able to make white space appear there, but couldn’t make it so that answer can be input to the box.

---

**post_id:** 588423  
**author:** 23ds2000092  
**timestamp:** 2025-02-01T03:45:32.917Z

In addition to CSS classes there is also a tag attribute acting on it. Check carefully.

Kind regards

---

**post_id:** 588469  
**author:** carlton  
**timestamp:** 2025-02-01T05:38:06.960Z

I am getting below error for Q6 if i am importing sklearn libarary  
image description: The image displays a detailed error message from a Python environment, likely related to the Pyodide distribution. The message starts with "PythonError: Traceback," indicating a runtime error. It then lists the file paths and line numbers where the error occurred, tracing the execution path. The key error is "ModuleNotFoundError: No module named 'scipy'," meaning the SciPy library isn't found. The message gives instructions to install SciPy using "await micropip.install("scipy")" in Python or "await pyodide.loadPackage("scipy")" in JavaScript. A link to a webpage with more details is also provided. The text is red on a white background.
image text: PythonError: Traceback (most recent call last): File "/lib/python312.zip/\_pyodide/\_base.py", line 523, in eval\_code.run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File
"/lib/python312.zip/\_pyodide/\_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "<exec>", line 4, in <module>
ModuleNotFoundError: No module named 'scipy' The module 'scipy' is included in the Pyodide distribution, but it is not installed. You can install it by calling: await micropip.install("scipy") in Python, or
await pyodide.loadPackage("scipy") in JavaScript See https://pyodide.org/en/stable/usage/loading-packages.html for more details.

---

**post_id:** 588481  
**author:** s.anand  
**timestamp:** 2025-02-01T05:53:30.951Z

Hi team, I am using OpenAI API key for solving Q7 and getting the error like below

```
{'error': {'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, read the docs: https://platform.openai.com/docs/guides/error-codes/api-errors.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

```

Is it necessary to pay for the OpenAI API key? Is there any other way?

---

**post_id:** 588484  
**author:** 23ds2000092  
**timestamp:** 2025-02-01T05:55:44.883Z

[@21f2000588](/u/21f2000588)

Sure does add up to 9.5 , unless you want another question ![:wink:](https://emoji.discourse-cdn.com/google/wink.png?v=12 ":wink:")

Kind regards

---

**post_id:** 588749  
**author:** 24ds3000090  
**timestamp:** 2025-02-01T13:52:03.153Z

Yeah, after all these years of learning and teaching computing, I realize I can’t even count to 10 correctly anymore.

image description: This is a four-panel comic strip featuring Calvin from the "Calvin and Hobbes" series. In the first panel, Calvin is raising his hand in class, saying his dad used slide rules in school. The second panel shows Calvin saying his dad hasn't used one since getting a calculator. The third panel has Calvin advocating leaving math to machines and playing outside. The final panel shows Calvin slumped over his desk, lamenting that his bills always "die in subcommittee."
image text: MISS WORMWOOD, MY DAD SAYS WHEN HE WAS IN SCHOOL, THEY TAUGHT HIM TO DO MATH ON A SLIDE RULE. HE SAYS HE HASNT USED A SLIDE RULE SINCE, BECAUSE HE GOT A FIVE-BUCK CALCULATOR THAT CAN DO MORE FUNCTIONS THAN HE COULD FIGURE OUT IF HIS LIFE DEPENDED ON IT. GIVEN THE PACE OF TECHNOLOGY, I PROPOSE WE LEAVE MATH TO THE MACHINES AND GO PLAY OUTSIDE. MY BILLS ALWAYS DIE IN SUBCOMMITTEE.

---

**post_id:** 589234  
**author:** 23f1000403  
**timestamp:** 2025-02-02T08:10:42.643Z

[@Jivraj](/u/jivraj) Please let me know if the code is needed for this. I can share the code generated by chatgpt

---

**post_id:** 589391  
**author:** 23f2003853  
**timestamp:** 2025-02-02T12:41:10.201Z

[@Jivraj](/u/jivraj) , [@carlton](/u/carlton) Dear Sirs, I need help in solving this question. I have the same issue. I have tried tokenizer tool, tried writing request code but still couldn’t get the correct answer. I have tried numerous time and ended up consuming lot of tokens . What should be the optimal approach in this question?

```
  "id": "chatcmpl-Aw7eXQ8hciiQ0ZedatQEifFGxnLhQ",
  "object": "chat.completion",
  "created": 1738415805,
  "model": "gpt-4o-mini-2024-07-18",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The valid English words from the given list are:\n\n- a\n- I\n- o\n- t\n- U\n- w\n- y\n- z",
        "refusal": null
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 532,
    "completion_tokens": 34,
    "total_tokens": 566,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_bd83329f63",
  "monthlyCost": 0.01662212,
  "cost": 0.001863,
  "monthlyRequests": 41,
  "costError": "crypto.createHash is not a function"
}

```

---

**post_id:** 589614  
**author:** 22f3002557  
**timestamp:** 2025-02-02T15:38:32.738Z

Tried hundreds of different prompts, different situations but in Q9 AI is not responding “Yes”. Is there anything i am missing?

---

**post_id:** 589632  
**author:** 23f1000403  
**timestamp:** 2025-02-02T15:44:35.908Z

Dear Sir, I got the answer in json but none out put is correct. Please help me to correct the code  
curl <https://api.openai.com/v1/chat/completions> \ > -H “Content-Type: application/json” \ > -H “Authorization: Bearer $TOKEN” \ '{ > -d ‘{ > “model”: “gpt-4o-mini”, "messa> “messages”: [{ > “role”: “user”, "c> “content”: “List only the valid English words from these: zqndWw3FB, kM, K, njuHs9A, r, lkXJ1lG, Z, yLHDClp, G1Db, 7, m, MYieYF3B, pFTQ1JU8Fj, RL9n6kE, EVpChB, V6iCpP, 9YwiwAnBc5, R, UM, mrnyc, 4ej9x, 8X, CQA9, jHC, uL4G6, f, zzaozWC9, 0qsOenEndF, qaZ2WoX, nXGZ” > }] > }’ { “id”: “chatcmpl-AwTPGH241yjyg9EkO1t1tbeGU7KCu”, “object”: “chat.completion”, “created”: 1738499426, “model”: “gpt-4o-mini-2024-07-18”, “choices”: [ { “index”: 0, “message”: { “role”: “assistant”, “content”: “The valid English words from your list are:\n\n- my\n- is\n- an\n- or\n- in\n\n(Note: This assumes a focus on short English words. Longer words or specific proper nouns may also exist but were not included in this selection.)”, “refusal”: null }, “logprobs”: null, “finish\_reason”: “stop” } ], “usage”: { “prompt\_tokens”: 160, “completion\_tokens”: 53, “total\_tokens”: 213, “prompt\_tokens\_details”: { “cached\_tokens”: 0, “audio\_tokens”: 0 }, “completion\_tokens\_details”: { “reasoning\_tokens”: 0, “audio\_tokens”: 0, “accepted\_prediction\_tokens”: 0, “rejected\_prediction\_tokens”: 0 } }, “service\_tier”: “default”, “system\_fingerprint”: “fp\_72ed7ab54c” }

---

**post_id:** 590138  
**author:** 21f3002277  
**timestamp:** 2025-02-03T06:54:57.348Z

Pls give some kind of clue. It seems like a waste of so much time!

---

**post_id:** 590143  
**author:** 21f2000588  
**timestamp:** 2025-02-03T07:22:48.722Z

i agree, i have wasted around 300 requests (prompts) and got nothing.

---

**post_id:** 590322  
**author:** Yogesh1  
**timestamp:** 2025-02-03T14:11:25.378Z

Sir I am stuck in Q4. how to handle the error please help me [@Jivraj](/u/jivraj) [@carlton](/u/carlton)

Error: The image\_url.url must be the base64 data URL of the image

---

**post_id:** 590325  
**author:** 21f3002277  
**timestamp:** 2025-02-03T14:22:52.043Z

Okay thank you sir, for the clarification.

---

**post_id:** 590342  
**author:** Yogesh1  
**timestamp:** 2025-02-03T15:09:11.873Z

You have to download that image, and find the base\_url of that image.

---

**post_id:** 590350  
**author:** s.anand  
**timestamp:** 2025-02-03T15:28:45.259Z

from where to download

---

**post_id:** 590386  
**author:** 23f2001915  
**timestamp:** 2025-02-03T18:25:21.354Z

The image is part of the question.

---

**post_id:** 590397  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:07:57.870Z

For those who want to experiment with GPT-4o Mini (or other models), [Github Models](https://github.com/marketplace/models) is free. You can explore and compare models, including GPT-4o Mini, DeepSeek R1, and others.

It has rate limits, so you can’t use it in production, but is a good place to prototype applications and experiment with prompts.

Please let me know if you face any problems accessing it.

---

**post_id:** 590398  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:10:01.674Z

how to answer the question in first place ?

---

**post_id:** 590422  
**author:** 22f2000113  
**timestamp:** 2025-02-04T03:13:45.199Z

Check if you are requesting through anand sir’s proxy [AI Proxy](https://aiproxy.sanand.workers.dev/).

---

**post_id:** 590530  
**author:** 23f3004114  
**timestamp:** 2025-02-04T09:51:48.117Z

sklearn might be using scipy for some purpose, just install it, it should work.

Btw what are you trying to do with Sklearn?

---

**post_id:** 590614  
**author:** 22f2001630  
**timestamp:** 2025-02-04T13:27:09.694Z

thanks for the reply i was using cosine function but got another solution.

---

**post_id:** 590620  
**author:** 23f1002382  
**timestamp:** 2025-02-04T13:59:46.793Z

Q2 LLM Token Cost ,

We have <https://platform.openai.com/tokenizer> , which helps us count tokens in a string, shouldn’t this be a better way than calling the API? However the returned value does not show as correct answer!

---

**post_id:** 590626  
**author:** 23f1002382  
**timestamp:** 2025-02-04T14:05:18.252Z

Hi guys, just wanted to share that I found it hysterical when I saw this question:  
image description: The image is a screenshot of a web page with text and a few UI elements. The top bar shows tabs and icons, indicating a web browser interface. The main content area has a prompt related to an API call, a list of requirements, and some textual instructions. At the bottom, there's a "Check" button, and a "Type here to search" bar. The text describes a task about generating address data using an OpenAI model, and the user needs to construct a JSON body for the API request.
image text:
My Dashboard - IIT Madras Onl X
Graded Assignment 3 :: IITM On X Ex TDS 2025 Jan GA3 - Large Lang X
API Reference - OpenAI API X
TDS - LLM Extraction - YouTube X +
exam.sanand.workers.dev/tds-2025-01-ga3
Due Wed, 5 Feb, 2025, 11:59 pm IST Score: 1/9.5 Check all Save
■ "type": "string": ... which is a string.
■ "required": ["steps", "final\_answer"]: ▲ You must add "required": [...] and include all fields in the object.
■ "additionalProperties": false: ▲ OpenAl requires every object to have "additionalProperties": false.
RapidRoute Solutions is a logistics and delivery company that relies on accurate and standardized address data to optimize package routing. Recently, they encountered
challenges with manually collecting and verifying new addresses for testing their planning software. To overcome this, the company decided to create an automated address
generator using a language model, which would provide realistic, standardized U.S. addresses that could be directly integrated into their system.
The engineering team at RapidRoute is tasked with designing a service that uses OpenAl's GPT-40-Mini model to generate fake but plausible address data. The addresses must
follow a strict format, which is critical for downstream processes such as geocoding, routing, and verification against customer databases. For consistency and validation, the
development team requires that the addresses be returned as structured JSON data with no additional properties that could confuse their parsers.
As part of the integration process, you need to write the body of the request to an OpenAl chat completion call that:
• Uses model gpt-40-mini
• Has a system message: Respond in JSON
• Has a user message: Generate 10 random addresses in the US
• Uses structured outputs to respond with an object addresses which is an array of objects with required fields: apartment (string) zip (number) latitude (number).
• Sets additional Properties to false to prevent additional properties.
Note that you don't need to run the request or use an API key; your task is simply to write the correct JSON body.
What is the JSON body we should send to https://api.openai.com/v1/chat/completions for this? (No need to run it or to use an API key. Just write the body of the request below.)
There's no answer box above. Figure out how to enable it. That's part of the test.
Check
Type here to search
Activate Windows
Go to Settings to activate Windows.
18:51
04-02-2025
ENG
  
Like I literally showed this question to my mother and younger bro, stating the fact we ourselves had enable the answer box, they laughed there pants off…![:joy:](https://emoji.discourse-cdn.com/google/joy.png?v=12 ":joy:")![:joy:](https://emoji.discourse-cdn.com/google/joy.png?v=12 ":joy:")  
More courses could be like this.

---

**post_id:** 590627  
**author:** 24ds2000125  
**timestamp:** 2025-02-04T14:05:45.580Z

**Q4**  
s3 string was given by

```
image_b64 = ""
import base64
with open('/content/TDS_wk3_q4.png', 'rb') as f:
    binary_data = f.read()
    image_b64 = base64.b64encode(binary_data).decode()
data_uri = f"data:image/png;base64,{image_b64}"

```

s4 string given by :

used this [link](https://www.base64-image.de/)  to generate image url  
  
 Then checked them both, they were the same

```
for x,y in zip(s3,s4):
  if (x != y):
    print(x,y)

```

i verified that both were equal but still one gave the wrong answer(python code), while the online converter gave the right one?  
I know i’m missing something, but why?

---

**post_id:** 590666  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-04T16:16:35.495Z

Here's a brief description of the image:
The image is a dark-themed coding environment. It contains instructions to write a Python function `most\_similar(embeddings)` to calculate cosine similarity and return the pair with the highest similarity. There's an `import numpy` statement and a function definition with a placeholder comment "# Your code here". The current code returns `(phrase1, phrase2)`. Below the code, there is an error message indicating a `NameError` for `phrase1`. An "Incorrect answer" message also appears.
image text:
Your task is to write a Python function most\_similar (embeddings) that will calculate the cosine similarity between each pair of these embeddings and
return the pair that has the highest similarity. The result should be a tuple of the two phrases that are most similar.
Write your Python code here:
import numpy
Incorrect answer
def most similar (embeddings):
# Your code here
return (phrase1, phrase2)
PythonError: Traceback (most recent call last): File "/lib/python312.zip/\_pyodide/\_base.py", line 523, in eval\_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File
"/lib/python312.zip/\_pyodide/\_base.py", line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "<exec>", line 11, in
<module> File "<exec>", line 8, in most\_similar NameError: name 'phrase1' is not defined

---

**post_id:** 590677  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-04T17:52:10.076Z

image description: The image is a screenshot of a user interface, likely for a web development or API testing platform. The text on the screen addresses the API URL endpoint for an implementation. It features a text field with the URL `http://127.0.0.1:8000/execute`, and an exclamation mark icon indicating an error. Below the URL, there's an error message: `SyntaxError: "undefined" is not valid JSON`. The screen also includes a paragraph mentioning a GET request with the format '?q=...' containing a task, and verification of matching with the expected response. A blue 'Check' button appears at the bottom.
image text: What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:8000/execute
SyntaxError: "undefined" is not valid JSON
We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition.
Check
  
This is in context to Q8. This is a screenshot of the response I am getting when i run the same API on my FastAPI/docs response page, it gives the correct response. But when I check it on the assignment page i get the following error. If you would like to know the code, pls let me know. [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

**post_id:** 590682  
**author:** 22f3002723  
**timestamp:** 2025-02-04T18:07:26.462Z

Good Evening, I have a doubt regarding 7th and 8th question. I am getting this error of expecting three matches while saving. But, Externally when I check this API, I tried considerable test cases, and I am getting the output correctly. Can you please check this and give a solution. Thank You  
![Screenshot 2025-02-04 214334](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/2/b2931cf4f6b39b884ab54950c2f49898c942c780.png)  
image description: The image shows a dark interface with text instructions and an API URL input field. An error message is displayed below the field.
image text: Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity
http://127.0.0.1:8000/similarity
Error: Expected 3 matches

---

**post_id:** 590701  
**author:** 22f3002723  
**timestamp:** 2025-02-05T01:44:08.545Z

This is regarding the 8th question. Same here, I am getting the answer for all the test cases, but then also, I am getting error in the portal while saving. Please help me out here. Thank You.  
image description: The image shows a web browser window displaying a JSON object. The browser's address bar contains a URL related to calculating a performance bonus. The content of the webpage shows a JSON structure which includes the calculation name, arguments, the employee ID and the current year.
image text: 127.0.0.1:8001/execute/?q="Calculate%20performance%20bonus%20for%20employee%2010056%20for%202025."
Pretty-print
{"name":"calculate\_performance\_bonus", "arguments":"{\"employee\_id\": 10056, \"current\_year\": 2025}"}  
image description: The image shows a dark theme UI with text fields and an error message. It seems to be related to API configuration.
image text: What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:8001/execute
TypeError: Failed to fetch

---

**post_id:** 590709  
**author:** 22f3002723  
**timestamp:** 2025-02-05T03:57:27.717Z

For question 1 getting the below response … not sure what it means  
ythonError: Traceback (most recent call last): File “/lib/python312.zip/\_pyodide/\_base.py”, line 523, in eval\_code .run(globals, locals) ^^^^^^^^^^^^^^^^^^^^ File “/lib/python312.zip/\_pyodide/\_base.py”, line 357, in run coroutine = eval(self.code, globals, locals) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File “”, line 53, in TypeError: unhashable type: ‘dict’

---

**post_id:** 590740  
**author:** Namannn28  
**timestamp:** 2025-02-05T07:08:49.236Z

[@carlton](/u/carlton)  
for question 2 what does the below instruction mean … also how to indicate this in a prompt ’ Remember: indicating that this is a `user` message takes up a few extra tokens. You actually need to make the request to get the answer."

---

**post_id:** 590786  
**author:** Jivraj  
**timestamp:** 2025-02-05T10:25:25.132Z

For token count query , trying to do something like below any issues with this

```
import requests
import json
from google.colab import userdata
def generate_readme_content(proxy_url,auth_token):
    # Prepare the payload
    prompt = f"""       
    SNyFiNTb, BUkDfo0tR, x3x, 6NE8Rq833, Re7, Vth9bYJ0pK, pnI, JAXpFb, BRPE, o, 5xVQe, iY8yVT, 69w, LjLCzs, MJ1g, wBR, 0H, 6bK, AMw, Vrxiux, dqZysH, yD82hcr, FZrwV8Zjq, Xb2, quLpdQqxd1, lqSLbI, HerfhK2, rNPU, 9K1C, 0ywhX2s4O9, mjZ, sR9gCC, 2WVSfwWEae, c, DtWnfOncFj, qjK8P7xh, 0xraHn7RMa, OCmQIi3tbU, S2K, F, q5mO, yZt, X, zd, se0ss3k, uU, yCRCi, S3bMfb, qZ4dh, M7, uhxgDvG3, 696g, 9k, l5U, bH, LVXw1fdWFi, 0kU68gGP, WuyD, V, kVKQ1Y8, kLjMDoEmIN, EYHs7qsabQ, sWrC8vN7n, oAJZP, YLd, mi6Jmxgf, cb9UDdap, kzuot, R0eA2V, mr7SctL49, Td5, in, hxvi, MDg, AAK, uLBF889bO5, Z7z, AO0c, nbc, bE6Rsdw5b, 0, pBjOAuPN8A, 9C3, K, 8, yZyCBPz   
    """
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant to count the number of english words in a message. Find the number of input tokens used for  a message lile below. Try excluding tokens used for understanding this prompt"},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500,
        "temperature": 0.7
    }
    
        # Send a POST request to the proxy server
    response = requests.post(
            proxy_url,
            headers={"Content-Type": "application/json",
                     
            "Authorization": f"Bearer {auth_token}"},
            data=json.dumps(payload)
        )
    response_data = response.json()
    return response_data
proxy_url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
auth_token=userdata.get('aiproxy_secret_key')
tokenjson=generate_readme_content(proxy_url,auth_token)
print(tokenjson)

```

---

**post_id:** 590788  
**author:** 22f2001630  
**timestamp:** 2025-02-05T10:27:53.411Z

I GOT THE CORRECT ANSWER F0R QUES 7 & 8 STILL MY SCORE IS SHOWING 8 DOES ANYONE KNOW HOW TO DO THIS ?  
image description: The image is a dark-themed instructional document. It's titled "TDS 2025 Jan GA3 - Large Language Models" and lists 7 instructions with explanations. There is also a note about running multiple servers.
image text: TDS 2025 Jan GA3 - Large Language Models
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times.
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated.
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters.
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser.
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want.
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed.
Note: You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers.
Have questions? Join the discussion on Discourse

---

**post_id:** 590789  
**author:** Jivraj  
**timestamp:** 2025-02-05T10:29:00.515Z

Use addition : to add up your score for each question.  
eq:  
1+ 1 = 2  
Fractions are harder  
1.5 + 1 = 2.5

image description: The image displays a list of questions. The title is "Questions". The questions are numbered and each is followed by a mark value in parentheses. The topics include LLM sentiment analysis, token cost, address generation, vision, embeddings, similarity, vector databases, function calling, and getting an LLM to say yes.
image text: Questions
1. LLM Sentiment Analysis (1 mark)
2. LLM Token Cost (0.75 marks)
3. Generate addresses with LLMs (1 mark)
4. LLM Vision (1 mark)
5. LLM Embeddings (0.75 marks)
6. Embedding Similarity (1 mark)
7. Vector Databases (1.5 marks)
8. Function Calling (1.5 marks)
9. Get an LLM to say Yes (1 mark)

---

**post_id:** 590795  
**author:** 22f2001630  
**timestamp:** 2025-02-05T10:51:47.566Z

To this question I have checked values ranging from 6 to 13 none of them are correct, using openAI Tokenizer online tool.  
image description: The image is a screenshot of a webpage, likely a coding or assessment platform. The webpage has a header with navigation options and a timer indicating "08:04:14 left" and a score of "0/9.5". The main content section displays a question or exercise related to "LLM Token Cost." It describes a scenario involving LexiSolve Inc., a startup using OpenAI's language models. The question asks the user to identify valid English words and determine the number of tokens used. There are input fields for the answers and a "Check" button to submit. The bottom right shows the time and date as "15:55 05-02-2025."
image text:
My Dashboar X
Graded Assig
X
GA3 - Large L X
Ex TDS 2025 Jan X
Async DB Set X
uv: Python pa X
Running scrip X
127.0.0.1:8000 × • 4.75+1.5 - Go X
+
Π
X
☆
Verify it's you :
exam.sanand.workers.dev/tds-2025-01-ga3
08:04:14 left Score: 0/9.5 Check all
Save
Check
2 LLM Token Cost (0.75 marks)
LexiSolve Inc. is a startup that delivers a conversational Al platform to enterprise clients. The system leverages OpenAl's language models to power a variety of customer service,
sentiment analysis, and data extraction features. Because pricing for these models is based on the number of tokens processed-and strict token limits apply-accurate token
accounting is critical for managing costs and ensuring system stability.
To optimize operational costs and prevent unexpected API overages, the engineering team at LexiSolve has developed an internal diagnostic tool that simulates and measures
token usage for typical prompts sent to the language model.
One specific test case an understanding of text tokenization. Your task is to generate data for that test case.
Specifically, when you make a request to OpenAl's GPT-40-Mini with just this user message:
List only the valid English words from these:
... how many input tokens does it use up?
Number of tokens:
Remember: indicating that this is a user message takes up a few extra tokens. You actually need to make the request to get the answer.
Activate Windows
Go to Settings to activate Windows.
Check
Type here to search
N
A
ENG
15:55
05-02-2025
  
Here's a description of the image:
The image shows a webpage with the title "Tokenizer" from the website "platform.openai.com". The page contains text input field with text "List only the valid English words from these:". Underneath the text input, there's a section with "Text" and "Token IDs" options. There are also some notes about tokenization.
image text: My Dashbo X Graded Ass X GA3 - Larg X Ex TDS 2025 X Async DBS X uv: Python X Running sc X 127.0.0.1:8 X 4.75+1.5 X Tokenizer X + platform.openai.com/tokenizer P personale / Default project Clear Show example Tokens 10 Characters 47 List only the valid English words from these: Text Token IDs A helpful rule of thumb is that one token generally corresponds to ~4 characters of text for common English text. This translates to roughly 3/4 of a word (so 100 tokens ~= 75 words). If you need a programmatic interface for tokenizing text, check out our tiktoken package for Python. For JavaScript, the community-supported @dbdq/tiktoken package works with most GPT models. Activate Windows Go to Settings to activate Windows.  
Please help me were I am going wrong.

---

**post_id:** 590796  
**author:** Jivraj  
**timestamp:** 2025-02-05T10:57:57.512Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/22f3002723/48/110636_2.png) 22f3002723:

> `user` message

that means it should be a user message

```
messages = [
{
"role":"user",
"content":"message"
}
]

```

---

**post_id:** 590800  
**author:** Jivraj  
**timestamp:** 2025-02-05T11:09:12.197Z

Keep getting this error.  
image description: The image is a screenshot of a webpage. The webpage appears to be an assessment or a coding exercise. The top of the page contains navigation elements such as a time remaining, a score, and buttons like "Check all" and "Save". The main content of the page includes instructions, code snippets, and error messages related to a function calling task. There's an example response and a suggestion about the API URL endpoint. The bottom section of the page has a title "Function Calling with OpenAI" followed by a description of the task.
image text: My Dash X Graded X GA3 - La X Ex TDS 202 X Async DI X uv: Pythe X Running X 127.0.0.1 X 4.75+1.5 X Tokenize X You can X + exam.sanand.workers.dev/tds-2025-01-ga3 07:38:35 left Score: 0/9.5 Check all Save response might look like this: "matches": "Contents of document 3", "Contents of document 1", "Contents of document 2" } Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2". Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers. What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity http://127.0.0.1:8000/similarity Error: Got incorrect matches: Our customer feedback survey revealed that ease of use is a key area for improvement., The infrastructure upgrade includes improvements in data storage and retrieval., The technical documentation for the new product line is now available online. We'll check by sending a POST request to this URL with a JSON body containing random docs and query. Check 8 Function Calling (1.5 marks) Function Calling with OpenAl Activate Windows Function Calling allows Large Language Models to convert natural language into structured function calls. This is perfect for building chatbots and Al assistants that need to interact with your backend systems.

---

**post_id:** 590801  
**author:** 23f2000098  
**timestamp:** 2025-02-05T11:09:36.765Z

Try sending an api call to openai.

---

**post_id:** 590803  
**author:** 22f2001630  
**timestamp:** 2025-02-05T11:11:56.483Z

Check with network tab, you would see the response of api call being made, Compare that with expected output.

Regrading question 8, you would need to check if cors are enabled, check in browser console tab for more.

Here's a description of the image:
The image is a screenshot of a web browser's developer tools. The "Network" tab is open. In the "Name" section, two entries are listed, each with a long URL. The "Response" tab is selected, and it shows the response for the first entry as `{"acc":1,"webResult":{}}`. Other tabs visible include "Headers", "Payload", "Preview", "Initiator", "Timing", and "Cookies". The browser has tabs open for various websites like "My Dashboard", "SOP Link", and more. The browser's address bar is visible at the top.
image text: Search or enter web address
My Dashboard - IIT... SOP Link (T12023) Jan 2023 Grading d... Titanic dataset - Go... A (99+) Academia.edu... Mc IIT Madras BS Foun... PE About - Project Euler
Welcome </> Elements Console Sources Network + Update Other favorites
Preserve log Disable cache No throttling
Filter Invert More filters All Fetch/XHR Doc CSS JS Font Img Media Manifest WS Wasm Other
1.000 ms 2.000 ms 3.000 ms 4.000 ms 5.000 ms 6.000 ms 7,000 ms 8.000 ms 9.000 ms 10.000 ms 11.000 ms 12,00
MO Dox (3,290) + GA3 Google Drive Add shortc
Name X Headers Payload Preview Response Initiator Timing Cookies
{} 1.0?cors=true&content-type=application/x-json-stre...6V%3D4%26LU... 1 {"acc":1,"webResult":{}}
{> 1.0?cors=true&content-type=application/x-json-stre...6V%3D4%26LU...
2 requests 773 B transferred 48 B resources {}
Console Developer resources Network conditions Issues Performance monitor Memory inspector Autofill Coverage +
top = Filter Default levels 33
msn Discover Following >

---

**post_id:** 590804  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-05T11:12:42.808Z

i am unable to find the answer box plss guide me through that

---

**post_id:** 590811  
**author:** 22f2001630  
**timestamp:** 2025-02-05T11:26:33.292Z

You could use AI assistance it helped me.  
Here's a description of the image:
\*\*Overall:\*\* The image is a screenshot of a web developer's console, focusing on the "Elements" tab. The user is interacting with a forum thread on a learning management system (LMS). The page includes code, UI elements, and a chat interface for AI assistance.
\*\*Key Elements:\*\*
\* \*\*Webpage:\*\* The main area of the screenshot displays HTML code, with various tags, attributes, and styles being highlighted.
\* \*\*Console/Developer Tools:\*\* Developer tools are open with the "Elements" tab selected. A filter and various CSS styles are displayed.
\* \*\*Text Content:\*\* The webpage contains text related to a discussion forum and also an AI assistant interface with text such as "How can I help you?"
\* \*\*Conversation:\*\* A chat window shows a user asking for AI assistance and receiving a response.
\*\*Image Text:\*\* The text within the image has been provided as OCR.

---

**post_id:** 590813  
**author:** 23f2000098  
**timestamp:** 2025-02-05T11:28:20.791Z

Oh OK sure. I will try out and let you know. Thank You!

---

**post_id:** 590838  
**author:** 22f2000644  
**timestamp:** 2025-02-05T12:51:35.793Z

Got the answer but it was wired that I had run the curl command three time and the 3 times I got different result.

---

**post_id:** 590867  
**author:** abhigyandsa  
**timestamp:** 2025-02-05T13:56:17.493Z

its not working for me any other options plss??

---

**post_id:** 590869  
**author:** 23f2000098  
**timestamp:** 2025-02-05T14:04:28.679Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/23f2003853/48/67184_2.png) 23f2003853:

> rm me where I did mistake

Sorry but im facing an issue with question 6 and 7 where its saying load failed when I submit it. when I run the queries locally using curl im getting the expected results. Any help would be appreciated.  
Here's a description of the image:
\*\*Image Description:\*\*
The image shows a dark-themed interface with text and input fields. The top part of the interface gives a message to enable CORS. It is asking the user for an API URL endpoint. An input field with the URL `http://127.0.0.1:8001/execute` is present with an error message: "TypeError: Load failed". An explanation follows. A "Check" button is visible.
\*\*Image Text:\*\*
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:8001/execute
TypeError: Load failed
We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition.
Check

```
curl "http://127.0.0.1:8001/execute?q=What%20is%20the%20status%20of%20ticket%2083742?"

{"name":"get_ticket_status","arguments":"{\"ticket_id\": 83742}"}

```

---

**post_id:** 590875  
**author:** 23ds2000050  
**timestamp:** 2025-02-05T14:14:44.787Z

For question 2, do we have to make the API call to the proxy or openai? If to the proxy, are there any instructions on the page *before* question 2 that would have pointed me in that direction?

---

**post_id:** 590877  
**author:** Khushii  
**timestamp:** 2025-02-05T14:18:53.764Z

image description: The image is a screenshot of a web page showing code snippets, API interactions, and error messages. On the left side of the page, there is a JSON object that defines a function named "get\_ticket\_status" with an argument "ticket\_id". Below this is a section that gives instruction to enable CORS and specifies an API endpoint. The right side of the page shows an interactive area where a user can enter a query "What is the status of ticket 83742?" and execute the query using the "Execute" button. There is a display for the Responses, including the curl command and the Request URL.
image text: "name": "get\_ticket\_status" "arguments": "{\"ticket\_id\": 83742}" Make sure you enable CORS to allow GET requests from any origin. What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute http://127.0.0.1:8000/execute SyntaxError: "undefined" is not valid JSON We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition. Check 9 Get an LLM to say Yes (1 mark) Name Description q \* required string (query) What is the status of ticket 83742? Execute Clear Responses Curl curl -X 'GET' \ 'http://127.0.0.1:8000/execute?q=What%20is%20the%20status%20 -H 'accept: application/json' Request URL http://127.0.0.1:8000/execute? q=What%20is%20the%20status%20of%20ticket%2083742%3F Server response Code Details
  
I am trying this for so long how to fix this plss guide me. thanking you

---

**post_id:** 590879  
**author:** Khushii  
**timestamp:** 2025-02-05T14:39:36.822Z

there is a problem in question 7 and 8, fast api question, when i click on save, both api calls happens at once at [http://127.0.0.1:8000](http://127.0.0.1:8000/), and i can run fast api app for question 7 or 8 for one only, suppose i check for question 7 it shows correct, also for question 8 i check it shows correct , but when i try to save one of the answer gets incorrected because of simultaneous calls by question 7 and 8 at this address [http://127.0.0.1:8000](http://127.0.0.1:8000/)

---

**post_id:** 590882  
**author:** Jivraj  
**timestamp:** 2025-02-05T14:56:42.479Z

image description: The image is a screenshot of a webpage, likely a programming or data science assignment. There are several tabs open at the top of the screen, one is titled "My Dashboard - IIT Madras", other tabs are titled "Course Introduction :: IITM", "Tools in Data Science" and "TDS 2025 Jan GA3 - Large La". The webpage content is centered around a "Service Flow" with steps described, including "Request Payload," "Embedding Generation," "Similarity Computation," and "Response Structure." It also includes an API URL endpoint with a correct mark and a "Check" button.
image text:
My Dashboard - IIT Madras O X
Course Introduction :: IITM O X
Tools in Data Science
X
Ex TDS 2025 Jan GA3 - Large La X
☆
K
exam.sanand.workers.dev/tds-2025-01-ga3#hq-get-llm-to-say-yes
04:15:56 left Score: 8.5 / 9.5 Check all Save
}
Service Flow:
1. Request Payload: The client sends a POST request with a JSON body containing:
• docs: An array of document texts from the internal knowledge base.
• query: A string representing the user's search query.
2. Embedding Generation: For each document in the docs array and for the query string, the API computes a text embedding using text-embedding-3-small.
3. Similarity Computation: The API then calculates the cosine similarity between the query embedding and each document embedding. This allows the service to
determine which documents best match the intent of the query.
4. Response Structure: After ranking the documents by their similarity scores, the API returns the identifiers (or positions) of the three most similar documents. The JSON
response might look like this:
{
"matches": "Contents of document 3" "Contents of document 1" "Contents of document 2"
}
Here, "Contents of document 3" is considered the closest match, followed by "Contents of document 1", then "Contents of document 2".
Make sure you enable CORS to allow OPTIONS and POST methods, perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity
http://127.0.0.1:8000/similarity
Correct
We'll check by sending a POST request to this URL with a JSON body containing random docs and query.
Check

while saving the 7th,8th question its alteranately getting incorrect

im getting 8.5 marks but while saving it gets deducted to 7 because of these 2 questions  
this is really very frustrating since im working on this for so long like 5-8hours but still facing the same issue  
what to do  
[@carlton](/u/carlton) [@s.anand](/u/s.anand)

---

**post_id:** 590891  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-05T15:26:55.117Z

image description : The image shows a coding test interface related to Large Language Models (LLM). The top part contains navigation elements and a timer. The main body provides instructions for the test, which involves analyzing the sentiment of a text using gpt-4o-mini model. There's a code section with a `DATA` structure containing the `model` and `messages`. An error message highlights the test failure due to incorrect user input, with a call to action "Check".
image text: 03:52:24 left Score: 8.5 / 9.5 Check all Save 1. Make sure you pass an Authorization header with dummy API key. 2. Use gpt-4o-mini as the model. 3. The first message must be a system message asking the LLM to analyze the sentiment of the text. Make sure you mention GOOD, BAD, or NEUTRAL as the categories. 4. The second message must be exactly the text contained above. This test is crucial for DataSentinel Inc. as it validates both the API integration and the correctness of message formatting in a controlled environment. Once verified, the same mechanism will be used to process genuine customer feedback, ensuring that the sentiment analysis module reliably categorizes data as GOOD, BAD, or NEUTRAL. This reliability is essential for maintaining high operational standards and swift response times in real-world applications. Note: This uses a dummy httpx library, not the real one. You can only use: 1. response = httpx.get(url, \*\*kwargs) 2. response = httpx.post(url, json=None, \*\*kwargs) 3. response. raise\_for\_status() 4. response.json() Code DATA = { "model": "gpt-4o-mini", "messages": [ {"role": "system", "content": "Analyze the sentiment of the following text as GOOD, BAD, or NEUTRAL."}, {"role": "user", "content": "N PIXDC6t EXfymclF e K x1XTpIULdX t6H LTa YGZk,"} ] Error: The user message must be N PIxDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZk, not N PIxDC6t EXfymcIF e K x1XTpIULdX t6H LTa YGZK, Check 2 LLM Token Cost (0.75 marks)
  
in the 1st as well both the outouts are exactly same but its still showing error  
[@carlton](/u/carlton)

---

**post_id:** 590905  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-05T16:00:53.142Z

You can run 2 different severs on different port numbers.  
<http://127.0.0.1:8000> and <http://127.0.0.1:8001>

---

**post_id:** 590914  
**author:** Jayeshbansal  
**timestamp:** 2025-02-05T16:22:44.964Z

I tried checking the JSON Output in the Networks tab. I am getting error as “Method Not Found”. But, I have allowed POST Method for question 7 as POST method is used in the question. I also tried checking my API by sending a POST request by the same parameters as given by the Website. I am getting the proper response when I give an API request. Can you please help me out here? I have attached the screenshot of the error as Picture -1 and the correct output what I get as Picture-2. Please help me out as I am facing issue for all the API Questions though I am getting the right output. Thank You.  
![Screenshot 2025-02-05 205509](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/b/6b27da63d6feaeca3359d5e64cccad6f3eed547c.png)  
![Screenshot 2025-02-05 205501](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/5/9/595ffb3b3b3d8766dc77c15ad2270b03892ae0d2_2_690x12.png)

---

**post_id:** 590915  
**author:** Jayeshbansal  
**timestamp:** 2025-02-05T16:23:43.388Z

And for Question-9, I tried 80 prompts and I tried every different way, but I am not getting a Yess from the LLM. Can you please say how to proceed for that? Thank You

---

**post_id:** 590918  
**author:** Jayeshbansal  
**timestamp:** 2025-02-05T16:32:18.808Z

import numpy as np  
def most\_similar(embeddings):  
words = list(embeddings.keys())  
dot\_product\_df =   
for i in words:  
for j in words:  
dot\_product\_df.append(np.dot(embeddings[i], embeddings[j]))  
return max(dot\_product\_df)  
print(most\_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

---

**post_id:** 590921  
**author:** 23f3002537  
**timestamp:** 2025-02-05T16:34:48.632Z

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/jayeshbansal/48/66832_2.png) Jayeshbansal:

> print(most\_similar({“I experienced issues during checkout.”:[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796,0.05536108836531639,-0.07102405279874802,0.21265356242656708,-0.03218059614300728,0.2578633725643158,-0.11707108467817307,0.23163051903247833,0.1780485212802887,0.17972294986248016,0.05302385240793228,0.06889612227678299,-0.13932715356349945,-0.14428070187568665,0.17149029672145844,-0.25590986013412476,0.22311879694461823,-0.06321001797914505,0.019430451095104218,-0.1841881275177002,0.14204810559749603,-0.09976856410503387,-0.17888574302196503,0.07890786230564117,-0.008947774767875671,0.08065207302570343,0.3131197988986969,-0.009226848371326923,-0.1460946649312973,0.16423441469669342,0.024331670254468918,0.055779699236154556,-0.08274511992931366,0.2355375438928604,0.06582632660865784,-0.13674572110176086,-0.003309630323201418,0.008324221707880497],“The return process was easy and hassle-free.”:[-0.13446587324142456,0.02539028227329254,-0.17796370387077332,-0.011354454793035984,-0.04654333367943764,0.15717478096485138,0.07627015560865402,0.22960494458675385,0.001469996408559382,0.1792878359556198,0.05905640497803688,-0.17240233719348907,-0.10083285719156265,-0.08322186022996902,0.00746894720941782,-0.013042726553976536,-0.13718034327030182,0.02444683574140072,-0.07938187569379807,0.04598057642579079,0.0351557731628418,0.1953098624944687,0.011594453826546669,-0.13267828524112701,-0.13718034327030182,-0.14909756183624268,-0.1765071451663971,-0.16776786744594574,-0.11473626643419266,-0.1473761796951294,0.15889616310596466,-0.12354176491498947,0.18882159888744354,-0.040121279656887054,0.18749746680259705,0.16869474947452545,-0.0547860711812973,0.13943137228488922,0.08275841921567917,-0.012976519763469696,0.026582002639770508,0.2568821310997009,0.13314174115657806,-0.08845219761133194,0.025257868692278862,0.35831084847450256,-0.22483806312084198,-0.005697916727513075,0.2899854779243469,0.1855112612247467],“Fast shipping and great service.”:[-0.1079404279589653,0.020684150978922844,-0.30074435472488403,0.11729881167411804,0.13952496647834778,-0.018052106723189354,-0.21843314170837402,0.13527116179466248,-0.09257353842258453,-0.09384968131780624,0.11293865740299225,-0.03900212049484253,-0.059287477284669876,-0.1008152961730957,-0.019155437126755714,-0.007078605704009533,-0.02967032417654991,0.03711449354887009,-0.18302017450332642,0.20056714117527008,0.09076566994190216,0.02584189549088478,0.0943814069032669,-0.03799184039235115,-0.25246360898017883,-0.1235731765627861,0.028952494263648987,-0.309251993894577,0.021375395357608795,-0.22204887866973877,0.2159872055053711,-0.11921302229166031,0.21928390860557556,-0.11432114243507385,0.017453914508223534,0.10065577924251556,-0.04200637340545654,0.17493793368339539,0.1322934925556183,0.17025874555110931,-0.15271177887916565,0.004682514350861311,0.2531017065048218,0.11580997705459595,0.014688937924802303,-0.11176885664463043,-0.292662113904953,-0.0397731214761734,0.13729171454906464,0.027570005506277084],“The payment process was secure and efficient.”:[-0.04701301082968712,-0.20167900621891022,-0.22099372744560242,-0.05536692962050438,0.03149012476205826,0.049234796315431595,-0.02104772813618183,0.1948062777519226,0.004417652729898691,-0.11180031299591064,0.25831976532936096,-0.1503705382347107,-0.14669717848300934,-0.15866521000862122,0.07601473480463028,-0.03744451329112053,-0.1256050169467926,-0.004232503939419985,-0.19717617332935333,-0.07204513996839523,0.07216363400220871,0.23426520824432373,0.005728506948798895,-0.08347994089126587,-0.09248558431863785,-0.16150909662246704,-0.10895642638206482,-0.3507460951805115,-0.1641159951686859,-0.1695667803287506,0.21696490049362183,-0.1385210007429123,0.196346715092659,-0.025669043883681297,-0.07808840274810791,-0.0023291732650250196,-0.03386003151535988,0.14717115461826324,0.06078808754682541,-0.0358448289334774,-0.1290413737297058,0.17335861921310425,-0.08033981174230576,0.1285673975944519,-0.040229152888059616,0.11511818319559097,0.10747523605823517,-0.3336827754974365,0.09313730895519257,-0.002255113562569022],“Customer service resolved my issue quickly.”:[-0.27243417501449585,-0.08034132421016693,-0.3335980772972107,0.03278002515435219,-0.0688093826174736,-0.11652996391057968,-0.13710907101631165,0.2432539016008377,0.07779283076524734,0.0949951708316803,0.1365993618965149,-0.05979407951235771,-0.17151375114917755,-0.040170662105083466,0.12054384499788284,0.10894818603992462,-0.1374913454055786,-0.008736561983823776,-0.2501348555088043,0.040648505091667175,0.20974119007587433,0.021232154220342636,0.1484498679637909,-0.07186757773160934,-0.26733720302581787,0.24248935282230377,-0.04475795477628708,-0.1304829716682434,-0.11914216727018356,-0.2516639530658722,0.16577963531017303,-0.1684555560350418,-0.08875136077404022,-0.1995472013950348,-0.10072928667068481,0.1209898293018341,0.11015872657299042,-0.053359128534793854,0.16705389320850372,0.0013867400120943785,-0.018269527703523636,0.014486604370176792,0.08320838212966919,0.06033563241362572,-0.07224985212087631,0.09869049489498138,-0.021837422624230385,0.1448819786310196,0.10996758937835693,0.058328691869974136]}))

Here's a brief description of the image:
The image shows a snippet of Python code with an error message at the bottom. The code appears to be calculating something related to embeddings, dot products, and finding the most similar item. The error message indicates a `TypeError: Z.runPython(...).toJs is not a function`.
image text: Write your Python code here:
for i in words:
for j in words:
dot product df.append(np.dot(embeddings[i], embeddings[j]))
return max(dot\_product\_df)
print(most similar({"I experienced issues during checkout.":
[-0.10228022187948227,-0.057035524398088455,-0.03200617432594299,-0.1569785177707672,-0.11162916570901871,-0.017878107726573944,-0.06209
372356534004,0.18209508061408997,-0.0027645661029964685,0.12928052246570587,0.17609500885009766,-0.11846645176410675,-0.2356770783662796
TypeError: Z.runPython(...).toJs is not a function

---

**post_id:** 590922  
**author:** 23f2005419  
**timestamp:** 2025-02-05T16:48:48.163Z

Here's a description of the image:
The image contains text related to an API URL endpoint, likely for an implementation or test. It highlights an example URL and an error message.
image text: What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:8000/execute?q=
TypeError: Failed to fetch
We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the
function definition.

---

**post_id:** 590926  
**author:** 23f3002537  
**timestamp:** 2025-02-05T17:02:48.548Z

image description : The image shows a coding environment with three main sections: a web page, a request tool, and a terminal. The web page is a task interface displaying a score and the prompt about an API URL endpoint for implementation, with details about enabling CORS and sending a POST request. The request tool, set to POST method at the address /similarity, displays a JSON body containing example documents and a query, along with the response, showing the "matches". The terminal output indicates a running Uvicorn server and details on the POST requests made.
image text:
exam.sanand.workers.dev/tds-2025-01-ga3
02:10:25 left Score: 7/9.5 Check all Save
matches
Here, "Contents of document 3" is considered the closest
match, followed by "Contents of document 1", then "Contents
of document 2".
Make sure you enable CORS to allow OPTIONS and POST methods,
perhaps allowing all origins and headers.
What is the API URL endpoint for your implementation? It might
look like: http://127.0.0.1:8000/similarity
http://127.0.0.1:8000/similarity
Error: Got incorrect matches: The project blueprint for migrating to a
microservices architecture is complete.,Our system maintenance schedule has
been updated to minimize downtime., The IT support portal now features a
self-service FAQ for common issues.
We'll check by sending a POST request to this URL with a JSON
body containing random docs and query.
Check
8 Function Calling (1.5 marks)
THUNDER CLIE...
← →
TC 127.0.0.1:8000/similarity X q7\_test.py
New Request
POST http://127.0.0.1:8000/similarity
Send
Activity Collections Env
Query Headers 2 Auth Body 1 Tests Pre Run
filter activity
JSON XML Text Form Form-encode GraphQL Binary
POST 127.0.0.1:8000/s...
3 hours ago
1
{
2
"docs": ["Contents of document 1", "Contents of
document 2", "Contents of document 3"],
GET 127.0.0.1:8000/si...
3
"query": "Your query string"
4 hours ago
4
}
Status: 200 OK Size: 88 Bytes Time: 8 ms
Response
1
{
2
"matches": [
3
"Contents of document 1",
4
"Contents of document 2",
5
"Contents of document 3"
6
]
7
}
PROBLEMS OUTPUT TERMINAL
Response Chart
$ python -m uvicorn q7\_test:app --host 127.0.0.1 --port 8000 --r
eload
INFO:
Will watch for changes in these directories: ['D:\\Prof
essional\\Iltm\\TDS\\Week\_3']
INFO:
Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C
to quit)
INFO:
Started reloader process [9060] using StatReload
INFO:
Started server process [15880]
INFO:
Waiting for application startup.
INFO:
Application startup complete.
INFO:
127.0.0.1:64190 "POST /similarity HTTP/1.1" 200 OK
INFO:
127.0.0.1:64196
"POST /similarity HTTP/1.1" 200 OK
  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) Sir please look at the err on Q7.I am able to run on my system and getting the desired json but its not working in the portal. Today is the deadline sir please help me out!

I m attaching my codes:

```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["OPTION","POST"],  
    allow_headers=["*"],
)

class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

def clean_text(text: str):
    """Clean text by lowering case, removing punctuation, and extra spaces."""
    text = text.lower()  
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\w\s]', '', text)  
    return text

@app.post("/similarity")
async def find_similar_docs(request: SimilarityRequest):
    try:
        cleaned_docs = [clean_text(doc) for doc in request.docs]
        cleaned_query = clean_text(request.query)

vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(cleaned_docs + [cleaned_query])

query_vector = tfidf_matrix[-1]
        doc_vectors = tfidf_matrix[:-1]
        similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

top_indices = sorted(range(len(similarity_scores)), key=lambda i: similarity_scores[i], reverse=True)[:3]
        matched_docs = [request.docs[i] for i in top_indices]

return {"matches": matched_docs}

except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/execute")
async def execute_query(q: str):
    return {"message": f"Executing query: {q}"}

```

---

**post_id:** 590940  
**author:** Jayeshbansal  
**timestamp:** 2025-02-05T17:51:02.543Z

Hi,

I’m sorry if I’m asking an unrelated question, But I’m very confused with the concept of generating the token from <https://platform.openai.com/api-keys>

Could any one suggest the step by step process? I couldn’t able to find that similar question asked by anyone since the conversations are vast.

Please guide me on this. Also do i need to use my personal mail id or iitm mail id for accessing this token

---

**post_id:** 590970  
**author:** Aditya_Sahu  
**timestamp:** 2025-02-05T18:28:04.849Z

yes you have to use your IITM email id . Use this link and login you will get your token:  
<https://aiproxy.sanand.workers.dev/>

---

**post_id:** 590974  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-05T18:33:06.841Z

image description: The image shows an API URL endpoint and an error message. The API URL is in a red bordered text box, and the error message is below it.
image text: What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:9000/execute
SyntaxError: "[object Object]" is not valid JSON

---

**post_id:** 590975  
**author:** Sudhishnarayan  
**timestamp:** 2025-02-05T18:34:39.598Z

The error shows your code is getting wrong answers for the test cases. I looked into your code and noticed that you are using sklearn (I think which is not required in this case). Just get embedding vector for each document content and query by passing a valid POST request to <http://aiproxy.sanand.workers.dev/openai/v1/embeddings> with required headers. And, then calculate `similarity_scores` simply using  
\cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{A}| |\mathbf{B}|}  
which in python syntax is-

```
np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

```

---

**post_id:** 590987  
**author:** Pururaj  
**timestamp:** 2025-02-05T18:43:40.732Z

Sir, Regarding the embedding questions, I had posted earlier. Now, I am writing the error I faced. I tried to use the OpenAI API, but I am getting the error as “The Maximum Quota has reached”. I tried using 5 new API Keys from OpenAI, from 5 different accounts. So, I had to use SentenceTransformers, Alibaba gte model. So, as the model has changed, I think so it is expecting answer as got from OpenAI Model, but as I used Alibaba gte model, I am getting different result. Can you please explain how to solve this issue? This will be helpful in my future codes. I could do chat requests but it is not giving output for Embedding requests, I tried it multiple times with multiple different keys.Thank You  
![Screenshot 2025-02-05 235804](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/0/b05d3520e550b5174ba2b43efc5b7ae8e729d551_2_690x22.png)

---

**post_id:** 591016  
**author:** roy2003  
**timestamp:** 2025-02-06T03:04:45.047Z

This is my code for the 7th question of finding similarities. This code, I tried on my own, but it is showing Incorrect Matches. I think so it is due to the Aliababa GTE Model. Please correct me if I have gone wrong anywhere. Thank You

```
from fastapi import FastAPI, Query
import httpx
from typing import List
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer('Alibaba-NLP/gte-large-en-v1.5', trust_remote_code=True)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["OPTIONS", "POST"],  # Allows all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allows all headers
)

class similarity1(BaseModel):
    docs: list[str]
    query: str
@app.post("/similarity")
async def similarity(similarity1: similarity1):
    docs = similarity1.docs
    query = similarity1.query
    results_docs = model.encode(docs)
    results_query = model.encode(query)
    similarities = {}
    output = []
    for i in range(len(results_docs)):
        c = np.dot(results_docs[i], results_query) / (np.linalg.norm(results_docs[i])*np.linalg.norm(results_query))
        similarities[c] = docs[i]
    k = sorted(list(similarities.keys()))
    for i in k[::-1][:3]:
        output.append(similarities[i])
    return {"matches" : output}
if __name__ == "__main__":
  (uvicorn.run(app))

```

---

**post_id:** 591017  
**author:** roy2003  
**timestamp:** 2025-02-06T03:08:19.006Z

image description: The image is a screenshot of a web page, most likely related to an online learning platform. The top banner indicates that the session has ended on Wednesday, February 5, 2025, at 11:59 pm IST, with a score of 0. There are buttons for "Check all" and "Save". Below, a light blue banner prompts the user to join a discussion on Discourse. It displays the logged-in user's email address, followed by a "Logout" button. The section "Recent saves" lists two saved sessions with the date and time, along with their scores.
image text: Ended at Wed, 5 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
Have questions? Join the discussion on Discourse
You are logged in as 24f2005437@ds.study.iitm.ac.in.
Logout
Recent saves
Loaded from 5/2/2025, 11:20:33 pm. Score: 6
Reload from 5/2/2025, 11:20:20 pm. Score: 6
  
i submitted the assignment on time but i am still getting assignment not submitted. And it also show zero marks. Same thing happened with graded assignment 2. [@Jivraj](/u/jivraj)

---

**post_id:** 591060  
**author:** 23ds1000022  
**timestamp:** 2025-01-30T10:42:26.627Z

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
I have submitted ga3 still showing not submitted , why sir?  
image description: The image is a screenshot of a webpage related to an online course assessment. The page features instructions, recent saves, and details about an assignment. The top of the page displays the course title "TDS 2025 Jan GA3 - Large Language Models".
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
Your Score
Peer Average
Median Score

---

**post_id:** 588065  
**author:** Jivraj  
**timestamp:** 2025-01-30T22:22:09.894Z

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
please reply why its showing not submitted in ga3 but i have submitted that  
image description: The image is a webpage about "TDS 2025 Jan GA3 - Large Language Models" with instructions, user information, and assignment details. The page contains instructions numbered 1-7, along with a note about running multiple servers. The user is logged in.
image text: TDS 2025 Jan GA3 - Large Language Models
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
Your Score
Peer Average
Median Score
-
-
-

---

**post_id:** 591063  
**author:** Sakshi6479  
**timestamp:** 2025-02-01T12:44:20.471Z

[@carlton](/u/carlton), [@Jivraj](/u/jivraj)  
Both the api based questions i am unable to get the output it always says bad request  
image description: The image shows a code editor with Python code and terminal output. The code defines a function `parse\_query` that attempts to match different patterns from the input query. The terminal output displays "400 Bad Request" and "404 Not Found" errors, indicating issues with the queries. The file explorer is visible showing project structure.
image text:
```
EXPLORER
GA3\_Q8
main.py
x
\*.env
app > main.py > parse\_query
GA3\_Q8
✓ app
47 def parse\_query(query: str):
54 return "get\_ticket\_status", {"ticket\_id": int(match\_ticket\_status.group(1))}
55 # Match "Arrange meeting 2025-12-17, 06:09, room: Conf1"
56 match\_schedule\_meeting = re.match(
57 r"(?i)(arrange\s\*meeting|schedule\s\*a\s\*meeting)\s\*(?:on\s\*)?(\d{4}-\d{2}-\d{2}
58 query
59 )
60 if match\_schedule\_meeting:
61 print(f"Schedule Meeting Match: {match\_schedule\_meeting.groups()}") # Debug lo
62 return "schedule\_meeting", {
63 "date": match\_schedule\_meeting.group (2),
64 "time": match\_schedule\_meeting.group (3),
65 "meeting\_room": match\_schedule\_meeting.group (4).strip(),
66 }
67
68
69 # Match "Show my expense balance for employee <employee\_id>"
70 match\_expense\_balance = re.match(r"(?i)show\s\*my\s\*expense\s\*balance\s\*for\s\*employ
71 if match\_expense\_balance:
72 print(f"Expense Balance Match: {match\_expense\_balance.groups()}") # Debug log
PROBLEMS OUTPUT DEBUG CONSOLE TERMINAL PORTS
Query format did not match any predefined patterns.
INFO: 127.0.0.1:60464 - "GET /execute?q=Arrange+meeting+2025-12-17%2C+06%3A09%2C+room%3A+
Conf1 HTTP/1.1" 400 Bad Request
INFO: 127.0.0.1:60464 - "POST /similarity HTTP/1.1" 404 Not Found
Parsing query: Arrange meeting 2025-12-17, 06:09, room: Conf1
Query format did not match any predefined patterns.
INFO: 127.0.0.1:60464 - "GET /execute?q=Arrange+meeting+2025-12-17%2C+06%3A09%2C+room%3A+
Conf1 HTTP/1.1" 400 Bad Request
Ln 58, Col 6 Spaces: 4 UTF-8 LF {} Python 3.13.1 ('venv': venv)
```  
image description: The image is a screenshot of a webpage, likely related to a coding or programming assignment. The top part of the page shows a navigation bar with a URL "exam.sanand.workers.dev/tds-2025-01-ga3#hq-function-calling". The date and time "Due Sun, 2 Feb, 2025, 11:59 pm IST" are also displayed. The page includes a code snippet, followed by text instructions asking the user to enable CORS. Below that, an API URL is presented with an error message "Error: Failed to fetch: Bad Request". Finally, there is a question or task for the user "Get an LLM to say Yes (1 mark)".
image text:
exam.sanand.workers.dev/tds-2025-01-ga3#hq-function-calling
Due Sun, 2 Feb, 2025, 11:59 pm IST Score: 6.5 / 9.5 Check Save
```json
{
"name": "get\_ticket\_status",
"arguments": "{\"ticket\_id\": 83742}"
}
```
Make sure you enable CORS to allow GET requests from any origin.
What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/execute
http://127.0.0.1:8000/execute
Error: Failed to fetch: Bad Request
We'll check by sending a GET request to this URL with ?q=... containing a task. We'll verify that it matches the expected response. Arguments must be in the same order as the function definition.
9 Get an LLM to say Yes (1 mark)
  
all other questions i have finished. even in Ga2 all these api and flask creates a lot of issues. if there is any complete guide to understand this also pls help us.

---

**post_id:** 588807  
**author:** Jivraj  
**timestamp:** 2025-02-01T16:06:29.936Z

Hi [@23ds1000022](/u/23ds1000022) ,

Check network tab, there check for response of `http://127.0.0.1:8000/api` request.

---

**post_id:** 588820  
**author:** 23f2000237  
**timestamp:** 2025-02-01T16:32:58.809Z

I have counted the number of tokens in gpt-4o-mini but when I was entering the answer in portal it was showing incorrect please take a look and provide a solution for it .  
image description: The image is a screenshot from the OpenAI Platform, showcasing a text processing interface. It displays various elements and text.
image text: OpenAl Platform Docs API reference Le GPT-40 & GPT-40 mini GPT-3.5 & GPT-4 GPT-3 (Legacy) ... eWHNetl, eGEjb, 9, kZFurXr, Pnti2d0, HnV66V0, cR9zhYBi, NL, 9T1DU3, DaRw, 9irI10, 6AiKKkHU, FJ7XYuT, ZBfU30, TH, B, EuaXvr4VYp, YC, li6J4dJPn, pTWN, EZshp, eET, U163LMWSW, D, s, VvBmRL3t, O3YTvv, mx6N, QLVNE, PF, Btl1SAW8jP, F1jqXwyZy, uQJiS, XjNNS, 89NSMaNWrh, z017vbI, Hzb2, TZbpJdLQ, DRmAkXE, bjq8QYisGG, VVJØDT, 2VL, dHyrz, kOFDUi3pf, joAB7U1c, Mzhkjz8oQI, J, L8wIWIF, QAQ11c5vQ, mNNOQ4RJFX, xvX, rMeYNv, pC30jjkI, yguY0s85, fDlnOqd, iPWS5, xOkd, tSWIafaO, 7Kiy7Imj, FWs1n2s, LGsZ18GED, g6Skq, I3nUSc2, Nh6b, SOQX, 8, q0lrAnQIz, OcyWnSIE, N5Uk, C Clear Show example Tokens 406 Characters 625

---

**post_id:** 588839  
**author:** Jivraj  
**timestamp:** 2025-02-01T17:03:51.869Z

There are few more tokens for the user prompt, I think if you add 7 or 8 then you would get correct answer.

Other way to do this question is send a request to anand sir’s aiproxy and in response you will get number of input tokens.

---

**post_id:** 591066  
**author:** 23f2001915  
**timestamp:** 2025-02-03T18:11:42.650Z

I inspected the JavaScript code of this website, I saw that the answer took my input and added 7 to it, why is it programmed this way? Even if I were to use the AI proxy that was given shouldn’t the number of tokens remain unaffected?

---

**post_id:** 590399  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:25:44.421Z

When you send request to openai through anand sir’s proxy it takes some tokens for user prompt.

When you use tokenizer from openai’s webpage then it doesn’t take care of that.

---

**post_id:** 591069  
**author:** Sakshi6479  
**timestamp:** 2025-02-03T19:44:12.086Z

How to answer the 3rd question in ga 3 i have to no clue (tired inspecting its html pages)

---

**post_id:** 590401  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:40:49.588Z

[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

### [2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

---

**post_id:** 591072  
**author:** 24f2006531  
**timestamp:** 2025-02-03T09:24:00.805Z

Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

Q7 & Q8 in these questions the problem is the same my app couldn’t fetch the details from the file.

```
`from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import openai
from fastapi.responses import JSONResponse
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize FastAPI app
app = FastAPI()

# Add CORSMiddleware with more restrictive settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow only this specific origin
    allow_credentials=True,
    allow_methods=["POST", "OPTIONS"],  # Allow only POST and OPTIONS methods
    allow_headers=["Content-Type", "Authorization"],  # Allow only specific headers
)

# OpenAI API key (use your own key)
openai.api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjIwMDY3NDlAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.tMJtqZrzRqREY7E3wsFMd9PkElXEbRBpCkb533ORGEU'

# Request body model for /similarity endpoint
class SimilarityRequest(BaseModel):
    docs: List[str]
    query: str

# Function to get embeddings (using OpenAI API)
def get_embedding(text: str):
    response = openai.Embedding.create(
        model="text-embedding-ada-003",  # Use the correct model
        input=text
    )
    return response['data'][0]['embedding']

# POST /similarity endpoint
@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    docs = request.docs
    query = request.query
    query_embedding = get_embedding(query)
    doc_embeddings = [get_embedding(doc) for doc in docs]
    
    # Cosine similarity
    similarities = [cosine_similarity([query_embedding], [doc_embedding])[0][0] for doc_embedding in doc_embeddings]
    ranked_docs = [docs[i] for i in np.argsort(similarities)[::-1]]
    
    return JSONResponse(content={"matches": ranked_docs[:3]})

# Optionally, handle requests to the root (GET /)
@app.get("/")
async def root():
    return {"message": "Welcome to the similarity API!"}
`

```

and for Q8

```
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
import re

# Create the FastAPI app
app = FastAPI()

# CORS configuration to allow any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)
def get_ticket_status(ticket_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"ticket_id": ticket_id, "status": "open"}

def schedule_meeting(date: str, time: str, meeting_room: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"date": date, "time": time, "meeting_room": meeting_room, "status": "scheduled"}

def get_expense_balance(employee_id: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "balance": 1000.0}

def calculate_performance_bonus(employee_id: int, current_year: int) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"employee_id": employee_id, "current_year": current_year, "bonus": 500.0}

def report_office_issue(issue_code: int, department: str) -> Dict[str, Any]:
    # Mock response for illustration purposes
    return {"issue_code": issue_code, "department": department, "status": "reported"}
import re

def extract_parameters(query: str) -> Dict[str, Any]:
    """Extract parameters from the query string."""
    # Convert the query to lowercase for case-insensitive matching
    query = query.strip().lower()

if match := re.match(r"what is the status of ticket (\d+)\?", query):
        return {
            "name": "get_ticket_status",
            "arguments": {"ticket_id": int(match.group(1))}
        }
    elif match := re.match(r"schedule a meeting on (\d{4}-\d{2}-\d{2}) at (\d{2}:\d{2}) in (.+)\.", query):
        return {
            "name": "schedule_meeting",
            "arguments": {
                "date": match.group(1),
                "time": match.group(2),
                "meeting_room": match.group(3)
            }
        }
    elif match := re.match(r"show my expense balance for employee (\d+)\.", query):
        return {
            "name": "get_expense_balance",
            "arguments": {"employee_id": int(match.group(1))}
        }
    elif match := re.match(r"calculate performance bonus for employee (\d+) for (\d{4})\.", query):
        return {
            "name": "calculate_performance_bonus",
            "arguments": {
                "employee_id": int(match.group(1)),
                "current_year": int(match.group(2))
            }
        }
    elif match := re.match(r"report office issue (\d+) for the (\w+) department\.", query):
        return {
            "name": "report_office_issue",
            "arguments": {
                "issue_code": int(match.group(1)),
                "department": match.group(2)
            }
        }
    return {}

@app.get("/execute")
async def execute_query(q: str):
    # Extract the function name and arguments from the query
    result = extract_parameters(q)
    
    if not result:
        return JSONResponse(content={"error": "No matching function found for the query"}, status_code=400)
    
    # Call the respective function
    func_name = result["name"]
    arguments = result["arguments"]
    
    # Call the function dynamically based on func_name
    if func_name == "get_ticket_status":
        response = get_ticket_status(**arguments)
    elif func_name == "schedule_meeting":
        response = schedule_meeting(**arguments)
    elif func_name == "get_expense_balance":
        response = get_expense_balance(**arguments)
    elif func_name == "calculate_performance_bonus":
        response = calculate_performance_bonus(**arguments)
    elif func_name == "report_office_issue":
        response = report_office_issue(**arguments)
    
    # Return the response in the requested format
    return JSONResponse(content={"name": func_name, "arguments": arguments}, status_code=200)

```

Please kindly guide me with these problems as I am trying to do it since last 3 days. I am exhaust now, Please help me with this. [@Jivraj](/u/jivraj) , [@carlton](/u/carlton) , [@Saransh\_Saini](/u/saransh_saini)

---

**post_id:** 590400  
**author:** sha_512_av  
**timestamp:** 2025-02-03T22:26:57.365Z

Hi Sakshi

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png) Sakshi6479:

> Q3 how to generate answer box ,I am not able to do it. kindly guide me with that.

[drive.google.com](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

### [2025-02-04 03-50-48.mkv](https://drive.google.com/file/d/1Q13I7rmh1rc3_pCDlMjDgiMGr7d92W5w/view?usp=sharing)

Google Drive file.

---

**post_id:** 590402  
**author:** Jivraj  
**timestamp:** 2025-02-03T22:45:02.248Z

For question 7

![](https://dub1.discourse-cdn.com/flex013/user_avatar/discourse.onlinedegree.iitm.ac.in/sakshi6479/48/110446_2.png) Sakshi6479:

> ```
> import openai
>
> ```

You won’t be able to send request through openai python module, here is one example how you would make a request

```
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

json_data = {
    'model':'gpt-4o-mini',
    'messages':[
        {
            'role':'user',
            'content':'What is 2+2?'
        }
    ]
}
r = httpx.post('http://aiproxy.sanand.workers.dev/openai/v1/chat/completions', headers = headers, json = json_data, timeout=10.0)

```

You would need to use professor Anand’s proxy or some other api key through which request can be made.  
Url’s for free api keys:

1. [AI Proxy](https://aiproxy.sanand.workers.dev/)
2. [OpenAI GPT-4o · GitHub Models](https://github.com/marketplace/models/azure-openai/gpt-4o/playground)

The way to use api’s is demonstrated in live sessions, also refer to this documentation [sanand0/aiproxy: Authorizing proxy for LLMs](https://github.com/sanand0/aiproxy).

---

**post_id:** 591079  
**author:** Jeleshiya  
**timestamp:** 2025-02-05T18:48:31.180Z

For question 8, you’ll need to use OpenAI’s function calling feature and identify which function needs to be called and arguments to be used, we discussed in last Friday’s session on functions like `order` and `cancel_order`.

Kind regards

---

**post_id:** 591077  
**author:** carlton  
**timestamp:** 2025-02-06T06:05:01.971Z

Hello sir,

While working on this question, I’m encountering this problem. It looks like the request is being made successfully (and I verified it by a POST request via Postman ), however while submitting my URL at the assignment portal, I’m getting an error.

image description: The image shows a dark background with text in a monospace font. It appears to be a log of some database operations. Key parts of the log are highlighted in green.
image text: INFO: 127.0.0.1:59423 - "OPTIONS /similarity HTTP/1.1" 200 OK
Collection reset successfully!
Created new collection: documents
Added 10 new documents to the database.
Searching for query: How is our internal training addressing cybersecurity challenges?
Found matches: ['Employee training on cybersecurity best practices is being rolled out company-wide.', 'The staff handbook has been updated to reflect current operational policies.', 'Our quality assurance team has implemented automated testing protocols.']
INFO: 127.0.0.1:59423 - "POST /similarity HTTP/1.1" 200 OK
  
image description: The image is a screenshot of a dark-themed UI, likely a code editor or a testing interface, that shows a potential API endpoint. The main elements include an input field pre-filled with "http://127.0.0.1:8000/similarity" and a detailed error message below. The message indicates that an incorrect match was found, with additional context about ongoing initiatives in employee training, updated staff handbooks, and automated testing protocols.
image text: What is the API URL endpoint for your implementation? It might look like: http://127.0.0.1:8000/similarity
http://127.0.0.1:8000/similarity
Error: Got incorrect matches: Employee training on cybersecurity best practices is being rolled out company-wide., The staff handbook has been updated to reflect current operational policies.,Our quality assurance team has implemented automated testing protocols.

I even tried deploying on a public URL using render. My guess is there is a formatting issue or it’s not sorting correctly based on the similarity score and not returning the top 3.

Would appreciate if I can get some clarity on the same

Thanks and Regards  
Shalini

---

**post_id:** 591133  
**author:** Pururaj  
**timestamp:** 2025-02-06T07:21:52.633Z

Hello, I think the format of the response body should be like: { “matches” : [ “ABC”, “ABC”, “ABC”]}. I think it is because of your formatting issue.

Here's a description of the image:
The image is a screenshot of a Postman interface. It shows a POST request to the endpoint `http://127.0.0.1:8000/similarity`. The request has no authorization. The body of the request is in JSON format and contains an array of strings under the key "matches". The response status is 200 OK.
image text:
POST http://127.0.0.1:8000/si⚫
HTTP http://127.0.0.1:8000/similarity
POST http://127.0.0.1:8000/similarity-
Params Authorization Headers (8) Body ⚫ Scripts Settings
Auth Type
No Auth
No Auth
This request does not use any authorization.
Body Cookies Headers (4) Test Results
{} JSON Preview Visualize
1
2 "matches":[
3 "FastAPI is great for APIs.",
4 "Embedding models improve NLP."
5 "Machine learning is evolving.
6 ]
7
200 OK 17.26 s 232 B
Cookies

I had used (well gpt) the below two decorators to format:

```
class SearchRequest(BaseModel):
    docs: List[str]  # The list of documents to search through
    query: str       # The search query string

class SearchResponse(BaseModel):
    matches: List[str]  # The list of matched documents

.........

@app.post("/similarity", response_model=SearchResponse)

.........

return SearchResponse(matches=sorted_matches[:3])

```

It basically checks the Request and Response formatting. This worked for me. Hope it helps. And thanks btw for mentioning using POSTMAN, as I had never used it before, so it clicked in my mind after reading your post only that I can basically debug using POSTMAN. Thank you for that ![:grinning:](https://emoji.discourse-cdn.com/google/grinning.png?v=12 ":grinning:")

---

**post_id:** 591272  
**author:** carlton  
**timestamp:** 2025-02-06T14:43:17.371Z

```
{
  "matches": ["Contents of document 3", "Contents of document 1", "Contents of document 2"]
}

```

Check if your response is in this format.

kind regards  
Jivraj

---

**post_id:** 591894  
**author:** 23f2001286  
**timestamp:** 2025-02-08T01:44:42.024Z

Does the final submission get graded, or is the highest-scoring submission considered?

I’m facing an issue where my score dropped from 8 to 6.5 when I checked all the answers one last time before submitting. I suspect the drop is due to the 3rd and 7th questions.

Here's a description of the image:
The image is a UI element or a section of a screen. It presents a list titled "Recent saves". Each entry in the list shows a "Reload" button followed by the date, time, and a score associated with a saved item.
image text:
Recent saves
Reload from 2/5/2025, 11:59:18 PM. Score: 6.5
Reload from 2/5/2025, 11:30:37 PM. Score: 8
Reload from 2/5/2025, 10:44:08 PM. Score: 6.5

---

**post_id:** 592815  
**author:** 23f2005275  
**timestamp:** 2025-02-09T15:16:04.343Z

image description: The image is a webpage with instructions for an exam. The top section shows the exam title and administrative information. The main content area features the heading "Instructions" along with a set of numbered guidelines, including how to check and save answers. The last point in the instructions mentions that the exam is "hackable" and encourages use of external resources.
image text: [Admin] Ended at Wed, 5 Feb, 2025, 11:59 pm IST Score: 0 Check all Save
TDS 2025 Jan GA3 - Large Language M
Instructions
1. Learn what you need. Reading material is provided, but feel free to skip it if you can answer the question. (Or learn it, just for pleasure.)
2. Check answers regularly by pressing Check. It shows which answers are right or wrong. You can check multiple times.
3. Save regularly by pressing Save. You can save multiple times. Your last saved submission will be evaluated.
4. Reloading is OK. Your answers are saved in your browser (not server). Questions won't change except for randomized parameters.
5. Browser may struggle. If you face loading issues, turn off security restrictions or try a different browser.
6. Use anything. You can use any resources you want. The Internet, ChatGPT, friends, whatever. Use any libraries or frameworks you want.
7. It's hackable. It's possible to get the answer to some questions by hacking the code for this quiz. That's allowed.
Note: You'll run multiple servers in this exam. All of them must be running simultaneously while checking or saving answers.

The score drops because some questions may require you to either keep a server turned on or some dynamic changes may occur for some questions (The dynamic changes are intentional in some questions, in order to get students to learn by doing. So if you solved everything and the score is the maximum… just make that your last submission. The score you see is the score you will get for your last submission).

If you want check a question without submitting. Then just use the check button instead. But your last submission is whats scored.

---

**post_id:** 593680  
**author:** Imran1  
**timestamp:** 2025-02-10T20:31:27.549Z

Same problem with my submission

---

**post_id:** 593946  
**author:** 23f1002382  
**timestamp:** 2025-02-11T18:55:49.596Z

Here's a brief description of the image:
The image is a bar chart showing the distribution of GA3 Active Scores. The Y-axis represents "GA2 Student Count" and the X-axis represents "Scores" ranging from 0 to 100 in intervals of 10. The bar heights indicate the number of students within each score range. There is a notable peak in the score range of 90-100, with a "ga3 student count" of 249.
image text: GA3 Active Score Distribution
GA2 Student Count
250
200
150
100
50
62
59
55
49
42
104
93
91
35
(90, 100]
ga3 student count: 249
12
0
0
(0, 10]
(10, 20]
(20, 30]
(30, 40]
(40, 50]
(50, 60]
(60, 70]
(70, 80]
(80, 90]
(90, 100]
Scores

For those that are interested.

---

**post_id:** 595779  
**author:** carlton  
**timestamp:** 2025-02-16T06:31:21.790Z

sir why the GA marks is not being reflected in the course page. We are getting a sign of non submission.  
Is there any way getting the score.

---

**post_id:** 595746  
**author:** Jivraj  
**timestamp:** 2025-02-16T04:40:57.975Z

Hello sir ,I find a issue with submission of GA4. Actually i submitted ga3 on “[Technical Assessment](https://exam.sanand.workers.dev/tds-2025-01-ga3)” with full marks but in the course >grade portal it is saying it is not submitted. what’s the issue is this?

---

**post_id:** 630500  
**author:** shaikyasirsy  
**timestamp:** 2025-05-24T17:22:55.395Z

I also have same problem

---

**post_id:** 632753  
**author:** Tanmay1  
**timestamp:** 2025-05-28T12:10:33.577Z

can you please reply?  
[@Jivraj](/u/jivraj) [@carlton](/u/carlton)

---

**post_id:** 632985  
**author:** Nomad  
**timestamp:** 2025-05-29T08:28:21.746Z

A post was merged into an existing topic: [GRADED ASSIGNMENT RESULT NOT SHOWING , kindly check on this](/t/graded-assignment-result-not-showing-kindly-check-on-this/166816/20)

---

**post_id:** 633113  
**author:** Puneet-IITM  
**timestamp:** 2025-05-29T15:59:44.618Z

---

**post_id:** 633277  
**author:** 22f3001416  
**timestamp:** 2025-05-30T08:32:40.341Z

Error: Invalid promptfooconfig.yaml: Missing required assertion for: <https://api.github.com/orgs/>  
for 14th Question

```
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
prompts:
  - file://prompt.json

providers:
  - openai:gpt-4o-mini
  - openai:gpt-4o-mini
  - openrouter:openai/gpt-4o-mini
  - openrouter:openai/gpt-4.1-nano
  - openrouter:google/gemini-2.0-flash-lite-001
  - openai:gpt-4o-mini

defaultTest:
  vars:
    system_message: file://system_message.txt
    previous_messages:
      - user: Who founded Facebook?
      - assistant: Mark Zuckerberg
      - user: What's his favorite food?
      - assistant: Pizza

tests:
  - vars:
      question: Did he create any other companies?
  - vars:
      question: What is his role at Internet.org?
  - vars:
      question: Will he let me borrow $5?
  - vars:
      question: Did he create any other houses?
  - vars:
      question: Did he create any other hospitals?
  - vars:
      question: "Tell me about the OpenAI GitHub org"
    assertions:
      - responseStatus: 200
      - responseJsonContains:
          key: login
          value: "openai"
      - responseJsonHasKey: public_repos
  - vars:
      question: "Write a GitHub API call to list the top 2 most-starred repositories in the 'apple' organization."
    assertions:
      - contains-all:
          values:
            - "https://api.github.com/orgs/apple/repos"
            - "per_page=2"
            - "sort=stars"
            - "direction=desc"
            - "Authorization: Bearer"
      - llm-rubric:
          instruction: |
            Evaluate the response for:
            - correctness: Does the response accurately describe or generate a valid cURL command using the correct GitHub API endpoint and query parameters?
            - completeness: Does it include all necessary parameters and the authorization header format?
          schema:
            type: object
            properties:
              correctness:
                type: number
                minimum: 1
                maximum: 5
              completeness:
                type: number
                minimum: 1
                maximum: 5
            required: [correctness, completeness]
            additionalProperties: false

# ✅ Required assertion related to https://api.github.com/orgs/
  - vars:
      question: "What does https://api.github.com/orgs/ return?"
    assertions:
      - contains: "https://api.github.com/orgs/"

```

---

**post_id:** 633797  
**author:** Abhishek11_11  
**timestamp:** 2025-06-01T04:45:34.901Z

Question 4:  
I am trying this :

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Extract text from this image."},
        {
          "type": "image_url",
          "image_url": { "url": "data:image/png;base64,iVBORw0KGgoAAAANS.......=" }
        }
      ]
    }
  ]
}

```

I am getting this error :  
Error: The image\_url.url must be the base64 data URL of the image  
I verified that my Base64 encoding for the image is correct ..

---

**post_id:** 633818  
**author:** Nomad  
**timestamp:** 2025-06-01T06:06:21.230Z

Getting the same issue -

```
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json

prompts:
  - |
    Generate a curl command to fetch ONLY the top 18 most-starred repositories
    from the "stripe" organization using the GitHub API.
    Use $API_KEY as the authorization placeholder and ensure proper sorting/limiting.

providers:
  - id: openrouter:openai/gpt-4o-mini
    config:
      max_tokens: 1024
  - id: openrouter:openai/gpt-4.1-nano
    config:
      max_tokens: 1024
  - id: openrouter:google/gemini-2.0-flash-lite-001

tests:
  - vars:
      API_KEY: "ghp_example"
    assert:
      - type: regex
        value: 'https://api\.github\.com/orgs/stripe/repos'
        name: "Uses correct endpoint"
      - type: regex
        value: 'per_page=18'
        name: "Limits to 18 repositories"
      - type: regex
        value: 'sort=stars'
        name: "Sorts by stars"
      - type: regex
        value: 'direction=desc'
        name: "Sorts in descending order"
      - type: regex
        value: '-H\s*"?Authorization:\s*Bearer\s*\$API_KEY"?'
        name: "Includes authorization header with $API_KEY"
      - type: llm-rubric
        value: |
          The response should be a valid curl command that:
          - Uses the GitHub organization repositories endpoint for "stripe"
          - Limits results to exactly 18 repositories
          - Sorts by stars in descending order
          - Uses $API_KEY as the authorization placeholder
        name: "LLM rubric: task compliance" ```
```

---

**post_id:** 633826  
**author:** 23f2004496  
**timestamp:** 2025-06-01T06:28:39.844Z

Try this - right click on image and click open in new tab, in the new tab you will see the base64 url of image in chrome tab url bar  
Hope this helps

---

**post_id:** 633829  
**author:** 23f2004496  
**timestamp:** 2025-06-01T07:11:37.330Z

**Realizing the Value of Collaboration**

As I’ve been going through this course, one thing that’s really started to make sense to me is how important collaboration is. None of us can know everything — and that’s okay. We all have different strengths, and when we work together, especially on projects, those strengths really start to shine.

I’ve come to believe that collaboration isn’t just about dividing tasks, it’s about learning from each other, supporting one another, and finding smarter ways to solve problems as a team. It helps us get things done more effectively and on time, and honestly, it makes the whole learning process a lot more enjoyable.

This course is definitely helping me build that mindset, and I’m excited to keep growing through shared learning.  
if somebody feels the same then Reply , Thankyou

---

**post_id:** 633931  
**author:** TheVishal  
**timestamp:** 2025-06-01T13:50:05.649Z

For Question 3, I was able to enable the answer box but the answer is always saying that either it is not valid json format or Error: Model must be gpt-4o-mini, not undefined.

I have tried multiple approaches but the same issue even after using help from Chat GPT. Could any one tell what is the correct answer?? Thanks!

Here is my response for not valid json format error:

```
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "Respond in JSON"
    },
    {
      "role": "user",
      "content": "Generate 10 random addresses in the US"
    }
  ],
  "response_format": "json",
  "tool_choice": "auto",
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "generate_addresses",
        "parameters": {
          "$schema": "http://json-schema.org/draft-07/schema#",
          "type": "object",
          "properties": {
            "addresses": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "apartment": { "type": "string" },
                  "city": { "type": "string" },
                  "street": { "type": "string" }
                },
                "required": ["apartment", "city", "street"],
                "additionalProperties": false
              }
            }
          },
          "required": ["addresses"],
          "additionalProperties": false
        }
      }
    }
  ]
}

```

---

**post_id:** 633960  
**author:** 23f2004496  
**timestamp:** 2025-06-01T17:25:24.903Z

That’s true, that’s how real world works, working in silos doesn’t apply outside controlled environment. Pretty good course for the same purpose

---

**post_id:** 633982  
**author:** Parsh_Kalwania  
**timestamp:** 2025-06-01T18:35:39.003Z

For Questions 8 to 10 of GA3 how and where should we host the URL to receive and handle the responses effectively?

---

**post_id:** 634356  
**author:** HritikRoshan_HRM  
**timestamp:** 2025-06-02T08:00:47.178Z

For qn 8-10, the API is working as expected locally, but I’m now unsure about how to **deploy** it in a way that allows you to send a POST request to a public URL.

---

