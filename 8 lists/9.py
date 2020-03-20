#!/usr/bin/env python3

N, K = list(map(int, input().split()))

ans = ['I'] * N

for i in range(K):
    a, b = list(map(int, input().split()))
    ans[a-1:b] = ['.'] * (b + 1 - a)

print(''.join(ans))
