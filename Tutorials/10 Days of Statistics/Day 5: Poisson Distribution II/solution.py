import math

def poissonMoment2(l):
    return l**2+l

A = 0.88
B = 1.55

print('%.3f' % (160 + 40*poissonMoment2(A)))
print('%.3f' % (128 + 40*poissonMoment2(B)))
