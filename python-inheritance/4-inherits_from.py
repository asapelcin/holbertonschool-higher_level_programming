#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if inherited, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
