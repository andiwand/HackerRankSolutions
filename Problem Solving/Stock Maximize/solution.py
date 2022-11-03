#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    max_prices = []
    current_max = prices[-1]
    for p in prices[::-1][1:]:
        max_prices = [current_max] + max_prices
        current_max = max(current_max, p)

    result = 0
    for i in range(len(prices)-1):
        now = prices[i]
        result += max(0, max_prices[i]-now)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
