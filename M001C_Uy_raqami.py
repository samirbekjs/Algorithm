n = int(input())
for i in range(1,n + 1):
  if i + (i % 100) == n:
    print(i,end=" ")
