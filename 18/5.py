#!/usr/bin/env python3


sizes = list(map(int, input().split()))
sizes.sort(reverse=True)
feet = list(map(int, input().split()))
feet.sort()

ans = 0
for i in feet:
    if i > sizes[0]:
        break
    for num, k in enumerate(sizes):
        if i > k:
            ans += 1
            sizes.pop(num-1)
            break

print(ans)