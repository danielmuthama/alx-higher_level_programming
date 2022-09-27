#!/usr/bin/python3
"""Square implementation based on Rectangle class
    with __str__ method overriding"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ private instance attr size is the size of the square
        the __str__ method is overridden"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        super().__str__()
        return f"[Square] {self.__size}/{self.__size}"
