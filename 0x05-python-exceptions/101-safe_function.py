#!/usr/bin/python3
import sys
"""a function that executes a function safely."""


def safe_function(fct, *args):
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)

    return res
