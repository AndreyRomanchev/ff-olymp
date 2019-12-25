#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == b == 0:
    print("INF")
elif a == 0 and b != 0:
    print("NO")
elif a != 0:
    if b % a == 0:
        x = -b // a
        if c * x + d == 0:
            print("NO")
        else:
            print(x)
    else:
        print("NO")