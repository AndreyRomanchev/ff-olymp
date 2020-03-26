#!/usr/bin/env python3


n = int(input())
students = []
for _ in range(n):
    name, cl = input().split()
    students.append([name, int(cl)])

for name, cl in sorted(students, key=lambda f: (f[1], f[0])):
    print(cl, name)
