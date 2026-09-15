text=input()
c=len(text)
for i in range(0,c - 1):
    if text[i]=="1" and text[i+1]=="3":
      print("omadsiz chipta")
      break
else:
    print("omadli chipta")
