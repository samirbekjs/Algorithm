n = int(input())
a = n // 10 * 2
if n % 10 < 3:
  print(a)
elif n % 10 >= 3 and n % 10 < 7:
  print(a + 1)
else:
  print(a + 2)
