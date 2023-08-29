#!/usr/bin/python3

""" containing safe_print_list_integers function"""


def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    n_items = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n_items = n_items + 1
        except (ValueError, TypeError):
            continue
    print()
    return n_items
