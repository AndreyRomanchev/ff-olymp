#!/usr/bin/env python3

from sys import setrecursionlimit

setrecursionlimit(100010)

n = int(input())

A = [1,]
for i in range(n):
    A.append(list(map(int, input().strip().split())))

produced = [0] * 100001

def produce(a: int):
    for i in A[a]:
        if A[i] != 1:
            produce(i)
    produced[a] = 1

produce(1)

print(produced.count(1))
