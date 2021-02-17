# Create a function which receiving a positive int value through input,
# calculates its factorial
def factorialIter(x):
    """

    Parameters
    ----------
    x : int
        Value to be obtained its factorial, must be greater than 0.

    Returns
    -------
    int
        Factorial of x (x!).

    """
    resul = 1
    for i in range(1, x + 1):  # x! = 1 * 2 * 3 * ... * n
        resul *= i
    return resul
