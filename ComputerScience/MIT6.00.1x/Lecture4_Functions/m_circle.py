# Module for circle methods, functions and variables

PI = 3.14159


def area(radius):
    """

    Parameters
    ----------
    radius : int or float
        Length of the circle's radius.

    Returns
    -------
    int or float
        Area of the circle.

    """
    return PI * (radius ** 2)


def circumference(radius):
    """

    Parameters
    ----------
    radius : int or float
        Length of the circle's radius.

    Returns
    -------
    int or float
        Length of the circle's circumference.

    """
    return 2 * PI * radius
