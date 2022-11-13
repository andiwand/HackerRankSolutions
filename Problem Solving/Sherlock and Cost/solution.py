#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    s1, s2 = 0, 0
    for i in range(1,len(B)):
        s1, s2 = max(s1, s2+B[i-1]-1), max(s1+B[i]-1,s2+abs(B[i-1]-B[i]))
    return max(s1, s2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
