#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

f = [0] * n
count = [0] * n
count[0] = 1

for i in range(n):
    for j in range(i):
        print(i, j)
        if A[j] < A[i] and f[j] > f[i]:
            if f[j] - f[i] == 1:
                count[i] += count[j]
            f[i] = f[j]

    f[i] += 1
    print(count)

print(f)

print(max(f))
