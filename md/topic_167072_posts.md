# sudo-permission-needed-to-create-data-folder-in-root

**post_id:** 594729  
**author:** vikramjncasr  
**timestamp:** 2025-02-14T03:57:16.864Z

# sudo-permission-needed-to-create-data-folder-in-root

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) sir please help

When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?  
needs sudo permission all the time…  
image description: The image is a terminal window displaying the output of the "ls" command in a Linux environment. The command lists the files and directories present in the root directory ("/") of the file system.
image text: vikramjncasr@ANJANEYA:/mnt/c/IIT\_Madras/TDS\_Project\_1$ sudo / /data
vikramjncasr@ANJANEYA:/mnt/c/IIT\_Madras/TDS\_Project\_1$ ls /
bin boot etc init lib.usr-is-merged lost+found mnt proc run sbin.usr-is-merged srv tmp var
bin.usr-is-merged dev home lib lib64 media opt root sbin snap sys usr
vikramjncasr@ANJANEYA:/mnt/c/IIT\_Madras/TDS\_Project\_1$

---

**post_id:** 594766  
**author:** carlton  
**timestamp:** 2025-02-14T04:53:36.939Z

Hi Vikram,

This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py  
Inside the docker container, permission for the data folder is set by the Dockerfile  
which then allows your application to access the root folder inside your docker image and create the /data folder.

So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):

1. You create your application server that serves 2 endpoints on localhost:8000
2. You create a docker image that runs this application server.
3. You run the docker image using podman as described in the project page.
4. For mimicking the testing conditions. You need two files:  
   evaluate.py and datagen.py to be in the same folder where you are running these two scripts.
5. Run evalute.py using uv.

If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.

Hope that gives clarity.

Kind regards

---

