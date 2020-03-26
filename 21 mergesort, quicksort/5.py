#!/usr/bin/env python3


n = int(input())
t = list(map(int, input().split()))
tasks = []
for i, task in enumerate(t):
    tasks.append([task, i+1])

tasks.sort(reverse=True)

total = 0
order = []
for i, t in enumerate(tasks):
    task, num = t
    total += task * (i+1)
    order.append(str(num))

print(total)
print(' '.join(order))
