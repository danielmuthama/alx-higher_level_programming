#!/usr/bin/python3
"""Compare if Exact same object"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly
    an instance of the specified class; otherwise False"""

    return type(obj) is a_class
