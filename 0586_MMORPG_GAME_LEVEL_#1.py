s,n = map(int,input().split())
a = [(0,0)]*n
l = 0
for i in range(n):
  x,y = map(int,input().split())
  a[i]=(x,y)
a.sort()
for i in range(len(a)):
    if s>a[i][0]:
        l+=1
        s=s+a[i][1]
    else:
        l+=0
if l >= n :
  print("YES")
else:
  print("NO")
