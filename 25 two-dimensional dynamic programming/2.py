#!/usr/bin/env python3


n, m = map(int, input().split())

field = [[0]*(m+1) for _ in range(n+1)]
field[1][1] = 1

for i in range(2, n+1):
    for j in range(2, m+1):
        # print(i, j)
        field[i][j] = field[i-2][j-1] + field[i-1][j-2]

#for i in range(9, -1, -1):
#    print(field[i])

print(field[n][m])