#!/usr/bin/python3
"""Implements a full rectangle based on BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Full rectangle implementation
        Args:
        width - width of rectangle
            height - height of rectangle
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
