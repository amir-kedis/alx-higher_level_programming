#!/usr/bin/python3
"""Contain inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a_class or a class inherited from.

    Args:
        obj (any): object to check.
        a_class (type): class to check against.

    Return:
        True if obj is an instance of a_class or a class inherited from,
        False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
