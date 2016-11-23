#import random and computer signs list
import random

signchoices = ["rock", "paper", "scissors"]

#formula for choosing computer sign
compSign = signchoices[random.randint(0,2)]

#rock paper scissors game

#player 1 and 2 inputs
hand1 = input("Enter rock, paper, or scissors Player1 > ").lower()

print("Computer chooses " + compSign)

#if nothing is entered by both players
if hand1 == "" and compSign == "":
    print("Neither player entered a sign, invalid game")

#if nothing is entered
elif hand1 == "":
    print("Nothing was entered for Player 1, invalid game")

elif  compSign == "":
    print("Nothing was entered for Computer, invalid game")

#tie game condition
elif hand1 == compSign:
    print("Tie!")

#rock and paper combination results
elif hand1 == "rock" and compSign == "paper":
    print("Computer wins!")

elif hand1 == "paper" and compSign == "rock":
    print("Player1 wins!")

#scissors and paper combination results
elif hand1 == "paper" and compSign == "scissors":
    print("Computer wins!")

elif hand1 == "scissors" and compSign == "paper":
    print("Player1 wins!")

#rock and scissors combination results
elif hand1 == "scissors" and compSign == "rock":
    print("Computer wins!")

elif hand1 == "rock" and compSign == "scissors":
    print("Player1 wins!")
