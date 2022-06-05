from models.player import Player

class Game():
 def __init__(self, player_1, player_2):
     self.player_1 = player_1
     self.player_2 = player_2 

player_1 = Player("Moath")
player_2 = Player("adam")
players = [player_1, player_2]     



def result():
    if player_1.choice == "Rock" and player_2.choice== "Paper":
        return "palyer2 won"
    if player_1.choice == "Rock" and player_2.choice== "Scissors":
        return "palyer1 won"
    if player_1.choice == "Rock" and player_2.choice== "Rock":
        return "None"


    if player_1.choice == "Paper" and player_2.choice== "Paper":
        return "None"
    if player_1.choice == "Paper" and player_2.choice== "Scissors":
        return "palyer2 won"
    if player_1.choice == "Paper" and player_2.choice== "Rock":
        return "Player1 won"


    if player_1.choice == "Scissors" and player_2.choice== "Paper":
        return "palyer1 won"
    if player_1.choice == "Scissors" and player_2.choice== "Scissors":
        return "None"
    if player_1.choice == "Scissors" and player_2.choice== "Rock":
        return "player2 won"