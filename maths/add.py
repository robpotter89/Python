"""
Just to check
"""
from __future__ import print_function


def add(a, b):
    """
    >>> add(2, 2)
    4
    >>> add(2, -2)
    0
    """
    return a + b


if __name__ == "__main__":
    a = 5
    b = 6
    print(f"The sum of {a} + {b} is {add(a, b)}")
