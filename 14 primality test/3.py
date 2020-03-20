#!/usr/bin/env python3


def isPrime(n: int) -> bool:
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


num_list = [2445304333, 4092947611, 6278397751, 6300693019, 7999219357]
print(len(list(filter(isPrime, num_list))))