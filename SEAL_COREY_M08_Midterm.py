# Program written by COREY SEAL
# March 11th, 2018
# Midterm

def main():  # main module
    first = input('Enter first word of sentence: ')  # get initial input
    sentence = first[0].upper() + first[1:]  # caps the first letter in the string
    loop = 'y'  # initialize loop variable
    while loop.lower() == 'y':  # checks status of loop variable
        new_input = input('Enter next word: ')  # gets next word in string
        sentence += ' ' + new_input  # concatenated it into sentence string
        loop = input('Continue? y/n: ')  # ask for loop variable
    sentence += '.'  # adds period to end
    print(sentence)  # prints sentence
    print('There are ', len(sentence.split()), ' words in the sentence.')  # prints length of str

# call main function
main()
