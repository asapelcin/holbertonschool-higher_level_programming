#!/usr/bin/python3
"""Module for Shape, Circle and Rectangle classes"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class Shape"""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter"""
        pass


class Circle(Shape):
    """Class Circle that inherits from Shape"""

    def __init__(self, radius):
        """Initializes Circle with radius"""
        self.radius = radius

    def area(self):
        """Calculates circle area: pi * r^2"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculates circle perimeter: 2 * pi * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class Rectangle that inherits from Shape"""

    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculates rectangle area: w * h"""
        return self.width * self.height

    def perimeter(self):
        """Calculates rectangle perimeter: 2 * (w + h)"""
        return 2 * (self.width + self.height)

