n = int(input()) + 1
if n % 4 != 0 :
  print(-1)
else:
  print(int(((n + 3)**0.5 - 1)//4))
