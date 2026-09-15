n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
  if a.count(i) == 2 :
    b.append(i)
if len(b) >= 1:
    print(max(b)) 
else:
    print(-1)
