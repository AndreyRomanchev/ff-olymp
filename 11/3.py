#!/usr/bin/env python3

from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

# a = list(map(int, input().split()))
n = int(input())


def wrongfib(a: int):
    if a <= 2:
        return 1
    else:
        return wrongfib(a - 1) + wrongfib(a - 3)

print(wrongfib(n))