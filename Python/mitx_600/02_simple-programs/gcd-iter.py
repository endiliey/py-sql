def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        test = a
    else:
        test = b

    while (a % test != 0 or b % test != 0):
        test -= 1
    return test

print(gcdIter(225, 144))