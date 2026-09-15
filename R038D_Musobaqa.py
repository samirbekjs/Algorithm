for i in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  cnt = 0
  for i in a:
    if i > 0:
      continue
    cnt += 1
  if cnt >= k:
    print("Qizg'in")
  else:
    print("Zerikarli")
