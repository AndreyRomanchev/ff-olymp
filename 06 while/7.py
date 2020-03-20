#!/usr/bin/env python3

a = int(input())
b = int(input())
n = int(input())

for i in range(a, b + 1):
    sum = 0
    tmp = i
    while tmp // 10 != 0:
        num = tmp % 10
        sum += num
        tmp = tmp // 10
    sum += tmp
    if sum == n:
        print(i)

