import math as m
n = input()
ts = []
qiymatlar = []
for i in range(len(n)):
    sr = str(n[i])
    if sr not in qiymatlar:
        qiymatlar.append(sr)
        ts.append(n.count(sr))
qiymat = m.factorial(len(n))
for i in ts:
    qiymat //= m.factorial(i)
print(qiymat)
