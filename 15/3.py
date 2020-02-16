#!/usr/bin/env python3


def gcd_row(a: int, b: int) -> int:
    ans = 0
    while b != 0:
        ans += a//b
        a, b = b, a % b
    return ans


a = int(input())
b = int(input())

print(gcd_row(a, b))
