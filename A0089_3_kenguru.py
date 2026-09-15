a,b,c = map(int,input().split())
b1 = b - a - 1
b2 = c - b - 1
if b1 > b2:
  print(b1)
else:
  print(b2)
