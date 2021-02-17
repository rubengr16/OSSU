def gcd_recur(a, b):
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
    if b == 0:
        return a
    else:
        return gcd_recur(b, a % b)
