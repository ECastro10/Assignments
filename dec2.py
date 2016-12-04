def likefizzbuzz():
    '''
    INPUT: the floor and ceiling of the range in numlist
    USAGE: To find the numbers that are divisible by 7 but not by 5
    OUPUT: To print said numbers ^
    '''
    userlowinput = int(input("Enter in the floor of the range > "))
    userhighinput = int(input("Enter in the ceiling of the range > "))

    numlist = list(range(userlowinput,userhighinput + 1))
    for i in numlist:
        if i % 7 == 0 and i % 5 != 0:
            print(i)


def alpha_and_digits(word):
    '''
    INPUT: will take user input string with digits and letters
    USAGE: it will count how many letters and numbers are in the string
    OUTPUT: it will print the number of letters and numbers in the string
    '''
    letter_count = 0
    number_count = 0
    for i in word:
        if i.isalpha():
            letter_count += 1
        elif i.isdigit():
            number_count += 1
    return letter_count, number_count



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
    primo(number)

def main():
    while 3 > 2:
        number = int(input('number please > '))
        print(primo(number))
    '''
    word = input("Enter in words and numbers only, no spaces > ")
    word = alpha_and_digits(word)
    print('Letters = ',word[0])
    print('Numbers = ',word[1])
    '''
main()
