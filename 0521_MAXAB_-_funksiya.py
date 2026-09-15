n = int(input())
s = 0
for i in range(2,int(n**(1/2))+1):
    if n % i==0:
        s = i
else:
    if s ==0:
        print(len(str(n)))
    else:
        print(len(str(n//s)))
