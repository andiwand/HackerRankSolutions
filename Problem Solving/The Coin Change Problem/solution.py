#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    if not c:
        return 0
    def solve(n, c, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if (n,len(c)) in memo:
            return memo[(n,len(c))]
        result = 0
        for i in c:
            result += solve(n-i, [j for j in c if j >= i], memo)
        memo[(n,len(c))] = result
        return result
    return solve(n, c, {})

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
