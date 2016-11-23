#import random and computer signs list
import random

signchoices = ["rock", "paper", "scissors"]
player1_score = 0
comp_score = 0
game = 0



while game < 3:

    hand1 = input("Enter rock, paper, or scissors Player1 > ").lower()
    compSign = random.choice(signchoices)
    print("Computer chooses " + compSign)
    if hand1 == "":
        print("Nothing was entered for Player 1, invalid game")

    elif hand1 == compSign:
        print("Tie!")

    elif hand1 == "rock" and compSign == "paper":
        print("Computer wins!")
        comp_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))

    elif hand1 == "paper" and compSign == "rock":
        print("Player1 wins!")
        player1_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))

    elif hand1 == "paper" and compSign == "scissors":
        print("Computer wins!")
        comp_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))
    elif hand1 == "scissors" and compSign == "paper":
        print("Player1 wins!")
        player1_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))

    elif hand1 == "scissors" and compSign == "rock":
        comp_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))
        print("Computer wins!")

    elif hand1 == "rock" and compSign == "scissors":
        print("Player1 wins!")
        player1_score += 1
        game += 1
        print("You have won {} games".format(player1_score))
        print("The computer has won {} games".format(comp_score))
if comp_score > player1_score:
    print("Computer Wins!!!")
else:
    print("You win, it was a fluke")
