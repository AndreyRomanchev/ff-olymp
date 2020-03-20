#!/usr/bin/env python3


def bubblesort(array: list) -> list:
    l = len(array)
    for i in range(l-1):
        for j in range(l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = list(map(int, input().split()))

array = bubblesort(array)
print(array[len(array) // 2])
