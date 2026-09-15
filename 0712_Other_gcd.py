import math as m
a,b,c = map(int,input().split())
print((a ** m.gcd(b,c) - 1) % int(1e9 + 7))
