# pyq-haversine

Here's a description of the image:
The image is a screenshot of an online quiz or exam interface. On the left side, there's information about the exam: "End Term Quiz", subject "TDS", total marks "40.00", and the exam name. There are also options for "Exam Mode" and "Learning Mode", plus a question menu with numbers. The main content area on the right displays a "Background" section explaining the use of the Haversine formula. It appears to be a discussion between a student and ChatGPT involving calculations of distance between two locations.
image text: Exam : End Term Quiz Subject : TDS Total Marks : 40.00 QP : 2024 Dec22: IIT M FN EXAM QDD2 Exam Mode Learning Mode QUESTION MENU 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 TIMER Backgrouna: As part of the course, you have been introduced with the concept of Haversine formula and its use in distance calculations between two points. The below is a transcript of the conversation between a student in TDS and ChatGPT while they were trying to solve the questions in Graded Assignment 6. Student-ChatGPT Discussion Thread Student: Hi, I have two locations with the following coordinates: - Location A: Latitude = 40.748817, Longitude = -73.985428 Location B: Latitude = 40.761293, Longitude = -73.982294 I need to calculate the distance between them. I heard that the Haversine formula can be used for this. Can you help me understand how to do this step-by-step?
  
image description: The image is a screenshot of a quiz practice website. On the left side, it shows exam details, a question menu with numbers and a timer. In the main window, it displays a question about the Haversine formula for calculating distance, with explanations and a student's response.
image text: Latest Courses/Tools in Data Sci ... Inbox (901) - 23f2003511@ds.st ... Practice TDS questions : 2024 D ... https://quizpractice.space/question-paper/practise/53/3a44150b-f92#question24 ... IIT Website ... Discourse ... AceGrade ... global ... mad2 task ... mad2 eg ... sep mad 2 ... MLP ... java ... sc ... tds ... Exam: End Term Quiz Subject: TDS Total Marks: 40.00 QP : 2024 Dec22: IIT M FN EXAM QDD2 Exam Mode Learning Mode QUESTION MENU 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 TIMER ChatGPT: Sure! The Haversine formula calculates the distance between two points on the surface of a sphere (like the Earth) using their latitudes and longitudes. Here's how you can calculate it step-by-step: 1. Convert degrees to radians: Since latitude and longitude are in degrees, you need to convert them to radians. Use the formula: radians = (π/180) \* degrees 2. Calculate differences in latitude and longitude: Δφ = φ2 - φ1; Δλ = λ2 - λ1 Where φ and λ are respectively latitudes and longitudes of the locations 3. Apply the Haversine formula: d = 2r arcsin(sin² (Δφ/2) + cos(φ1) \* cos(φ2) \* sin² (Δλ/2)) Where r = Radius of earth (6371 km) The term inside the root can be simplified as a = sin² (Δφ/2) + cos(φ1) \* cos(φ2) \* sin² (Δλ/2) These are the basic steps. Do you want to start by converting the coordinates to radians? Student: Yes, I converted the latitude and longitude for Location A and Location B to radians. Here's what I got: φ1 (Latitude of Location A) = 0.7112 radians λ1 (Longitude of Location A) = -1.2915 radians φ2 (Latitude of Location B) = 0.7116 radians λ2 (Longitude of Location B) = -1.2914 radians Does this look correct? ates the distance between two points on the using their latitudes and longitudes. Here's p: e in degrees, you need to convert them to grees ude and longitude: λ1 ly latitudes and longitudes of the locations 2 2) + cos(φ1) \* cos(φ2) \* sin² (Δλ/2) simplified as  
Here's a description of the image:
The image displays a quiz or exam interface, likely for a data science or related subject. Key elements include:
\* \*\*Exam Information:\*\* The exam is titled "End Term Quiz" with "TDS" as the subject and a total of 40 marks. The QP is "2024 Dec22: IIT M FN EXAM QDD2". There are options to switch between Exam Mode and Learning Mode.
\* \*\*Question Menu:\*\* A numerical question menu is visible, highlighting question 19.
\* \*\*Question Content:\*\* The content is about calculating distances using the Haversine formula. The question asks for the closest distance in meters from the "Emergency Supply Center" to "Eastview Medical Center", providing the coordinates. There are four options provided for the answer.
image text: The first step is to calculate the distance (in meters) between the Emergency Supply Center and each of the 4 hospitals using the Haversine formula. Which of the following is the correct distance (in meters, most closest) from the Emergency Supply Center (Latitude: 40.7222, Longitude: -74.0134) to Eastview Medical Center (Latitude: 40.7306, Longitude: -73.9866)? OPTIONS: 1,975 meters 2,346 meters 2,925 meters 3,254 meters  
Here's a description of the image:
The image is a screenshot of an online quiz. The left side shows exam details: "End Term Quiz", subject "TDS", total marks 40, and the QP. There's also a question menu. The right side presents a question asking to identify the closest hospital to an Emergency Supply Center based on given latitude and longitude coordinates. Four hospital options are provided. Below the options, there are buttons labeled "Discussions (0)", and a camera icon. At the bottom, there is a timer.
image text:
Exam :
Subject :
Total Marks :
QP:
End Term Quiz
TDS
40.00
2024 Dec22: IIT M FN EXAM QDD2
Exam Mode
Learning Mode
QUESTION MENU
1 2 3 4 5 6 7 8 9 10 11 12
13 14 15 16 17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32 33 34 35 36
37 38 39 40
TIMER
The response team wants to deliver to the nearest hospital first.
Which of the following hospitals is closest to the Emergency Supply
Center (Latitude: 40.7222, Longitude: -74.0134)?
OPTIONS :
North Hill Hospital (Latitude: 40.7128, Longitude: -74.0060)
Eastview Medical Center (Latitude: 40.7306, Longitude: -73.9866)
Westbrook Hospital (Latitude: 40.6995, Longitude: -74.1745)
Southend Clinic (Latitude: 40.6526, Longitude: -73.9497)
Discussions (0)

This question is in 2024 Dec22: IIT M FN EXAM QDD2  
Can anyone tell how to solve this?

---

