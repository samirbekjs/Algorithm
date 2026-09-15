def top(n):
  arr = list(n)
  s = 0
  for i in arr:
    i = int(i)
    s += i
  return s
for i in range(int(input())):
  n = input()
  l = 2
  while l > 1:
    n = str(top(n))
    l = len(str(n))
  print(n)
