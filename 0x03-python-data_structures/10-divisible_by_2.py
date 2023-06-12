#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a new list containing True for numbers divisible by 2 in the input list, and False for others.

    Args:
        my_list (list): List of numbers.

    Returns:
        list: New list with True or False values.

    Raises:
        None.
    """
    new_list = []  # Initialize an empty list to store the results
    for num in my_list:
        if num % 2 == 0:  # Check if the number is divisible by 2
            new_list.append(True)  # Append True to the new list if divisible by 2
        else:
            new_list.append(False)  # Append False to the new list if not divisible by 2
    return new_list  # Return the new list containing True and False values
