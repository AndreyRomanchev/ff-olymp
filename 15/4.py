#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    if b > 0:
        return gcd(b, a % b)
    else:
        return a


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

a = abs(x1 - x2)
b = abs(y1 - y2)
d = gcd(a, b)
print(a + b - d)
