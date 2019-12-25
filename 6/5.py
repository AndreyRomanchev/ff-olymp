#!/usr/bin/env python3
from typing import Any, Union

x = int(input())
y = int(input())

day = 1
while x <= y:
    day += 1
    x *= 1.1
print(day)
