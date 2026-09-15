m,n = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
s = 0
cnt = 0
if sum(a) <= n:
  print("Shokoladxo'r") 
else:
  for i in a:
    s += i
    if s <= n:
      cnt += 1
    else:
      break
  print(cnt)
