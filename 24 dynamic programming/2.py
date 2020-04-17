#!/usr/bin/env python3


n = int(input())
arr = list(map(int, input().split()))

painted = [0] * n

for i in range(4, n):
    painted[i] = max(painted[i-1], painted[i-5] + 10 * (arr[i] + arr[i-1] + arr[i-2] + arr[i-3] + arr[i-4]))

print(painted[-1])