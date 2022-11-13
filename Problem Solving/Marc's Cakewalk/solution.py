#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#

def marcsCakewalk(calorie):
    calorie.sort()
    calorie=calorie[::-1]
    return sum(2**i*c for i,c in enumerate(calorie))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
