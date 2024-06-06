### chap12/unsort.py

# Some unsorted lists to use as examples and tests
def unsort():
    a = [5, 2, 1, 4, 7, 3, 6]
    c = ['6\u2663', '3\u2663', '2\u2660', '2\u2661', '4\u2663', '6\u2662', '5\u2660']
    w = ['The', 'sun', 'did', 'not', 'shine',
        'It', 'was', 'too', 'wet', 'to', 'play']
    return a, c, w

def main():
    a, c, w = unsort()
    print(f'A = {a}\nC = {c}\nW = {w}')

if __name__ == '__main__':
    main()
