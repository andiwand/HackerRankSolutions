#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    min_a = min(arr)
    arr = [a-min_a for a in arr]
    result = sum(a//5 for a in arr)
    arr = [a%5 for a in arr]
    occ = [sum(1 for a in arr if a==i) for i in range(5)]
    return result + min(
        occ[1] + occ[2] + 2*occ[3] + 2*occ[4],
        occ[0] + 2*occ[1] + 2*occ[2] + occ[3] + 2*occ[4],
        occ[0] + occ[1] + 2*occ[2] + 2*occ[3] + occ[4],
    )

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
