#!/usr/bin/python3
import math

class MagicClass:
    """A class representing MagicClass"""

    def __init__(self, radius=0):
        """
        Initializes an instance of MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the MagicClass instance.

        Raises:
            TypeError: If the radius is not a number.

        Returns:
            None
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Args:
            None

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Args:
            None

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
