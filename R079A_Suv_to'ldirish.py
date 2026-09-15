a,b,m = map(int,input().split())
a1 = m // a
b1 = m// b
umumiy = []
t = 0
for i in range(a1 + 1):
    for j in range(b1 + 1):
        yig = i * a + j * b
        if yig <= m:
          t = max(t,yig)
print(t)
