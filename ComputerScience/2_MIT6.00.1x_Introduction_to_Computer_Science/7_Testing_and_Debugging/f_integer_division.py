# Function which calculates the integer division,
# it had a bug which was solved adding a line of code,
# it is indicated with a comment.
def integerDivision(x, a):
    """

    Parameters
    ----------
    x : int
        Non-negative integer.
    a : int
        Positive integer.

    Returns
    -------
    count : int
        Integer division of x divided by a.

    """
    count = 0  # Added Line, preiously count was not initialized
    while x >= a:
        count += 1
        x = x - a
    return count
