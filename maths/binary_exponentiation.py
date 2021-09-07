"""Binary Exponentiation."""
from __future__ import division
from __future__ import print_function

# Author : Junth Basnet
# Time Complexity : O(logn)


from builtins import input
from past.utils import old_div
def binary_exponentiation(a, n):

    if n == 0:
        return 1

    elif n % 2 == 1:
        return binary_exponentiation(a, n - 1) * a

    else:
        b = binary_exponentiation(a, old_div(n, 2))
        return b * b


if __name__ == "__main__":
    try:
        BASE = int(input("Enter Base : ").strip())
        POWER = int(input("Enter Power : ").strip())
    except ValueError:
        print("Invalid literal for integer")

    RESULT = binary_exponentiation(BASE, POWER)
    print(f"{BASE}^({POWER}) : {RESULT}")
