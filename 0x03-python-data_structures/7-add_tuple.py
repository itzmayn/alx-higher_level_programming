#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Set default values if the tuples are empty
    a = tuple_a or (0, 0)
    b = tuple_b or (0, 0)

    # Convert single-element tuples to (element, 0) format
    if len(tuple_a) == 1:
        a = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        b = (tuple_b[0], 0)

    # Perform element-wise addition
    new = (a[0] + b[0], a[1] + b[1])

    return new
