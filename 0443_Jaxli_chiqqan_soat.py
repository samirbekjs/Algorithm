a,b = map(int,input().split(":"))
if a >= 12:
  a -= 12
soat = a * 30
m = b * 6
s1 = b / 2 + soat
print('{:.2f}'.format(s1),'{:.2f}'.format(m))
