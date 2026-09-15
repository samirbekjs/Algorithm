n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
for i in a:
  if i == 4 or i == 1 or i == 2 :
    print("NO")
  else:
    print("YES")
