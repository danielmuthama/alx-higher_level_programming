#!/usr/bin/python3

"""a function that prints an integer
-- handling exceptions encountered"""


import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
