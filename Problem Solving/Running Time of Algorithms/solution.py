#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    return insertionSort2(len(arr), arr)

def insertionSort2(n, arr):
    r = 0
    for i in range(1, n):
        r += insertionSort1(i, arr)
    return r

def insertionSort1(n, arr):
    r = 0
    e = arr[n]
    i = n
    while i >= 1 and arr[i-1] > e:
        arr[i] = arr[i-1]
        i = i-1
        r += 1
    arr[i] = e
    return r
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
