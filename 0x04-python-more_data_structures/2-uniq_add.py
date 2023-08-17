#!/usr/bin/python3
def uniq_add(my_list=[]):
    num_sum = 0
    if isinstance(my_list, list) and len(my_list):
        for i in list(set(my_list)):
            num_sum += i
        return num_sum
