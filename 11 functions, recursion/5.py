#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)

a = int(input())
n = int(input())

def power(a: int, n: int):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return power(a, n - 1) * a % 1000
    else:
        return power(a, n // 2) ** 2 % 1000

print(power(a, n))
