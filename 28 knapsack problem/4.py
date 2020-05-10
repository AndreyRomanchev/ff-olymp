#!/usr/bin/env python3

n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))


F = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, m + 1):
        if k >= w[i]:
            F[i][k] = max(F[i - 1][k], F[i - 1][k - w[i]] + p[i])
        else:
            F[i][k] = F[i - 1][k]

#for i in range(n+1):
#    print(F[i])

print(F[n][m])