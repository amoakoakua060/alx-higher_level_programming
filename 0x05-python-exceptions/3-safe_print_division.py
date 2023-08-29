#!/usr/bin/python3

""" containing safe_print_division function"""


def safe_print_division(a, b):
    """that divides 2 integers and prints the res"""
    res = 0
    try:
        res = a / b
    except Exception:
        res = None
    finally:
        print("Inside res: {}".format(res))
    return res
