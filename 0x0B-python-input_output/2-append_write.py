#!/usr/bin/python3
def append_write(filename: str = "", text: str = "") -> int:
    """
    Appends a string at the end of a text file (UTF-8) and returns the number
    of characters added.

    Args:
        filename (str): Name of the file to be opened.
        text (str): Characters to be written.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
