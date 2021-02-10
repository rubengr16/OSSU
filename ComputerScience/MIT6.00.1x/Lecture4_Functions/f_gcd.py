# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder.
def gcd_iter(a, b):
    '''
    Input:a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        c = b
    else:
        c = a

    while a % c != 0 or b % c != 0:
        c -= 1
    return c
