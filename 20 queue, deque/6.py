#!/usr/bin/env python3

from collections import deque


n, x = map(int, input().split())
a = []
d = deque()
ans = [-1] * n
ans[x-1] = 0
for i in range(n):
    a.append(list(map(int, input().split())))

d.append(x-1)
while d:
    u = d.popleft()
    # print('u', u, 'ans[u]', ans[u])
    for i, v in enumerate(a[u]):
        # print('v', v, 'ans[v]', ans[v])
        if v == 1 and ans[i] == -1:
            ans[i] = ans[u] + 1
            d.append(i)

print(' '.join(map(str, ans)))
