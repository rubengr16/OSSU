# Python function, fourthPower, that takes in one number
# and returns that value raised to the fourth power
def fourthPower(x):
    """

    Parameters
    ----------
    x : int or float
        Value to be raised to the forth power.

    Returns
    -------
    int or float
        Value of x^4.

    """
    def square(x):
        """

        Parameters
        ----------
        x : int or float
            Value to be squared.

        Returns
        -------
        int or float
            Value of x^2.

        """
        return x ** 2
    return square(square(x))  # 2 calls to square: square(x)^2 = x^2^2 = x^4
