#!/usr/bin/env python3

#a = list(map(int, input().split()))
a = int(input())

ans = []

for i in range(a):
    ans.append([])
    for j in range(a):
        if i + j + 1 == a:
            ans[i].append(1)
        elif i + j + 1 > a:
            ans[i].append(2)
        else:
            ans[i].append(0)

for i in ans:
    print(' '.join(map(str, i)))