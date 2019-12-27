#!/usr/bin/env python3

a = list(map(int, input().split()))

a = [x for x in a if x != 0] + [0] * a.count(0)

print(' '.join(map(str, a)))