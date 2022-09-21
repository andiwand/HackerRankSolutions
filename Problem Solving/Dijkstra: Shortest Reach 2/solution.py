#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

def shortestReach(N, edges, s):
    maxdist = 100000

    edges = [(a-1,b-1,r) for a,b,r in edges]
    s -= 1

    connections = [{} for _ in range(N)]
    for a,b,r in edges:
        if b not in connections[a] or r < connections[a][b]:
            connections[a][b] = r
            connections[b][a] = r

    result = [maxdist for _ in range(N)]
    result[s] = 0

    missing = set(n for n in range(N))
    while missing:
        n = min(missing, key=result.__getitem__)
        missing.remove(n)

        for nn,nd in connections[n].items():
            if nn not in missing:
                continue
            alt = result[n]+nd
            if alt < result[nn]:
                result[nn] = alt

    return [r if r!=maxdist else -1 for i,r in enumerate(result) if i!=s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        # stupid performance hack
        hack = set()
        for _ in range(m):
            i = input().rstrip()
            if i not in hack:
                edges.append(list(map(int, i.split())))
                hack.add(i)

        s = int(input().strip())

        result = shortestReach(n, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
