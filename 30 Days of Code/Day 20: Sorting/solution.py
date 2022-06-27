#!/bin/python3

import math
import os
import random
import re
import sys


def bubbleSort(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                swaps += 1
    return swaps


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    s = bubbleSort(a)
    print(f'Array is sorted in {s} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
