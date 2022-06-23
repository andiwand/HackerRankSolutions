import sys

x = 80
xys = [list(map(float, line.split())) for line in sys.stdin]
xs = [xy[0] for xy in xys]
ys = [xy[1] for xy in xys]
n = len(xys)

mx = sum(xs)/n
my = sum(ys)/n

b = (n*sum(x*y for x,y in zip(xs,ys)) - sum(xs)*sum(ys)) / (n*sum(x**2 for x in xs) - sum(xs)**2)
a = my - b * mx

y = a + b * x
print('%.3f' % y)
