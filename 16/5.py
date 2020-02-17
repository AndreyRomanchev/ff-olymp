#!/usr/bin/env python3

def sieve_fast(n: int) -> list:
    is_prime = [0] * (n + 1)
    for d in range(2, n + 1):
        if is_prime[d] == 0:
            for i in range(d, n + 1, d):
                is_prime[i] += 1
        if is_prime[d] >= 3:
            print(d, end=' ')


n = int(input())

sieve_fast(n)
