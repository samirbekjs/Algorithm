import math
a, b = map(int, input().split())
d = math.gcd(a, b)
res = []
for n in range(1, int(d**0.5)+1):
  if d % n == 0:
    res.append(n)
    res.append( d// n )
print(len(set(res)))
