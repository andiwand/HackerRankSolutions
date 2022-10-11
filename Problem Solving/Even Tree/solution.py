#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    t_from = [i-1 for i in t_from]
    t_to = [i-1 for i in t_to]
    
    children = {i:{} for i in range(t_nodes)}
    for i,j in zip(t_from, t_to):
        children[j][i] = True
    
    def count_nodes(i, count):
        result = 1
        for j in children[i].keys():
            result += count_nodes(j, count)
        count[i] = result
        return result
    count = {}
    count_nodes(0, count)
    
    def count_result(i):
        result = 0
        for j in children[i].keys():
            if count[j] % 2 == 0:
                result += 1
            result += count_result(j)
        return result
    
    return count_result(0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
