n,k = map(int,input().split())
y = []
a = list(map(int,input().split()))
s = a.count(k) * k
print(s)
for i in range(0,n): 
    if a[i] == k:
        y.append(i + 1)
print(*y)
