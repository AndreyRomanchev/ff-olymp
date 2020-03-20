#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

ans = 0
for i in range(10**5, 10**6):
    if gcd(i, 70) == 1:
        ans += 1

print(ans)