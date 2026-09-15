import math as m

a,b = map(int,input().split())
c = abs(b - a)
print(m.ceil(c / 10))
