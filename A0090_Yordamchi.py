a,b = map(int,input().split())
x = []
l = 0
for i in range(1,70):
    for j in range(i):
        x.append(i)
        l += 1
s = 0
for i in range(a, b + 1):
    s += x[i - 1]
print(s)
