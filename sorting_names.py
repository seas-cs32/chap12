### chap12/sorting_names.py
from unsort import unsort

# Some famous computer scientists and one who followed in
# his mother's footsteps
names = [
    'Ada Lovelace',
    'Grace Hopper',
    'danah boyd',
    'Moses Liskov',
    'Barbara Liskov',
    'Anita Borg',
    ]

def sort_key(item):
    '''Expects item to be a string of the form "first last"'''
    first, last = item.lower().split()
    return last + first

print(sorted(names, key=sort_key))
