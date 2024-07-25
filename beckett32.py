### chap12/beckett32.py

# Set the number of actors in your play, which
# must be less than or equal to 10
num_actors = 3
assert num_actors <= 10

# Setup for pretty printing
on_stage = 0  # encoding of who is on stage
if num_actors == 3:
    # Used to demonstrate the dance with playing cards
    names = 'KQJ'
else:
    names = 'ABCDEFGHIJ'[:num_actors]

def stage_print(dir, n):
    global on_stage
    if dir == 'enter':
        on_stage += 2 ** (n-1)
    else:
        on_stage -= 2 ** (n-1)
    print(f'{bin(on_stage)[2:].zfill(num_actors)} {dir} {names[num_actors - n]}')
    
def beckett(n, enters):
    if n == 0:
        # No characters so no stage directions
        return

    beckett(n - 1, True)
    if enters:
        stage_print('enter', n)
    else:
        stage_print('exit', n)
    beckett(n - 1, False)

def main():
    print(f'{bin(on_stage)[2:].zfill(num_actors)} empty stage')
    beckett(num_actors, True)

if __name__ == '__main__':
    main()