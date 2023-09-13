#!/usr/bin/python3

"""
module containing write_file function
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns the number of characters
    """
    if not isinstance(text, str):
        return 0

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
