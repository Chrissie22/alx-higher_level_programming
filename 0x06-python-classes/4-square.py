#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """Initializes a new square."""
        self.size = size

    @property
    def size(self):
        """Gets/sets size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area of size"""
        return (self.__size * self.__size)
