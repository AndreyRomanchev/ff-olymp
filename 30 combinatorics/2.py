#!/usr/bin/env python3


n = int(input())

F = [[0] * (n + 1) for _ in range(3)]
F[0][1] = 1
F[1][1] = 1
F[2][1] = 1

for i in range(2, n + 1):
    F[0][i] = F[0][i - 1] + F[1][i - 1] + F[2][i - 1]
    F[1][i] = F[0][i - 1] + F[2][i - 1]
    F[2][i] = F[0][i - 1] + F[1][i - 1]
    # print(F[0][i], F[1][i], F[2][i])

# print(F[0][n], F[1][n], F[2][n])
print(F[0][n] + F[1][n] + F[2][n])
