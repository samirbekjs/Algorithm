n = int(input())
if n >= 0:
  print(n)
else:
  nn = n * (-1)
  l = len(str(nn))
  n1 = nn // 10 ** (l - 1)
  n2 = nn % 10 ** (l - 1)
  print(n2 - n1)
