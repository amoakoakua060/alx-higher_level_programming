#!/usr/bin/python3

"""
module containing Rectangle class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle geometry class
    """

    def __init__(self, width, height):
        """
        instantiate rectangle class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
