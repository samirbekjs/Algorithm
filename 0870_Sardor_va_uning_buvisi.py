a,b = map(int,input().split())
x = a - 2 * b
if x >= 0:
  print(x)
elif x < 0:
  print(-1)
