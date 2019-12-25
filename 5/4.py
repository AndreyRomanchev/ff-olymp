#!/usr/bin/env python3

a = int(input())

for i in range(100, 999):
    sum = int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
    if sum == a:
        print(i)