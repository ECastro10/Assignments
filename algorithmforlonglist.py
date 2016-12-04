


def efficientgenlist(lo,hi):
    '''
    INPUT: the hi and lo numbers in main()
    USAGE: this will generate a list of only prime numbers
    OUTPUT: print the list out
    '''
    num_list = []
    num_range = range(lo,hi + 1)
    for i in num_range:
        if primo(i) == True:
            num_list.append(i)
        else:
            continue

    return num_list


def primo(number):
    '''
    INPUT: user number
    USAGE: to determine whether user number is prime or not
    OUTPUT: it will print true or false
    '''
    num_list = [2,3,5,7]
    if number / 1:
        if number in num_list:
            return True
    for i in num_list:
        if number / i != number // i:
            continue
        elif number / i == number // i:
            return False
    return True

def main():

    lo = int(input("Enter in the floor of the range > "))
    hi = int(input("Enter in the ceiling of the range > "))
    print(efficientgenlist(lo,hi))

main()
