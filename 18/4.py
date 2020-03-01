#!/usr/bin/env python3


n = int(input())
limits = list(map(int, input().split()))
k = int(input())
presses = list(map(int, input().split()))

sorted_presses = [0] * n
for i in presses:
    sorted_presses[i-1] += 1

for i in range(n):
    if limits[i] >= sorted_presses[i]:
        print("NO")
    else:
        print("YES")