a = int(input()) 
b = []
for i in range(a):
  b.append(int(input()))
for i in b:
  print(pow(i ** 2,1,1000000007))
