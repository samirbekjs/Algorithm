n = int(input())
cnt = 0
x = 0
if n == 7 or n == 4:
  print(-1)
elif n % 5 == 0:
  print(n // 5)
else:
  while True:
    n -= 3
    cnt += 1
    if n % 5 == 0:
      x = n // 5
      break
  print(cnt + x)
