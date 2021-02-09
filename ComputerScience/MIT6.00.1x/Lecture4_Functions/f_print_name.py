# Function which decides how to print a firstName and lastName (input) based on a boolean value (input, reverse)
def printName (firstName, lastName, reverse):
    """
    Input: firstName, lastName, two str
           reverse bool
    Output: if reverse is True prints firstly the lastName ', ' and firstName
            otherwise prints firstName followed by lastName
    Returns: None
    """
    if reverse:
        print(lastName + ',', firstName)
    else:
        print(firstName, lastName)
