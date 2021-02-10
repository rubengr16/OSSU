# Iterative function iterPower(base, exp), calculates the exponential base^exp
# by simply using successive multiplication
def powerRecur(base, exp):
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
    if exp == 0:
        return 1  # Base Case 1: base^0 = 1
    elif exp == 1:
        return base  # Base Case 2: base^1 = base
    else:
        return base * powerRecur(base, exp - 1)
        # Recursive Case: base^exp = base * base^(exp - 1)
