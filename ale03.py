### chap12/ale03.py

def fib(n):
    '''Return the Fibonacci number at 0-based index n'''
    if n < 0:
        raise ValueError('Fibonacci is defined only for positive n')
    
    # INSERT BASE CASES AND THE RECURSIVE CALL
    return 0  # and REMOVE THIS


def ifib(n):
    '''Return the Fibonacci number at 0-based index n'''
    if n < 0:
        raise ValueError('Fibonacci is defined only for positive n')
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    ra = 0    # fib(0) 
    rb = 1    # fib(1)
    for i in range(2, n + 1):
        # Use last two fib numbers to compute fib(i)
        ra, rb = rb, ra + rb

    return rb


def main():
    # Test code
    print('Testing fib ...')
    assert fib(0) == 0, 'Failed for n = 0'
    assert fib(1) == 1, 'Failed for n = 1'
    assert fib(2) == 1, 'Failed for n = 2'
    assert fib(3) == 2, 'Failed for n = 3'
    assert fib(4) == 3, 'Failed for n = 4'
    assert fib(5) == 5, 'Failed for n = 5'
    assert fib(6) == 8, 'Failed for n = 6'
    assert fib(8) == 21, 'Failed for n = 8'
    assert fib(12) == 144, 'Failed for n = 12'
    print('PASSED our unit tests!')

    print('Testing ifib ...')
    assert ifib(0) == 0, 'Failed for n = 0'
    assert ifib(1) == 1, 'Failed for n = 1'
    assert ifib(2) == 1, 'Failed for n = 2'
    assert ifib(3) == 2, 'Failed for n = 3'
    assert ifib(4) == 3, 'Failed for n = 4'
    assert ifib(5) == 5, 'Failed for n = 5'
    assert ifib(6) == 8, 'Failed for n = 6'
    assert ifib(8) == 21, 'Failed for n = 8'
    assert ifib(12) == 144, 'Failed for n = 12'
    print('PASSED our unit tests!')

    print()

    # Run with a bigger n
    n = 38
    print(f'Running ifib({n}) = ')
    print(ifib(n))
    print(f'Running fib({n}) = ')
    print(fib(n))    

if __name__ == '__main__':
    main()