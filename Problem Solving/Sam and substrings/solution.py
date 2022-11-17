#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    mod = 10**9+7
    result = 0
    left = 0
    for i,d in enumerate(n,1):
        left = (left*10 + i*int(d)) % mod
        result = (result+left) % mod
    return result   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
