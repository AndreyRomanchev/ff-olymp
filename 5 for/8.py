#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

ans = 0
for x in range(0, 1001):
    if x == e:
        continue
    if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
       ans += 1
print(ans)
