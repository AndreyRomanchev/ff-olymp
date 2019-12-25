#!/usr/bin/env python3

n = int(input())
a = int(input())
b = int(input())

if a + b < n:
    print("0")
else:
    print(min(a, b) + 1)
