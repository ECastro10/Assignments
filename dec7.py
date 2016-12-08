


def genlist():
    '''
    INPUT: none
    USAGE: creates a list with the numbers 1-100
    OUTPUT: returns said list
    '''
    num_list = list(range(1,101))
    return num_list

def fizzbuzz_steroids(list):
    '''
    INPUT: takes in a list
    USAGE: to print fizz instead of prime #s and buzz if # / 3, and fizzbuzz
    if both conditions are met
    OUTPUT: print out same list except with the replacements mentioned above
    '''




    for i in list:
        if primo(((i ** 2) + 2)) == True and i % 3 == 0:
            print('fizzbuzz')
        if primo(((i ** 2) + 2)) == True:
            print('Fizz')
        elif i % 3 == 0:
            print('Buzz')
        else:
            print(i)




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

    fizzbuzz_steroids(genlist())


main()
