import sqlalchemy as alch
from getpass import getpass
#from import tools.sql_tools as sql

password = getpass("Introduce tu pass de sql: ")
dbName="starwars"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)
print(f"me conecté a {dbName}")


def check(que,string):
    """
    Función parametrizada que comprueba en cada tabla si existe el user, artista o canción.
    Devuelve True si existe y False si no
    """
    if que == "characters":
        query = list(engine.execute(f"SELECT name FROM characters WHERE name = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
        
    elif que == "script":
        query = list(engine.execute(f"SELECT script_l FROM script WHERE script_l = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False
    
    elif que == "episodes":
        query = list(engine.execute(f"SELECT episode FROM episodes WHERE episode = '{string}'"))
        if len(query) > 0:
            return True
        else:
            return False


def insertCharacter(string):
    """
    Llama a la función check para comprobar si existe el ironhacker
    Inserta ironhacker si no existe
    """
    if check("character", string):
        return "character exists"
    else:
        engine.execute(f"INSERT INTO characters (name) VALUES ('{string}');")


def insertEpisode(ep):
    """
    Llama a la función check para comprobar si existe el artista
    Inserta artista si no existe
    """
    if check("episodes", ep):
        return "episode exists"
    else:
        engine.execute(f"INSERT INTO episodes (episode) VALUES ('{ep}');")

def giveId(que,string):
    """
    Devuelve el ID de lo que le pidamos sabiendo que ese elemento EXISTE
    """
    if que == "characters":
        return list(engine.execute(f"SELECT char_id FROM characters WHERE name ='{string}';"))[0][0]
    elif que == "episodes":
        return list(engine.execute(f"SELECT ep_id FROM episodes WHERE episode ='{string}';"))[0][0]


def insertLine(row):
    """
    La función final 
    """
    if check("script", row["dialogue"]):
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
        
        meme_id = 0
        engine.execute(f"""
        INSERT INTO script (line_n, script_l, characters_char_id, episodes_ep_id) VALUES
        ("{row['line']}", "{row['dialogue']}", "{char_id}", "{ep_id}");
        """)

def insertLines(data):
    for index,row in data.iterrows():
        insertLine(row)