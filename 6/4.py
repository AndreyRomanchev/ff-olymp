#!/usr/bin/env python3

tmp = int(input())
min = 10
max = 0
while tmp // 10 != 0:
    num = tmp % 10
    if num < min:
        min = num
    if num > max:
        max = num
    tmp = tmp // 10
if tmp < min:
    min = tmp
if tmp > max:
    max = tmp
print(min, max)
