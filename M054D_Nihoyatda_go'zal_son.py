n = int(input())
b = []
for i in range(n):
  b.append(int(input()))
for i in b:
  if i % 4 == 2:
    print("YES")
  else:
    print("NO")
