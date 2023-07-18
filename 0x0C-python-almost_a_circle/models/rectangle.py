#!/usr/bin/python3
"""
Rectangle Module
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance
        """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        Setter for the width attribute
        """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """
        Getter for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        Setter for the height attribute
        """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """
        Getter for the x attribute
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        Setter for the x attribute
        """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """
        Getter for the y attribute
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        Setter for the y attribute
        """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """
        Checks if the value is a valid integer parameter
        """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """
        Computes the area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the Rectangle using '#' characters
        """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
