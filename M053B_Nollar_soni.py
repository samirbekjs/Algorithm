a,b = map(int,input().split())
ans = 0
i = 1
bns = 0
i1 = 1
while True:
  ans += (a - 1) // 5 ** i
  i += 1
  if (a - 1) // 5 ** i < 1:
    break
while True:
  bns += b // 5 ** i1
  i1 += 1
  if b // 5 ** i1 < 1:
    break
if a <= 5:
  print(bns)
else:
  print(bns - ans)
