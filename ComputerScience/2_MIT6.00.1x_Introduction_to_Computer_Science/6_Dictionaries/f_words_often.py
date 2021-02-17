# Function which returns a list with the words with frequencies greater or
# equal to a minimum of times
import f_most_common_words


def words_often(freqs, min_times):
    """

    Parameters
    ----------
    freqs : dict
        str:int pairs, where we have word:frequency.
    min_times : int
        Required times of appearance at least.

    Returns
    -------
    resul : list
        Each element is a tuple with a word (str) and its frequency (int).

    """
    resul = []
    done = False  # Loop controller
    while not done:
        temp = f_most_common_words.most_common_words(freqs)
        # Auxiliar variable to save the tuple returned
        if temp[1] >= min_times:
            resul.append(temp)  # We add the tuple to the list
            for w in temp[0]:
                del(freqs[w])  # Remove the word from dictionary
        else:  # There is no word which meets our min_times requirement
            done = True

    return resul
