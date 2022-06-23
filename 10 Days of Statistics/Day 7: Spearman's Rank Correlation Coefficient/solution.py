n = int(input())
xs = list(map(float, input().split()))
ys = list(map(float, input().split()))

xs_argsort = sorted(range(n), key=lambda i: xs[i])
ys_argsort = sorted(range(n), key=lambda i: ys[i])

rxs = [0]*n
for i, a in enumerate(xs_argsort): rxs[a]=i
rys = [0]*n
for i, a in enumerate(ys_argsort): rys[a]=i

c = 1 - 6 * sum((rx-ry)**2 for rx,ry in zip(rxs,rys)) / (n*(n**2-1))

print('%.3f' % c)
