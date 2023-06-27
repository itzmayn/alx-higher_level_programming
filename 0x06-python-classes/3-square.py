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
        # Check if the size is an integer
        if type(size) is not int:
            raise TypeError("size must be an integer")
        # Check if the size is non-negative
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Args:
        None

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
