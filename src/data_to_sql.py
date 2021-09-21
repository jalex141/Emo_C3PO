import sqlalchemy as alch
import pandas as pd
from getpass import getpass
#from import tools.sql_tools as sql
from config.configuration import engine




def check(what,string):
    """
    recieves a table name and a string
    returns True if 'string' exists in table name and False if not
    """
    if what == "characters":
        query = list(engine.execute(f"SELECT name FROM characters WHERE name = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif what == "script":
        query = list(engine.execute(f"SELECT script_l FROM script WHERE script_l = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif what == "episodes":
        query = list(engine.execute(f"SELECT episode FROM episodes WHERE episode = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    #extra meme..


def insertCharacter(string):
    """
    calls check function and inserts the character if it does not exist
    recieves a string
    inserts a character in the db
    """
    if check("character", string):
        return "character exists"
    else:
        engine.execute(f"INSERT INTO characters (name) VALUES ('{string}');")


def insertEpisode(ep):
    """
    does the same as insertCharcter for Episodes
    """
    if check("episodes", ep):
        return "episode exists"
    else:
        engine.execute(f"INSERT INTO episodes (episode) VALUES ('{ep}');")

def giveId(what,string):
    """
    used only when the string exist in a table 
    recieves a table name and a string
    returns the ID of string in a table
    """
    if what == "characters":
        return list(engine.execute(f"SELECT char_id FROM characters WHERE name ='{string}';"))[0][0]
    elif what == "episodes":
        return list(engine.execute(f"SELECT ep_id FROM episodes WHERE episode ='{string}';"))[0][0]


def insertLine(row):
    """
    checks for existing items in the database tables, gets id's for the main table
    insets the data in the specific tables
    recieves a row of data
    inserts into a database
    """
    if check("script", row["dialogue"]) and check("characters", row["character"]) and  check("episodes", row["episode"]):
        return "line exists"
    else:
        if check("characters", row["character"]):
            char_id = giveId("characters", row["character"])
        else:
            insertCharacter(row["character"])
            char_id = giveId("characters", row["character"])
        
        if check("episodes", row["episode"]):
            ep_id = giveId("episodes", row["episode"])
        else:
            insertEpisode(row["episode"])
            ep_id = giveId("episodes", row["episode"])
        #meme optional insert somehow
        #meme_id = 0
        engine.execute(f"""
        INSERT INTO script (line_n, script_l, characters_char_id, episodes_ep_id) VALUES
        ("{row['line']}", "{row['dialogue']}", "{char_id}", "{ep_id}");
        """)
def insertLines(data):
    """
    applies insertline iterating through a dataset 
    recieves a dataset
    loads said data to sql database
    """
    data = pd.DataFrame(data)
    for _,row in data.iterrows():
        insertLine(row)