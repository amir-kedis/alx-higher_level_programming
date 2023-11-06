#!/usr/bin/python3
"""Contain the class BaseGeometry."""


class BaseGeometry:
    """Define a class BaseGeometry."""

    def area(self):
        """Raise an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
            name (str): name of the variable.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
