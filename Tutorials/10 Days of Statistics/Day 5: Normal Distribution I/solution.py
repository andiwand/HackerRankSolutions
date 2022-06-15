from statistics import NormalDist

m = 20
s = 2

a = 19.5
b = [20, 22]

dist = NormalDist(mu=m, sigma=s)

print('%.3f' % dist.cdf(a))
print('%.3f' % (dist.cdf(b[1]) - dist.cdf(b[0])))
