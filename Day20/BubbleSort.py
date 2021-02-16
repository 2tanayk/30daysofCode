#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
l = len(a)
swaps = 0

for i in range(l):
    for j in range(l - 1):
        if a[j] > a[j + 1]:
            swaps += 1
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print(f"Array is sorted in {swaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
