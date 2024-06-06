### chap12/ale01/shell.py
'''
Shellsort, translated to Python using pseudocode from: 

https://en.wikipedia.org/wiki/Shellsort
'''

def gen_gaps(n):
    '''Compute and return a shellsort gap sequence'''
    gaps = []
    k = 1
    g = n // (2**k)
    while g != 0:
        gaps.append(g)
        k += 1
        g = n // (2**k)
    return gaps
    

def shell_sort(s):
    '''Sorts the unsorted sequence s in place and
       returns the number of swaps performed.

       Comments below this line are unchanged from
       the wikipedia entry.
    '''
    swaps = 0

    gaps = gen_gaps(len(s))
    #print(f'gap sequence: {gaps}\n')
    
    # Start with the largest gap and work down to a gap of 1
    # similar to insertion sort but instead of 1, gap is being used in each step
    for gap in gaps:
        # Do a gapped insertion sort for every elements in gaps
        # Each loop leaves a[0..gap-1] in gapped order
        for i in range(gap, len(s), 1):
    
            # save s[i] in temp and make a hole at position i
            temp = s[i]
    
            # shift earlier gap-sorted elements up until the correct location
            # for s[i] is found
            j = i
            while j >= gap and s[j - gap] > temp:
                s[j] = s[j - gap]
                j -= gap
                swaps += 1
    
            # put temp (the original a[i]) in its correct location
            s[j] = temp

    return swaps
    

def main():
    # A simple test routine
    s_test = [62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28]
    print(f'unsorted list: {s_test}\n')

    swaps = shell_sort(s_test)
    print(f'sorted list: {s_test}\n')
    print(f'total swaps (SHELL sort) = {swaps}')


if __name__ == '__main__':
    main()
