#!/usr/bin/python3
"""Implements BaseGeometry for a rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """it inherits from the BaseGeometry class,
        validates and sets values"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
