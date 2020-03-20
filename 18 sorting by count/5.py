#!/usr/bin/env python3


sizes = sorted(list(map(int,input().split())))
feet = sorted(list(map(int,input().split())))

ans = 0
for i in feet:
    for k in sizes:
        if i <= k:
            ans += 1
            sizes.remove(k)
            break

print(ans)