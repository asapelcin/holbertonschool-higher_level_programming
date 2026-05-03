#!/usr/bin/python3
"""Module that defines a Square class with private size attribute."""


class Square:
    """A class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
