#!/usr/bin/python3
"""Square class with size."""


class Square:
    """Square with size."""

    def __init__(self, size=0):
        """Initialize the data."""
        self.__size = size

    @property  # getter
    def size(self):
        """Retrieve the size."""
        return self.__size

    @size.setter  # setter
    def size(self, value):
        """Set the size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size**2
