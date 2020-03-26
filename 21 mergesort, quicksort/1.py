#!/usr/bin/env python3


def f(i: int) -> int:
    ans = 0
    for s in str(i)[1:-1]:
        ans += int(s)
    return ans

print(list(sorted(range(100,10001), key = f))[2018])