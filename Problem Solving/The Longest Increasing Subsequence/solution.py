#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestIncreasingSubsequence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestIncreasingSubsequence2(arr):
    dp = [0]*len(arr)
    for i,a in enumerate(arr):
        dp[i] = 1 + max([0] + [dp[j] for j in range(len(arr)) if arr[j]<a])
    return max(dp)

def longestIncreasingSubsequence(arr):
    dp = [0]*len(arr)
    lis = 0
    for a in arr:
        l, r = 0, lis
        while l != r:
            m = l+(r-l)//2
            if dp[m] < a:
                l = m+1
            else:
                r = m
        lis = max(lis, l+1)
        dp[l] = a
    return lis

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = longestIncreasingSubsequence(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
