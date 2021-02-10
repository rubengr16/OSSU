# Function which decides how to print a firstName and lastName (input)
# based on a boolean value (input, reverse)
def printName(firstName, lastName, reverse):
    """

    Parameters
    ----------
    firstName : str
        Name.
    lastName : str
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
        print(lastName + ',', firstName)
    else:
        print(firstName, lastName)
