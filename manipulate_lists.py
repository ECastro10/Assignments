"""
This problem was posed on hackerrank.com.
****************************************************************************
Initialize your list and read in the value of followed by lines of commands
where each command will be of the types listed above. Iterate through each
command in order and perform the corresponding operation on your list.
****************************************************************************

By "types listed above", it meant list methods such as: sort, insert, pop,
reverse, remove, append, print.

The input looks like this for the first test case.
***************************************************************************
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
***************************************************************************

The output for this test case should look like this.

***************************************************************************
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
***************************************************************************

After looking through the discussion I settled on this solution for a couple
of reasons.
1. I understood the try except paradigm as well as many of these functions.
  a. functions that I understood: split, input, list, getattr, map, format
2. It didn't use the eval function which is apparently evil and should be
avoided.

**************************************************************************
if __name__ == '__main__':
    N = int(input())
    li = list()
    for _ in range(N):
        command = input().split()
        try:
            getattr(li, command[0])(*(map(int, command[1:])))
        except AttributeError:
            exec('{}({})'.format(command[0], 'li'))
*************************************************************************

I didn't quite understand how they all played together though so I
started playing with the script and here are my findings.
"""
# First, I created a separate file called manipulate_lists_inputs.txt
# manipulate_that_list will take that file as its input.
def manipulate_that_list(file_of_inputs):
    """
    INPUT: an int as first input to determine how many commands to run
           consequentially.
    USAGE: To manipulate a list with input feeds
    OUTPUT: N/A
    """
    N = int(input())
    li = list()
    for _ in range(N):
        command = input().split()
        # print("*************")
        # print("li:")
        # print(li)
        # print("***************")
        # print("command:")
        print(command)
        try:
            getattr(li, command[0])(*(map(int, command[1:])))
        except AttributeError:
            exec('{}({})'.format(command[0], 'li'))

def open_file(file_name):
    '''
    input: a txt file
    usage: going to open and read a txt file
    output: returns a list of words in the txt file
    '''
    f = open(file_name)
    for i, line in enumerate(f):
        line = line.rstrip().replace('\\n', '\n')
        print(i, line)
        # counter = 0
        # for line in file:
        #     return line

open_file("manipulate_lists_inputs.txt")
