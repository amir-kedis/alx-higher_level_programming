#!/usr/bin/python3
"""Contain is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a class inherited from.

    Args:
        obj (any): object to check.
        a_class (type): class to check against.

    Return:
        True if obj is an instance of a_class or a class inherited from,
        False otherwise.
    """
    return isinstance(obj, a_class)
