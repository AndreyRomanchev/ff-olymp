#!/usr/bin/env python3


n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))


f = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if nlist[i-1] == mlist[j-1]:
            f[i][j] = f[i - 1][j - 1] + 1
        else:
            f[i][j] = max(f[i - 1][j], f[i][j - 1])

#for i in range(0, n+1):
#    print(f[i])

print(f[n][m])
