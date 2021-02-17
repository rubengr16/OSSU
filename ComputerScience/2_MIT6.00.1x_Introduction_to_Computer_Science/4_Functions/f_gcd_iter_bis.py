# The greatest common divisor of two positive integers is the largest integer
# that divides each of them without remainder
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
    if b > a:
        aux = a
        a = b
        b = aux

    c = b  # c is the gcc
    while a % b != 0:  # Euclides formula: gcd(a,b) = gcd (b, a % b)
        c = a % b
        a = b
        b = c
    return c
