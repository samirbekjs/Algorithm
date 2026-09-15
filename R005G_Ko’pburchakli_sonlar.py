mod = 1000000007

k, n = map(int, input().split())

if n % 2 == 0:
    res = n // 2
    res = (res * (n - 1)) % mod
else:
    res = (n - 1) // 2
    res = (res * n) % mod

res = (res * (k - 2)) % mod
print((res + n) % mod)
