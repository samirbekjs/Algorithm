x1,v1,x2,v2 = map(int,input().split())
if x1 > x2:
  if v2 > v1:
    if (x1 - x2) % (v2 - v1) == 0:
      print("YES")
    else:
      print("NO")
  else: 
    print("NO")
elif x1 < x2:
    if v1 > v2:
      if (x2 - x1) % (v1 - v2) == 0:
        print("YES")
      else:
        print("NO")
    else: 
      print("NO")
else: 
  print("YES")
