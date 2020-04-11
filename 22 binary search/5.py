#!/usr/bin/env python3


n, k = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(int(input()))

left = 0
right = max(arr) + 1

while right > left + 1:
    m = (right + left) // 2
    count = 0
    for i in arr:
        count += i // m
    if count >= k:
        left = m
    else:
        right = m

print(left)
