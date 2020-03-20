#!/usr/bin/env python3

from collections import deque


def print_time(t: int) -> None:
    h = t // 60
    m = t % 60
    print(h, m)

n = int(input())
queue = []
for _ in range(n):
    queue.append(input().strip())

d = deque()
exit_queue = []

for client in queue:
    h, m, w = map(int, client.split())
    time = h*60 + m
    while d and time - d[0] >= 0:
        d.popleft()
    if not d:
        d.append(time + 20)
        exit_queue.append(time + 20)
        continue
    if w < len(d):
        exit_queue.append(time)
    else:
        d.append(d[-1] + 20)
        exit_queue.append(d[-1])

for client in exit_queue:
    print_time(client)