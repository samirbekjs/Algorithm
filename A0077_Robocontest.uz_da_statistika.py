arr = [0]
cnt = 0
for i in range(int(input())):
  a,b = map(int,input().split())
  if b == 0:
    arr.append(a)
    cnt += 1
  else:
    arr.append(1)
if cnt == 0:
  print(-1)
else:
  print(arr.index(max(arr)))
