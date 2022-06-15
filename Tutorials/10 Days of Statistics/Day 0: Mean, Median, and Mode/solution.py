import numpy as np
from scipy import stats

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = np.array([int(n) for n in input().split()])
print("%.1f" % np.mean(X))
print("%.1f" % np.median(X))
mode = stats.mode(X)
if len(mode) > 0:
    print(int(mode[0]))
