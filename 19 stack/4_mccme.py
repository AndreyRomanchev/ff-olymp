#!/usr/bin/env python3


n = int(input())
wagons = list(map(int, input().split()))
wagons.reverse()

deadend = []
way2 = []

current_wagon = 1

have_turn = True
while have_turn:
    if deadend and deadend[-1] == current_wagon:
        way2.append(deadend.pop())
        current_wagon += 1
    elif wagons:
        deadend.append(wagons.pop())
    else:
        have_turn = False

if deadend:
    print("NO")
else:
    print("YES")
