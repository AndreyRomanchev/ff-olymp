#!/usr/bin/env python3


def bubblesort(array: list) -> list:
    l = len(array)
    for i in range(l-1):
        for j in range(l-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

s, n = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

array = bubblesort(array)

sum = 0
ans = 0
for i in array:
    if sum + i <= s:
        sum += i
        ans += 1
    else:
        break

print(ans)
