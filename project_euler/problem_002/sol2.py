"""
Project Euler Problem 2: https://projecteuler.net/problem=2

Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

References:
    - https://en.wikipedia.org/wiki/Fibonacci_number
"""
from __future__ import print_function


def solution(n: int = 4000000) -> int:
    """
    Returns the sum of all even fibonacci sequence elements that are lower
    or equal to n.

    >>> solution(10)
    10
    >>> solution(15)
    10
    >>> solution(2)
    2
    >>> solution(1)
    0
    >>> solution(34)
    44
    """

    even_fibs = []
    a, b = 0, 1
    while b <= n:
        if b % 2 == 0:
            even_fibs.append(b)
        a, b = b, a + b
    return sum(even_fibs)


if __name__ == "__main__":
    print(f"{solution() = }")
