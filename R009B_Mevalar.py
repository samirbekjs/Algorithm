s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
ol = list(map(int,input().split()))
ap = list(map(int,input().split()))
ols = 0
aps = 0
for i in ol:
  if s <= a + i <= t:
    ols += 1
for i in ap:
  if s <= b + i <= t:
    aps += 1
print(ols)
print(aps)
