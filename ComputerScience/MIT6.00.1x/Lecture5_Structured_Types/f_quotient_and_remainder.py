# Calculates quotien and the remainder and returns it
def quotien_and_remainder(x, y):
    """

    Parameters
    ----------
    x : int ot float
        Divisor.
    y : int or float
        Divident.

    Returns
    -------
    q : int
        Quotient.
    r : int
        Remainder.

    """
    q = x // y
    r = x % y
    return (q, r)  # Tuple to return more than one value
