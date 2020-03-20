#!/usr/bin/env python3

from collections import deque


n, m = map(int, input().split())
a, b = map(int, input().split())
vertices = []
for i in range(m):
    vertices.append(list(map(int, input().split())))

matrix = [[0] * n for _ in range(n)]
for vertice in vertices:
    matrix[vertice[0] - 1][vertice[1] - 1] = 1
    matrix[vertice[1] - 1][vertice[0] - 1] = 1

d = deque()
d.append(a-1)
dist = [-1] * n
dist[a-1] = 0
prev = [-1] * n

while d:
    # print('d', d)
    cur = d.popleft()
    for i, v in enumerate(matrix[cur]):
        # print('v', v, 'dist[v]', dist[v])
        if v == 1 and dist[i] == -1:
            dist[i] = dist[cur] + 1
            d.append(i)
            prev[i] = cur

# print(dist)
# print(prev)

print(dist[b-1])
if dist[b-1] != -1:
    prev_edge = b-1
    ans = []
    while prev_edge != -1:
        ans.append(prev_edge+1)
        prev_edge = prev[prev_edge]
    ans.reverse()
    print(' '.join(map(str, ans)))
