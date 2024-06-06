### chap12/wfactorial.py

def wfactorial(n):
    if n < 0:
        raise ValueError("factorial is not defined for negative integers")
    elif n < 2:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
    
def main():
    # Test code
    print('Testing factorial ...')
    assert wfactorial(0) == 1, 'Failed for n = 0'
    assert wfactorial(1) == 1, 'Failed for n = 1'
    assert wfactorial(2) == 2, 'Failed for n = 2'
    assert wfactorial(3) == 6, 'Failed for n = 3'
    assert wfactorial(4) == 24, 'Failed for n = 4'
    assert wfactorial(16) == 20922789888000, 'Failed for n = 16'
    print('PASSED our unit tests!')

if __name__ == '__main__':
    main()