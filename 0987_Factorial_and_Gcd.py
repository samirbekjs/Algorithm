import math as m

a,b = map(int,input().split())
if a < b:
  print(m.factorial(a))
else:
  print(m.factorial(b))
