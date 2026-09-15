n = int(input())
for i in range(n + 1):
    k = 1
    for j in range(i + 1):
        print(k % int(1e9 + 7),end=' ')
        k = k * (i-j) // (j+1)
    print()
