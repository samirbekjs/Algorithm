x = []
for i in range(9):
  x.append(int(input()))
s = sum(x) - 100
for i in x:
  for j in x:
    if i + j == s:
      x.remove(i)
      x.remove(j)
      break
for i in x:
    print(i)
