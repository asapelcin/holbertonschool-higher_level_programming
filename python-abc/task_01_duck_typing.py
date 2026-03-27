#!/usr/bin/python3
"""Module for shapes"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Shape class"""
    @abstractmethod
    def area(self):
        """Area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter method"""
        pass


class Circle(Shape):
    """Circle class"""
    def __init__(self, radius):
        """Init circle"""
        self.radius = radius

    def area(self):
        """Circle area"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Circle perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    def __init__(self, width, height):
        """Init rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter"""
        return 2 * (self.width + self.height)