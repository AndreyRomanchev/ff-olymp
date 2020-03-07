#!/usr/bin/env python3


n = int(input())
wagons = list(map(int, input().split()))

deadend = []
way2 = []

current_wagon = 1


for wagon in wagons:
    if wagon == current_wagon:
        way2.append(wagon)
        current_wagon += 1
        print(way2, deadend)
    else:
        deadend.append(wagon)
        print(way2, deadend)
    while deadend[-1] == current_wagon:
        way2.append(deadend.pop())
        current_wagon += 1
        print(way2, deadend)
        if not deadend:
            break

if deadend:
    print("NO")
else:
    print("YES")