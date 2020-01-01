#!/usr/bin/env python3

#n, m = map(int, input().split())
N = int(input())

A = []

for i in range(N):
    A.append(list(map(int, input().split())))

ans = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(A[i][0]):
        ans[i][A[i][j+1]-1] = 1


for i in range(N):
    print(' '.join(map(str, ans[i])))
