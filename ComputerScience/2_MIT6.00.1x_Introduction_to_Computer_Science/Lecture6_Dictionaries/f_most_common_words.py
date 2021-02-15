#  Function which search for the words with the greatest number of appearances.
def most_common_words(freqs):
    """

    Parameters
    ----------
    freqs : dict
        str:int pairs, where we have word:frequency.

    Returns
    -------
    words : list
        Most frequent words in a list.
    best : int
        Frequency of appearance.

    """
    values = freqs.values()  # list of values
    best = max(values)  # Obtain the maximum appearances
    words = []

    for i in freqs:
        if freqs[i] == best:
            # Save the words with the maximum number of appearances
            words.append(i)

    return (words, best)
