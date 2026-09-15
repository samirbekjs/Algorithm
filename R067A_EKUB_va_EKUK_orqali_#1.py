import math as m
a,b = map(int,input().split())
if m.gcd(a,b) == a:
  print(a,b)
else:
  print(-1)
