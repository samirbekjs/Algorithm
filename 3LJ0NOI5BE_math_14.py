a,b,c = map(int,input().split())
d = (b ** 2 - 4 * a * c) ** (0.5)
y = (d - b) / (2 * a)
print('{:.3f}'.format(y))
