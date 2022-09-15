#!/usr/bin/python3

"""a class Square that defines a
square by: (based on 3-square.py)

Instantiation with optional parameter
size: def __init__(self, size=0):
size must be an integer, otherwise raise a
TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception
with the message size must be >= 0"""


class Square:
    """Includes a Public instance method:
def area(self): that returns the current square area"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
