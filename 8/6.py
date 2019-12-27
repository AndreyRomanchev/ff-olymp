#!/usr/bin/env python3

a = map(int, input().split())

min = 10 ** 10

for i in a:
    if i > 0 and i < min:
        min = i
print(min)
