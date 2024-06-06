### chap12/merge_sort.py
from unsort import unsort
from merge import merge

def merge_sort(s):
    """Recursive merge sort: returns a sorted list"""

    # Catch trivial cases (i.e., lists that are sorted by definition)
    if len(s) < 2:
        return s

    # Find index at truncated midpoint of list
    mid = len(s) // 2

    # Return merge of the two sorted halves
    return merge(merge_sort(s[0:mid]), merge_sort(s[mid:]))

def main():
    # Test merge_sort using our unsorted lists
    a, c, w = unsort()
    aa = merge_sort(a)
    cc = merge_sort(c)
    ww = merge_sort(w)
    print(f'a = {aa}\nc = {cc}\nw = {ww}')

if __name__ == '__main__':
    main()
