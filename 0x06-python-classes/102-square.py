#!/usr/bin/python3

"""
a class Square that defines a square: (based on 4-square.py)

size: def __init__(self, size=0):
size must be a foat or integer, otherwise raise a
TypeError exception with the message size must be a number
if size is less than 0, raise a ValueError exception
with the message size must be >= 0

"""


class Square:
    """
    Includes:
    (1) Public instance method:
    def area(self): that returns the current square area
    (2) Private instance attribute + property:
    def size(self): holds the size of the square
    """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int or type(value) is float:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be a number")

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
