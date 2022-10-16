#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_element, current_sum, best_sum, positive_sum = -1e4, 0, 0, 0
    for a in arr:
        max_element = max(max_element, a)
        current_sum = max(0, current_sum + a)
        best_sum = max(best_sum, current_sum)
        positive_sum += max(0, a)
    
    if max_element < 0:
        return max_element, max_element
    return best_sum, positive_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
