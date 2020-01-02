#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())

A = [1,]
for i in range(n):
    A.append(list(map(int, input().strip().split())))

ans = set()

def get_item(a: int):
    ans.add(a)
    if A[a]:
        for i in A[a]:
            get_item(i)

get_item(1)

print(len(ans))
