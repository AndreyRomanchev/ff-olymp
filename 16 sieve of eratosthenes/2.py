#!/usr/bin/env python3


def sieve(n: int) -> list:
    primes = []
    is_prime = [True] * (n + 1)
    for d in range(2, n + 1):
        if is_prime[d]:
            primes.append(d)
            for i in range(d*d, n+1, d):
                is_prime[i] = False
    return primes


for number in sieve(10**5)[::-1]:
    if str(number) == str(number)[::-1]:
        print(number)
        break