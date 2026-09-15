n,m = map(int,input().split())
x = []
ox = n % 10
for i in str(n):
  x.append(int(i))
if m in x:
  print("Yes")
else:
  if ox > m:
    print(ox - m)
  else:
    print(10 - m + ox)
