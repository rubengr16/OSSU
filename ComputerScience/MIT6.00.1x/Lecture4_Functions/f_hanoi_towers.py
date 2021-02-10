# Solve the problem of the Towers of Hanoi:
# Given n sized discs order from lower (upper) to greater (lower)
# move those n discs from one column to the objective
def print_move(fr, to):
    """

    Parameters
    ----------
    fr : int or str
        Value or string which represents the from column.
    to : int or str
        Value or string which represents the to column.

    Output
    ------
    Displays from where to to move.

    Returns
    -------
    None

    """
    print('Move from', str(fr), 'to', str(to))


def towers(n, fr, to, spare):
    """

    Parameters
    ----------
    n : int
        Number of discs.
    fr : int or str
        Value or string which represents the from column.
    to : int or str
        Value or string which represents the to column.
    spare: int or str
        Value or string which represents the spare column.

    Output
    ------
    Displays the process of how to move.

    Returns
    -------
    None

    """
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)  # Move n - 1 to the spare column.
        # to free the bottom disc.
        towers(1, fr, to, spare)  # Move the bottom disc to the to column.
        towers(n - 1, spare, to, fr)  # Move n - 1 discs to the to column.
