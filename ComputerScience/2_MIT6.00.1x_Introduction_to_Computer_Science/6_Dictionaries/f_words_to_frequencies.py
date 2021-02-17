# Function which counts the number of appearances of each word
# of a given text in a list
def words_to_frequencies(text):
    """

    Parameters
    ----------
    text : list
        Words of the text as elements of a list.

    Returns
    -------
    my_dict : dict
        str:int pairs, where we have word:frequency.

    """
    my_dict = {}

    for word in text:
        if word in my_dict:  # if the word has appeared, we increment its count
            my_dict[word] += 1
        else:  # The word hasn't appeared yet
            my_dict[word] = 1

    return my_dict
