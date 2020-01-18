#!/usr/bin/env python3


def dfs(k: int, color: int) -> None:
    mark[k] = color
    for i in range(n):
        if a[k][i] == 1 and mark[i] == 0:
            dfs(i, color)


# n, s = map(int, input().split())
n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

mark = [0] * n
color = 0
for i in range(n):
    if mark[i] == 0:
        color += 1
        dfs(i, color)

print(color)
