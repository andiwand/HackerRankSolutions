n = int(input())
xs = list(map(float, input().split()))
ys = list(map(float, input().split()))

mx = sum(xs)/n
sx = (sum((x-mx)**2 for x in xs)/n)**0.5
my = sum(ys)/n
sy = (sum((y-my)**2 for y in ys)/n)**0.5

c = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / (n * sx * sy)

print('%.3f' % c)
