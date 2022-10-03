#!/bin/python3

import math
import os
import random
import re
import sys
import functools

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def kruskals(g_nodes, g_from, g_to, g_weight):
    n = g_nodes
    edges = [(a-1,b-1,r) for a,b,r in zip(g_from, g_to, g_weight)]

    connections = [{} for _ in range(n)]
    for a,b,r in edges:
        connections[a][b] = r
        connections[b][a] = r

    def compare(a,b):
        if a[2] == b[2]:
            return sum(a)-sum(b)
        return a[2]-b[2]

    result = 0
    collected = set([0])
    while len(collected) < n:
        active = [(a,b,r) for a in collected for b,r in connections[a].items()]
        min_active = min(active, key=functools.cmp_to_key(compare))

        collected.add(min_active[1])
        result += min_active[2]

        for a,b,_ in active:
            if min_active[1] == b:
                del connections[a][b]
                del connections[b][a]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + '\n')

    fptr.close()
