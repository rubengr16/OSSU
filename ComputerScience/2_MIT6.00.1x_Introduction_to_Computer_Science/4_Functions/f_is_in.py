# Implement the function is_in(char, a_str) which implements the above idea,
# recursively to test if char is in a_str.
# Use bisection search.
# First, test the middle character of a string against char.
# if they're not the same, check if the test character is "smaller"
# than the middle character.
# if so, we need only consider the lower half of the string;
# otherwise, we only consider the upper half of the string
def is_in(char, a_str):
    """

    Parameters
    ----------
    char : chr
        Single character.
    a_str : str
        Alphabetized string.

    Returns
    -------
    int or float
        True if char is in a_str, False otherwise.

    """
    k = int((len(a_str) - 1) // 2)  # Calculates the middle character
    if len(a_str) == 0:  # if aStr is ''
        return False
    else:
        if char == a_str[k]:  # We have found the character we were looking for
            return True
        elif char < a_str[k]:  # char is < than the middle, go to lower half
            return is_in(char, a_str[:k])
        else:  # otherwise, search on upper half
            return is_in(char, a_str[k + 1:])
