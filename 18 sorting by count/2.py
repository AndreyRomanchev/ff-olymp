#!/usr/bin/env python3


n = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(' '.join(map(str, arr)))