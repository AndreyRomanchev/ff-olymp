#!/usr/bin/env python3


def isPrime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


k = int(input())

if k == 1:
    print(2)
else:
    count = 1
    i = 1
    while count != k:
        i += 2
        if isPrime(i):
            count += 1
    print(i)