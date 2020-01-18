#!/usr/bin/env python3


def dfs(k: int) -> None:
    mark[k] = 1
    for i in range(n):
        if a[k][i] == 1 and mark[i] == 0:
            dfs(i)


# n, s = map(int, input().split())
n = int(input())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

mark = [0] * n
dfs(0)

print("YES") if mark.count(0) == 0 else print("NO")
