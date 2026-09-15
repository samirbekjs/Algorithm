n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    n1 = list(map(int, input().split()))
    a.append(n1)
for i in range(n):
    m1 = list(map(int, input().split()))
    b.append(m1)
for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print()
