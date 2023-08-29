#!/usr/bin/python3

""" containing safe_print_integer function"""


def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
