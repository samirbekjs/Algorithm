n = int(input())
s = 1 
a = n //5
b = n % 5
massiv_2 = [6,2,4,8]
massiv_factorial = [1,1,2,6,4]
if n < 0:
    print(-1)
elif n == 1:
  print(1)
else: 
  while n > 1 :
    s *= (massiv_2[a%4] * massiv_factorial[b])%10
    n = a
    a = n // 5
    b = n % 5
  print(s%10)
