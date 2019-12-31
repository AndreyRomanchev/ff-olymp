#!/usr/bin/env python3

# a = list(map(int, input().split()))
m = int(input())
n = int(input())


def ackerman(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n - 1))


print(ackerman(m, n))
