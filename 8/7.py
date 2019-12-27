#!/usr/bin/env python3

a = list(map(int, input().split()))
b = int(input())

for i, n in enumerate(a):
    if n >= b:
        continue
    else:
        a.insert(i, b)
        print(i + 1)
        break
else:
    print(i + 2)
