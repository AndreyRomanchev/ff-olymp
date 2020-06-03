#!/usr/bin/env python3

import itertools


N = int(input())

for item in itertools.product(['0', '1'], repeat=N):
    count0 = 0
    count1 = 0
    flag = True
    for s in item:
        if s == '0':
            if count1 > 0:
                count1 = 0
            count0 += 1
            if count0 >= 3:
                flag = False
        else:
            if count0 > 0:
                count0 = 0
            count1 += 1
            if count1 >= 3:
                flag = False
    if flag:
        print(' '.join(item))
