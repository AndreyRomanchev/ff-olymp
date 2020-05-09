#!/usr/bin/env python3


nstring = input()
mstring = input()
n = len(nstring)
m = len(mstring)


f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(0, n+1):
    for j in range(0, m+1):
        if i == 0:
            f[i][j] = j
        if j == 0:
            f[i][j] = i


for i in range(1, n+1):
    for j in range(1, m+1):
        if nstring[i-1] == mstring[j-1]:
            f[i][j] = min(f[i-1][j] + 1, f[i-1][j-1], f[i][j-1] + 1)
        else:
            f[i][j] = min(f[i-1][j] + 1, f[i-1][j-1] + 1, f[i][j-1] + 1)

#for i in range(0, n+1):
#    print(f[i])

print(f[n][m])
