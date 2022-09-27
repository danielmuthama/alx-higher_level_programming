#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """returns a list of the attributes and methods of obj"""
    return dir(obj)
