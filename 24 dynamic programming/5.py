#!/usr/bin/env python3


n = input()

l = len(n)
f = [0] * (l + 1)
f[0] = 1

for i in range(1, l + 1):
    f[i] = f[i - 1]
    if n[i - 2] in ['1', '2', '3'] and 1 <= (int(n[i - 2]) * 10 + int(n[i - 1])) <= 33:
        f[i] += f[i - 2]

print(f[l])
