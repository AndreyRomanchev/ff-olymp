#!/usr/bin/env python3


def isPrime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


for i in range(10001, 100000, 2):
    s += isPrime(i)

print(s)
