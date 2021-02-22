#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

    nlist = []

    for N_itr in range(N):
        fNEI = input().strip()
        firstNameEmailID = fNEI.split()

        firstName = firstNameEmailID[0]

        if '@gmail.com' in fNEI:
            nlist.append(firstName)

    nlist.sort()
    for n in nlist:
        print(n)
