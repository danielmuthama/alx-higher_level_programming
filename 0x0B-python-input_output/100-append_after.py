#!/usr/bin/python3
"""
student class
"""


def append_after(filename="", search_string="", new_string=""):
    """appends a new line afther a specific line as a parameter"""
    with open(filename, "r", encoding="utf8") as file:
        new_list = []
        while True:
            line = file.readline()
            if line == "":
                break
            new_list.append(line)

            if search_string in line:
                new_list.append(new_string)

    with open(filename, 'w', encoding="utf8") as file:
        file.writelines(new_list)
