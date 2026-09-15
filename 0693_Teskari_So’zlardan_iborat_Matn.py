a = int(input())
n = list(map(str,input().split()))
x = []
for i in n:
  l=len(i)
  if l > a:
    s = i[::-1]
    x.append(s)
  else:
    x.append(i)
print(*x)
