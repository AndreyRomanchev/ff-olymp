#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


a = int(input())
b = int(input())
n = int(input())

if n % gcd(a, b) == 0 and n <= max(a, b):
    a_v = 0
    b_v = 0
    while a_v != n and b_v != n:
        if a_v == 0:
            a_v += a
            print('>A')
        elif b_v == b:
            b_v = 0
            print('B>')
        else:
            if a_v <= b - b_v:
                b_v += a_v
                a_v = 0
            else:
                a_v -= b - b_v
                b_v = b
            print('A>B')
else:
    print('Impossible')
