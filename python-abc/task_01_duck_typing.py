#!/usr/bin/python3
"""Duck typing with abstract classes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Return area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
    