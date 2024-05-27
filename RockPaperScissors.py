# program to automate paying rock paper scissors

import random

#Add a seed to allow for more of a random experience
seed = 1000
random.seed(int(seed))

#ASSIGNING ROCK PAPER AND SCISSORS AS A VARIABLE
ROCK = 0
PAPER = 1
SCISSORS = 2

#CREATE A RANDOM NUMBER GENERATOR
min = 0
max = 2

#create a dictionary to hold user and computer scores
scores = {'computer': 0, 'user': 0}

#read the player's name from input
player_name = input("Player, please enter your name: ")
#capture the number of rounds that the user wants to play
game_rounds = int(input("Please enter the number of games you would like to play: "))
#output the player's name and the nubmer of rounds to play
print(f"Welcome to the game {player_name}! You have selected to run {game_rounds} rounds!")

#Create a loop that runs the number of times stored in the variable game_rounds
counter = 0

while counter <  game_rounds:
    print(f"This is round # {counter +1}")
    computer_selection = random.randint(min, max)
    user_selection = int(input("Please enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))

#output of user selection
    if user_selection == ROCK:
        print(f"{player_name} selected Rock")
    elif user_selection == SCISSORS:
        print(f"{player_name} selected Scissors")
    elif user_selection == PAPER:
        print(f"{player_name} selected Paper")

#output of computer selection
    if computer_selection == ROCK:
        print("Computer selected Rock")
    elif computer_selection == SCISSORS:
        print("Computer selected Scissors")
    elif computer_selection == PAPER:
        print("Computer selected Paper")

#compare selections to see if the user won
    if  user_selection == ROCK and computer_selection == SCISSORS:
        print(f"{player_name} wins!")
        #update the score for the user
        scores["user"] = scores["user"] + 1
    elif user_selection == PAPER and computer_selection == ROCK:
        print(f"{player_name} wins!")
        scores["user"] = scores["user"] + 1
    elif user_selection == SCISSORS and computer_selection == PAPER:
        print(f"{player_name} wins!")
        scores["user"] = scores["user"] + 1

#compare selections to see if computer won
    if  computer_selection == ROCK and user_selection == SCISSORS:
        print("The computer wins!")
        #update the score for the computer
        scores["computer"] = scores["computer"] + 1
    elif computer_selection == PAPER and user_selection == ROCK:
        print("The computer wins!")
        scores["computer"] = scores["computer"] + 1
    elif computer_selection == SCISSORS and user_selection == PAPER:
        print("The computer wins!")
        scores["computer"] = scores["computer"] + 1

#increment the counter variable
    counter = counter + 1


#display the number of rounds won for the player and computer
print(f"The user has won {scores['user']} rounds")
print(f"The computer has won {scores ['computer']} rounds")

if scores['user'] > scores["computer"]:
       print(f"{player_name} won the game!")
elif scores["computer"] > scores["user"]:
       print("The computer has won!")
else:
       print("The scores are tied! There is no clear winner!")
