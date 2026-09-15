a,k,l,r=map(int,input().split())
s = 0
for i in range(l,r+1):
    if i % a==k:
        s += i
        break
if s == 0:
    print(0)
else:
    print((r-s)//a+1)
