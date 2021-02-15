# Write a procedure, called how_many, which returns the sum of the number of
# values associated with a dictionary
def how_many(a_dict):
    """

    Parameters
    ----------
    a_dict : dict
        All the values are lists.

    Returns
    -------
    count : int
        How many values are in the dictionary, including the list values.

    """
    count = 0

    for e in a_dict.values():
        for v in e:
            count += 1

    return count
