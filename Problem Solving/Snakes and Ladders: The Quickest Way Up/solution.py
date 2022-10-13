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
    inf = 100
    
    dead = set([i for i,_ in ladders] + [i for i,_ in snakes])
    
    nodes = [i for i in range(1,101)]
    edges = []
    
    for i in range(1,101):
        if i in dead:
            continue
        for d in range(1,7):
            j = i+d
            if j > 100:
                break
            edges.append((i,j,1))
    
    for i,j in ladders:
        edges.append((i,j,0))
    for i,j in snakes:
        edges.append((i,j,0))
    
    sol = floyd(nodes,edges, inf)
    return sol[1][100] if sol[1][100] != inf else -1

def floyd(nodes, edges, inf):
    dist = {i:{j:inf for j in nodes} for i in nodes}
    for i in nodes:
        dist[i][i] = 0
    for i,j,w in edges:
        dist[i][j] = w
    
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

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
