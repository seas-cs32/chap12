### chap12/sorting_names.py

###
# Solution #1
###

# Some famous computer scientists and one who followed in
# his mother's footsteps
cnames = [
    'Ada Lovelace',
    'Grace Hopper',
    'danah boyd',
    'Moses Liskov',
    'Barbara Liskov',
    'Anita Borg',
]

def sort_key_c(item):
    '''Expects item to be a string of the form "first last"'''
    first, last = item.lower().split()
    return last + first

###
# Solution #2
###

# Cast of the musical Hamilton
hnames = [
    'Lin-Manuel Miranda',
    'Leslie Odom Jr.',
    'Phillipa Soo',
    'Renée Elise Goldsberry',
    'Christopher Jackson',
    'Daveed Diggs',
    'Anthony Ramos',
    'Okieriete Onaodowan',
    'Brian d\'Arcy James',
    'Jasmine Cephas Jones',
]

def sort_key_h(item):
    '''Expects item to be a string of the form "first [middle ...] last"'''
    name = item.lower().split()

    # Grab the last name while avoiding common English name suffixes. This code
    # certainly doesn't handle every conceivable name suffix.
    last = name[-1]
    if last[-1] == '.' or last == 'ii' or last == 'iii' or last == 'iv':
        # Skip suffixes like "Jr." and "Sr." and related with Roman numerals
        last = name[-2]
        # Remove this suffix from the `others` computation
        name.pop()

    others = ''.join(name[:-1])
    return last + others

def main():
    # Solution that handles names with only a first
    # and last name.
    print(sorted(cnames, key=sort_key_c))

    # A more general solution for names with any number of
    # components beyond one (i.e., no Madonna or Prince).
    print(sorted(hnames, key=sort_key_h))

if __name__ == '__main__':
    main()
