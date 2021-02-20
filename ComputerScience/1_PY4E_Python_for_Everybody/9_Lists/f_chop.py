# Create a function which takes a list and modifies it, removing the first and
# last elements, and returns None
def chop(my_list):
    """

    Parameters
    ----------
    my_list : list
        List to delete the first and last element.

    Returns
    -------
    None.

    """
    del my_list[0]  # del modifies the original list
    del my_list[len(my_list) - 1]
    # pop does the same, but as it returns the element, is less pythonic
