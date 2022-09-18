#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    connected = [set([i]) for i in range(n)]
    for a,b in astronaut:
        u = connected[a].union(connected[b])
        for i in u:
            connected[i] = u
    countries = frozenset(frozenset(c) for c in connected)
    countries = [len(c) for c in countries]
    
    subsums = []
    s = 0
    for c in countries[::-1]:
        subsums.append(s)
        s += c
    subsums = subsums[::-1]
    
    result = 0
    for i in range(len(countries)):
        result += countries[i] * subsums[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
