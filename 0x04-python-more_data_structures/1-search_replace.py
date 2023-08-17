#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if isinstance(my_list, list) and len(my_list):
        new_list = my_list.copy()
        for key, value in enumerate(new_list):
            if value == search:
                new_list[key] = replace
        return new_list
    return my_list
