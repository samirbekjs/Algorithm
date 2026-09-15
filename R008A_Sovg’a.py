a = list(map(int,input().split()))
n = int(input())
a1 = sum(a)
if a1 >= n:
  print(0)
else:
  print(n - a1)
