for i in range(int(input())):
  k,q,n = map(int,input().split())
  s = q
  for i in range(n):
    s = (s + k) * 2
  print(s)
