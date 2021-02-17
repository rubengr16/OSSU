# Iterative function iterPower(base, exp), calculates the exponential base^exp,
# by simply using successive multiplication
def powerIter(base, exp):
    """

    Parameters
    ----------
    base : int or float
        Value to be raised.
    exp : int
        Exponent, must be greater or equal than 0

    Returns
    -------
    int or float
        Result of base^exp.

    """
    resul = 1
    for i in range(exp):
        resul *= base  # Successive multiplications exp times
    return resul
