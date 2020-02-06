#!/usr/bin/env python3


def isPrime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


i = 1e14
while not isPrime(i):
    i += 1

print(i)
