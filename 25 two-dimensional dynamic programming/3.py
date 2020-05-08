#!/usr/bin/env python3


n, m = map(int, input().split())

field = [[0]*(m+3) for _ in range(n+3)]


for k in range(2, m+n+2):
    # print(k)
    for j in range(2, k+1):
        if k == j == 2:
            field[k][j] = 1
        else:
            i = k - j + 2
            # print(i, j)
            if i < n+2 and j < m+2:
                field[i][j] = field[i - 2][j - 1] + field[i - 1][j - 2] + field[i + 1][j - 2] + field[i - 2][j + 1]


# for i in range(n+3):
#    print(field[i])

print(field[n+1][m+1])