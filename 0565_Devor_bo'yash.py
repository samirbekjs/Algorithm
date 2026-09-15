n = int(input())
a,b = map(int,input().split())
c,d = map(int,input().split())
x = []
for i in range(a,b + 1):
  x.append(i)
for j in range(c,d + 1):
  x.append(j)
print(n - len(set(x)))
