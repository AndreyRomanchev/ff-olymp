#!/usr/bin/env python3
import sys

braces = input()
braces_dict = {')': '(', '}': '{', ']': '['}

stack = []
for brace in braces:
    if brace in "{([":
        stack.append(brace)
    elif brace in braces_dict.keys():
        if len(stack) == 0:
            print('NO')
            sys.exit(0)
        elif stack.pop() != braces_dict[brace]:
            print('NO')
            sys.exit(0)

if len(stack) == 0:
    print("YES")
else:
    print("NO")
