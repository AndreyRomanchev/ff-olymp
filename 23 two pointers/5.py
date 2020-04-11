#!/usr/bin/env python3


def upper_bound(l: list, i: int) -> int:
    left = -1
    right = len(l)
    while right > left + 1:
        m = (left + right) // 2
        if l[m] > i:
            right = m
        else:
            left = m
    return left


n, m = list(map(int, input().split()))
n_arr = list(map(int, input().split()))

n_arr.sort()
ans = 0

for i, v in enumerate(n_arr):
    j = upper_bound(n_arr, v + m)
    print(i, j)
    ans += j - i

print(ans)
