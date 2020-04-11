#!/usr/bin/env python3


w, h, n = list(map(int, input().split()))

left = 0
right = n * max(w, h)

while right > left + 1:
    m = (right + left) // 2
    if (m // w) * (m // h) >= n:
        right = m
    else:
        left = m

print(right)
