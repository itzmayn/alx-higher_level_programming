#!/usr/bin/python3
# Importing the lookup function from module '0-lookup'
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    """
    A simple class representing MyClass1.
    """

    pass

class MyClass2(object):
    """
    A class representing MyClass2.

    Attributes:
        my_attr1 (int): An attribute with a value of 3.
    """

    my_attr1 = 3

    def my_meth(self):
        """
        A method defined within MyClass2.
        """
        pass

# Using the lookup function to get the information of MyClass1, MyClass2, and int
print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
