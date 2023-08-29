#!/usr/bin/python3

""" containing safe_print_list function"""


def safe_print_list(my_list=[], x=0):
    """x elements of a list"""
    n_items = 0
    try:
        for item in my_list:
            if n_items == x:
                print()
                return n_items

            print("{}".format(item), end="")
            n_items += 1
    except Exception:
        print()
        return n_items

    print()
    return n_items
