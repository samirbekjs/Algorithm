n = int(input())
a = 0
for i in str(n):
  a += int(i)
if a % 3 == 0:
  print("Yes")
else:
  print("No")
