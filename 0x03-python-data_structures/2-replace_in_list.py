#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n_elem = len(my_list)
    if n_elem == 0 or idx < 0 or n_elem - 1 < idx:
        return my_list

        my_list[idx] = element
        return my_list
