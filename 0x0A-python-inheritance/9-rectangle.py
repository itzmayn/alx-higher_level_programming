#!/usr/bin/python3
""" 0x0A 8 """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry, for use with rectangular constructs.

    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area as width * height.

        """
        return self.__width * self.__height

    def __str__(self):
        """ Provides printable representation of Rectangle object.

        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
