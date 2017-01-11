def main():
    '''
    INPUT: none
    USAGE: runs the grading order of functions to achieve letter grade
    OUTPUT: letter grade
    '''

    file = open("grades.txt", "r")
    file = list(file)
    file = file[0].split(',')
    mapped_file = map(int, file)


    average = average_grade(mapped_file, file)
    letter = convert_to_letter(average)
    print(letter)


def average_grade(grade_list, unmapped_list):
    '''
    INPUT: takes in a list of numbers
    USAGE: to find the total sum of that list and divide by the length of that list
    OUTPUT: returns the average
    '''


    average = (sum(grade_list)) / len(unmapped_list)

    return average

def convert_to_letter(number):
    '''
    INPUT: takes in a number
    USAGE: to convert that number to a grade
    OUTPUT: a grade letter
    '''

    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"


main()