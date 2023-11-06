#!/usr/bin/python3
"""Define a function that adds a new attribute to an object if it’s possible."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it’s possible.

    Args:
        obj (object): The object to add the new attribute.
        name (str): The name of the new attribute.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object can’t have new attribute.
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
