#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    cand = [0]*n
    for i, s in sorted(enumerate(arr), key=lambda x: x[1]):
        c1 = cand[i-1] if i>0 and s>arr[i-1] else 0
        c2 = cand[i+1] if i<n-1 and s>arr[i+1] else 0
        cand[i] = 1+max(c1, c2)
    return sum(cand)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
