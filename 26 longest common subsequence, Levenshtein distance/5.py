#!/usr/bin/env python3


nstring = input()
mstring = input()
n = len(nstring)
m = len(mstring)


f = [[''] * (m + 1) for _ in range(n + 1)]
for i in range(0, n+1):
    for j in range(0, m+1):
        if i == 0:
            f[i][j] = ''
        if j == 0:
            f[i][j] = ''


for i in range(1, n+1):
    for j in range(1, m+1):
        ns = nstring[i-1]
        ms = mstring[j-1]
        if ns == ms and ns.isalpha():
            f[i][j] = f[i-1][j-1] + ns
        elif (ns.isalpha() or ns == '?') and (ms.isalpha() or ms == '?'):
            if ns.isalpha() and ms.isalpha():
                f[i][j] = '#' * 10
            elif ns.isalpha():
                f[i][j] = f[i - 1][j - 1] + ns
            elif ms.isalpha():
                f[i][j] = f[i - 1][j - 1] + ms
            else:
                # Both are '?', choose any symbol
                f[i][j] = f[i - 1][j - 1] + 'Z'
        elif ns == '*' and (ms.isalpha() or ms == '?'):
            if len(f[i - 1][j]) < len(f[i][j - 1]):
                if ms.isalpha():
                    f[i][j] = f[i - 1][j] + ms
                else:
                    f[i][j] = f[i - 1][j] + 'Z'
            else:
                if ms.isalpha():
                    f[i][j] = f[i][j-1] + ms
                else:
                    print(3)
                    print(ns, ms)
                    f[i][j] = f[i][j-1] + 'Z'
        elif ms == '*' and (ns.isalpha() or ns == '?'):
            if len(f[i - 1][j]) < len(f[i][j - 1]):
                if ns.isalpha():
                    f[i][j] = f[i - 1][j] + ns
                else:
                    f[i][j] = f[i - 1][j] + 'Z'
            else:
                if ns.isalpha():
                    f[i][j] = f[i][j-1] + ns
                else:
                    f[i][j] = f[i][j-1] + 'Z'
        elif ns == '*' and ms == '*':
            if len(f[i - 1][j]) < len(f[i][j - 1]):
                f[i][j] = f[i - 1][j]
            else:
                f[i][j] = f[i][j - 1]
        else:
            # Two different symbols
            f[i][j] = '#' * 100
    for i in range(0, n + 1):
        print(f[i])
    print()

#for i in range(0, n+1):
#    print(f[i])

if '#' in f[n][m]:
    print('No solution!')
else:
    print(f[n][m])
