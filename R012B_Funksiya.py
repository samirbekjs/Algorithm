def top(x):
  if x % 3 == 0:
    return x // 3
  elif x % 3 == 1:
    return 2 * x + 1
  else:
    return 2 * x - 1
n = int(input())
cnt = 0
while n != 1:
  cnt += 1
  n = top(n)
print(cnt)
