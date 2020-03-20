#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

xleft = max(x1, x3)
xright = min(x2, x4)
ydown = max(y1, y3)
yup = min(y2, y4)

if xleft > xright or ydown > yup:
    print("0")
else:
    print((xright - xleft) * (yup - ydown))