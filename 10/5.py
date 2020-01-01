#!/usr/bin/env python3

import sys

n, m = map(int, input().split())
#n = int(input())
A = [[0] * n for i in range(n)]
for i in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    A[u][v] = 1

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if A[i][j] == 0 and A[j][i] == 0:
            print("NO")
            sys.exit(0)

print("YES")
