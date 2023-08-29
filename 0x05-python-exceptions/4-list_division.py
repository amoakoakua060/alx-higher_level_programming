#!/usr/bin/python3

""" containing list_division function"""


def list_division(my_list_1, my_list_2, list_length):
    res = 0
    n_list = []
    for idx in range(list_length):
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except (ValueError, TypeError):
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            n_list.append(res)
    return n_list
