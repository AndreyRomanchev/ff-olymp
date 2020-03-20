#!/usr/bin/env python3

a = int(input())
A = [list(map(int, input().split())) for i in range(a)]

gena = 0
che = 0

for i in range(a):
    for j in range(a):
        if i == j:
            gena += A[i][j]
        if i + j + 1 == a:
            che += A[i][j]

if gena > che:
    print(1)
elif che > gena:
    print(2)
else:
    print(0)