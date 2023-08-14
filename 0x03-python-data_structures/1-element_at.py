#!/usr/bin/python3
def element_at(my_list, idx):
    n_elem = len(my_list)
    if n_elem == 0 or idx < 0 or n_elem - 1 < idx:
        return None

    return my_list[idx]
