#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
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
    return [int(r) for r in result]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
