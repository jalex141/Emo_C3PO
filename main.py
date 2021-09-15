from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from numpy import character
from sqlalchemy.util.langhelpers import method_is_overridden
import tools.sql_tools as sql

app = Flask(__name__)



@app.route("/")
def inicio():
    return "Hello there!"



@app.route("/lines/<name>")
def line_char(name):
    print(name)
    lines = sql.lines_from_char(name)
    return lines



@app.route("/newline", methods=["POST"])
def new_line():
    line_n = request.form.get("line_n")
    line = request.form.get("line")
    character = request.form.get("character")
    episode = request.form.get("episode")

    return sql.new_line(line_n,character,line,episode)



app.run(debug=True)