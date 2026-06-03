#!/usr/bin/python3
"""Convert class instance to JSON-serializable dictionary."""


def class_to_json(obj):
    """Return dictionary description of an object for JSON serialization."""
    return obj.__dict__
