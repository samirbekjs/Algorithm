n = int(input())
a = list(map(int,input().split()))
n,m= map(int,input().split())
x = []
for i in range(n-1,m):
  x.append(a[i])
print(*x)
