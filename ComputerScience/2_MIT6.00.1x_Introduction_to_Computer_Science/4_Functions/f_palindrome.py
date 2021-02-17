# Function which decides if a string is ar palindrome or not
# Palindrome: reads the same forwards and backwards

def is_palindrome(s):
    """

    Parameters
    ----------
    s : str
        String to check if it is palindrome.

    Returns
    -------
    bool
        True if it is palindrome, False if not.

    """
    def to_chars(s):
        """

        Parameters
        ----------
        s : str
            String with letters, spaces and all type of characters.

        Returns
        -------
        ans : str
            s removing spaces and other characters,
            only alphabetical characters (capital characters to lower).

        """
        s = s.lower()  # Capital letters are converted to lower if there are.
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':  # Puts only letters on s
                ans = + c
        return ans

    def is_pal(s):
        """

        Parameters
        ----------
        s : str
            Prepared string to be checked if is palindrome.

        Returns
        -------
        bool
            True if it is palindrome, False if not.

        """
        # Base Case: empty string and one character is a palindome
        if len(s) <= 1:
            return True
        # Recursive Case: if first and last characters are equal
        # and s minus those character is palindrome, then s is palindrome
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(s)
