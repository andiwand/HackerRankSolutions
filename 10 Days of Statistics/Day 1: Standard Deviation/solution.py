#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    mean = sum(arr) / len(arr)
    std = (sum((a-mean)**2 for a in arr) / len(arr)) ** 0.5
    print('%.1f' % std)

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
