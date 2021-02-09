# Iterative function iterPower(base, exp) that calculates the exponential base^exp  by simply using successive multiplication
def powerRecur(base, exp):
    '''
    Input: base: int or float, exp: int >= 0
    Returns: base^exp: int or float
    '''
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * powerRecur(base, exp - 1)
