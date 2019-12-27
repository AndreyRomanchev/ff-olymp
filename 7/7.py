#!/usr/bin/env python3

a = input()

sum = 0
num = ''

for l in a:
    if ord('0') <= ord(l) <= ord('9'):
        num += l
    else:
        if num:
            sum += int(num)
        num = ''
if num:
    sum += int(num)
print(sum)
