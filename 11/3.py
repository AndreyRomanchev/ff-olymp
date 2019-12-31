#!/usr/bin/env python3

# a = list(map(int, input().split()))
a = int(input())


def wrongfib(a: int):
    if a <= 2:
        return 1
    else:
        return wrongfib(a - 1) + wrongfib(a - 3)

print(wrongfib(a))