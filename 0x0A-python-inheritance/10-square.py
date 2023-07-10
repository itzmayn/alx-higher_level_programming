#!/usr/bin/python3
""" 0x0A 8 """


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle and BaseGeometry.
    
    Args:
        size (int): Length of the side of the square.
    
    Attributes:
        __size (int): Length of the side of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size.
        
        Args:
            size (int): Length of the side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square (__size * __size).
        """
        return self.__size ** 2
