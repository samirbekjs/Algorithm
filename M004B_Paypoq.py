n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(1,101):
    s+=a.count(i)//2
print(s)
