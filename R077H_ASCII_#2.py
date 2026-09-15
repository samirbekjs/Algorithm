n = int(input())
x = []
while n != 0:
    if n % 100 < 25:
        x.append(n % 1000)
        n = n // 1000
    else:
        x.append(n % 100)
        n = n // 100
s = ''
for i in x:
    s += str(chr(i))
print(s[::-1])
