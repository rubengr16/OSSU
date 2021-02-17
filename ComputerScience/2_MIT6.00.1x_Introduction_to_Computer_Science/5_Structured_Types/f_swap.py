# Swapping variable values
def swap(x, y):
    """

    Parameters
    ----------
    x : int, float, str, list, tuple, dictionary, some object
        First variable.
    y : int, float, str, list, tuple, dictionary, some object
        Second variable.

    Returns
    -------
    x : int, float, str, list, tuple, dictionary, some object
        Second variable in first position.
    y : int, float, str, list, tuple, dictionary, some object
        First variable in second position.

    """
    (x, y) = (y, x)  # Swapping, it can be done by just returning (y, x)
    return (x, y)
