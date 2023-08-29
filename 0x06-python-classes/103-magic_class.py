#!/usr/bin/python3
"""Defines a class MagicClass"""
import math

class MagicClass:
    """Thes represents a circle"""
    def __init__(self, radius=0):
        """Initializes the magic class"""
        self.__radius = radius

    def area(self):
        """Calculates the are of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumstance(self):
        """Calculates the circumstances of the circle"""
        return 2 * math.pi * self.__radius
