# Iterative function iterPower(base, exp) that calculates the exponential base^exp  by simply using successive multiplication
def powerIter(base, exp):
    '''
    Input: base: int or float, exp: int >= 0
    Returns: base^exp: int or float
    '''
    resul = 1
    for i in range(exp):
        resul *= base
    return resul
