a,b = map(int,input().split())
alf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
x = ""
for i in range(b):
    x += alf[i]
for i in range(a - b):
    if i >= b:
        s = i - (i // b * b)
        x += alf[s]
    else:
        x += alf[i]
print(x)
