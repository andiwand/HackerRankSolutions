import numpy as np

m, n = [int(i) for i in input().split()]
data = [[float(d) for d in input().split()] for _ in range(n)]
q = int(input())
test = [[float(d) for d in input().split()] for _ in range(q)]

data = np.array(data)

A = np.hstack([np.ones([n, 1]), data[:,:-1]])
b = data[:,-1]
p, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

test = np.array(test)

X = np.hstack([np.ones([q, 1]), test])
Y = X @ p

print('\n'.join('%.2f' % y for y in Y))
