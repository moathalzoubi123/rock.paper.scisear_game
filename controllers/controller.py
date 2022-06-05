# from crypt import methods
from crypt import methods
from flask import render_template, request 
from app import app 
from models.player import Player
from models.game import Game



@app.route('/')
def index():
    return render_template("base.html")


@app.route("/explain")
def explain():
    return render_template("explain.html", title = "Explain")


@app.route("/<choice1>/<choice2>") 
def result():
    player_1_choice = request.form["choice1"]
    player_2_choice = request.form["choice2"]
    player_1 = Player("Moath", player_1_choice)
    player_2 = Player("Adam", player_2_choice)
    playerss = Game(player_1, player_2)
    winner= result(playerss)
    return render_template("result.html", title= "Result", winner=winner, player_1_choice= player_1_choice , player_2_choice=player_2_choice)  
