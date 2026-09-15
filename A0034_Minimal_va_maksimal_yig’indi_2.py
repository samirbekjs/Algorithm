t = int(input())
for i in range(t):
  n,m = map(int,input().split())
  a = list(map(int,input().split()))
  if n == m or m == 0:
      print(0)
      continue
  x = n - m
  a.sort()
  minimum = 0
  maximum = 0
  y = 0
  for i in a:
    minimum += i
    y += 1
    if x == y:
      y = 0
      break
  s = sum(a)
  for i in a:
    maximum += i
    y += 1
    if y == m:
      break
  maximum = s - maximum
  print(maximum - minimum)
