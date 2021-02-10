# Create a function which receiving a positive int value through input,
# calculates its factorial
def factorialIter(x):
    """
    Input: x: a positive int

    Returns: resul: the factorial of x (n!)
    """
    resul = 1
    for i in range(1, x + 1):
        resul *= i
    return resul
