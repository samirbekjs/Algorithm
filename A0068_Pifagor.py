a = int(input())
if a % 2 == 1:
    k = (a - 1) // 2
    m = k + 1
    n = k
    b = 2 * m * n
    c = m * m + n * n
    print(a, b, c)
else:
    k = a // 2
    b = k * k - 1
    c = k * k + 1
    print(a, b, c)
