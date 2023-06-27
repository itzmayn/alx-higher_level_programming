#!/usr/bin/python3

class Square:
    """A class representing a square"""
    
    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
        size (int): The size of the square.

        Returns:
        None
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
