#!/usr/bin/python3

"""a class Square that defines a
square (based on 4-square.py) with private instance attributes
and a property which is accessed and changed
by a getter and setter respectively"""



class Square:
    """"
    Square (class): creates a square with the size specified by
    the parameter size and raise error if type is not int or
    size is less than zero.
    Attributes:
        size (int): specify the size of the square.
        area(): returns the area of the square.
        my_print(): prints out the square with # character to stdout.
    Args:
        size (int): size of the square.
    """

    def __init__(self, size=0):
        self.size = size

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

    def area(self):
        """Calculates area of the square and return the result"""

        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with the character # to the stdout. """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
