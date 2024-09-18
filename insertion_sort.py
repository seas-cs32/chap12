### chap12/insertion_sort.py
import unsort

# Terminal colors
GRN = '\033[32m'   # green
BLU = '\033[34m'   # blue
BLK = '\033[0m'    # back to black

def insertion_sort(s):
    """Sorts the unsorted sequence s in place"""
    for i in range(1, len(s)):
        # observe_start(s, i)

        for j in range(i, 0, -1):
            if s[j-1] > s[j]:
                # Swap the two items
                s[j-1], s[j] = s[j], s[j-1]
                # observe_swap(s, i, j)
            else:
                # When swaps are done, the ith element is where it belongs
                break

        # observe_done(s, i)

def observe_start(s, i):
    print(f'\nConsidering item with value {BLU}{s[i]}{BLK} at index {i}')
    print(f'Start:         [', end='')
    print(f'{GRN}{", ".join([str(item) for item in s[:i]])}', end='')       # sorted items
    print(f', {BLK}{", ".join([str(item) for item in s[i:]])}', end='')
    print(f']')

def observe_swap(s, i, j):
    print(f'Swapped {j-1:2},{j:2}: [', end='')
    if j > 1:
        print(f'{", ".join([str(item) for item in s[:j-1]])}, ', end='')
    print(f'{BLU}{", ".join([str(item) for item in s[j-1:j+1]])}', end='')    # compared pair
    if j + 1 != len(s):
        print(f', {BLK}{", ".join([str(item) for item in s[j+1:]])}', end='')
    print(f'{BLK}]')

def observe_done(s, i):
    print(f'Done:          [', end='')
    print(f'{GRN}{", ".join([str(item) for item in s[:i+1]])}', end='')       # sorted items
    if i + 1 != len(s):
        print(f', {BLK}{", ".join([str(item) for item in s[i+1:]])}', end='')
    print(f'{BLK}]')

def main():
    a, c, w = unsort.unsort()

    print(f'\nSorting list A: {a}')
    insertion_sort(a)
    print(f'\nSorting list C: {c}')
    insertion_sort(c)
    print(f'\nSorting list W: {w}')
    insertion_sort(w)

    print(f'\nSorted lists:')
    print(f'A = {a}\nC = {c}\nW = {w}')

if __name__ == '__main__':
    main()
