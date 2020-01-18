#!/usr/bin/env python3


def dfs_or(k: int) -> None:
    global ans
    mark[k] = 1
    for i in range(n):
        if a[k][i] == 1:
            if mark[i] == 0:
                dfs_or(i)
            elif mark[i] == 1:
                ans = 1
    mark[k] = 2


# n, s = map(int, input().split())
n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

mark = [0] * n
ans = 0
for i in range(n):
    dfs_or(i)

print(ans)
