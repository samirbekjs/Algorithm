m,n = map(int,input().split())
a = n * (n - 1) * m * ( m - 1) // 4
if a >= 2 and m >= 2:
  print(pow(a,1,1000000007))
else:
  print(0)
