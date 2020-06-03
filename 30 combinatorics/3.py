#!/usr/bin/env python3


n = int(input())

F = [[0] * (n + 1) for _ in range(10)]
for i in range(1, 10):
    F[i][1] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            F[j][i] = F[j][i - 1] + F[j + 1][i - 1]
        elif j == 9:
            F[j][i] = F[j - 1][i - 1] + F[j][i - 1]
        else:
            F[j][i] = F[j - 1][i - 1] + F[j][i - 1] + F[j + 1][i - 1]
    # print(F[0][i], F[1][i], F[2][i])

# print(F[0][n], F[1][n], F[2][n])
s = 0
for i in range(10):
    s += F[i][n]
    # print(F[i][n])
# print(F[0][n] + F[1][n] + F[2][n])
print(s)