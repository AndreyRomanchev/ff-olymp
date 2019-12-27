#!/usr/bin/env python3

a = list(map(int, input().split()))

sum_zeroes = 0

for i, n in enumerate(a):
    if n == 0:
        sum_zeroes += 1
        a.remove(0)
print(a)
