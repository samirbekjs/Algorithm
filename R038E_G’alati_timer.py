nn = int(input())
for i in range(1, nn + 1):
  kk = 4 + 3 * (2 ** i - 1) - 3
  if kk - nn > 0:
    print(int(kk - nn))
    break
