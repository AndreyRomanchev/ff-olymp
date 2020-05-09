#!/usr/bin/env python3


nlist = list(map(int, input().split()))
n = len(nlist)

f = [0] * n

for i in range(n):
    for j in range(i):
        if nlist[i] % nlist[j] == 0 and f[j] > f[i]:
            f[i] = f[j]
    f[i] += 1

# print(f)

print(max(f))
