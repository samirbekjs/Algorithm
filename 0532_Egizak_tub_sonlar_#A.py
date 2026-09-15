def tub(n):
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return 0
      break
  else:
    return 1
a,b = map(int,input().split())
s = 0
s += tub(a)
s += tub(b)
if abs(a - b) == s == 2:
  print("Yes")
else:
  print("No")
