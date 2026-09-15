import math as m
a,b = map(int,input().split())
sin = m.sqrt(3) / 2
log = m.log(a,b)
y = (a ** 2) / (2 * b)
print('{:.2f}'.format(sin + log + y))
