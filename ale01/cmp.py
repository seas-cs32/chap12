### chap12/ale01/cmp.py
'''
Compare insertion and shell sorts
'''

import random
from insertion import insertion_sort
from shell import shell_sort

def rnd_list(n, max_elem):
    '''Generate a random, unsorted list 'a' of n numbers 
       between 0 and max_elem
    '''
    a = []
    for i in range(n):
        a.append(random.choice(range(max_elem + 1)))
    return a

def aprint(header, a):
    '''Avoids printing huge arrays'''
    n = len(a)

    print(header, end='')
    if n > 10:
        print(f'[{a[0]}, {a[1]}, {a[2]}, {a[3]}, ... \
              {a[n-4]}, {a[n-3]}, {a[n-2]}, {a[n-1]}]')
    else:
        print(a)

def main():
    for n in (10, 100, 1000):
        a = rnd_list(n, 999)
        b = a.copy()

        print(f'\n***{n} elements in array***')
        aprint('  unsorted list: ', a)
        print()

        swaps = insertion_sort(a)
        aprint('  sorted list: ', a)
        print(f'  total swaps (INSERTION sort) = {swaps}')

        print()

        swaps = shell_sort(b)
        aprint('  sorted list: ', a)
        print(f'  total swaps (SHELL sort) = {swaps}')

if __name__ == '__main__':
    main()
