#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    arr = list(map(lambda e: [int(e[0]),e[1]], arr))

    m = len(arr)//2
    arr = list(map(lambda e: [e[0],'-'], arr[:m])) + arr[m:]

    tmp = [[] for _ in range(100)]
    for x,s in arr:
        tmp[x].append(s)

    result = []
    for t in tmp:
        result.extend(t)

    print(' '.join(result))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
