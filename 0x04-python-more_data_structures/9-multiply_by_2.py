#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):
        return dict((key, val*2) for key, val in a_dictionary.items())
    return a_dictionary
