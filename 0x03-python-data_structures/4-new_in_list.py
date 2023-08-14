#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n_list = []
    n_elem = len(my_list)
    if n_elem == 0 or idx < 0 or n_elem - 1 < idx:
        return my_list
    for i in range(len(my_list)):
        n_list.append(my_list[i])
    n_list[idx] = element
    return n_list
