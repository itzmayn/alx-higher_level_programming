#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int: A peak in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    # Binary search-like approach
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak might be on the left side
            right = mid
        else:
            # Peak might be on the right side
            left = mid + 1

    return list_of_integers[left]