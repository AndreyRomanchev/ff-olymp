#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    x1, y1 = ar[i]
    if i == n-1:
        x2, y2 = ar[0]
    else:
        x2, y2 = ar[i+1]
    x_diff = abs(max(x1, x2) - min(x1, x2))
    y_diff = abs(max(y1, y2) - min(y1, y2))
    ans += gcd(x_diff, y_diff)

print(ans)

