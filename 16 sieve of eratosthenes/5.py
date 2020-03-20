#!/usr/bin/env python3

from time import time

def sieve_fast(n: int):
    is_prime = [0] * (n + 1)
    ans = []
    for d in range(2, n + 1):
        if is_prime[d] == 0:
            for i in range(d, n + 1, d):
                is_prime[i] += 1
        if is_prime[d] >= 3:
            ans.append(str(d))
    return ans

n = int(input())

print(' '.join(sieve_fast(n)))
