
queue = ['Wake up', 'Take a Shower', 'Morning Coffee']

def print_menu():
    '''
    INPUT: none
    USAGE: will print a menu for user to interact with
    OUTPUT: printing the menu (not return it)
    '''

    print("")
    print("Python Implementation of a Queue")
    print("********************************")
    print("1: View the Queue")
    print("2: Push onto the Queue")
    print("3: Pop out of the Queue")
    print("________________________________")

def view():
    for x in range(len(queue)):
        print(queue[x])

def push():
    item = input("Please enter item you wish to add to the queue")
    queue.append(item)

def pop():
    item = queue.pop(0)
    print("You just popped out", item)

while True:
    print_menu()

    menu_choice = int(input("Enter your menu choice > "))

    if menu_choice == 1:
        view()
    elif menu_choice == 2:
        push()
    elif menu_choice == 3:
        pop()






