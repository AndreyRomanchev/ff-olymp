#!/usr/bin/env python3


n, m = map(int, input().split())

mmap = []
for i in range(n):
    mmap.append(list(map(int, input().split())))

#for i in range(0, n):
#    print(mmap[i])

field = [[0]*(m+1) for _ in range(n+1)]
field[0][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        field[i][j] = (field[i][j-1] + field[i-1][j]) * mmap[i-1][j-1]

#for i in range(0, n+1):
#    print(field[i])

print(field[n][m])
