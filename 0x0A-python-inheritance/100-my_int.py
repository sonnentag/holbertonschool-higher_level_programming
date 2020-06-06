#!/usr/bin/python3
"""100-my_int"""


class MyInt(int):
    """introverted"""

    def __eq__(self, other):
        """equals"""
        return (super().__ne__(other))

    def __ne__(self, other):
        """not equals"""
        return (super().__eq__(other))
