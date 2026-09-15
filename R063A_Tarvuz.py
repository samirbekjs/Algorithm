n,a,b = map(int,input().split())
m = (n / 100) * (100 - a)
c = 100 - b
d = (m * 100) / c
print('{:.5f}'.format(d))
