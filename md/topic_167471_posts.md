# project-1-submission-marked-as-fail-despite-having-dockerfile-image

**post_id:** 596311  
**author:** 21f3002647  
**timestamp:** 2025-02-17T10:07:56.783Z

# project-1-submission-marked-as-fail-despite-having-dockerfile-image

Dear TDS Team,

I have verified my submission, and my repository **does include a Dockerfile**, and the **Docker image is accessible on DockerHub**. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.

Looking forward to your confirmation.

Best regards,  
Arnav Mehta  
(21f3002647)

Here's a description of the image:
The image shows a file explorer view with a list of files and directories. The view is in dark mode. There are various files related to a project, including Python scripts and a Dockerfile.
image text:
...
..
LLM\_PROJECT1
\_\_pycache\_\_
Dockerfile
LICENSE
app.py
datagen.py
evaluate.py
requirements.txt
tasksA.py
tasksB.py
  
Here's a description of the image:
The image shows a project named "llm\_project1" by "arnavmehta2025". There is a cube-like logo on the left. The project was updated 2 days ago.
image text: arnavmehta2025/llm\_project1
By arnavmehta2025 • Updated 2 days ago
IMAGE
0 16

---

**post_id:** 596337  
**author:** 21f3002647  
**timestamp:** 2025-02-17T12:30:15.244Z

[@Saransh\_Saini](/u/saransh_saini) sir what should i do?

---

**post_id:** 596404  
**author:** Saransh_Saini  
**timestamp:** 2025-02-17T15:43:39.614Z

[@carlton](/u/carlton) Kindly have a look into this.

---

**post_id:** 596467  
**author:** satviksawhney  
**timestamp:** 2025-02-18T00:48:03.881Z

Good Morning Sir,  
Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.

Looking forward to your reply.

Thank you  
Satvik Sawhney  
23f2003680

---

**post_id:** 596517  
**author:** carlton  
**timestamp:** 2025-02-18T05:00:31.191Z

So the reason for the failure is:

You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)

Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.

Then once you realised your mistake, on **Feb 17th at 9:11 pm IST** i.e *yesteday*, you changed your repo to put the files in the correct locations.

Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]  
image description: The image shows a list of files and folders in a dark theme, likely from a file explorer or code editor.
image text:
..
LLM\_PROJECT1
\_\_pycache\_\_
Dockerfile
LICENSE
app.py
datagen.py
evaluate.py
requirements.txt
tasksA.py
tasksB.py
  
[/quote]

showing that your files are in the correct place.

We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.

Kind regards

---

**post_id:** 596587  
**author:** 21f3002647  
**timestamp:** 2025-02-18T06:35:49.560Z

[@carlton](/u/carlton) sir  
Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.

I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered ![:frowning:](https://emoji.discourse-cdn.com/google/frowning.png?v=12 ":frowning:")

Kind regards,  
Arnav Mehta  
21f3002647

---

**post_id:** 596639  
**author:** satviksawhney  
**timestamp:** 2025-02-18T08:28:16.577Z

Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.

Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.

Sir it is a humble request to please consider it.

Warm Regards,  
Satvik Sawhney  
23f2003680

Here's a description of the image:
The image displays a list of files and folders, likely from a code repository. Each entry shows the name, a brief description or action taken, and the time since the last modification.
image text: Business Reconfigured taskB8 taskB9 taskB10 2 days ago Operations Reconfigured taskA8 taskA9 taskA10 2 days ago app Updated Dockerfile and requirements.txt 2 days ago Dockerfile Rename dockerfile to Dockerfile yesterday LICENSE MIT License 3 days ago README.md Project Structure 3 days ago

---

