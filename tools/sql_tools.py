from config.configuration import engine
import pandas as pd

def lines_from_char(character):
    query = f"""
SELECT * FROM lines
WHERE name = '{character}'
"""
    data = pd.read_sql_query(query,engine)

    return data.to_json(orient="records")



def new_line(line_n,character,line,episode):
    engine.execute(f"""
    INSERT INTO lines (line,character,phrase,episode)
    VALUES ({line_n}, '{character}', '{line}', '{episode}');
    """)

    return f"Se ha introducido correctamente: {line_n},{character},{line},{episode}"


