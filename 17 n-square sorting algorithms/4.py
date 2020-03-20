#!/usr/bin/env python3


def bubblesort(array: list) -> list:
    l = len(array)
    for i in range(l-1):
        for j in range(l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

distances = bubblesort(distances)
prices = bubblesort(prices)

ans = 0
l = len(distances)
for i in range(l):
    ans += distances[i] * prices[l-i-1]

print(ans)
