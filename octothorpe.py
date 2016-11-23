user_input = input("please enter in any word > ")
new_word = []
number_of_octothorpes = "#" * (len(user_input) - 4)
if len(user_input) <= 4:
    print("#" * len(user_input))
elif len(user_input) >= 5:
    print(number_of_octothorpes + (user_input[(len(user_input)-4):]))
