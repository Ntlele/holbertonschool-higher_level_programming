#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5

    s = add(a, b)
    d = sub(a, b)
    p = mul(a, b)
    q = div(a, b)

    print("{} + {} = {}".format(a, b, s))
    print("{} - {} = {}".format(a, b, d))
    print("{} * {} = {}".format(a, b, p))
    print("{} / {} = {:.0f}".format(a, b, q))


if __name__ == "__main__":
    main()
