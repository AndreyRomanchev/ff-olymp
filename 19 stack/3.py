#!/usr/bin/env python3
import sys

polish = input().split()

ops = {"+": (lambda x, y: x+y),
       "-": (lambda x, y: x-y),
       "*": (lambda x, y: x*y)}

stack = []
for item in polish:
    if item.isdigit():
        stack.append(int(item))
    else:
        first = stack.pop()
        second = stack.pop()
        stack.append(ops[item](second, first))

print(stack[0])
