n = int(input())
if n == 1:
  print(1)
elif n == 2 or n == 3:
  print(2)
else:
  a = n + 1
  for i in range(2,int(a ** 0.5) + 1):
    if a % i == 0:
      print(0)      
      break
  else: 
    print(n)
