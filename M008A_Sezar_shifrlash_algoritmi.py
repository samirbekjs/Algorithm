k=int(input())
k=k%26
a=input()
s=""
for i in a:
    if i=="_":
        s+=i
    else:
        if 64<ord(i)<91:
            if ord(i)+k>90:
                s+=chr(ord(i)+k-90+64)
            else:
                s+=chr(ord(i)+k)
        else:
            if ord(i)+k>122:
                s+=chr(ord(i)+k-122+96)
            else:
                s+=chr(ord(i)+k)
print(s)
