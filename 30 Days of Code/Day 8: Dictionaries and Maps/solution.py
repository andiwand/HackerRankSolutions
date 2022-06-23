import sys

n = int(input())

d = {i[0]:i[1] for i in [input().split() for _ in range(n)]}
ks = [line.rstrip() for line in sys.stdin]

for k in ks:
    if k in d:
        print(f'{k}={d[k]}')
    else:
        print('Not found')
