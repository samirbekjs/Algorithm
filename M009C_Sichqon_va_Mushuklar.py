a,b,c = map(int,input().split())
m2 = abs(b - c)
m1 = abs(c - a)
if m1 == m2:
  print("sichqon")
elif m2 < m1:
  print("2-mushuk")
else:
  print("1-mushuk")
