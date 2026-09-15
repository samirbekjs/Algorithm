a , b = map(str,input().split())
a1 , b1 = map(str,input().split())
k = int(b)
k1 = int(b1)
s = ''
s1 = ''
harf = [a,a1]
for i in a:
  if i == "a":
    s += "1"
  elif i == "b":
    s += "2"
  elif i == "c":
    s += "3"
  elif i == "d":
    s += "4"
  elif i == "e":
    s += "5"
  elif i == "f":
    s += "6"
  elif i == "g":
    s += "7"
  elif i == "h":
    s += "8"
for i in a1:
  if i == "a":
    s1 += "1"
  elif i == "b":
    s1 += "2"
  elif i == "c":
    s1 += "3"
  elif i == "d":
    s1 += "4"
  elif i == "e":
    s1 += "5"
  elif i == "f":
    s1 += "6"
  elif i == "g":
    s1 += "7"
  elif i == "h":
    s1 += "8"
masofa = (k - k1)**2 + ( int(s)-int(s1))**2
if masofa == 5 :
  print("YES")
else:
  print("NO")
