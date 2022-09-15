#!/usr/bin/python3

"""a class Square that defines a
square (based on 5-square.py) with private instance attributes
and a properties which are accessed and changed
by getters and setters respectively"""


class Square:
    """"
    Square (class): creates a square with the size specified by
    the parameter size and raise error if type is not int or
    size is less than zero.
    Attributes:
        size (int): specify the size of the square.
        position(): specifies a tuple containing square pos
        area(): returns the area of the square.
        my_print(): prints out the square with # character to stdout.
        checker(tuple): checks a tuple for conformity
    Args:
        size (int): size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def checker(self, items):
        """method to check if the elements in a tuple
        conform with specific requirements"""
        status = False
        if (type(items) is tuple and len(items) == 2):
            for elem in items:
                if (type(elem) is int) and (elem >= 0):
                    status = True
                    continue
                else:
                    status = False
                    break
        return status

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if self.checker(value) is True:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Calculates area of the square and return the result"""
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square with the character # to the stdout
        depending on the position specified"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
