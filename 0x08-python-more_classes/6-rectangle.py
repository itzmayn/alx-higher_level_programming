#!/usr/bin/python3
"""6-rectangle, 0x08.
"""

class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self._width = 0
        self._height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def _draw_rectangle(self):
        rectangle_str = ""
        for row in range(self.height):
            rectangle_str += "#" * self.width
            if row < self.height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __str__(self):
        return self._draw_rectangle()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
