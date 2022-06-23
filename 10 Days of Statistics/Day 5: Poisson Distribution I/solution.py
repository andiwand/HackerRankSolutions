import math

m = 2.5
x = 5

def p(k, l):
    return (l**k * math.exp(-l)) / math.factorial(k)

print('%.3f' % p(x, m))
