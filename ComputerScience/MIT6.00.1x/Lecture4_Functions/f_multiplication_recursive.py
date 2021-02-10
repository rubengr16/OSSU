# Create a function that receiving through input a and b, two integers,
# returns the multiplication of both without using *
def multRecur(a, b):
    """

    Parameters
    ----------
    a : int and float
        First value of the multiplication.
    b : int and float
        First value of the multiplication.

    Returns
    -------
    int or float
        Result of multiplying a by b.

    """
    if b == 1:
        return a  # Base Case: a * 1 = a
    else:
        return a + multRecur(a, b - 1)
