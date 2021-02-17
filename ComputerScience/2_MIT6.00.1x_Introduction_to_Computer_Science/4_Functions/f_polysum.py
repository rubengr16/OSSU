# A regular polygon has n number of sides. Each side has length s.
# The area of a regular polygon is:  (0.25 * n * s^2) / tan(π/n)
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the
# regular polygon. The function returns the sum, rounded to 4 decimal places.
import math


def polysum(n, s):
    """

    Parameters
    ----------
    n : int
        Number of sides of the regular polygon.
    s : int or float
        Size of the sides.

    Returns
    -------
    int or float
        Addition of the area of the polygon ((0.25 * n * s^2) / tan(π/n))
        plus the perimeter (n * s) squared.

    """
    def area(n, s):
        """

        Parameters
        ----------
        n : int
            Number of sides of the regular polygon.
        s : int or float
            Size of the sides.

        Returns
        -------
        int or float
            Area of the polygon ((0.25 * n * s^2) / tan(π/n)).

        """
        return (0.25 * n * s ** 2) / (math.tan(math.pi / n))  # Area's formula

    def perimeter(n, s):
        """

        Parameters
        ----------
        n : int
            Number of sides of the regular polygon.
        s : int or float
            Size of the sides.

        Returns
        -------
        int or float
            Perimeter of the polygon (n * s).

        """
        return n * s  # Perimeter's formula

    return round(area(n, s) + perimeter(n, s) ** 2, 4)  # area + perimeter^2
