# graded-assignment-6

Please post any questions related to [Graded Assignment 6 - Data Analysis](https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&type=assignment&tab=courses&unitId=23)

Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.

Deadline 2025-03-15T18:30:00Z

---

---

The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?

[@carlton](/u/carlton)

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
I have similar concern  
For Q1, I used the following code:

```
print(f'Pearson correlation for Karnataka between price retention and column')
kk = df[df['State'] == 'Karnataka']
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = kk['price_retention'].corr(kk[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

And got the following output:

```
Pearson correlation for Karnataka between price retention and column
	Mileage (km/l)            : 0.03
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.04

```

Whereas options are below where none of them are correct.  
Here's the image description:
The image shows a series of multiple-choice options. One option is selected.
image text:
'Mileage: 0.95'
'AvgDistance: -0.05'
'Mileage: 0.21'
'Engine Capacity: 0.17'

Whereas for Q2 (Punjab and Yamaha) I used the following code:

```
print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
pb = df[(df['State'] == 'Punjab') & (df['Brand'] == 'Yamaha')]
for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
    pearson_corr = pb['price_retention'].corr(pb[col])
    print(f'\t{col:25} : {pearson_corr:.2f}')

```

and got the following answers:

```
Pearson correlation for Punjab and Yamaha between price retention and column
	Mileage (km/l)            : 0.24
	Avg Daily Distance (km)   : -0.06
	Engine Capacity (cc)      : -0.08

