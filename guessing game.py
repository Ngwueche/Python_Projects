# Humans guessing
import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess= int(input(f"Guess between a number between 1 and {x}: "))
        if guess < random_number:
            print('Sorry, your guess is too low. ')
        elif guess > random_number:
            print('Sorry, your guess is too high. ')
    print(f"You guessed {random_number} just right! You're a genius")


# Computer guessing
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high or too low or correct? ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1 
    print(f'Computer is a genius, Your number is {guess}!')

computer_guess(1000)
