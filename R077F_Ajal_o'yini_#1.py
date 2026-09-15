a,b = map(int,input().split())
x = []
x.append(0)
c = b
for i in range(a):
  x.append(int(input()))
for i in range(a // 2):
    if b == x[c]:
        print("Yes")
        break
    else:
        c = x[c]
else:
    print("No")
