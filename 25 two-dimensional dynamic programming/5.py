#!/usr/bin/env python3


n, m = map(int, input().split())

mmap = []
for i in range(n):
    mmap.append(list(map(int, input().split())))

#for i in range(0, n):
#    print(mmap[i])

field = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if field[i][j-1] > field[i-1][j]:
            field[i][j] = field[i][j-1] + mmap[i-1][j-1]
        else:
            field[i][j] = field[i-1][j] + mmap[i-1][j-1]

#for i in range(0, n+1):
#    print(field[i])

print(field[n][m])

i = n
j = m
path = []
while not (i == 1 and j == 1):
    # print(field[i][j - 1], field[i - 1][j])
    if field[i][j-1] > field[i-1][j]:
        path.append('R')
        j -= 1
        #print('R', j)
    else:
        path.append('D')
        i -= 1
        #print('D', i)

print(' '.join(path[::-1]))