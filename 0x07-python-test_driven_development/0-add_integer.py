#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if type(a) is int and type(b) is int:
        return a + b
    elif type(a) is float and type(b) is float:
        return int(a) + int(b)
    else:
        if type(a) is not int and type(a) is not float:
            raise TypeError("a must be an integer")
        elif type(b) is not int and type(b) is not float:
            raise TypeError("b must be an integer")
        return int(a) + int(b)
