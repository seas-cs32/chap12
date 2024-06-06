### chap12/factorial.py

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError('factorial is defined only for positive n')
    return n * factorial(n - 1)

def main():
    # Test code
    print('Testing factorial ...')
    assert factorial(0) == 1, 'Failed for n = 0'
    assert factorial(1) == 1, 'Failed for n = 1'
    assert factorial(2) == 2, 'Failed for n = 2'
    assert factorial(3) == 6, 'Failed for n = 3'
    assert factorial(4) == 24, 'Failed for n = 4'
    assert factorial(16) == 20922789888000, 'Failed for n = 16'
    print('PASSED our unit tests!')

if __name__ == '__main__':
    main()