a,b,c,x = map(int,input().split())
y = a * x ** 2 + b * x + c
if y == 0:
  print("YES")
else:
  print("NO")
