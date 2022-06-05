# from crypt import methods
from crypt import methods
from flask import render_template, request 
from app import app 
from models.player import Player
from models.game import Game



@app.route('/')
def index():
    return render_template("base.html")


@app.route('/game')
def game():
    return render_template("game.html", title= "Game")

@app.route("/explain")
def explain():
    return render_template("explain.html", title = "Explain")

app.route("/game/result", methods=["POST"])
def result():
    player_1= Player("moath", request.form["choice1"])
    player_2= Player("adam", request.form["choice2"])
    playerss = Game( player_1, player_2)
    result(playerss)
    return render_template("result.html", title= "Result", players= playerss) 
