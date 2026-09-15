n = int(input())
uch = n % 3
besh = n % 5
yetti = n % 7 
if uch == 0 and besh == 0 and yetti == 0:
  print(3,5,7)
elif uch == 0 and besh != 0 and yetti == 0:
  print(3,7)
elif uch == 0 and besh == 0 and yetti != 0:
  print(3,5)
elif besh == 0 and uch != 0 and yetti == 0:
  print(5,7)
elif uch == 0 and besh != 0 and yetti != 0:
  print(3)
elif uch != 0 and besh == 0 and yetti != 0:
  print(5)
elif uch != 0 and besh != 0 and yetti == 0:
  print(7)
else:
  print(-1)
