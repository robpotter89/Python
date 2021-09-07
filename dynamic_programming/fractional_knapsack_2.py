# https://en.wikipedia.org/wiki/Continuous_knapsack_problem
# https://www.guru99.com/fractional-knapsack-problem-greedy.html
# https://medium.com/walkinthecode/greedy-algorithm-fractional-knapsack-problem-9aba1daecc93

from __future__ import annotations
from __future__ import division


from builtins import zip
from builtins import range
from past.utils import old_div
def fractional_knapsack(
    value: list[int], weight: list[int], capacity: int
) -> tuple[float, list[float]]:
    """
    >>> value = [1, 3, 5, 7, 9]
    >>> weight = [0.9, 0.7, 0.5, 0.3, 0.1]
    >>> fractional_knapsack(value, weight, 5)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 15)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 25)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, 26)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(value, weight, -1)
    (-90.0, [0, 0, 0, 0, -10.0])
    >>> fractional_knapsack([1, 3, 5, 7], weight, 30)
    (16, [1, 1, 1, 1])
    >>> fractional_knapsack(value, [0.9, 0.7, 0.5, 0.3, 0.1], 30)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack([], [], 30)
    (0, [])
    """
    index = list(range(len(value)))
    ratio = [old_div(v, w) for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value: float = 0
    fractions: list[float] = [0] * len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = old_div(capacity, weight[i])
            max_value += old_div(value[i] * capacity, weight[i])
            break

    return max_value, fractions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
