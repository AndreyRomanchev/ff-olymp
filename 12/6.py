#!/usr/bin/env python3


def dfs(k: int, color: int) -> None:
    mark[k] = color
    for i in range(n):
        if a[k][i] == 1 and mark[i] == 0:
            dfs(i, 3 - color)


n, m = map(int, input().split())
# n = int(input())

a = [[0] * n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    a[x - 1][y - 1] = 1
    a[y - 1][x - 1] = 1

mark = [0] * n
color = 0
for i in range(n):
    if mark[i] == 0:
        dfs(i, 1)

flag = True

for i in range(n):
    for j in range(n):
        if mark[i] == mark[j] and a[i][j] != 0:
            flag = False

if flag:
    print("YES")
    for i in range(n):
        if mark[i] == 1:
            print(i + 1, " ", end="")
else:
    print("NO")
