n = int(input())
k = bin(n)[2:]
bs = 0
ns = 0
for i in str(k):
    i = int(i)
    if i == 0 :
        ns += 1
    else :
        bs += 1
if ns == 0:
    print(-1)
else:
    print(bs//ns)
