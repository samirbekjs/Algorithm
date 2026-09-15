n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n):
  aa = a[i]
  bb = b[i]
  if (aa == 0 and bb == 0) or (aa == 1 and bb == 1):
    print(0,end=" ")
  else:
    print(1,end=" ")
