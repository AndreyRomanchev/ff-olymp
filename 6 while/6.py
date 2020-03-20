#!/usr/bin/env python3

x = int(input())

tmp1 = 1
tmp2 = 1
num = 2

while tmp2 <= x:
    if tmp2 == x:
        print(num)
        break
    tmp2 += tmp1
    tmp1 = tmp2 - tmp1
    num += 1
else:
    print("-1")
