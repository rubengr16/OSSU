# Create a function that receiving through input a and b, two integers,
# returns the multiplication of both without using *
def multIter(a, b):
    """

    Parameters
    ----------
    a : int and float
        Value to multiply.
    b : int and float
        Value to multiply.

    Returns
    -------
    int or float
        Result of multiplying a by b.

    """
    resul = 0
    while b > 0:
        resul += a  # Successive addition b times
        b -= 1
    return resul
