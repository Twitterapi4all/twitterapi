==========
How to run the project on local system
==========
1. Install Google App Engine from https://developers.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

2. Running the development web server

		dev_appserver.py analyzetweets

		The web server listens on port 8080 by default. You can visit the application at this URL: http://localhost:8080/.
		To on different port run as follow :
		dev_appserver.py --port=9999 analyzetweets
		To stop the web server: with Mac OS X or Unix, press Control-C or with Windows, press Control-Break in your command prompt window.

3. Before running above project analyzetweets, you should have paython 2.7



Twitter API for all organisations
==========

Initially it is a Web based twitter api for all organizations, might be also for selected organization initial, later on we have plan to extend in for various organization or any on can add organization and get the their tweets sentiments....

	This is an open source

	We have plan to manage every thing using open source e.g : google app engine or heroku or any others for access web based api

	repo will be maintained on github


Details of project
==========
As we know that people are expressing their happiness, anger, feeling, sharing and so on at social media special in twitter towards Individuals, Companies, Open Source. Sharing the thing e.g: I have shared a link as a tweet of Data Science while I was signed up for this course.

This type of information created by social media on a daily basis and I have plan to dig into the insights of these information i.e what is the sentiment, what are classes (classification) exist, what is the trends etc…

Example : Let me clear for an organisation : Let’s consider a company Airtel (leading telecom company in India as well as outside India) have the following tweets on twitter for a particular day: (I am just copy pasting the tweets of Airtel)

1. "text":"@Airtel_Presence @VodafoneIN Hey Vodafone plz call me? Need to move out of #airtel"

2. "text":"RT @daldino: Can we protest against prices of data plan in Nigeria?? Please na #MTN #Etisalat #Airtel #Glo”

3. "text":"First a super efficient, fcuked up ivr then a "super irritating #network #airtel #sucks @Airtel_Presence @VodafoneIN”

4. "text":"#Sanora thank you for your interest in Airtel Nigeria TopUp +info: http:\/\/t.co\/NhVvgfK9Fm\n#Airtel #refill #disco http:\/\/t.co\/4nAAgXL3Fh”

5. "text":"@Airtel_Presence @VodafoneIN Hey Vodafone plz call me? Need to move out of #airtel”

6. "text":"@Airtel_Presence as usual no reply apart from the standard 'Plz DM ur blah blah blah! #airtel #badcustomerservice #irritated #angry”

7. "text":"RT @daldino: Let's come nd fight #MTN #Etisalat "#Airtel #Glo ....we need data to be 1k for 1mnth”

and so on …, you can check it by fetching the data from the twitter api by the url = "https://api.twitter.com/1.1/search/tweets.json?q=%23airtel” /

**What we can do with these massive information related to Airtel:**

1. We can classify the tweets as per their sentiment e.g: which tweets goes to “happiness", “anger", “just sharing or neutral” or we can classify in n ways.

2. What is the mood of information now e.g: at the time I have taken this tweets, it clearly visible the in Nigeria mood is to protest against prices hike.

3. Even we can compare the sentiment/mood of two or more similar kind of companies.

4. we could use the data to advise the company to improve quality of care of customer on the basis of their tweets

And so on …..

*What are the scope to do within time limit* :
1. We can do the classification/clustering
2. predict the mood/sentiment

**Technology we could use:**

It would be better if we can use all open source to build a web page for doing above requirements, I suggest using Google App Engine, it provides enough space of storage, Both type of DB i.e NoSQL as well as MySQL, support multiple languages like : JAVA, Python, PHP, GO

If any one what to do in any other platform are always welcome.

Over the next 10 days we can do the initial task I have post which will help towards getting the final goal of this project.
