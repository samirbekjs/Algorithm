import math
def ehtimollik(a, n):
    return n * (a**(n-1)) * ((1 - a))
a,n = map(float,input().split())
r = ehtimollik(a, n)
print('{:.4f}'.format(r))
