w = 9800
b = 49
m = 205
s = 15

import math
from statistics import NormalDist

d = NormalDist(mu=m*b, sigma=s*math.sqrt(b))

print(f'%.4f' % d.cdf(w))
