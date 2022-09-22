#!/usr/bin/python3
"""A function that  prints a square with the character #"""


def print_square(size):
    """prints the square of length size, with character #.

    size must be greater than 0

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for x in range(size):
            print('#'*size)
