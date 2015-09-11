def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    lo = min(a, b)
    hi = max(a, b)
    q = hi / lo
    r = hi % lo
    if r == 0:
        return lo
    else:
        hi = lo
        lo = r
    return gcdRecur(lo, hi)

print gcdRecur(1071, 462)
