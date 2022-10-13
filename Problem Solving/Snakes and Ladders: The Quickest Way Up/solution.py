#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    portals = {i:j for i,j in (ladders+snakes)}
    
    current = [1]
    seen = set([1])
    depth = 1
    
    while current:
        next_current = set()
        for i in current:
            for j in range(i+1, min(i+7, 101)):
                if j in portals:
                    j = portals[j]
                if j == 100:
                    return depth
                if j not in seen:
                    next_current.add(j)
        current = list(next_current)
        seen.update(next_current)
        depth += 1
    
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
