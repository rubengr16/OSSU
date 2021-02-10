# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder
def gcd_iter(a, b):
    '''
    Input:a, b: positive integers

    Returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b > a:
        aux = a
        a = b
        b = aux

    c = b
    while a % b != 0:
        c = a % b
        a = b
        b = c
    return c
