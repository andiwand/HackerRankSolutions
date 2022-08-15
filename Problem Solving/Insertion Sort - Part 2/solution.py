#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        insertionSort1(i, arr)
        print(' '.join(str(a) for a in arr))

def insertionSort1(n, arr):
    e = arr[n]
    i = n
    while i >= 1 and arr[i-1] > e:
        arr[i] = arr[i-1]
        i = i-1
    arr[i] = e
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
