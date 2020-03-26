#!/usr/bin/env python3


n = int(input())
fractions = []
for _ in range(n):
    f = input()
    a, b = map(int, f.split('/'))
    fractions.append([a/b, a, b])

for fraction, a, b in sorted(fractions):
    print('%s/%s' % (a, b))
