n = int(input())
l = n * (n + 1) * (n + 2) * (n + 3)
print((l // 24) % (int(1e9 + 7)))
