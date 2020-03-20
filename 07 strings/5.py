#!/usr/bin/env python3

a = input()

sum = 0

for i in a:
    if i.isdigit():
        sum += 1
print(sum)