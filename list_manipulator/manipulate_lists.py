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
***Code By wx2020 on hackerrank***
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

NOTE: I wanted to mimic it reading a file of inputs hence why the addition
of a file reader.
"""
# First, I created a separate file called manipulate_lists_inputs.txt
# manipulate_that_list will take that file as its input.
def manipulate_that_list(file_of_inputs):
    """
    INPUT: a txt file that has the list commands, 1 command per line
    USAGE: To read that txt file, uses the first input which will be an
           integer, and carries out that number of commands which should
           all be in that txt file, no more, no less, than that first int.
    OUTPUT: N/A
    """

    # To make it work locally I made some fun modifications.
    # First open that file.
    f = open(file_of_inputs)
    # Then enumerate the number of lines
    for i, line in enumerate(f):
        # replace all lines with a single line break instead of the
        # double line break
        line = line.rstrip().replace('\\n', '\n')
        # if line 0, then N = to that integer and instantiate list object
        if i == 0:
            N = int(line)
            li = list()
        # if line number is not 0
        else:
            # If line number is greater than N, break the loop
            if i > N:
                break;
            # else, variable command = to split of the line in file
            else:
                # These print statements are here to see what the line
                # line looks like before and after the split.
                # We split it in order to map the function.
                # print("Line: ", line)
                command = line.split()
                # print(command)
                try:
                    # Here comes the fun part first we TRY the following:
                    # Get the attribute of this function with the getattr function
                    # 1. getattr(li, command[0]) == getattr(object<list>,
                    #   "string name of function")
                    #   This returns a string describing the method of the
                    #   object and memory location.
                    #   We are basically getting the function to use.
                    #   The next part are the parameters to pass into the function
                    # 2. From my understanding here is what happens.
                    #    map(int, command[1:]) = we change the numbers
                    #    in the command list index 1 and on into integers.
                    #    We do this via the map function.
                    #    The * before map is so that we choose all the items
                    #    in the mapped list as parameters.
                    #    If we didn't use the *, we would get an error stating
                    #    That we are only receiving one argument when we need 2.
                    #    i.e. with * == <function>(mappedints[1], mappedints[2])
                    #    without * == <function>(mappedints, blank)
                    getattr(li, command[0])(*(map(int, command[1:])))
                except AttributeError:
                    # If the try fails, then run this command.
                    # This will is here as a failsafe for functions that dont
                    # have parameters such as print, reverse, order, etc.
                    # So we will execute the command index zero on our list.
                    exec('{}({})'.format(command[0], 'li'))
    # I put in the close statement just in case, I really don't know if it is
    # necessary.
    f.close()

# You can change the file name here if you'd like.
manipulate_that_list("manipulate_lists_inputs.txt")
