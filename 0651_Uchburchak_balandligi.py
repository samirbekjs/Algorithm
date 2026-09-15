a,b,c = map(int,input().split())
l = max(a,b,c)
p = (a + b + c) / 2
s = (p*(p-a)*(p-b)*(p-c)) ** (0.5)
print('{:.10f}'.format((2 * s) / l))
