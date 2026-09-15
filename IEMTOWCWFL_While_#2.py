import math as m
n = int(input())
l = m.log2(n)
if l > 0 and l % 1 == 0:
  print("yes")
else:
  print("no")
