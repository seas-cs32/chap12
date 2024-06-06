### chap12/ffactorial.py

def ffactorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    elif n < 2:
        return 1
    else:
        result = 1
        for num in range(2, n+1):
            result *= num
        return result
        
def main():
    # Test code
    print('Testing factorial ...')
    assert ffactorial(0) == 1, 'Failed for n = 0'
    assert ffactorial(1) == 1, 'Failed for n = 1'
    assert ffactorial(2) == 2, 'Failed for n = 2'
    assert ffactorial(3) == 6, 'Failed for n = 3'
    assert ffactorial(4) == 24, 'Failed for n = 4'
    assert ffactorial(16) == 20922789888000, 'Failed for n = 16'
    print('PASSED our unit tests!')

if __name__ == '__main__':
    main()