#!/usr/bin/python3
"""Read file and print to stdout."""


def read_file(filename=""):
    """Read a text file and print it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
