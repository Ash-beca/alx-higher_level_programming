#!/usr/bin/python3
"""
This is the 2-matrix_divided module.
It contains 1 function: matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    returns a new matrix where all elements have been divided by div
    """
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    div = 0
    for num in matrix:
        if type(num) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of '
                    'integers/floats')
        if div == 0:
            div = len(num)
        elif div != len(num):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num / div, 2) for num in row] for row in matrix]
