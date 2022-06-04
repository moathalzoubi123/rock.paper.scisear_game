from crypt import methods
from flask import render_template 
from app import app 



@app.route('/')
def index():
    return render_template("base.html")


@app.route('/game')
def game():
    return render_template("game.html", title= "game")

@app.route("/explain")
def explain():
    return render_template("explain.html", title = "explain")

app.route("/game/result", methods="[POST]")
def result():
    return render_template("result.html", title="result")
