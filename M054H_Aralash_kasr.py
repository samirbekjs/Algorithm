from math import *
def sh(a,b):
  while(b!=0):
    t=a%b
    a=b;b=t
  return a
def lcm(a,b):
  return a*b//gcd(a,b)
a,b = map(int,input().split())
opa = '+'
opb = '+'
if(a<0):opa = '-'
if(b<0):opb = '-'
if(a<0 and b<0):
  a=abs(a)
  b=abs(b)
if a == 0:
  print(0)
elif b == 0:
  print('INF')
else:
  x=sh(abs(a),abs(b))
  a = a // x
  b = b // x
  z = a // b
  a = a - b*z
  if(b<0):opb='-'
  if(a<0):opa='-'
  if(opa == opb):
      a=abs(a)
      b=abs(b)
  if(z!=0):
    if(a == 0):print(z)
    else:print(str(z)+'+'+str(a)+'/'+str(b))
  else:print(a,b,sep='/')
