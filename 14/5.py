#!/usr/bin/env python3


def isPrime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())

if n == 4:
    print("2 2")
else:
    d = 3
    while not (isPrime(d) and isPrime(n - d)):
        d += 2
    print(d, n - d)