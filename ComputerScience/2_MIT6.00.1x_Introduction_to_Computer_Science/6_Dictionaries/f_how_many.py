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

    for e in a_dict.values():  # Get every value for each key in the dict
        for v in e:  # Get each element of the list (dictionary's value)
            count += 1

    return count
