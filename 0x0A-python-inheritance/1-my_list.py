#!/usr/bin/python3
""" 0x0A 1"""


class MyList(list):
    """
    Custom list type intended to only contain integers.
    """

    def print_sorted(self):
        """
        Prints the elements of MyList in ascending order.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)