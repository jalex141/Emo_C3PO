import flask
from flask import Flask, request
from flask import json
from flask.json import jsonify, load
import markdown
import markdown.extensions.fenced_code
import tools.sql_tools as sql
import src.data_to_sql as up
import src.sentiment as s

app = Flask(__name__)
#initialize API

@app.route("/")
def inicio():
    """API home page loads a .md"""
    readme_file = open("./data/cover.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template_string


@app.route("/lines/<name>")
def line_char(name):
    """tase a name, returns that characters lines"""
    print(name)
    name = name.upper()
    lines = sql.lines_from_char(name)
    return lines

@app.route("/lines/<name>/<episode>")
def line_char_ep(name,episode):
    """takes a name and an episode, returns the lines from that character and episode"""
    print(name)
    name = name.upper()
    episode = episode.upper()
    lines = sql.lines_from_char_ep(name,episode)
    return lines

@app.route("/wmap/<name>")
def word_map(name):
    """takes a name, returns a wordcloud from that character lines"""
    print(name)
    name = name.upper()
    s.wmap(name)

    filename = "./wordcloud_masks/wordcloud.png"
    return flask.send_file(filename, mimetype="image/png")

@app.route("/all_lines")
def lines_():
    """takes no arguments, returns the full database"""
    lines = sql.lines_()
    return lines

@app.route("/sent")
def senti():
    return s.dark_light()

    #filename = "./wordcloud_masks/sentiment.png"
    #return flask.send_file(filename, mimetype="image/png")


@app.route("/newline", methods=["POST"])
def new_line():
    script_l = request.form.get("script_l")
    character = request.form.get("character")
    episode = request.form.get("episode")

    return sql.new_line(script_l, character, episode)

@app.route("/newlines", methods=["POST"])
def new_lines_():
    req_json = request.json
    data_ = json.loads(req_json)
    return up.insertLines(data_)


app.run(debug=True)
# run the API