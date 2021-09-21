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

[kaggle link](https://www.kaggle.com/xvivancos/star-wars-movie-scripts)

## Guidelines

I took the datasets from kaggle, converted them to csv  
I created my database in SQL and then I loaded part of my data to my database  
Then prepared mi API with the first couple of endpoints to get some info and be able to upload some lines through my API  
Created a md file to be my API home page  
Prepared some .py files to use some functions according to their functionality  
I made some jupyter notebooks to explain a bit of the proyect development  


****************************


## Repo
- config: I make the connection to my database here 
-D ata folder: In here I store the data csv files and other files
- notebooks: Here I keep some notebooks which describe some of the processes to handle this proyect such as aquirring the data uploading it (...)
- src folder: Contains funtions
- tools: to store function concerning the database and most queries
-wordcloud_masks: contains images to make some wordclouds
- main.py:  I have my API running from here, contains the endpoints
hola 


## Libraries
- [sys](https://docs.python.org/3/library/sys.html)
- [requests](https://pypi.org/project/requests/2.7.0/)
- [pandas](https://pandas.pydata.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)
-[json](https://docs.python.org/3/library/json.html)
- [os](https://docs.python.org/3/library/os.html)
-[re](https://docs.python.org/3/library/re.html)
- flask 
- numpy 
- markdown
- sqlalchemy
- getpass
- spacy
- wordcloud 
- matplotlib.pyplot 
- requests
- pandas
- plotly.express 
- plotly.graph_objects 
- nltk



 
