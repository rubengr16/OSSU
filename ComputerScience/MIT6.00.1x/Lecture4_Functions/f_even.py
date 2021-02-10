# Create a function which returns true if the x passed as argument is even,
# and false otherwise
def even(x):
    """

    Parameters
    ----------
    x : int
        Value to be tested.

    Returns
    -------
    bool
        True if is even, False if is odd.

    """
    return (x % 2) == 0  # if is even, the module or remainder is 0
