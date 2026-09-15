n = int(input())
for i in range(n - 40, n + 1):
  if i + str(bin(i)[2:]).count("1") == n:
    print(i)
    break
else:
  print(-1)
