#!/usr/bin/env python3

a, b, c = map(int, input().split())

avg = (a + b + c) / 3
if avg != (a + b + c) // 3:
    print("IMPOSSIBLE")
else:
    ans = 0
    avg = int(avg)
    if a > avg:
        ans += a - avg
    if b > avg:
        ans += b - avg
    if c > avg:
        ans += c - avg
    print(ans)
