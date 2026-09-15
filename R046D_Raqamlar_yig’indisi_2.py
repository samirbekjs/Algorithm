c,b,n = map(int,input().split())
a = max(c,b)
b = min(c,b)
k = 0
if b == 0:
    if n % a == 0:
        print(str(a)*(n//a))
    else:
        print(-1)
else:
    z = 0
    while n - k * b > 0:
        if (n-k*b)%a==0:
            z+=1
            break
        k+=1
    if z==1:
        print(k*str(b)+(n-k*b)//a*str(a))
    else:
        print(-1)
