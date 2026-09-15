m,n = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
s = 0
cnt = 0
for i in a:
  s += i
  cnt += 1
  if s >= m:
    print(cnt) 
    break
else: 
  print(-1)
