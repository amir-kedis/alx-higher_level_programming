#!/usr/bin/python3
"""Contain the class MyList."""


class MyList(list):
    """Define a class MyList that inherits from list."""

    def __init__(self):
        """Initialize a MyList instance."""
        super().__init__()

    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
