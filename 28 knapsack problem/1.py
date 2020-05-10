#!/usr/bin/env python3

K = int(input())

F = [float('inf')] * (K + 1)
F[0] = 0
for i in range(1, K + 1):
    F[i] = F[i-1]
    j = 2
    while j ** 3 <= i:
        if F[i - j**3] < F[i]:
            F[i] = F[i - j**3]
        j += 1
    F[i] += 1

print(F[K])
