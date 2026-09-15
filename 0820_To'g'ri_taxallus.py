a=input()
l=len(a)
t=0
er = 0
for i in a:
    if 65 <=ord(i)<= 90 or 97<=ord(i)<=122 or ord(i)==45 or ord(i)==95 or 48<=ord(i)<= 57 :
        er+=1
    else:
        t+=1
if l-t>=2 and l-t<=24 and t != 0 :
  print("Erase",t)
elif l-t>24:
    print('Erase',t+l-t-24)
elif l >= 2 and l <= 24 and t == 0:
  print("Correct")
else:
  print("Error")
