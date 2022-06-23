#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def median(arr):
    arr.sort()
    mid = len(arr)//2
    if len(arr) % 2 == 0:
        return (arr[mid-1]+arr[mid])/2
    return sorted(arr)[mid]

def quartiles(arr):
    arr.sort()
    mid = len(arr)//2
    if len(arr) % 2 == 0:
        result = median(arr[:mid]), median(arr), median(arr[mid:])
    else:
        result = median(arr[:mid]), median(arr), median(arr[mid+1:])
    return result

def interQuartile(values, freqs):
    arr = []
    for v, f in zip(values, freqs):
        arr.extend([v]*f)
    q = quartiles(arr)
    iqr = q[2] - q[0]
    print('%.1f' % iqr)

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
