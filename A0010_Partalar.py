a = list(map(int,input().split()))
b = []
for i in a:
  if i % 2 == 0:
    b.append(i // 2)
  else:
    b.append((i + 1) // 2)
print(sum(b))
