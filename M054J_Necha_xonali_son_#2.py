a,b = map(int,input().split())
a = a - 1
ka = 0
kb = 0
ja = 0
jb = 0
la = len(str(a))
lb = len(str(b))
for i in range(la-1):
    ka+=9*10**i
    ja+=(9*10**i)*(i+1)
ha = (int(a)-ka)*la
for i in range(lb-1):
    kb+=9*10**i
    jb+=(9*10**i)*(i+1)
hb = (int(b)-kb)*lb
print(hb + jb - ha - ja)
