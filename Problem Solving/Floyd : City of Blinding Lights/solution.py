#!/bin/python3

import math
import os
import random
import re
import sys


def floyd(road_nodes, road_edges, road_from, road_to, road_weight, x, y):
    road_from = [i-1 for i in road_from]
    road_to = [i-1 for i in road_to]
    x = [i-1 for i in x]
    y = [i-1 for i in y]
    
    inf = int(139651)

    dist = [[inf for j in range(road_nodes)] for i in range(road_nodes)]
    for i in range(road_nodes):
        dist[i][i] = 0
    for i,j,w in zip(road_from, road_to, road_weight):
        dist[i][j] = w

    for k in range(road_nodes):
        for i in range(road_nodes):
            for j in range(road_nodes):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return [dist[i][j] if dist[i][j] < inf else -1 for i,j in zip(x,y)]

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    q = int(input().strip())

    x = [0] * q
    y = [0] * q

    for i in range(q):
        x[i], y[i] = map(int, input().rstrip().split())

    z = floyd(road_nodes, road_edges, road_from, road_to, road_weight, x, y)
    print('\n'.join(str(i) for i in z))
