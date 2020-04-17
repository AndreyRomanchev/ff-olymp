#!/usr/bin/env python3


n, k = map(int, input().split())

arr = [0] * (n + k + 1)
arr[0] = 1
for j in range(1, k+1):
    arr[-j] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        arr[i] += arr[i-j]

print(arr[n])
