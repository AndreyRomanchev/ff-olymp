#!/usr/bin/env python3

n = int(input())
a = int(input())
b = int(input())

s = 0

for i in range(a + 1):
    for j in range(b, -1, -1):
        if i + j == n:
            s += 1
print(s)