a,b,c = map(int,input().split())
a1,b1,c1 = map(int,input().split())
a11 = a * 3600 + b * 60 + c
a12 = a1 * 3600 + b1 * 60 + c1
print(a12 - a11)
