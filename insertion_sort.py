### chap12/insertion_sort.py
import unsort

def insertion_sort(s):
    """Sorts the unsorted sequence s in place"""
    for i in range(1, len(s)):
        # print(f'Considering item at index {i}')
        for j in range(i, 0, -1):
            if s[j-1] > s[j]:
                # Swap the two items
                s[j-1], s[j] = s[j], s[j-1]
                # print(f'Swapped {j-1},{j}: {s}')
            else:
                # When swaps are done, the ith element is where it belongs
                break

def main():
    a, c, w = unsort.unsort()

    print(f'Sorting list A: {a}')
    insertion_sort(a)
    print(f'Sorting list C: {c}')
    insertion_sort(c)
    print(f'Sorting list W: {w}')
    insertion_sort(w)

    print(f'Sorted lists:')
    print(f'A = {a}\nC = {c}\nW = {w}')

if __name__ == '__main__':
    main()
