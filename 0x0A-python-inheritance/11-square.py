#!/usr/bin/python3
"""Contain the class Square."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)

        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            """Return the print() and str() representation of a Square."""
            return "[Square] {}/{}".format(self.__size, self.__size)

        def area(self):
            """Return the area of the square."""
            return self.__size**2
