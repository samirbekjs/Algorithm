t,s,a,b = map(int,input().split())
a1 = ((2 * s) / t) ** (1 / 2)
a2 = (1 + (a * b) ** (1 / 2)) / (1+a)
au = a1 * a2
print('{:.4f}'.format(au))
