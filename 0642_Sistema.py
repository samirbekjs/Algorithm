n,m = map(int,input().split())
b = []
for i in range(0,21):
  for j in range(0,21):
    if i + j == n and i * j == m :
        print(i,j)
        break
else:
    print(-1)
