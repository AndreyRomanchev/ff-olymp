#!/usr/bin/env python3


n = input()
stack = []

for s in n:
    if not stack or stack[-1] != s:
        stack.append(s)
    else:
        stack.pop()

print(''.join(stack))
