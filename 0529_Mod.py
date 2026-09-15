a,c,k = map(int,input().split())
s = a // c
if a % c >= k :
  print(s + 1)
elif c == 1 :
  print(0)
elif c <= k :
  print(0)
else:
  print(s)
