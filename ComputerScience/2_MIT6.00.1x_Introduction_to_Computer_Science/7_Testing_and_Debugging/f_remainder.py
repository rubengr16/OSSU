# Function which calculates the remainder of a division,
# it had a bug which was solved adding a line of code,
# it is indicated with a comment.
def rem(x, a):
    """
    Parameters
    ----------
    x : int
        Non-negative integer.
    a : int
        Positive integer.

    Returns
    -------
    int
        Remainder when x is divided by a.

    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)  # Added line, previously rem(x-a, a)
