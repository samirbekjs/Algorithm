n = int(input())
j = 0
t = 0
if n % 2 == 0:
  for i in str(n):
    if int(i) % 2 == 0:
      j += int(i)
  print(j)
else: 
  for i in str(n):
    if int(i) % 2 == 1:
      t += int(i)
  print(t)
