from config.configuration import engine
import pandas as pd
import src.data_to_sql as up

def lines_from_char(character):
    """queries the database for a specific character
    takes a name
    returns a json with the lines"""
    query = f"""
SELECT script_l FROM script
JOIN characters 
ON characters.char_id = script.characters_char_id
WHERE name = '{character}'
"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")


def lines_from_char_ep(character,ep):
    """queries the database for a specific character and episode
    takes a name and episode
    returns a json with the filtered lines"""
    query = f"""
SELECT script_l FROM script
JOIN characters 
ON characters.char_id = script.characters_char_id
INNER JOIN episodes
ON episodes.ep_id = script.episodes_ep_id
WHERE name = '{character}' and episode = '{ep}'
"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")


def lines_():
    """queries the database for all lines
    takes no arguments
    returns a json with all the lines"""
    query = f"""
SELECT script_l, `name`, episode
FROM script
INNER JOIN characters
ON characters.char_id = script.characters_char_id
INNER JOIN episodes
ON episodes.ep_id = script.episodes_ep_id
"""
    data = pd.read_sql_query(query, engine)
    return data.to_json(orient="records")


def new_line(script_l, character, episode):
    """queries the database to insert a line from a character
    takes a name , character and episode
    returns a confirmation message"""
    if up.check("characters", character):
        char_id = up.giveId("characters", character)
    else:
        up.insertCharacter(character)
        char_id = up.giveId("characters", character)
    if up.check("episodes", episode):
        ep_id = up.giveId("episodes", episode)
    else:
        up.insertEpisode(episode)
        ep_id = up.giveId("episodes", episode)
    if up.check("script", script_l) and up.check("characters", character) and  up.check("episodes", episode):
        return "line exists"
    else:
        engine.execute(f"""
        INSERT INTO script (script_l, characters_char_id, episodes_ep_id) VALUES
        ("{script_l}", "{char_id}", "{ep_id}");
        """)
    return f"successfully loaded: {character},{script_l},{episode}"

