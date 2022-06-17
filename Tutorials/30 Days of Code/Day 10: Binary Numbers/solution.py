#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict



if __name__ == '__main__':
    n = int(input().strip())
    
    b = '{0:b}'.format(n)
    r = max(len(s) for s in b.split('0'))
    print(r)
