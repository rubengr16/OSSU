# Python function, odd, that takes in one number
# and returns True when the number is odd and False otherwise
def odd(x):
    """

    Parameters
    ----------
    x : int
        Value to be tested.

    Returns
    -------
    bool
        True if is odd, False if is even.

    """
    return (x % 2) == 1  # if is odd, the remainder is 1
