#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    edges = [(a-1,b-1,r) for a,b,r in edges]
    start -= 1

    connections = [{} for _ in range(n)]
    for a,b,r in edges:
        connections[a][b] = r
        connections[b][a] = r

    result = 0
    collected = set([start])
    while len(collected) < n:
        active = [(a,b,r) for a in collected for b,r in connections[a].items()]
        min_active = min(active, key=lambda e: e[2])

        collected.add(min_active[1])
        result += min_active[2]

        for a,b,_ in active:
            if min_active[1] == b:
                del connections[a][b]
                del connections[b][a]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
