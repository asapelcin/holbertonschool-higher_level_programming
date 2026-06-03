#!/usr/bin/python3
"""Basic serialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save to file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
