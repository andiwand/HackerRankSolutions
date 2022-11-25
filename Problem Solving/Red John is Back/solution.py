#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'redJohn' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def redJohn(n):
    def walls(n):
        elements = [{1:n-4*h, 4:h} for h in range(n//4+1)]
        return sum(math.factorial(e[1]+e[4])//(math.factorial(e[1])*math.factorial(e[4])) for e in elements)
    def primes(n):
        p = [False,False]+[True]*(n-1)
        for i in range(n):
            if not p[i]:
                continue
            for j in range(i*2,n+1,i):
                p[j] = False
        return sum(1 if i else 0 for i in p)
    return primes(walls(n))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
