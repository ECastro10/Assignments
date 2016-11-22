#alphabet dictionary
alpha_dict = {'a':0, 'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,
'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,
'w':22,'x':23,'y':24,'z':25,}

#alphabet list
letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z']


word_input = input("Please enter in a word > ")
shift_input = int(input("Please enter in a number > "))

#index counter
index = 0
#empty wordlist for new modified word
new_word = []

#for loop that converts 1. initial string of words into indeces. 2.Then it adds
#the shift input to all indeces. 3.Then converts back to letters for new string.
for i in word_input:
    new_index = alpha_dict[i] + shift_input
    if new_index >= 26:
        new_index = new_index % 26
        new_letter = letter_list[new_index]
        new_word.insert(index,new_letter)
    else:
        new_letter = letter_list[new_index]
        new_word.insert(index,new_letter)
    index += 1
print(''.join(new_word))
'''
THIS IS THE INITIAL VERSION OF THE CODE THAT WORKS FOR ONLY 3 LETTERS
letter1 = word_input[0]
index1 = alpha_dict[letter1]
shift_index_formula = index1 + shift_input
if shift_index_formula >= 25:
    shift_index_formula = abs(shift_index_formula - 26)
retrieve_letter1 = letter_list[shift_index_formula]

letter2 = word_input[1]
index2 = alpha_dict[letter2]
shift_index_formula = index2 + shift_input
if shift_index_formula >= 25:
    shift_index_formula = abs(shift_index_formula - 26)
retrieve_letter2 = letter_list[shift_index_formula]

letter3 = word_input[2]
index3 = alpha_dict[letter3]
shift_index_formula = index3 + shift_input
if shift_index_formula >= 25:
    shift_index_formula = shift_index_formula - 26
retrieve_letter3 = letter_list[shift_index_formula]

print(retrieve_letter1 + retrieve_letter2 + retrieve_letter3)
THIS IS THE END OF THE CODE MENTIONED ABOVE
'''
