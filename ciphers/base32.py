from __future__ import print_function
from builtins import input
import base64


def main() -> None:
    inp = eval(input("->"))
    encoded = inp.encode("utf-8")  # encoded the input (we need a bytes like object)
    b32encoded = base64.b32encode(encoded)  # b32encoded the encoded string
    print(b32encoded)
    print(base64.b32decode(b32encoded).decode("utf-8"))  # decoded it


if __name__ == "__main__":
    main()
