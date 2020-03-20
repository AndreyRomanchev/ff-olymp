#!/usr/bin/env python3


n = int(input())

count = 0
if n == 1:
    count = 1
else:
    d = 1
    while d * d <= n:
        if n % d == 0:
            if d * d == n:
                count += 1
            else:
                count += 2
        d += 1
print(count)
