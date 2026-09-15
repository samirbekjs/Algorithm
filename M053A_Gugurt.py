n,w,h = map(int,input().split())
c = (h ** 2 + w ** 2) ** (1 / 2)
b = []
for i in range(n):
    b.append(int(input()))
for i in b:
    if i <= c :
        print("YES")
    else:
        print("NO")
