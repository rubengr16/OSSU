# Create a function which receiving a positive int value through input,
# calculates its factorial
def factorialRecur(x):
    """
    Input: x: a positive int

    Returns: the factorial of x (n!)
    """
    if x == 1:
        return 1
    else:
        return x * factorialRecur(x - 1)
