#!/usr/bin/env python3

tmp = int(input())
sum = 0
while tmp // 10 != 0:
    if tmp % 10 == 0:
        sum += 1
    tmp = tmp // 10
print(sum)