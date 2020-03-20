#!/usr/bin/env python3


def divisors_sum(i: int) -> int:
    ans = 1
    d = 2
    while d * d < i:
        if i % d == 0:
            ans = ans + d + i//d
        d += 1
    if d * d == i:
        ans += d
    return ans


n = int(input())
for i in range(1, n+1):
    j = divisors_sum(i)
    if n >= j > i == divisors_sum(j):
        print(i, j)
