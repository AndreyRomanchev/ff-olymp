#!/usr/bin/env python3

a = 0

def f(n):
    global a
    a += 1
    print(a)
    if n < 0:
        return 1
    return n + f(n - 2)
f(50)