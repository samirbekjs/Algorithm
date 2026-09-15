a = list(map(int,input().split()))
if (sum(a)- a[1]) - a[1] > 0:
  print((sum(a)-a[1]) - a[1])
else:
  print(-1)
