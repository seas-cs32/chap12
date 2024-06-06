### chap12/merge.py

def merge(a, b):
    """Given two sorted lists, return a single sorted list"""

    # Check for and handle trivial merge cases
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    # Create a place to put the merged lists
    merged = []
    # Calculate how long the merged list should be
    tot_length = len(a) + len(b)

    # Merge a and b
    while (len(merged) < tot_length):
        if len(a) == 0:
            merged.append(b.pop(0))
        elif len(b) == 0:
            merged.append(a.pop(0))
        elif a[0] < b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))

    return merged

def main():
    # Test cases for merge. Uncomment one `a` and one `b`.
    #a = []
    a = [1, 3, 5, 7]
    #b = []
    #b = [2, 4]
    #b = [2, 4, 6, 8, 10]
    b = [2, 4, 6, 7, 8, 10]
    print(merge(a,b))

if __name__ == '__main__':
    main()
