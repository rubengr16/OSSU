# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder.
def gcd_iter(a, b):
    """

    Parameters
    ----------
    a : int
        Value to be tested, must be greater or equal than 0.
    b : int
        Value to be tested, must be greater or equal than 0.

    Returns
    -------
    int
        Greatest common divisor of a and b, greater or equal than 0.

    """
    if a > b:
        c = b
    else:
        c = a

    while a % c != 0 or b % c != 0:
        c -= 1
    return c
