# Function which calculates the n number of the fibonacci serie,
# it had a bug which was solved adding a line of code,
# it is indicated with a comment.
def f(n):
    """
    n: integer, n >= 0.
    """
    if n == 0:
        return 1  # Added line, previously return n
    else:
        return n * f(n-1)
