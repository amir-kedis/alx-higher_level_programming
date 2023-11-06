#!/usr/bin/python3
"""Contain is_same_class function."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class.

    Args:
        obj (any): object to check.
        a_class (type): class to check against.

    Return:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
