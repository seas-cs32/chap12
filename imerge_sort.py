### chap12/imerge_sort.py
from unsort import unsort
from merge import merge

def merge_sort(s):
    """Iterative merge sort: s sorted in place"""

    # Catch trivial cases (i.e., lists that are guaranteed to be sorted)
    if len(s) < 2:
        return
    
    # Imagine a splitting process all the way down
    # to sublists of length 1, which will then
    # grow back up to len(s) in powers of 2
    sublist_len = 1

    # Merge all sorted sublists back up the tree of splits
    while sublist_len < len(s):
        # i is the starting index of the next two sublists to merge
        i = 0

        # Merge all pairs of sorted sublists of length sublist_len
        while i <= len(s):
            # Compute the end index of the first sublist
            j = i + sublist_len
            # Catch the special case of the last sublist's length
            # that may be shorter than sublist_len
            k = min(j + sublist_len, len(s))

            merged = merge(s[i:j], s[j:k])

            # Put the merged list back into s
            ii = i
            for item in merged:
                s[ii] = item
                ii += 1

            # Move to the next pair of sublists to merge
            i += sublist_len * 2

        # Increase the length of the sublists to merge
        sublist_len *= 2

def main():
    # Test merge_sort using our unsorted lists
    a, c, w = unsort()
    merge_sort(a)
    merge_sort(c)
    merge_sort(w)
    print(f'a = {a}\nc = {c}\nw = {w}')

if __name__ == '__main__':
    main()
