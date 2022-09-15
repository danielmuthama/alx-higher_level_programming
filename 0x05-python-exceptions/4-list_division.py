#!/usr/bin/python3

"""a function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except Exception as e:
            if isinstance(e, ZeroDivisionError) is True:
                print("division by 0")
            elif isinstance(e, TypeError) is True:
                print("wrong type")
            elif isinstance(e, IndexError) is True:
                print("out of range")
            div = 0
        finally:
            new_list.append(div)
            continue
    return new_list
