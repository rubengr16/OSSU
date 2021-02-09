# Python function, fourthPower, that takes in one number and returns that value raised to the fourth power
def fourthPower(x):
    '''
    Input: x, int or float.
    Returns: the fourth power of x
    '''
    def square(x):
        '''
        Input: x, int or float.
        Returns: the square of x
        '''
        return x ** 2
    return square(square(x))
