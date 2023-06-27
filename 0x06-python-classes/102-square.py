class Square:
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (float or int): The size of the square.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.

        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Args:
            None

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The value to assign as the size.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.

        Returns:
            None
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Args:
            None

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the area of the square is equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if the area of the square is not equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if the area of the square is greater than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if the area of the square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if the area of the square is less than the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if the area of the square is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is
