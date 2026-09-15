import math as m

e = m.e
a,b,x = map(int,input().split())
x1 = (x + a * b ** (1/2)) ** ((3 * x) / (4 * x + a * b))
x2 = abs((3 * a - 4 * b) / (2 * a - 3 * b - 4))
x3 = e ** (a / b)
print('{:.2f}'.format(x1 + x2 + x3))
