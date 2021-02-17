# Function that aplies another function to a list
# both are given as parameter
def apply_to_each(L, f):
    """

    Parameters
    ----------
    L : list
        List to be modified.
    f : function
        Function to be applied to each element of the list.

    Returns
    -------
    None.

    """
    for i in range(len(L)):
        L[i] = f(L[i])
