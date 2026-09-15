n,m = map(int,input().split())
if n == m and n !=0 :
  print(n * 10,m * 10 + 1)
elif n == 9 and m == 1:
  print(9,10)
elif n == 0 and m == 1:
  print(0,1)
elif m - n == 1:
  print(n * 10 + 9,m * 10)
elif n == 0 and m == 0:
  print(-1)
else:
  print(-1)
