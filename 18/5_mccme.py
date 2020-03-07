#!/usr/bin/env python3


skates = sorted(list(map(int,input().split())))
visitors = sorted(list(map(int,input().split())))
res = 0
while True:
    try:
        skates = list(filter(lambda x : x>= min(visitors), skates))
        skates.pop(0)
        visitors.pop(0)
        res += 1
    except:
        break
print(res)