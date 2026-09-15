n = int(input())
k = 1
for j in range(n + 1):
    print(k % int(1e9 + 7),end=' ')
    k = k * (n-j) // (j+1)
