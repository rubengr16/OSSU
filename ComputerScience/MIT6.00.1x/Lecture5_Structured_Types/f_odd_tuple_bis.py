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
    ans = ()
    for i in range(len(a_tup)):  # Goes through the tuple
        if i % 2 == 0:  # if the element's index is odd
            ans = ans + (ans[i],)  # Element concatenation to the copy tuple
    return ans
