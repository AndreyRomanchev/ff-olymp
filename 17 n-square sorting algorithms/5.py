#!/usr/bin/env python3


def bubblesort(array: list) -> list:
    l = len(array)
    for i in range(l-1):
        for j in range(l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

s = int(input())
sizes = list(map(int, input().split()))

sizes = bubblesort(sizes)

ans = 0
min_size = s
for size in sizes:
    if size >= min_size:
        ans += 1
        min_size = size + 3

print(ans)
