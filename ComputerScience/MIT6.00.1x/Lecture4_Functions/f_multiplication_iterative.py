# Create a function that receiving through input a and b, two integers, returns the multiplication of both without using *
def multIter(a, b):
    """
    Input: a, b: two int
    Returns: resul: the result of multiplying a by b
    """
    resul = 0
    while b > 0:
        resul += a
        b -= 1
    return resul