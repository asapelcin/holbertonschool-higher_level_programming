#!/usr/bin/env python3
"""Module that defines CustomObject, a class demonstrating pickling
(serialization/deserialization) of custom Python objects.
"""
import pickle


class CustomObject:
    """A simple custom class with name, age, and is_student attributes,
    supporting serialization/deserialization via the pickle module.
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): the name of the object.
            age (int): the age of the object.
            is_student (bool): whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to filename.

        Args:
            filename (str): path of the file to write the pickle data to.

        Returns:
            None. If an error occurs, it is silently handled and None
            is returned.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (pickle.PickleError, OSError, TypeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from filename.

        Args:
            filename (str): path of the file to read the pickle data from.

        Returns:
            CustomObject: the deserialized instance, or None if the file
            does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (pickle.PickleError, OSError, EOFError,
                AttributeError, ImportError, IndexError):
            return None
