n = int(input())
if n % 3 == 0:
  print(3)
elif n % 3 != 0 and n % 5 == 0:
  print(5)
elif n % 5 != 0 and n % 7 == 0:
  print(7)
else:
  print(-1)
