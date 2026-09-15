a = input()
ll = len(a)
l = ll // 2
m,n = 1,0
tartib = []
satr = ''
for i in range(l):
    satr += a[m]
    satr += a[n]
    m += 2
    n += 2
if ll % 2 == 1:
    satr += a[ll - 1]
yk = ""
for i in satr:
    yk += chr(96 + (27 - (ord(i) - 96)))
print(yk)
