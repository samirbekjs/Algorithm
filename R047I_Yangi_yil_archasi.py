n = int(input())
s = 0
for i in range(2,n+2):
  s += i ** 2 + (i - 1)
print(s)
