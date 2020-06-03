#!/usr/bin/env python3

import itertools


N, K = map(int, input().split())

for item in itertools.product(range(K), repeat=N):
    print(' '.join(map(str, item)))

