# Function which count how mani times appears on a string a letter,
# both passed as arguments
def count(string, char):
    """

    Parameters
    ----------
    string : str
        String for searching.
    char : str
        Letter (char) to search.

    Returns
    -------
    count : int
        Number of appearances of char in string.

    """
    count = 0
    for c in string:
        if c == char:
            count += 1

    return count
