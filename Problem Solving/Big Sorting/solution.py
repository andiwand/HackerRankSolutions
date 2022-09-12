#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    def compare(item1, item2):
        d = len(item1) - len(item2)
        if d == 0:
            return int(item1) - int(item2)
        return d
    
    return sorted(unsorted, key=functools.cmp_to_key(compare))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
