#!/usr/bin/env python3


array = list(map(int, input().split()))

l = len(array)

ans = 0
for i in range(l - 1):
    for j in range(l - i - 1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            ans += 1

print(ans)
