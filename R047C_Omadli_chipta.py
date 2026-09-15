a = int(input())
l = len(str(a))
if l == 6:
  a1 = a // 100000
  a2 = (a // 10000) % 10
  a3 = (a // 1000) % 10
  a4 = (a // 100) % 10
  a5 = (a // 10) % 10
  a6 = a % 10
  if a1 + a2 + a3 == a4 + a5 + a6:
    print("YES")
  else:
    print("NO")
else: 
  print("NO")
