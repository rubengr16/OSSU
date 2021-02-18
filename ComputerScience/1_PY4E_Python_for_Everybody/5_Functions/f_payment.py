# Function which asks for worked hours and the rate , and prints the payment:
# normal hours are multiplied by rate, extra ones (> 40) by rate * 1.5
def payment(hours, rate):
    """

    Parameters
    ----------
    hours : int or float
        Hours worked.
    rate : int or float
        Rate per hour.

    Returns
    -------
    int
        Payment calculation with the 50% more for the extra hours worked which
        passes the 40 hours, the other hours are paid as rate indicates,
        as well as, if hours is lower than 40.

    """
    overtime = 0
    if hours > 40:
        overtime = hours - 40
        hours = 40
    return (hours + overtime * 1.5) * rate


try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    print('Pay:', payment(hours, rate))
except ValueError:
    print('Wrong Data')
