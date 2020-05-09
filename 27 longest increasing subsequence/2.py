#!/usr/bin/env python3

n = int(input())
nlist = list(map(int, input().split()))

f = [0] * n

for i in range(n):
    for j in range(i):
        if nlist[j] < nlist[i] and f[j] > f[i]:
            f[i] = f[j]
    f[i] += 1

#print(f)

ans = []
ansl = max(f)
i = f.index(ansl)
ans.append(str(nlist[i]))
while f[i] > 1:
    j = i - 1
    while nlist[j] >= nlist[i] or f[j] != f[i] - 1:
        j -= 1
    ans.append(str(nlist[j]))
    i = j

print(' '.join(ans[::-1]))