n = int(input())
a = list(map(int,input().split()))
k = int(input())
a.sort()
if len(a) == n:
  print(a[k-1])
