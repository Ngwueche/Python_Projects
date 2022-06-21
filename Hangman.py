import random
from words import words
import string



def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what rhe user has guessed

    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #Letters used 
        print('You have', lives, 'lives left and You have used these letters: ', ' '.join(used_letters).upper())

        # what are the current words
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current Word: ', ' '.join(word_list).upper())

        user_letter = input('Guess a letter: ')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('letter is not in the word.')
                
        elif user_letter in used_letters:
            print('You have already used that charater. Please try again.')
        
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print('You died! The word was', word)
    else:
        print('You guess the word', word)

hangman()