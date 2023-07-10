#!/usr/bin/python3
""" 0x0A 13 """


def add_attribute(obj, attribute, value):
    """Attempts to set or update `attribute` with `value`.
    """
    if hasattr(obj, "__dict__"):
        # if __dict__ is present, attributes can be dynamically added
        setattr(obj, attribute, value)
    elif hasattr(obj, "__slots__") and attribute in obj.__slots__:
        # even if no __dict__, existing attributes in __slots__ can be updated
        setattr(obj, attribute, value)
    else:
        # out of options, can't add
        raise TypeError("can't add new attribute")
