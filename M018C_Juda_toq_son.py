def f(n):
    v=[9,1,3,5,7]
    s=0
    while(n>0):
        s=s*10+v[n%5]
        if(n%5==0):
            n=n//5
            n=n-1
        else:n=n//5
    q=[]
    while(s>0):
        q.append(s%10)
        s=s//10
    while(len(q)>0):
        s=s*10+q[0]
        q.pop(0)
    return s
n=int(input())
print(f(n))
