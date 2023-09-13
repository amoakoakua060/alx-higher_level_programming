#!/usr/bin/python3

"""
module containing Student class
"""


class Student():
    """ Student Class with instance variables """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of new Student object
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns dictionary representation of Student class
        """
        return self.__dict__
