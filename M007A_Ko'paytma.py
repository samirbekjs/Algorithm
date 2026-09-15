def top(n):
  n = abs(n)
  cnt = 0
  for i in range(1,int(n ** 0.5) + 1):
    if n % i == 0:
      cnt += 1
  return 2 * cnt
n = int(input())
if n < 0:
  n = -n
  if (n ** 0.5) % 1 == 0:
    print(top(n) - 1)
  else:
    print(top(n))
elif n == 0:
  print(-1)
else:
  print(top(n))
