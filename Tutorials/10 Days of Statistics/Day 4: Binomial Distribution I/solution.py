import math

a, b = [float(s) for s in input().split(' ')]

n = 6

p = a / (a+b)

prop = sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(3,n+1))

print('%.3f' % prop)
