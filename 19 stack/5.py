#!/usr/bin/env python3


balls = list(map(int, input().split()))

stack = []
i = 0

while i < len(balls):
    stack.append(balls[i])
    if len(stack) >= 3 and stack[-1] == stack[-2] == stack[-3]:
        delete = stack[-1]
        stack.pop()
        stack.pop()
        stack.pop()
        while i < len(balls) and balls[i] == delete:
            i += 1
    else:
        i += 1

print(len(balls) - len(stack))