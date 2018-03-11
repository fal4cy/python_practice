# Program written by COREY SEAL
# March 11th, 2018
# Midterm

def main():
    first = input('Enter first word of sentence: ')
    sentence = first[0].upper() + first[1:]
    loop = 'y'
    while loop.lower() == 'y':
        new_input = input('Enter next word: ')
        sentence += ' ' + new_input
        loop = input('Continue? y/n: ')
    sentence += '.'
    print(sentence)
    print('There are ', len(sentence.split()), ' words in the sentence.')

# call main
main()