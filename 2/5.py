#!/usr/bin/env python3

n = int(input())

n = n % (24 * 60)

hour = n // 60
minute = n % 60

print(hour, minute)
