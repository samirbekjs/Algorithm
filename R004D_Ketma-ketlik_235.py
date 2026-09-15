#56
s = [0] * 12501

def tub_boluvchilar():
    i2 = 1
    i3 = 1
    i5 = 1
    n2 = 0
    n3 = 0
    n5 = 0
    natija = 0
    s[1] = 1
    n2 = s[i2] * 2
    n3 = s[i3] * 3
    n5 = s[i5] * 5
    i = 0
    for i in range(2, 12501):
        natija = min(n2, min(n3, n5))
        s[i] = natija
        if natija == n2:
            i2 += 1
            n2 = s[i2] * 2
        if natija == n3:
            i3 += 1
            n3 = s[i3] * 3
        if natija == n5:
            i5 += 1
            n5 = s[i5] * 5

t = int(input())
s1 = []
for i in range(t):
    s1.append(int(input()))
tub_boluvchilar()
for i in range(t):
    print(s[s1[i]])
