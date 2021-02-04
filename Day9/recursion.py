#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the factorial function below.
def factorial(n):
    if (n == 1):
        return 1
    else:
        return n * factorial(n - 1)
