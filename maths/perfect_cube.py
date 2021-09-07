from __future__ import division
from __future__ import print_function
from past.utils import old_div
def perfect_cube(n: int) -> bool:
    """
    Check if a number is a perfect cube or not.

    >>> perfect_cube(27)
    True
    >>> perfect_cube(4)
    False
    """
    val = n ** (old_div(1, 3))
    return (val * val * val) == n


if __name__ == "__main__":
    print(perfect_cube(27))
    print(perfect_cube(4))
