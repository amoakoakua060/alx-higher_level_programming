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

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of Student class
        """

        if isinstance(attrs, list):
            return {k: self.__dict__[k] for k in self.__dict__ if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """

        for key in json:
            self.__dict__[key] = json[key]
