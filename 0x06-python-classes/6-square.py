#!/usr/bin/python3
"""Square class with size."""


class Square:
    """Square with size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the data."""
        self.size = size
        self.position = position

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

    @property  # getter
    def position(self):
        """Retrieve the position."""
        return self.__position

    @position.setter  # setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size**2

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
