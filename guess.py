### chap12/guess.py
import random

# Global constants for guessing range
LO = 1
HI = 10000

def guess():
    print('## Welcome to GUESS THE NUMBER! ##')

    secret = random.randint(LO, HI)

    while True:
        # Grab a guess from the player
        while True:
            try:
                guess = int(input('Please input your guess: '))
                break
            except ValueError:
                print('Guesses must be an integer. Try again...')

        if guess < secret:
            print('Too small!')
        elif guess == secret:
            print('Exactly! You win!')
            return
        else:
            print('Too big!')

if __name__ == '__main__':
    guess()
    