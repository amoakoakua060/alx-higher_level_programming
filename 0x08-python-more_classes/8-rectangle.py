#!/usr/bin/python3

"""
A module containing a Rectangle class
"""


class Rectangle():
    """
    A representation of a Rectangle class
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Instantiate the class and set private properties
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        prints a string on deletion
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """
        returns a formal representation of object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """
        To access width private property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width property
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        To access the height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height property
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Calculate the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints a # Rectangle
        """
        _str = ""
        if self.__width == 0 or self.__height == 0:
            return ""

        _hash = str(self.print_symbol)
        for i in range(self.__height):
            _str += f"{_hash * self.__width}"
            if i + 1 != self.__height:
                _str += "\n"

        return _str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1
