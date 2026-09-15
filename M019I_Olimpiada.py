n = int(input())
a = list(map(int,input().split()))
a.sort()
b = a[-1]
c = a[-2]
d = a[-3]
if n<3 or n>1000 and len(a)!=n and b>100 or b<1 and c>100 or c<1 and d>100 or d<1:
    print(0)
else:
    print(b,c,d)
