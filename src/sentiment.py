import string
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

def wordcloud(string):
    wordcloud = WordCloud(width=1600,height=400).generate(string)
    plt.figure(figsize=(15,10), facecolor="k")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    #plt.savefig('images/wordcloud.png', facecolor='k', bbox_inches='tight')
    plt.show();
    return 

def tokenizer(txt):

    tokens = nlp(txt)
    filters = []
    
    for word in tokens:
        if not word.is_stop:
            lemma = word.lemma_.lower().strip()
            if re.search('^[a-zA-Z]+$',lemma):
                filters.append(lemma)
            
    return " ".join(filters)
#requests.get("http://127.0.0.1:5000/all_lines")
#sql.lines_from_char(name)
def wmap(name):
    dt = requests.get(f"http://127.0.0.1:5000/lines/{name}").json()
    pdf = pd.json_normalize(dt)
    for _,row in pdf.iterrows():
        row.script_l= row.script_l.replace(" ll ", " ").replace(" s "," ").replace(" ve "," ")
        row.script_l= tokenizer(row.script_l)
    lines = ""
    for _,row in pdf.iterrows():
        lines += row.script_l + " "
    return wordcloud(lines)

