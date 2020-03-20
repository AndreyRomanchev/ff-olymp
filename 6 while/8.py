#!/usr/bin/env python3

a = int(input())

ans = ''
while a > 0:
    ans += str(a % 2)
    a //= 2
print(ans)
