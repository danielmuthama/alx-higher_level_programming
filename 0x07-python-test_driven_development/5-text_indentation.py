#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ''
    cont = []
    for letter in text:
        temp += letter
        if letter == '?' or letter == ':' or letter == '.':
            cont.append(temp)
            temp = ''
    cont.append(temp)
    final = [tex.lstrip() for tex in cont]
    last = final[-1:]
    for each in final:
        if each == last[0]:
            print(each, end='')
        else:
            print(each, end='\n\n')
