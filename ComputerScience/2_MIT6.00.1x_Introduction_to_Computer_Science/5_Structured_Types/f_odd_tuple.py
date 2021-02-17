# Write a procedure called oddTuples, which takes a tuple as input,
# and returns a new tuple as output, where every other element of the input
# tuple is copied, starting with the first one.
def oddTuples(a_tup):
    """

    Parameters
    ----------
    a_tup : tuple
        A tuple to get its odd elements.

    Returns
    -------
    ans : tuple
        New tuple with the odd elements of a_tup.

    """
    return a_tup[::2]  # tuple with the elements of a_tup by 2
    # Also possible a_tup[:len(a_tup):2]
