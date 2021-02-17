# Create a function which receiving a positive int value through input,
# calculates its factorial
def factorialRecur(x):
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
    if x == 1:
        return 1  # Base Case: x = 1, whose factorial is 1
    else:
        return x * factorialRecur(x - 1)  # Recursive Case: x! = x * (x - 1)!
