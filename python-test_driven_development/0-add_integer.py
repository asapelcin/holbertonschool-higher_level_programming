#!/usr/bin/python3
"""This module provides a function to add two integers."""


def add_integer(a, b=98):
    """Add two integers or floats cast to integers.

    Args:
        a: first number (int or float)
        b: second number (int or float), default is 98

    Returns:
        Integer sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
