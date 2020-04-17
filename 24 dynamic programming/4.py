#!/usr/bin/env python3


n = int(input())

f = [0] * (n + 1)
prev = [0] * (n + 1)
f[1] = 0

for i in range(2, n + 1):
    f[i] = f[i-1]
    prev[i] = i - 1
    if i % 3 == 0 and f[i//3] < f[i]:
        f[i] = min(f[i//3], f[i-1])
        prev[i] = i//3
    elif i % 2 == 0 and f[i//2] < f[i]:
        f[i] = f[i//2]
        prev[i] = i // 2
    f[i] += 1

print(f[n])

path = []
i = n
while i > 0:
    path.append(i)
    i = prev[i]
path.append(0)
path = path[::-1][1:]
print(' '.join(map(str, path)))
