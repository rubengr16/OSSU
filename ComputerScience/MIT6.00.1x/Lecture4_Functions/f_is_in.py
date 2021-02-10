# Implement the function is_in(char, aStr) which implements the above idea,
# recursively to test if char is in aStr.
# Use bisection search.
# First, test the middle character of a string against char.
# if they're not the same, check if the test character is "smaller"
# than the middle character.
# if so, we need only consider the lower half of the string;
# otherwise, we only consider the upper half of the string
def is_in(char, aStr):
    """

    Parameters
    ----------
    char : chr
        Single character.
    aStr : str
        Alphabetized string.

    Returns
    -------
    int or float
        True if char is in aStr, False otherwise.

    """
    k = int((len(aStr) - 1) // 2)  # Calculates the middle character
    # if aStr is ''
    if len(aStr) == 0:
        return False
    else:
        if char == aStr[k]:  # We have found the character we were looking for
            return True
        elif char < aStr[k]:  # char is lower than the middle, go to lower half
            return is_in(char, aStr[:k])
        else:  # otherwise, search on upper half
            return is_in(char, aStr[k + 1:])
