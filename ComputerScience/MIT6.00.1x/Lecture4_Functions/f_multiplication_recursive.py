# Create a function that receiving through input a and b, two integers, returns the multiplication of both without using *
def multRecur(a, b):
    """
    Input: a, b, two int
    Returns: resul, the result of multiplying a by b
    """
    if b == 1:
        resul = a
    else:
        resul = a + multRecur(a, b - 1)
    return resul
