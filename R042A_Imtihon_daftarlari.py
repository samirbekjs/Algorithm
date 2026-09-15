n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(1, n + 1):
    b.append(i)
if a == b:
    print("YES")
else:
    print("NO")
