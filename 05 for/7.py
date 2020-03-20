#!/usr/bin/env python3

a = int(input())
b = int(input())

a = (a + 1) // 2 * 2
for i in range(a, b + 1, 2):
    print(i, end=" ")
