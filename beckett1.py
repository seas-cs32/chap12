### chap12/beckett1.py

def beckett(n):
    """Given n actors, print stage directions"""
    if n == 0:
        return
    
    beckett(n - 1)     # recursive call here?
    print('enter', n)
    # beckett(n - 1)     # or here?

def main():
    # Test with 1 actor
    num_actors = 1

    print(f'empty stage')

    beckett(num_actors)

if __name__ == '__main__':
    main()
