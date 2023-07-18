#!/usr/bin/python3
"""
A module that test differents behaviors
of the Square class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    A class to test the Square Class
    """

    def test_pep8_base(self):
        """
        Test that checks PEP8 style guide
        """
        # Create a PEP8 style guide object
        style_guide = pep8.StyleGuide(quit=True)
        # Check the style of the square.py file
        check_result = style_guide.check_files(['models/square.py'])
        # Verify that there are no code style errors or warnings
        self.assertEqual(
            check_result.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_getter(self):
        # Create a Square object with size 5
        square = Square(5)
        # Verify that the getter method returns the correct size
        self.assertEqual(square.size, 5)

    def test_setter(self):
        # Create a Square object with size 5
        square = Square(5)
        # Change the size using the setter method
        square.size = 8
        # Verify that the size has been updated correctly
        self.assertEqual(square.size, 8)

    def test_string(self):
        # Create a Square object with size 3
        square = Square(3)
        # Verify that assigning a string value to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = "Hi"

    def test_negative(self):
        # Create a Square object with size 6
        square = Square(6)
        # Verify that assigning a negative value to size raises a ValueError
        with self.assertRaises(ValueError):
            square.size = -5

    def test_zero(self):
        # Create a Square object with size 6
        square = Square(6)
        # Verify that assigning zero to size raises a ValueError
        with self.assertRaises(ValueError):
            square.size = 0

    def test_decimal(self):
        # Create a Square object with size 6
        square = Square(6)
        # Verify that assigning a decimal value to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = 1.5

    def test_tuple(self):
        # Create a Square object with size 7
        square = Square(7)
        # Verify that assigning a tuple value to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = (2, 8)

    def test_empty(self):
        # Create a Square object with size 7
        square = Square(7)
        # Verify that assigning an empty string to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = ''

    def test_none(self):
        # Create a Square object with size 5
        square = Square(5)
        # Verify that assigning None to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = None

    def test_list(self):
        # Create a Square object with size 4
        square = Square(4)
        # Verify that assigning a list value to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = [4, 7]

    def test_dict(self):
        # Create a Square object with size 5
        square = Square(5)
        # Verify that assigning a dictionary value to size raises a TypeError
        with self.assertRaises(TypeError):
            square.size = {"hi": 5, "world": 8}

    def test_width(self):
        # Create a Square object with size 5
        square = Square(5)
        # Change the size using the setter method
        square.size = 6
        # Verify that both width and height have been updated correctly
        self.assertEqual(square.width, 6)
        self.assertEqual(square.height, 6)

    def test_to_dictionary(self):
        # Reset the counter for the number of objects
        Base._Base__nb_objects = 0

        # Create a Square object with size 10, position (2, 1), and id 9
        square = Square(10, 2, 1, 9)
        # Convert the square object to a dictionary
        square_dict = square.to_dictionary()
        # Define the expected dictionary
        expected_dict = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        # Verify that the converted dictionary matches the expected dictionary
        self.assertEqual(square_dict, expected_dict)

        # Create a Square object with size 1, position (0, 0), and id 9
        square = Square(1, 0, 0, 9)
        # Convert the square object to a dictionary
        square_dict = square.to_dictionary()
        # Define the expected dictionary
        expected_dict = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        # Verify that the converted dictionary matches the expected dictionary
        self.assertEqual(square_dict, expected_dict)

        # Update the square object with id 5, size 5, position (5, 5)
        square.update(5, 5, 5, 5)
        # Convert the square object to a dictionary
        square_dict = square.to_dictionary()
        # Define the expected dictionary
        expected_dict = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        # Verify that the converted dictionary matches the expected dictionary
        self.assertEqual(square_dict, expected_dict)

