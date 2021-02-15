# Write a procedure, called biggest, which returns the key corresponding to
# the entry with the largest number of values associated with it.
# If there is more than one such entry, return any one of the matching keys.
# If the dictionary is empty, return None.
def biggest(a_dict):
    """

    Parameters
    ----------
    a_dict : dict
        All the values are lists.

    Returns
    -------
    biggest : type of the dictionary's key or None
        Key with the largest number of values associated with it.

    """
    biggest = None

    for e in a_dict:
        if biggest is not None:
            if len(a_dict[biggest]) < len(a_dict[e]):
                biggest = e
        else:
            biggest = e

    return biggest
