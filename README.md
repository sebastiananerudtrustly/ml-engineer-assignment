# Predicting the weather

This repo contains some data and instructions for one main task and one bonus task (not necessary, but will grant extra points if you have the time). 
Your solution to this exercise will be used to evaluate your fit for the Machine Learning Engineer position at Trustly. 
We expect the main exercise to take a few hours at most and we don't expect the code to be "perfect", but you should be able to talk about your decisions and what you could improve upon if you had more time.

## Scenario
Your first day as a Machine Learning Engineer at Trustly you are asked to look at a Jira card with the title "Predict tomorrow's weather". There is no description but you manage to get hold of the stakeholder who wrote this card and the following conversation ensues:

__You__: I saw this Jira card about predicting the weather. What is that and why do you need it?

__Stakeholder__: We would like to understand if the weather will be colder or hotter tomorrow than it is today.

__You__: Okay, for what will you use that?

__Stakeholder__: We are launching an initiative where we want to help predict our merchants' demand and since many of our merchants' businesses are dependent on the weather, this is an important piece of the puzzle.

__You__: I can have a look to see what can be done. Has there been any previous work on this matter?

__Stakeholder__: Thanks! Yes, we had a Data Engineer who fetched some weather data and a Data Scientist that did an analysis of how different weather measurements correlated with tomorrow's weather. You should talk to them!

## Exercise 1 (main exercise)

_After some discussion with the Data Scientist you receive the dataset that that was used for the analysis and some tips on what correlations was found in the data.
You now believe that you have what it takes to build a model that will predict tomorrow's weather._

1. Use the data in `data/weather_data.csv` and transform it into a dataset that can be used for building a machine learning classification model that can answer the question "Will the weather be warmer tomorrow than today?". Each combination of a station and a day should constitute an observation in the dataset. 

The Data Scientist recommended the following features that you can start with:
   * Today's temperature as a percent of yesterday's temperature
   * Today's temperature as a percent of the average temperature of the previous 7 days (not including today)
   * Today's temperature as a percent of the min temperature of the previous 7 days (not including today)
   * Today's temperature as a percent of the max temperature of the previous 7 days (not including today)
   * The total amount of rain the last 7 days (including today)

Since the Data Scientist did not have time to look into the matter further, you will also need to come up with some features on your on to enhance the prediction.

2. Train and evaluate a classification model that can be used to predict if tomorrow is going to be colder or warmer. Some things to consider:
   1. How well is the model performing, and how will you explain that to the stakeholder?
   2. Are all features contributing to the prediction, or can some features be removed?
   3. Anything else that you can think of?


__Tip__: _If you haven't already done so, it may be a good idea to create a virtual environment for this project and then install the script with_:
````
$ make install
````

Once you are done, make a zip file of the repo and send it back to us via email or, if you have created your own fork, share it with us. Please do not push any code back to our git repo!

## Bonus exercise

_Unfortunately, the Data Engineer who retrieved the dataset has quit Trustly and you would need to recreate the dataset but with more recent data. 
You do some googling and find that SMHI has an [Open Data API](https://opendata.smhi.se/apidocs/metobs/index.html) that you can use. Sweet!_

There is some boilerplate code available in the file [smhi.py](smhi/smhi.py) in this repo. You should modify it to enable this behaviour so that it can be used to recrate the data in `data/weather_data.csv`:

````
$ python3 -m smhi.smhi --parameters x,y,z
Downloading data for parameter x... Done!
Downloading data for parameter y... Done!
Downloading data for parameter z... Done!
Finished! Data stored in "data/weather_data.csv"
````
