#!/usr/bin/python3

"""
Contains a My_list
"""


class MyList(list):
    """
    a list class
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self.copy()))
