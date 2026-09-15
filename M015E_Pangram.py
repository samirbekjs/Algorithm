a = input()
l = list(a)
k = []
for i in l:
     if 65 <= ord(i) <=90 or 97 <= ord(i) <= 122 :
         k.append(i.lower())
if len(set(k)) == 26  :
  print("pangram")
else:
  print("pangram emas")
