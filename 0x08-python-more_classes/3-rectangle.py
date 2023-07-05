#!/usr/bin/python3
"""3-rectangle,  0x08.
"""


class Rectangle:
    """A class that represents a rectangle.

    Args:
        width (int): The width of the rectangle. Defaults to 0.
        height (int): The height of the rectangle. Defaults to 0.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return (self.__width + self.__height) * 2

    def _draw_rectangle(self):
        """Formats a string representation of the rectangle."""
        rect_str = ""
        for _ in range(self.__height):
            rect_str += '#' * self.__width + '\n'
        return rect_str.rstrip('\n')

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return self._draw_rectangle()
