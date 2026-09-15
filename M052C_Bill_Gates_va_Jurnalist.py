n = int(input())
a = ''
b = True
for i in str(n):
  if i != "9" and b:
    i = 9
    a += str(i)
    b = False
  else: 
      a += str(i)
print(a)
