#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/set position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                all(n < 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area of size"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            [print() for i in range(0, int(self.__position[1]))]
            for i in range(0, int(self.__size)):
                [print(' ', end='') for j in range(0, int(self.__position[0]))]
                [print('#', end='') for k in range(0, int(self.__size))]
                print()
