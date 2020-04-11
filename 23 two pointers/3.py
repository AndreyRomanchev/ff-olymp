#!/usr/bin/env python3


n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_index = 0
m_index = 0

while n_index < len(n_arr) and m_index < len(m_arr):
    if abs(n_arr[n_index] - m_arr[m_index]) == 1:
        print('YES')
        break
    if n_arr[n_index] < m_arr[m_index]:
        n_index += 1
    else:
        m_index += 1
else:
    print('NO')