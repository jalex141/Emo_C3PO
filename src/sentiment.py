import spacy
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#%matplotlib inline
import re
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import sys
nlp = spacy.load("en_core_web_sm")
import tools.sql_tools as sql
import json
import kaleido

def drop(df):
    """asks for user authorization to drop columns with scarse data"""
    percent_ = round(df.name.value_counts() * 100 / len(df), 2)
    #t=int(input("Threshold [%] for data "))
    t=2
    for c,n in zip(percent_.index,percent_.values):
        if n<t:
            df.drop(df[df.name == c].index, inplace=True)
    return df

def wordcloud(string):
    """takes a string
    saves a .png of a wordcloud of the string"""
    wordcloud = WordCloud(width=1600,height=400).generate(string)
    plt.figure(figsize=(15,10), facecolor="k")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig('./wordcloud_masks/wordcloud.png', facecolor='k', bbox_inches='tight')
    
    

def tokenizer(txt):

    tokens = nlp(txt)
    filters = []
    
    for word in tokens:
        if not word.is_stop:
            lemma = word.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filters.append(lemma)
            
    return " ".join(filters)

def sentiment(line):
    sia = SentimentIntensityAnalyzer()
    polaridad = sia.polarity_scores(line)
    pol = polaridad["compound"]
    return pol

# dt = requests.get(f"http://127.0.0.1:5000/lines/{name}").json()
# pdf = pd.json_normalize(dt)
def wmap(name):
    lines_json = sql.lines_from_char(name)
    lines_list = json.loads(lines_json)
    pdf = pd.DataFrame(lines_list)

    for _,row in pdf.iterrows():
        row.script_l= row.script_l.replace(" ll ", " ").replace(" s "," ").replace(" ve "," ").replace(" m "," ")
        row.script_l= tokenizer(row.script_l)
    lines = ""
    for _,row in pdf.iterrows():
        lines += row.script_l + " "
    wordcloud(lines)

def dark_light():
    
    #dt = requests.get("http://127.0.0.1:5000/all_lines").json()
    #pdf = pd.json_normalize(dt)
    lines_json = sql.lines_()
    lines_list = json.loads(lines_json)
    pdf = pd.DataFrame(lines_list)
    
    #pdf = pd.read_csv('./data/tokens.csv')
    for _,row in pdf.iterrows():
        row.script_l= row.script_l.replace(" ll ", " ").replace(" s "," ").replace(" ve "," ")
        row.script_l= tokenizer(row.script_l)
    #pdf.to_csv('./data/tokens.csv', index = False)
    
    
    pdf["polarity"] = pdf.script_l.apply(sentiment)
    sent = pdf.groupby(["name"])["polarity"].mean().sort_values().to_frame().reset_index()
    #fig =px.bar(sent, x="name", y="polarity")
    #fig.write_image("./wordcloud_masks/sentiment.png'")

    #plt.savefig('./wordcloud_masks/sentiment.png', facecolor='k', bbox_inches='tight')
    return sent.to_json(orient="records")    
