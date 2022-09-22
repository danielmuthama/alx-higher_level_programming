#!/usr/bin/python3
"""A class that really defines a Rectangle"""


class Rectangle:
    """
    Rectangle (class): creates a rectangle with the size specified by
    the parameter height and width
    Attributes:
        width (int): specify the width of the rectangle.
        height (int): specifies the height of the rectangle
    Args:
        Area: returns the area of the rectangle
        Perimeter: returns the perimeter of the rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """rectangle class destructor"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(0, self.__height):
            [print("#", end="") for y in range(0, self.__width)]
            if x != self.__height - 1:
                print("")
        return ""

    def __repr__(self):
        """Returns the string representation of the Rectangle."""

        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
