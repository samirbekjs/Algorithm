n = int(input())
y = len(str(n)) // 2 + 1
alf = ["","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d", "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x = 0
s =""
a = []
while x != y:
  if n % 100 < 25:
    a.append(n % 1000)
    n = n // 1000
    x += 1
  elif n % 100 > 25:
    a.append(n % 100)
    n = n // 100
    x += 1
for i in a:
    if i != 0:
        if i < 91:
            x1 = i - 64
            s += alf[x1]
        else:
            x2 = i - 70
            s += alf[x2]
print(s[::-1])
