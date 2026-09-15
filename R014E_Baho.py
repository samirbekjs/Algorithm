n = int(input())
a = n % 10
b = n // 10
if n < 38:
  print(n)
elif a < 5 and a >2:
  print(b * 10 + 5)
elif a > 7 and a < 10:
  print((b + 1) * 10)
else:
  print(n)
