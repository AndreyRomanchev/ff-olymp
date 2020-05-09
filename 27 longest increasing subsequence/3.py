#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

F = [float('inf')] * (n + 1)
F[0] = float('-inf')

for i in range(n):
    left = 0
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if F[middle] >= A[i]:
            right = middle
        else:
            left = middle
    F[right] = A[i]

# print(F)
k = n
while F[k] == float('inf'):
    k -= 1
print(k)