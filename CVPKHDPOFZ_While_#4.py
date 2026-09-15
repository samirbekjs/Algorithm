n = int(input())
a = list(map(int,input().split()))
s = 1
p = 0
for i in a:
  s *= i
  p += i
print(p,s)
