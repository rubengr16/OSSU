# Given a tuple of tuples with int-str pairs, sets the min and max int
# and counts how many different words there are
def get_data(a_tuple):
    """

    Parameters
    ----------
    a_tuple : tuple
        Tuple with pairs int-str.

    Returns
    -------
    min_num : int
        Minimum value of the ints of al the elements.
    max_num : int
        Maximum value of the ints of al the elements.
    unique_words : int
        Count of unique words.

    """
    nums = ()  # Empty tuple
    words = ()
    for t in a_tuple:  # tuple iteration
        nums += (t[0],)  # Necessary the , to indicate the conversion to tuple
        if t[1] not in words:
            words += (t[1],)

    min_num = min(nums)
    max_num = max(nums)
    unique_words = len(words)

    return (min_num, max_num, unique_words)


# Example
tu = ((1, 'egg'), (2, 'egg'), (1, 'bacon'), (3, 'bread'), (-1, 'oil'))
print(get_data(tu))
