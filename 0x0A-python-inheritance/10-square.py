#!/usr/bin/python3

"""
module containing Square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square geometry class
    """

    def __init__(self, size):
        """
        instantiate new object private attributes
        """
        self.integer_validator("size", size)

        super().__init__(size, size)

        self.__size = size

    def area(self):
        """
        returns the area of the Square
        """
        return (self.__size ** 2)
