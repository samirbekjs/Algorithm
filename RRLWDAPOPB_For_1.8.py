n = int(input())
s = 1
y = 0
for i in range(1,n + 1,2):
  s *= i	
for i in range(2,n + 1,2):
  y += i
print(y,s)
