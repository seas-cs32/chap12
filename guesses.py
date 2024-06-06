### chap12/guesses.py

# Global constants for guessing range
LO = 1
HI = 10000

def guesses():
    print("## Welcome to I'LL GUESS YOUR NUMBER ##")

    print(f"Please think of a number between {LO} and {HI}, but don't tell me.")
    input("Hit return when you're ready ...")

    # Possible user answers
    answers = ['too low', 'too high', 'yes']

    # Initializations
    lo = LO
    hi = HI

    # Use binary search as the algorithm we play by
    while True:
        # Generate new guess at mid-point
        mid = lo + (hi - lo) // 2

        # Grab answer from the player
        while True:
            ans = input(f'Is it {mid}? ').lower()
            if ans in answers:
                break
            print('Please answer "too low", "too high", or "yes".')

        # Update range of possible guesses
        if ans == 'yes':
            print('\U0001f60e')
            return
        if ans == 'too low':
            lo = mid + 1
        else:
            hi = mid - 1

if __name__ == '__main__':
    guesses()
    