#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, val in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(val), end="")
            else:
                print("{:d}".format(val))
        if len(row) == 0:
            print("")
