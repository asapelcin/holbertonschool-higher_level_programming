#!/usr/bin/python3
"""CountedIterator class that tracks iteration count."""


class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize with an iterable and counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated."""
        return self.count

    def __next__(self):
        """Fetch next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item
