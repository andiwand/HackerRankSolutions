#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'longestCommonSubsequence' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def longestCommonSubsequence(a, b):
    dp = [[[] for _ in range(len(b))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else []) + [a[i]]
            else:
                dp[i][j] = max([dp[i-1][j] if i > 0 else [], dp[i][j-1] if j > 0 else []], key=len)
    return dp[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = longestCommonSubsequence(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
