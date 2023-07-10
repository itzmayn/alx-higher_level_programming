#!/usr/bin/python3
""" 0x0A 8 """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.
    
    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with given width and height.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

