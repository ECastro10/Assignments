class Daily_Tasks:
    def __init__(self):
        self.queue = []

    def print_menu(self):
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

    def view(self):
        for x in range(len(self.queue)):
            print(self.queue[x])

    def push(self):
        item = input("Please enter item you wish to add to the queue")
        self.queue.append(item)

    def pop(self):
        item = self.queue.pop(0)
        print("You just popped out", item)
