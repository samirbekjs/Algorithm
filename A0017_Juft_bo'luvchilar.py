def juft(n):
    if n % 2 == 1:
        return 0
    n //= 2
    c = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n // i:
                c += 1
    return c

t = int(input())
for _ in range(t):
    n = int(input())
    print(juft(n))
