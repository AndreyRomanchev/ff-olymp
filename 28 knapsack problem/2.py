#!/usr/bin/env python3

N = int(input())
notes = list(map(int, input().split()))
S = int(input())

F = [float('inf')] * (S + 1)
F[0] = 0

for i in range(1, S + 1):
    for j in notes:
        if i - j >= 0 and F[i] > F[i - j]:
            F[i] = F[i - j] + 1

# print(F)

if F[S] == float('inf'):
    print('No solution')
else:
    Ans = []
    k = S
    while k != 0:
        for i in notes:
            if k - i >= 0 and F[k] == F[k - i] + 1:
                Ans.append(str(i))
                k -= i

    print(' '.join(Ans))