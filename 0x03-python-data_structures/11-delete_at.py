#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    remove value of idx
    """
    if not isinstance(my_list, list):
        return None

    n_list = len(my_list)
    if idx < 0 or n_list <= idx:
        return my_list
    for i in range(n_list):
        if i == idx:
            my_list.remove(my_list[idx])
            break
    return my_list
