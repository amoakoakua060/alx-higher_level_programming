#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Return a new list with True or False
    """
    if not isinstance(my_list, list):
        return None

    if len(my_list) > 0:
        return [a % 2 == 0 for a in my_list]
    else:
        return []
