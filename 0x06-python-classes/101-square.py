#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple and len(value) == 2 and type(value[0]) is int \
                and type(value[1]) is int and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        new = ""
        if self.__size == 0:
            return new
        else:
            for k in range(self.__position[1]):
                new += "\n"
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    new += " "
                for j in range(self.__size):
                    new += "#"
                if (i == self.__size - 1):
                    new += ""
                else:
                    new += "\n"
        return new
