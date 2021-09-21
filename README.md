# Emo_C3PO

![portada](https://p4.wallpaperbetter.com/wallpaper/501/761/145/star-wars-episode-iii-the-revenge-of-the-sith-obi-wan-kenobi-darth-vader-jedi-hd-wallpaper-preview.jpg)

## Objective

We were asked to gather messages or quotes data from chats, a dataset or the web to be stored in our database and accessed from an API we would also have to study the emotional value of the data

## Project Goals
- Design the **structure** of our own database to fit the info we want to store.
- Write an API using flask to receive chat messages and **store** them in a database (mysql).
- **Read** and serve data from the database using different endpoints.
- Extract the **emotional value** of lines per character/episode and make it _queryable_ through an endpoit.

## Data
I am working with a dataset taken from kaggle consisting of three txt files with the entire movie scripts for star wars episodes IV, V and VI. I then converted those txt to csv and worked my way from there 

[link](https://www.kaggle.com/xvivancos/star-wars-movie-scripts)

## Guidelines

I took the datasets from kaggle, converted them to csv
I created my database in SQL and then I loaded part of my data to my database
Then prepared mi API with the first couple of endpoints to get some info and be able to upload some lines through my API
Created a md file to be my API home page

****************************

I scrapped some data from the Brazilian federation about body structures for weightlifters
and tried to asimilate some of that data into my dataframe

## Repo
-config: I make the connection to my database here 
-Data folder: In here I store the data csv files and other files
-notebooks: Here I keep some notebooks which describe some of the processes to handle this proyect such as aquirring the data uploading it (...)
-src folder: Contains funtions
-tools: to store function concerning the database and most queries
-wordcloud_masks: contains images to make some wordclouds
-main.py:  I have my API running from here, contains the endpoints

## Libraries

[sys](https://docs.python.org/3/library/sys.html)
[requests](https://pypi.org/project/requests/2.7.0/)
[pandas](https://pandas.pydata.org/)
[dotenv](https://pypi.org/project/python-dotenv/)
[json](https://docs.python.org/3/library/json.html)
[os](https://docs.python.org/3/library/os.html)

[re](https://docs.python.org/3/library/re.html)
from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from numpy import character
import tools.sql_tools as sql
import src.data_to_sql as up
import markdown
import markdown.extensions.fenced_code
import sqlalchemy as alch
from getpass import getpass
 
