import math
s = 1
a = input()
b = a[5:]
f = set(b)
for i in f:
    g = b.count(i)
    s*=math.factorial(g)
print(5040//s)
