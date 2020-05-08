#!/usr/bin/env python3


n, m = map(int, input().split())

field = [[0]*10 for _ in range(10)]
field[n][m] = 1

for i in range(n+1, 9):
    for j in range(1, 9):
        field[i][j] = field[i-1][j-1] + field[i-1][j+1]

#for i in range(9, -1, -1):
#    print(field[i])

print(sum(field[8]))