```

The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).  
Here's the image description:
The image shows a series of selection options, each associated with a text label. The third option is selected, indicated by a filled-in circle.
image text:
'Mileage: 0.95'
'AvgDistance: -0.06'
'Mileage: 0.24'
'EngineCapacity: -0.08'

---

[@24f2006061](/u/24f2006061) We are looking into it. We will update based on our analysis. Thanks for letting us know.

Kind regards

---

I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one  
image description: The image displays a question asking to analyze key factors influencing motorcycle resale value in Delhi. It presents four options with different values related to 'Mileage', 'AvgDistance', and 'EngineCapacity'. The third option, 'EngineCapacity: 0.13', is selected.
image text: 1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Delhi. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha. Use Pearson Correlation Coefficient and price retention is (resale price / original price).
O 'Mileage: 0.01'
O 'AvgDistance: 0.00'
'EngineCapacity: 0.13'
O 'EngineCapacity: 0.95'
1 point

---

Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. [@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 & Q2, but both these questions are single-choice questions. Kindly look into it and help us out [@carlton](/u/carlton) !

---

I guess for both Q1 & Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.

---

Any updates on these? I am too facing the same issue.

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

---

In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one  
Here's a brief description of the image:
The image is a question from a test or assignment, asking to analyze the factors influencing motorcycle resale value. It provides multiple-choice answers with correlation coefficients.
image text:
1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in 1 point
Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Yamaha.
Use Pearson Correlation Coefficient and price retention is (resale price / original price).
'AvgDistance: 0.09'
'Mileage: 0.95'
'EngineCapacity: -0.02'
'Mileage: 0.12'

---

Kindly update us regarding the status of Q1 & Q2 [@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
Dear TDS Team,

There are multiple issues in Graded Assignment 6 that require urgent attention:

1. Questions 1 and 2, along with their options, are ambiguous.
2. In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.
3. The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.

The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.

Thank you for your support.

---

Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.

For instance:

> forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.

but is this talking about the average resale value as no input features are specified?

---

Let’s wait for their response.  
I submitted nearby option for Q3 and Q4

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton) [@Saransh\_Saini](/u/saransh_saini)  
Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).  
Thanks

---

Hi @all

Question intends you to select most correlated one.  
Select option which is absolute highest.

---

[@Jivraj](/u/jivraj) - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.  
Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance

---

image description: The image presents a multiple-choice question related to the analysis of factors influencing motorcycle resale value. The question is posed to a strategic consultant. There are four options with given values, and the last option "Mileage: -0.04" is selected.
image text: 1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing 1 point motorcycle resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Honda. Use Pearson Correlation Coefficient and price retention is (resale price / original price).
'AvgDistance: -0.04'
'AvgDistance: 0.95'
'EngineCapacity: -0.04'
'Mileage: -0.04'
  
what to do if 3 options have same value -0.04 and all are correct?

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
My question 7 for GA6 is :  
A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance  
Whose options provided are :  
10418 meters

12287 meters

10965 meters

11149 meters

However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)

I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)  
Kindly look into the question, and let me know about the same (the destination from central command post)

---

Have you succeeded in running the shape file for Q10? It seems to have some error.

[@lakshaygarg654](/u/lakshaygarg654)

---

No,  
I use google to get MTFCC code for given road segment and after that mtfcc pdf to classify that road segment.

---

I downloaded the complete shape file zip from the [census.gov](http://census.gov) site.  
Here is the link: <https://www2.census.gov/geo/tiger/TIGER2024/PRISECROADS/tl_2024_36_prisecroads.zip>

It works fine in QGIS.  
[@lakshaygarg654](/u/lakshaygarg654)

---

they have not provide all the files needed to read that shp file in the question .  
but your link includes them. thanks…

---

I tried to access shapefile from official website 4-5 days ago, but server was under maintenance. I will check again Q10 after quiz 2.  
Thanks for sharing.

---

My question 9 for GA6 is :  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
image description: The image is a screenshot of a Python script. The script is designed to calculate the distances between different communities and a central command post and then sort them based on distance. Key elements include variable declarations for the coordinates of the communities and the central command post, a calculation of distances using a haversine function, sorting of the communities by distance, and printing the optimal evacuation sequence with distances in kilometers. A numbered list with community names and distances is at the bottom.
image text: [26] from haversine import haversine
# Define the coordinates of each community and the central command post
OakParkTown = (27.0096, -72.3822)
EastSpringsSettlement = (27.0769, -72.394)
EastFieldsJunction = (27.0961, -72.4248)
RedPointTown = (26.9874, -72.426)
CentralCommandPostLocation = (27.0552, -72.4893)
# Calculate the distances between each community and the central command post
distances = {
"OakParkTown": haversine(OakParkTown, CentralCommandPostLocation),
"EastSpringsSettlement": haversine(EastSpringsSettlement, CentralCommandPostLoca
"EastFieldsJunction": haversine(EastFieldsJunction, CentralCommandPostLocation),
"RedPointTown": haversine(RedPointTown, CentralCommandPostLocation)
}
# Sort the communities based on their distances to the central command post
optimal\_sequence = sorted(distances, key=distances.get)
# Print the optimal evacuation sequence
for i, community in enumerate(optimal\_sequence, start=1):
print(f"{i}. {community} - Distance: {distances[community]:.2f} km")
1. EastFieldsJunction - Distance: 7.84 km
2. EastSpringsSettlement - Distance: 9.74 km
3. RedPointTown - Distance: 9.81 km
4. OakParkTown - Distance: 11.76 km
  
image description : The image is a question in a quiz format about evacuation strategy. The question provides the coordinates of four communities and asks for the optimal evacuation sequence using the "nearest community first" approach. The text also has Python code to use haversine.
image text: 9) If the four communities are: Oak Park Town: (27.0096,-72.3822); East Springs Settlement: (27.0769,-72.394); East Fields Junction: (27.0961,-72.4248); Red 1 point Point Town: (26.9874,-72.426) & Central Command Post Location: (27.0552,-72.4893)
Using the "nearest community first" evacuation strategy, where the nearest community is determined by the shortest path distance from one community to the other
location points, what would be the optimal sequence for evacuating the communities?
['Start/End', 'East Fields Junction', 'East Springs Settlement', 'Oak Park Town', 'Red Point Town', 'Start/End']
['Start/End', 'Oak Park Town', 'East Fields Junction', 'East Springs Settlement', 'Red Point Town', 'Start/End']
['Start/End', 'East Springs Settlement', 'Oak Park Town', 'East Fields Junction', 'Red Point Town', 'Start/End']
['Start/End', 'Red Point Town', 'Oak Park Town', 'East Springs Settlement', 'East Fields Junction', 'Start/End']
[26] from haversine import haversine
# Define the coordinates of each community and the central command post
OakParkTown (27.0096, -72.3822)

I solved it in colab but options are getting mismatched there…kindly clarify this issue..

---

for the above question the options are None of these are matching and answer is around 11.5 kms  
3848 meters  
6265 meters  
4110 meters  
5106 meters

---

For 7th Question in GA6 I got the answer 14265.93 Meters but the option I have in 7th are  
6069 meters  
7687 meters  
6106 meters  
7035 meters  
[@carlton](/u/carlton) [@Jivraj](/u/jivraj)

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)

for question 4, i have tried `=forecast` and also `=forecast.ets`, both of them are not working. There are two columns for years. One is year of manufacturing, another is year of registration. which one to take.

for question 7, none of the options match. I am selecting the `MOST ACCURATE` among the given options. Hope, it is correct

---

Can anyone help me out on how to approach and solve the 10th question please!?

---

Check the distances of other locations from the central location. One student found **Question 7** of the **GA6 Option Set** based on the distances of other points, which do not match the requirements of Question 7.

---

i have the same issue

---

yes i have the same issue  
and i got the same answer and am give the same options  
[@carlton](/u/carlton) sir what to do?

---

[@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
For 7th Question in GA6 I got the answer 14265.9275 Meters but the option I have in 7th are  
6069 meters  
7687 meters  
6106 meters  
7035 meters

---

Hello Sir,

Can you please check if this is the right answer. As per email received from [@carlton](/u/carlton) sir we should select the absolute maximum value.  
image description: The image displays a multiple-choice question about analyzing factors influencing motorcycle resale value, specifically in Uttar Pradesh. The question poses a scenario where a strategic consultant needs to evaluate the impact of mileage, average daily distance, and engine capacity on price retention for Royal Enfield motorcycles. The options are: 'Mileage: 0.01', 'EngineCapacity: 0.95', 'AvgDistance: -0.13', and 'EngineCapacity: 0.09'. The answer selected is incorrect and the score is 0. The accepted answer is 'EngineCapacity: 0.09'.
image text: 1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle resale value in Uttar Pradesh. Specifically, you 1 point will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price retention (%) for Royal Enfield. Use Pearson Correlation Coefficient and price retention is (resale price / original price).
'Mileage: 0.01'
'EngineCapacity: 0.95'
'AvgDistance: -0.13'
'EngineCapacity: 0.09'
No, the answer is incorrect.
Score: 0
Accepted Answers:
'EngineCapacity: 0.09'

Example : If we get answers as -0.3 and 0.2 then -0.3 is the right answer as it’s absolut value is maximum.

For the first question the correlation matrix is as follows,  
image description: A heat map is presented in a grid format. The x-axis represents 'Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)', and 'Price Retention (%)'. The y-axis corresponds to 'Engine Capacity (cc)' and 'Price Retention (%)'. Each cell in the grid displays a numerical value that ranges from -0.13 to 1.00. The colors of the cells vary based on their values, using a color scale from blue to red.
image text: Mileage (km/l) 0.01 0.04 1.00 0.09 Price Retention (%) 0.01 -0.13 0.09 1.00 Avg Daily Distance (km) - Engine Capacity (cc) Price Retention (%) Engine Capacity (cc) -

So shouldn’t it be -0.13?

---

Thanks for the colour picture.  
If you read the aforementioned email…  
image description: The image is a screenshot of an email. It's from "donot\_reply@study.iitm.ac.in" and the subject is "[TDS Jan 25] GA 6 Clarification." The body of the email clarifies an issue with a test and assures that students who chose the correct answer will have their scores updated.
image text: [TDS Jan 25] GA 6 Clarification Inbox x
donot\_reply@study.iitm.ac.in
to 25t1\_se2002-announce
Dear Learner,
GA6 Question 1 and 2 were not very clear in what was expected.
The answer we are looking for is the Absolute Maximum Correlation Coefficient.
eg. If you find -0.3 and 0.2 as the matching options. The correct answer is -0.3
Do not worry if the portal marks you as being incorrect. We will still push the right scores on the dashboard if you chose the correct option.
Kind regards

Kind regards (in colour ![:wink:](https://emoji.discourse-cdn.com/google/wink.png?v=14 ":wink:"))

---

Thank you sir. i have got questions 1 and 2 both marked as 0.  
Here's a brief description of the image:
The image is a screenshot of an online quiz question. The question presents a scenario where a strategic consultant is tasked with analyzing the factors affecting motorcycle resale value. It lists four options with correlation coefficient values. Below the options, it states "No, the answer is incorrect" with a score of 0 and provides the accepted answer "Mileage: 0.03'".
image text:
1) As a strategic consultant for a premium motorcycle dealership chain, your objective is to analyze the key factors influencing motorcycle 1 point
resale value in Maharashtra. Specifically, you will evaluate the impact of mileage (km/l), average daily distance traveled, and engine capacity on price
retention (%) for KTM. Use Pearson Correlation Coefficient and price retention is (resale price / original price).
'AvgDistance: 0.01'
'Mileage: 0.03'
'EngineCapacity: -0.06'
'Mileage: 0.95'
No, the answer is incorrect.
Score: 0
Accepted Answers:
'Mileage: 0.03'

In my case Please note the above two questions are asked to calculate pearson correlation coefficient for KTM brand and for maharashtra and Karnataka states.  
I have used excel to calculate the pearson correlation coefficient. Below the values I got for each question. Please verify.

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for Karnataka||  
-0.026685695

|pearson correlation coefficient between average distance travelled and Price retention for kTM for karnataka||  
0.003953219

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for karnataka||  
-0.010839295

|pearson correlation coefficient between impact of Mileage and Price retention for kTM brand for maharashta||  
0.029128825

|pearson correlation coefficient between average distance travelled and Price retention for kTM for Maharashtra||  
0.013019585

|pearson correlation coefficient between average Engine capacity and Price retention for kTM for Maharashtra||  
-0.056866212

---

[@Jivraj](/u/jivraj) [@carlton](/u/carlton)  
Dear sirs,  
I have question no 7 got marked as 0. Please check the question below and the haversine distance for the given post comes to around 11.5 kms which is not matccing with any of the options and I have selected the closest answer. please check and let me know.  
image description: The image is a question about finding the most accurate distance using the Haversine package. The question has a description of the scenario and four multiple-choice answers are given. The correct answer is highlighted. The score for an incorrect answer is 0.
image text: 7) A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction: (26.5596,-99.5336); Maple Fields Station: (26.4212,-99.4597); South Glen Crossing: (26.5962,-99.5243); Cedar Creek Retreat: (26.56,-99.4519) & Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance
3848 meters
6265 meters
4110 meters
5106 meters
No, the answer is incorrect.
Score: 0
Accepted Answers:
5106 meters
1 point

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj)  
I did raise the question 2 days before the GA6 Deadline and doing so again after being marked as incorrect

My question 7 was A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) & Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance

10418 meters

12287 meters

10965 meters

11149 meters

Whose right answer turned out 6873, however the answer pushed is 12287 meters, which is nowhere near the closest options (it would’ve been correct if the destination was summit shores village which isn’t the case with this question)

Also, my question 4 was :  
As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Kawasaki - Ninja 300 in Tamil Nadu, using historical data.

134483

94774

150666

199711

Whose correct option (through different methods and algorithms) was approximately closest to 94774 and again answer pushed is 150666 which again turns out to be incorrect

So is the case with questions 1 and 2 (where answers aren’t pushed according to absolute values, but as conveyed earlier, I believe this shall be resolved)

Kindly look into it

Thanks and Regards

---

[@carlton](/u/carlton) [@Jivraj](/u/jivraj) [@Saransh\_Saini](/u/saransh_saini)  
In Q4 , neither which regression model to use is given nor the what random state to use is given. I tried linear regression, random forest regression but it is giving answer which vary each time I compute, also, the option values are quite close.

Here's a description of the image:
The image is a quiz question. It asks the viewer to forecast the 2027 resale value of the Hero-HF Deluxe in Punjab. There are four multiple-choice options, with only one highlighted as the correct answer, but it is marked as incorrect.
image text: 4) As an investment analyst monitoring motorcycle resale values, develop a forecasting model to predict future resale prices by brand and segment, considering seasonality and long-term trends. Specifically, forecast the 2027 resale value of the Hero - HF Deluxe in Punjab, using historical data.
194515
185108
142646
152609
No, the answer is incorrect.
Score: 0

---

@all  
we are looking into problems with question 4, 6 and 10.

---

Hi,

Have the corrections been done on GA6 marks?

---

Yes, corrections have been done in Ga6 marks.

---

Just to confirm, were the answers shown on the portal correct because I’m getting the same score as shown in the portal.

---

