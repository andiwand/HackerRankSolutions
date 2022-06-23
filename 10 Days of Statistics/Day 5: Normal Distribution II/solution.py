from statistics import NormalDist

m = 70
s = 10

a = 80
b = 60

dist = NormalDist(mu=m, sigma=s)

print('%.2f' % (100*(1-dist.cdf(a))))
print('%.2f' % (100*(1-dist.cdf(b))))
print('%.2f' % (100*dist.cdf(b)))
