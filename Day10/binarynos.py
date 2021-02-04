#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

b = int(bin(n).replace("0b", ""))

ls = list(int(x) for x in str(b))

sl = []

hsum = 0
for i in ls:
    if i != 0:
        hsum += i
    else:
        sl.append(hsum)
        hsum = 0

sl.append(hsum)
print(max(sl))
