#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    edges = [(a-1,b-1) for a,b in edges]
    s -= 1

    connections = [set() for _ in range(n)]
    for a,b in edges:
        connections[a].add(b)
        connections[b].add(a)

    result = [-1 for _ in range(n)]
    active = set([(s,0)])
    while active:
        new_active = set()
        for a,u in active:
            if result[a] != -1:
                continue
            result[a] = u
            new_active.update((c,u+6) for c in connections[a])
        active = new_active

    return [r for i,r in enumerate(result) if i!=s]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
