import random
'''
user_num = int(input("type in a number > "))
while user_num < 23:
    user_num = int(input("Enter in a bigger number > "))
print("exit")
'''
com_num = random.randint(1,20)
user_num = int(input("Guess what number I am thinking of, you have 10 tries.\n\
Hint: It might be 1 - 20 > "))
tries = 10
while user_num != com_num:
    tries -= 1
    print("You have {} guesses left!".format(tries))
    if tries == 0:
        print("You lose!")
        break
    user_num = int(input("Incorrect! Guess again > "))
print("My number was {}".format(com_num))
