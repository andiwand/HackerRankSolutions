#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def abbreviation(a, b):
    def abbr(a, b, mem):
        if (a, b) in mem:
            return mem[(a, b)]
        if len(a) < len(b):
            result = False
        elif not b:
            result = a.lower() == a
        elif a[0].isupper():
            if a[0] != b[0]:
                result = False
            else:
                result = abbr(a[1:], b[1:], mem)
        elif a[0].upper() != b[0]:
            result = abbr(a[1:], b, mem)
        else:
            result = abbr(a[1:], b, mem) or abbr(a[1:], b[1:], mem)
        mem[(a, b)] = result
        return result
    sys.setrecursionlimit(10000)
    return 'YES' if abbr(a, b, {}) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
