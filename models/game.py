from models.player import Player

class Game():
 def __init__(self, player_1, player_2):
     self.player_1 = player_1
     self.player_2 = player_2 

player_1 = Player("Moath")
player_2 = Player("Adam")
players = [player_1, player_2]     



def result(player_1, player_2):
    winner = player_2.name

    if player_1.choice == player_2.choice:
        winner = "None"
    elif player_1.choice == "rock" and player_2.choice == "scissors":
        winner = player_1.name
    elif player_1.choice == "scissors" and player_2.choice== "paper":
        winner = player_1.name
    elif player_1.choice == "paper" and player_2.choice == "rock":
        winner = player_1.name
    return winner       