#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())

price = a * 100 + b
given = c * 100 + d

if price > given:
    print("0 0")
else:
    diff = given - price
    print(diff // 100, diff % 100)