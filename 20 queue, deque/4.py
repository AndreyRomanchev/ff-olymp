#!/usr/bin/env python3

from collections import deque


n = int(input())
actions = []
for _ in range(n):
    actions.append(input().strip())

d1 = deque()
d2 = deque()

for action in actions:
    if action[0] == '+':
        _, num = action.split()
        d2.append(num)
    elif action[0] == '*':
        _, num = action.split()
        d2.appendleft(num)
    elif action[0] == '-':
        print(d1.popleft())

    if len(d2) > len(d1):
        d1.append(d2.popleft())




