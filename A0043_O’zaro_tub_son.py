import math
n=int(input())
for i in range(n-2,0,-1):
  if math.gcd(n,i)==1:
    print(i)
    break
