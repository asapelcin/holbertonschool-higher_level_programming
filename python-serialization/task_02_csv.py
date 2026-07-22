#!/usr/bin/env python3
"""Module that defines convert_csv_to_json, a function that reads data
from a CSV file and serializes it into a JSON file (data.json).
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Read data from csv_filename and write it as JSON to data.json.

    Args:
        csv_filename (str): path to the CSV file to read.

    Returns:
        bool: True if the conversion was successful, False otherwise
        (e.g. file not found or malformed data).
    """
    try:
        with open(csv_filename, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = [row for row in reader]

        with open("data.json", "w") as json_file:
            json.dump(rows, json_file, indent=4)

        return True
    except (OSError, csv.Error, json.JSONDecodeError):
        return False
