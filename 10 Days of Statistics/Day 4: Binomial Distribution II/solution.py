import math

p = 12/100
n = 10

prop1 = sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(0,3))
prop2 = sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(2,n+1))

print('%.3f' % prop1)
print('%.3f' % prop2)
