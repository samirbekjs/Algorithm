a=int(input())
b=list(map(int,input().split()))
q=b[::-1]
s=0
for i in range(1,a+1):
  s+=len(b)-q.index(i)-2-b.index(i)
  b.remove(b[len(b)-q.index(i)-1])
  b.remove(i)
  s+=1
  q=b[::-1]
print(s)
