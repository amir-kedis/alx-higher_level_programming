#!/usr/bin/python3
"""Contain the class MyInt."""


class MyInt(int):
    """Represent a MyInt."""

    def __eq__(self, other):
        """Return the opposite of the equal."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Return the opposite of the not equal."""
        return super().__eq__(other)
