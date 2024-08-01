# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:51:24 2024

Project #1 Rock, Paper, Scissors, Lizard, Spock!
"""
#starting print
def startup():
    print("=-=-=-=-=-=-=-=")
    print("Rock, Paper, Scissors, Lizard, Spock!")
    print("Let's play a round, select one of the following:")
    print("A: Rock")
    print("B: Paper")
    print("C: Scissors")
    print("D: Lizard")
    print("E: Spock")
    print("=-=-=-=-=-=-=-=")


#Convert answer to letter
def paper_sum(player,answers):
    if answers == "rock" or answers == "a":
        answers = "Rock"
    elif answers == "paper" or answers == "b":
        answers = "Paper"
    elif answers == "scissors" or answers == "c":
        answers = "Scissors"
    elif answers == "lizard" or answers == "d":
        answers = "Lizard"
    elif answers == "spock" or answers == "e":
        answers = "Spock"
    else:
        answers = input(player + "Select your answer again as EITHER the letter or word... ")
    return (answers)

#START OF THE PROGRAM
startup()    
player_1 = input("Player 1, what is your pick?").lower()
P1 = "Player 1, "

#Makes sure user input is comparable for both players
results_1 = paper_sum(P1, player_1)
while results_1 != "Rock" or results_1 != "Paper" or results_1 != "Scissors" or results_1 != "Lizard" or results_1 != "Spock":
    if results_1 != "Rock" or results_1 != "Paper" or results_1 != "Scissors" or results_1 != "Lizard" or results_1 != "Spock":
            break
    results_1 = paper_sum(P1, results_1)
player_2 = input("Player 2, what is your pick?").lower()
P2 = "Player 2, "
results_2 = paper_sum(P2, player_2)
while results_2 != "Rock" or results_2 != "Paper" or results_2 != "Scissors" or results_2 != "Lizard" or results_2 != "Spock":
    if results_2 != "Rock" or results_2 != "Paper" or results_2 != "Scissors" or results_2 != "Lizard" or results_2 != "Spock":
            break
    results_2 = paper_sum(P2, results_2)

#Determines who won and prints results
if results_1 == results_2:
    print("It was a tie!!")
elif results_1 == "Rock":
    if results_2 == "Scissors" or results_2 == "Lizard":
        print("Player 1 wins! " + results_1 + " beats " + results_2 + "!")
    elif results_2 == "Paper" or results_2 == "Spock":
        print("Player 2 wins! " + results_2 + " beats " + results_1 + "!")
    else:
        print("Something went wrong... Line 58 if statement")
elif results_1 == "Scissors":
    if results_2 == "Paper" or results_2 == "Lizard":
        print("Player 1 wins! " + results_1 + " beats " + results_2 + "!")
    elif results_2 == "Rock" or results_2 == "Spock":
        print("Player 2 wins! " + results_2 + " beats " + results_1 + "!")
    else:
        print("Something went wrong... Line 64 if statement")
elif results_1 == "Paper":
    if results_2 == "Rock" or results_2 == "Spock":
        print("Player 1 wins! " + results_1 + " beats " + results_2 + "!")
    elif results_2 == "Scissors" or results_2 == "Lizard":
        print("Player 2 wins! " + results_2 + " beats " + results_1 + "!")
    else:
        print("Something went wrong... Line 71 if statement")
elif results_1 == "Lizard":
    if results_2 == "Paper" or results_2 == "Spock":
        print("Player 1 wins! " + results_1 + " beats " + results_2 + "!")
    elif results_2 == "Rock" or results_2 == "Scissors":
        print("Player 2 wins! " + results_2 + " beats " + results_1 + "!")
    else:
        print("Something went wrong... line 78")
elif results_1 == "Spock":
    if results_2 == "Scissors" or results_2 == "Rock":
        print("Player 1 wins! " + results_1 + " beats " + results_2 + "!")
    elif results_2 == "Paper" or results_2 == "Lizard":
        print("Player 2 wins! " + results_2 + " beats " + results_1 + "!")
    else:
        print("Something went wrong... line 85")
else:
    print("Something went wrong with line 55")


