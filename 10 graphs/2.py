#!/usr/bin/env python3

#n, m = map(int, input().split())
N = int(input())

A = [[0] * N for i in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))


for i in range(N):
    print(sum(A[i]), ' '.join(map(str, [i+1 for i, x in enumerate(A[i]) if x == 1])))
