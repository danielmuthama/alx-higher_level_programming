#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix that contains elements
    which are dividends of the division by the argument passed (div)
    All elements of the matrix are divided by div and
    rounded to 2 decimal places
    Raises:
        TypeError: if each row of the matrix is not of the same size
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if div is not a number (integer or float)
        ZeroDivisionError: if div is equal to 0
    """

    t_error = TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not isinstance(matrix, list):
        raise t_error
    if len(matrix) < 2:
        if len(matrix) == 0:
            raise t_error
        if len(matrix) == 1 and len(matrix[0]) < 1:
            raise t_error
        if isinstance(matrix[0], list) and len(matrix[0]) > 0:
            new_matrix = [matrix[:] for matrix in matrix]
            for y in range(0, len(matrix[0])):
                if type(matrix[0][y]) == int or\
                   type(matrix[0][y]) == float:
                    new_matrix[0][y] = round((matrix[0][y]/div), 2)
                else:
                    raise t_error

    else:
        if not isinstance(matrix[0], list):
            raise t_error
        length = len(matrix[0])
        new_matrix = [matrix[:] for matrix in matrix if type(matrix) == list]
        for x in range(0, len(matrix)):
            if not isinstance(matrix[x], list):
                raise t_error
            for y in range(0, len(matrix[x])):
                if type(matrix[x][y]) == int or\
                   type(matrix[x][y]) == float:
                    new_matrix[x][y] = round((matrix[x][y]/div), 2)
                else:
                    raise t_error
            if len(matrix[x]) != length:
                raise TypeError("Each row of the matrix "
                                "must have the same size")
    return new_matrix
