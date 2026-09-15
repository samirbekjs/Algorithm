n = int(input())
a = list(map(int,input().split()))
b = sum(a)
if b >= n:
  print("Yes")
else:
  print("No")
