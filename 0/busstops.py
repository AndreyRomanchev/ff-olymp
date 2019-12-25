#!/usr/bin/env python3

#a1 = int(input())
#a2 = int(input())
#b1 = int(input())
#b2 = int(input())

a1 = -1
a2 = 5
b1 = 3
b2 = 5

if a1 <= a2:
    a = range(a1, a2 + 1)
else:
    a = range(a2, a1 + 1)
if b1 <= b2:
    b = range(b1, b2 + 1)
else:
    b = range(b2, b1 + 1)

c = []

for item in a:
    if item in b:
        c.append(item)

print(len(c))