#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: list of lists of integers or floats
        div: number to divide by (int or float)

    Returns:
        New matrix with all elements divided by div

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if each row is not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(el, (int, float))
                    for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
