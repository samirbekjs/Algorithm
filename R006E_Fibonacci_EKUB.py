import sys
import math

mod = 10**9 + 7

def fib(n):
    if n == 0:
        return (0, 1)
    a, b = fib(n >> 1)
    c = a * ((b * 2 - a) % mod) % mod
    d = (a * a + b * b) % mod
    if n & 1:
        return (d, (c + d) % mod)
    else:
        return (c, d)

i, j = map(int, sys.stdin.read().split())
g = math.gcd(i, j)
print(fib(g)[0] % mod)
