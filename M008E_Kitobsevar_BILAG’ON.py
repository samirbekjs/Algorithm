n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s = 0
cnt = 0
if sum(a) <= m:
  print("Shokoladxo'r")
else:
  for i in a:
    s +=i
    if s <= m:
      cnt +=1
    else:
      break
  print(cnt)
