#!/usr/bin/env python3

N, M = map(int, input().split())
gold = list(map(int, input().split()))


F = [0] * (M + 1)
F[0] = 1

for g in gold:
    for m in range(M, g-1, -1):
        if F[m - g] == 1:
            F[m] = 1

# print(F)
e = M
while F[e] == 0:
    e -= 1

print(e)
