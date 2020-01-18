#!/usr/bin/env python3


def dfs(k: int) -> None:
    mark[k] = 1
    for i in range(n):
        if a[k][i] == 1 and mark[i] == 0:
            dfs(i)


n, m = map(int, input().split())
#n = int(input())

a = [[0] * n for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = 1
    a[y-1][x-1] = 1

mark = [0] * n
dfs(0)
#mark.sort()

print(sum(mark))
print(' '.join([str(i + 1) for i, x in enumerate(mark) if x]))