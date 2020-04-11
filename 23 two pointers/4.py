#!/usr/bin/env python3


n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_index = 0
m_index = 0
min_diff = min_n = min_m = float('inf')

while n_index < len(n_arr) and m_index < len(m_arr):
    if abs(n_arr[n_index] - m_arr[m_index]) < min_diff:
        min_diff = abs(n_arr[n_index] - m_arr[m_index])
        min_n = n_arr[n_index]
        min_m = m_arr[m_index]
    if n_arr[n_index] < m_arr[m_index]:
        n_index += 1
    else:
        m_index += 1

print(min_n, min_m)