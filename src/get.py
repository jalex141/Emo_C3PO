import pandas as pd
import seaborn as sns
import numpy as np
import re
import os
import sys
sys.path.append('../')

def download_dataset():
    '''Downloads a dataset from kaggle and only keeps the csv in your data file. Beware of your own data structure:
    this creates a data directory and also moves all the .csv files next to your jupyter notebooks to it.
    Takes: url from kaggle
    Returns: a folder with the downloaded and unzipped csv
    '''
    
    #Gets the name of the dataset.zip
    url = input("Introduce la url: ")
    
    #Gets the name ofA the dataset.zip
    endopint = url.split("/")[-1]
    #endopint was already like this 
    user = url.split("/")[-2]
    
    #Download, decompress and leaves only the csv
    download = f"kaggle datasets download -d {user}/{endopint}"
    decompress = f"unzip *.zip"
    delete = f"rm -rf *.zip"
    make_directory = "mkdir data"
    lista = "ls >> archivos.txt"
    
    for i in [download, decompress, delete, make_directory, lista]:
        os.system(i)
    
    #Move the csv to uour data folder
    for file in list("./archivos.txt"):
        read_file = pd.read_csv ('../SW_EpisodeIV.txt', sep= " ")
        read_file.to_csv ('./data/SW_EpisodeVI.csv', index=None)
        os.system(f"mv *.csv ./data/{file}")
        f"{file}>> archivos_csv.txt"
    return None

download_dataset()

