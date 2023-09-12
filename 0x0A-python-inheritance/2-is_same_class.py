#!/usr/bin/python3

"""
Contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    otherwise False
    """
    is_same = type(obj) is a_class
    return is_same
