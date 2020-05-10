#!/usr/bin/env python3

import sys


S = int(input())
N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

total = (sum(n) + 1) * 2

if sum(n) < S:
    print('Impossible')
    sys.exit(0)

F = [0] * (total + 1)
F[0] = 1
Prev = [0] * (total + 1)

c = n + [-x for x in m]

for m in c:
    F_new = F[:]
    for s in range(m, sum(n)+1):
        if F[s - m] == 1 and Prev[s] == 0:
            F_new[s] = 1
            Prev[s] = m
    F = F_new

if F[S] == 0:
    print('Impossible')
else:
    Ans = []
    k = S
    while k > 0:
        if Prev[k] > 0:
            Ans.append('+' + str(Prev[k]))
        else:
            Ans.append(str(Prev[k]))
        k -= Prev[k]

    print(' '.join(Ans))
