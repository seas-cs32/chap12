### chap12/ale01/insertion.py

def insertion_sort(s):
    '''Sorts the unsorted sequence s in place and
       returns the number of swaps performed.
    '''
    swaps = 0

    for i in range(1, len(s)):
        #print(f'Considering item at index {i}')
        for j in range(i, 0, -1):
            if s[j - 1] > s[j]:
                # Swap the two items
                s[j - 1], s[j] = s[j], s[j - 1]
                #print(f'Swapped {j-1},{j}: {s}')
                swaps += 1
            else:
                # When swaps are done, the ith element is where it belongs
                break
                
    return swaps


def main():
    # A simple test routine
    s_test = [62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28]
    print(f'unsorted list: {s_test}\n')
    
    swaps = insertion_sort(s_test)
    print(f'sorted list: {s_test}\n')
    print(f'total swaps (INSERTION sort) = {swaps}')


if __name__ == '__main__':
    main()
