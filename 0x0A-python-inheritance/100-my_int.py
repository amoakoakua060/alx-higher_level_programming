#!/usr/bin/python3

"""
module containing MyInt class
"""


class MyInt(int):
    """
    Extends int class which is a default type in pythone
    """

    def __eq__(self, other):
        """
        implemetation of == operation
        """
        if isinstance(other, MyInt):
            return self != other
        return False

    def __ne__(self, other):
        """
        implemetation of != operation
        """
        return not self.__eq__(other)
