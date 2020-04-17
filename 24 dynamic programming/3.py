#!/usr/bin/env python3


n = int(input())

f = [0] * (n + 1)
f[1] = 0

for i in range(2, n + 1):
    f[i] = f[i-1]
    if i % 3 == 0 and f[i//3] < f[i]:
        f[i] = min(f[i//3], f[i-1])
    elif i % 2 == 0 and f[i//2] < f[i]:
        f[i] = f[i//2]
    f[i] += 1

print(f[n])