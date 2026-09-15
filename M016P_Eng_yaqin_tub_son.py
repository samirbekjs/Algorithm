n = int(input())
s = 0
b = 0
x = 0
ts = 0
for i in range(2, int(n**(0.5)) + 1):
    if n % i == 0 :
        break
else:
    if n != 1:
        print(n)
        ts += 1
if n == 1:
    print(2)
elif n > 2 and ts == 0:
    for i in range(n - 1,1,-1):
        for j in range(2,int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            b += i
            break
    for i in range(n + 1, n + 100):
        for j in range(2,int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            x += i
            break
    if x - n == n - b:
        print(b,x)
    elif x - n > n - b:
        print(b)
    else:
        print(x)
