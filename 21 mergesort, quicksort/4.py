#!/usr/bin/env python3


n = int(input())
prices = list(map(int, input().split()))

prices.sort(reverse=True)
ans = 0
for i, price in enumerate(prices):
    if (i+1) % 3 != 0:
        ans += price

print(ans)
