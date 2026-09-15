x1,y1,x2,y2 = map(int,input().split())
x = max(abs(x1 - x2),abs(y2 - y1)) * 0.5
if x%1==0:
  print(int(x))
else:
  print(x)
