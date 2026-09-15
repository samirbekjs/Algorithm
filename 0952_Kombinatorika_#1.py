n = int(input())
if n < 3:
  print(n)
else:
  x = n * (n - 1) * (n - 2)
  print(pow(x,1,1000000007))
