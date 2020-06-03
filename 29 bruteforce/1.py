#!/usr/bin/env python3

import itertools


N = int(input())

for item in itertools.product(['0', '1'], repeat=N):
    print(''.join(item))
