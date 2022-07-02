import math

m = 2 * 1e9
mp = int(math.sqrt(m))
ps = set(range(2, mp+1))
for i in range(2, mp+1):
    ps.difference_update(i*mult for mult in range(2, int(mp/i)+1))
ps = sorted(list(ps))

T = int(input())
ns = [int(input()) for _ in range(T)]

for n in ns:
    d = any(n % p == 0 for p in ps if p < n)
    if n == 1:
        d = True
    if d:
        print('Not prime')
    else:
        print('Prime')
