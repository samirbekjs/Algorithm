a,b,c = map(str,input().split())
a = int(a)
b = int(b)
if c == "*":
  print(1,a * b)
elif c == "+":
  print(1,b + a - 1)
elif c == "-":
  print(1,b - a + 1)
else:
  print(a * 10,b * 10)
