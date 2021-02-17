# Function which decides how to print a firstName and lastName (input)
# based on a boolean value (input, reverse)
def printName(first_name, last_name, reverse):
    """

    Parameters
    ----------
    first_name : str
        Name.
    last_name : str
        Surname.
    reverse : bool
        Decides the order of printing the other parameters.

    Output
    ------
    If reverse is True prints firstly the lastName ', ' and firstName,
    otherwise prints firstName followed by lastName

    Returns
    -------
    None.

    """
    if reverse:
        print(last_name + ',', first_name)
    else:
        print(first_name, last_name)
