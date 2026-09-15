n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
kq = a[n - k]
cnt = 0
for i in a:
  if i >= kq and i > 0:
    cnt+= 1
  else:
    cnt += 0
print(cnt)
