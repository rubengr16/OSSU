# Given a list of numbers, a list with the division of all the numbers by the
# value of the given index
def fancy_divide(list_of_numbers, index):
    """

    Parameters
    ----------
    list_of_numbers : list
        List of numbers.
    index : int
        Index of the denominator of the fraction, must be between 0 and
        len(list_of_numbers).

    Returns
    -------
    list
        List of results of the divisions.

    """
    denom = list_of_numbers[index]  # Sets the denominator
    return [simple_divide(item, denom) for item in list_of_numbers]
    # list with the results for every item


def simple_divide(item, denom):
    """

    Parameters
    ----------
    item : int
        Numerator.
    denom : int
        Denominator.

    Returns
    -------
    float
        Division's result, 0.0 in case of denom == 0.

    """
    try:
        return item / denom
    except ZeroDivisionError:
        return 0.0
