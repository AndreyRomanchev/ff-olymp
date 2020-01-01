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
    A[v][u] = 1


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if A[i][j] == A[j][k] == A[k][i] == 1:
                print("YES")
                sys.exit()
print("NO")
