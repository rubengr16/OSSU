# Python function, evalQuadratic(a, b, c, x),
# that returns the value of the quadratic  a*x^2 + b*x + c
def evalQuadratic(a, b, c, x):
    """

    Parameters
    ----------
    a : int or float
        Numerical value for the coefficients of quadratic equation.
    b : int or float
        Numerical value for the coefficients of quadratic equation.
    c : int or float
        Numerical value for the coefficients of quadratic equation.
    x : int or float
        Numerical value at which to evaluate the quadratic.

    Returns
    -------
    int or float
        Value of a * x ** 2 + b * x + c

    """
    return a * x ** 2 + b * x + c
