#!/usr/bin/env python3


m, n = list(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

left = -1
right = 10
# right = 25

while right > left + 1:
    # print('left =', left)
    # print('right =', right)
    med = (right + left) // 2
    # print('med =', med)
    total_ballons = 0
    ballons = []
    for t, z, y in arr:
        cycles = med // (t * z + y)
        leftover = med % (t * z + y)
        count_ballons = cycles * z + min(leftover // t, z)
        ballons.append(count_ballons)
        total_ballons += count_ballons
        # print('ballons', count_ballons)
    # print('total_ballons =', total_ballons)
    if total_ballons >= m:
        right = med
        ans_ballons = ballons[:]
    else:
        left = med

print(right)
# print(' '.join(map(str, ans_ballons)))
