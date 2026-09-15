n = input()
l = len(n)
if l % 2 == 0:
  print("NO")
else:
  s = 0
  for i in n:
    i = int(i)
    if i % 2 == 0:
      print("NO")
  else:
    print("YES")
