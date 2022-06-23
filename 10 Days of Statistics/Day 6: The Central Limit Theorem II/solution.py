t = 250
b = 100
m = 2.4
s = 2.0

import math
from statistics import NormalDist

d = NormalDist(mu=m*b, sigma=s*math.sqrt(b))

print(f'%.4f' % d.cdf(t))
