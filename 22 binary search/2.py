#!/usr/bin/env python3


def upper_bound(l: list, i: int) -> int:
    left = -1
    right = len(l)
    while right > left + 1:
        m = (left + right) // 2
        if l[m] > i:
            right = m
        else:
            left = m
    return left


def lower_bound(l: list, i: int) -> int:
    left = -1
    right = len(l)
    while right > left + 1:
        m = (left + right) // 2
        if l[m] >= i:
            right = m
        else:
            left = m
    return right


sorted_list = list(map(int, input().split()))
unsorted_list = list(map(int, input().split()))

for num in unsorted_list:
    if num in sorted_list:
        print(lower_bound(sorted_list, num), upper_bound(sorted_list, num))
    else:
        print('-1')