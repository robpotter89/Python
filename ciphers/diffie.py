from __future__ import print_function
from builtins import input
from builtins import range
from typing import Optional


def find_primitive(n: int) -> Optional[int]:
    for r in range(1, n):
        li = []
        for x in range(n - 1):
            val = pow(r, x, n)
            if val in li:
                break
            li.append(val)
        else:
            return r
    return None


if __name__ == "__main__":
    q = int(eval(input("Enter a prime number q: ")))
    a = find_primitive(q)
    if a is None:
        print(f"Cannot find the primitive for the value: {a!r}")
    else:
        a_private = int(eval(input("Enter private key of A: ")))
        a_public = pow(a, a_private, q)
        b_private = int(eval(input("Enter private key of B: ")))
        b_public = pow(a, b_private, q)

        a_secret = pow(b_public, a_private, q)
        b_secret = pow(a_public, b_private, q)

        print(("The key value generated by A is: ", a_secret))
        print(("The key value generated by B is: ", b_secret))
