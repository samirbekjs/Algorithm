n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
for i in a:
  if i % 2 == 0:
    print(i)
    break
else:
  print(-1)
